"""Import Markdown image references as verified, local Obsidian attachments.

Only network/local-file reads and attachment writes occur here.  Executable book
cells are never run.  The caller supplies whole documents before section splitting;
vault-root wiki embeds remain valid after a document moves into section notes.
"""

from __future__ import annotations

import base64
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
import hashlib
import html
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import tempfile
import time
from typing import Any
from urllib.error import HTTPError
from urllib.parse import quote, unquote, urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

from PIL import Image, UnidentifiedImageError


MAX_IMAGE_BYTES = 40 * 1024 * 1024
USER_AGENT = "ObsidianVaultImport/1.0"
IMAGE_PATTERN = re.compile(
    r"!\[((?:\\.|[^\]\\])*)\]\(\s*(?:<([^>\n]+)>|([^\s)]+(?:\([^\n)]*\)[^\s)]*)?))"
    r"(?:\s+\"[^\"\n]*\"|\s+'[^'\n]*')?\s*\)"
    r"(?:\{[^}\n]*\})?"
)
FENCE_PATTERN = re.compile(r"^\s*(`{3,}|~{3,})")


@dataclass(frozen=True)
class ImageOccurrence:
    document_index: int
    start: int
    end: int
    original: str
    alt: str
    destination: str
    candidates: tuple[str, ...]


def _title(value: str) -> str:
    value = unquote(value)
    value = re.sub(r"[_-]+", " ", value)
    value = re.sub(r"[<>:\"/\\|?*#\[\]^]", " ", value)
    value = re.sub(r"\s+", " ", value).strip(" .") or "Figure"
    acronyms = {"gpu": "GPU", "cpu": "CPU", "tpu": "TPU", "ml": "ML",
                "ai": "AI", "kv": "KV", "llm": "LLM", "sram": "SRAM",
                "dram": "DRAM", "int8": "INT8", "fp16": "FP16", "fp32": "FP32"}
    return " ".join(acronyms.get(word.lower(), word if word.isupper() else word[:1].upper() + word[1:])
                    for word in value.split())[:100].rstrip(" .")


def _source_repository(repo: Path) -> str:
    """Read a nonsecret repository selector, never credential configuration."""
    result = subprocess.run(
        ["git", "-C", str(repo), "remote", "get-url", "origin"],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    match = re.search(r"github\.com[/:]([^/]+/[^/]+?)(?:\.git)?$", result)
    if not match:
        raise ValueError("Expected a GitHub origin for repository image provenance")
    return match.group(1)


def _candidate_locations(destination: str, doc: dict[str, Any], repo: Path,
                         repository: str, commit: str) -> tuple[str, ...]:
    destination = html.unescape(destination).replace("\\ ", " ")
    if destination.startswith("data:"):
        return (destination,)
    parsed = urlparse(destination)
    if parsed.scheme in {"https", "http"}:
        return (destination,)
    if destination.startswith("//"):
        return ("https:" + destination,)

    source = Path(str(doc["source_path"]))
    candidates: list[str] = []
    if doc.get("rendered_source_url"):
        candidates.append(urljoin(str(doc["rendered_source_url"]), destination))
    raw_path = unquote(parsed.path)
    if raw_path.startswith("/"):
        # Quarto website assets are rooted at books/, not the filesystem root.
        relative = Path("books") / raw_path.lstrip("/")
    else:
        relative = source.parent / raw_path
    normalized = Path(os.path.normpath(relative))
    local_path = (repo / normalized).resolve()
    try:
        local_path.relative_to(repo.resolve())
    except ValueError:
        # Some relative image links are written from books' project root.
        normalized = Path("books") / raw_path.lstrip("./")
        local_path = (repo / normalized).resolve()
    if local_path.is_file() and local_path.is_relative_to(repo.resolve()):
        candidates.insert(0, local_path.as_uri())
    if not str(normalized).startswith("../"):
        candidates.append(
            f"https://raw.githubusercontent.com/{repository}/{commit}/"
            + quote(normalized.as_posix(), safe="/")
        )
    # A source link such as /shared/assets/foo.svg can also be rendered directly.
    if raw_path.startswith("/"):
        candidates.append("https://mlsysbook.ai" + quote(raw_path, safe="/%"))
    return tuple(dict.fromkeys(candidates))


def _sanitize_svg(data: bytes) -> tuple[bytes, list[str]]:
    """Keep SVG artwork self-contained and inert; report removed active content."""
    if b"<!ENTITY" in data.upper() or b"<!DOCTYPE" in data.upper():
        # Ordinary SVG DOCTYPEs are harmless, but do not permit entity expansion.
        data = re.sub(br"<!DOCTYPE[^>]*(?:\[[\s\S]*?\]\s*)?>", b"", data,
                      flags=re.IGNORECASE)
        if b"<!ENTITY" in data.upper():
            raise ValueError("SVG has entity declarations")
    root = ET.fromstring(data)
    if root.tag.split("}")[-1].lower() != "svg":
        raise ValueError("XML response is not an SVG image")
    warnings: list[str] = []
    for parent in root.iter():
        for child in list(parent):
            if child.tag.split("}")[-1].lower() in {"script", "foreignobject"}:
                parent.remove(child)
                warnings.append("Removed Active SVG Content")
        for key in list(parent.attrib):
            local_key = key.split("}")[-1].lower()
            if local_key.startswith("on"):
                del parent.attrib[key]
                warnings.append("Removed SVG Event Handler")
            elif local_key == "href":
                value = parent.attrib[key].strip()
                if value.lower().startswith(("javascript:", "file:")):
                    del parent.attrib[key]
                    warnings.append("Removed Unsafe SVG Reference")
                elif value.startswith(("http://", "https://", "//")):
                    # Hyperlink wrappers do not affect the artwork; embedded
                    # remote images do and must not silently disappear offline.
                    if parent.tag.split("}")[-1].lower() in {"image", "use", "feimage"}:
                        raise ValueError("SVG embeds an external image dependency")
    # Avoid rewriting clean SVG namespaces/styles.  This also preserves CDATA.
    if not warnings:
        return data, warnings
    ET.register_namespace("", "http://www.w3.org/2000/svg")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True), warnings


def _image_kind(data: bytes) -> tuple[bytes, str, str, list[str]]:
    if not data or len(data) > MAX_IMAGE_BYTES:
        raise ValueError("Empty or Oversized Image")
    leading = data[:4096].lstrip()
    if b"<svg" in leading.lower():
        clean, warnings = _sanitize_svg(data)
        return clean, ".svg", "image/svg+xml", warnings
    if leading.lower().startswith((b"<!doctype html", b"<html")):
        raise ValueError("Server Returned HTML Instead of an Image")
    if data.startswith(b"%PDF-"):
        return data, ".pdf", "application/pdf", []
    try:
        with Image.open(io.BytesIO(data)) as image:
            image.verify()
            kind = str(image.format).upper()
    except (UnidentifiedImageError, OSError, SyntaxError) as error:
        raise ValueError("Response Is Not a Readable Image") from error
    formats = {"PNG": (".png", "image/png"), "JPEG": (".jpg", "image/jpeg"),
               "GIF": (".gif", "image/gif"), "WEBP": (".webp", "image/webp"),
               "AVIF": (".avif", "image/avif"), "BMP": (".bmp", "image/bmp"),
               "TIFF": (".tiff", "image/tiff"), "ICO": (".ico", "image/x-icon")}
    if kind not in formats:
        raise ValueError(f"Unsupported Attachment Format: {kind}")
    extension, mime = formats[kind]
    return data, extension, mime, []


def _fetch_one(candidates: tuple[str, ...], cache: Path) -> dict[str, Any]:
    errors: list[str] = []
    for location in candidates:
        key = hashlib.sha256(location.encode()).hexdigest()
        cache_data = cache / (key + ".bin")
        try:
            if cache_data.is_file():
                data = cache_data.read_bytes()
            elif location.startswith("data:"):
                prefix, encoded = location.split(",", 1)
                data = base64.b64decode(encoded, validate=True) if ";base64" in prefix else unquote(encoded).encode()
            elif location.startswith("file:"):
                data = Path(unquote(urlparse(location).path)).read_bytes()
            else:
                parsed = urlparse(location)
                safe_url = urlunparse(parsed._replace(path=quote(unquote(parsed.path), safe="/:%@+~!$&'*,;=-._"), fragment=""))
                for attempt in range(2):
                    try:
                        request = Request(safe_url, headers={"User-Agent": USER_AGENT, "Accept": "image/*,*/*;q=0.8"})
                        with urlopen(request, timeout=35) as response:
                            content_length = int(response.headers.get("Content-Length", "0"))
                            if content_length > MAX_IMAGE_BYTES:
                                raise ValueError("Image Exceeds Attachment Size Limit")
                            data = response.read(MAX_IMAGE_BYTES + 1)
                        break
                    except HTTPError as error:
                        if attempt == 0 and error.code in {429, 502, 503, 504}:
                            time.sleep(min(3, max(0, int(error.headers.get("Retry-After", "1")))))
                            continue
                        raise
            clean, extension, mime, warnings = _image_kind(data)
            if not cache_data.exists() and not location.startswith("file:"):
                temporary = cache_data.with_suffix(f".{os.getpid()}.tmp")
                temporary.write_bytes(data)
                temporary.replace(cache_data)
            return {"data": clean, "source_url": location, "extension": extension,
                    "mime": mime, "sha256": hashlib.sha256(clean).hexdigest(),
                    "warnings": warnings}
        except Exception as error:
            errors.append(f"{location if not location.startswith('data:') else 'Embedded Data Image'}: {type(error).__name__}: {error}")
    return {"error": "; ".join(errors), "candidates": list(candidates)}


def _code_ranges(body: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    marker = ""
    start = 0
    offset = 0
    for line in body.splitlines(keepends=True):
        found = FENCE_PATTERN.match(line)
        if found:
            token = found.group(1)
            if not marker:
                marker, start = token, offset
            elif token[0] == marker[0] and len(token) >= len(marker) and line.strip() == token:
                ranges.append((start, offset + len(line)))
                marker = ""
        offset += len(line)
    if marker:
        ranges.append((start, len(body)))
    return ranges


def import_media(documents: list[dict[str, Any]], repo: Path, vault: Path,
                 source_commit: str) -> dict[str, Any]:
    """Mutate document bodies and return complete local-attachment provenance.

    Every failed import stays visible as a source link at the original position.
    Returned data are JSON serializable; raw image bytes never enter a manifest.
    """
    repo, vault = Path(repo), Path(vault)
    repository = _source_repository(repo)
    cache = Path(tempfile.gettempdir()) / "cs249r-obsidian-image-cache"
    cache.mkdir(parents=True, exist_ok=True)
    occurrences: list[ImageOccurrence] = []
    for index, document in enumerate(documents):
        body = str(document["body"])
        ranges = _code_ranges(body)
        for match in IMAGE_PATTERN.finditer(body):
            if any(start <= match.start() < end for start, end in ranges):
                continue
            alt = html.unescape(re.sub(r"\\([\[\]\\])", r"\1", match.group(1))).strip()
            destination = match.group(2) or match.group(3)
            candidates = _candidate_locations(destination, document, repo, repository, source_commit)
            occurrences.append(ImageOccurrence(index, match.start(), match.end(), match.group(0), alt,
                                               destination, candidates))
    unique = list(dict.fromkeys(item.candidates for item in occurrences))
    print(f"Importing {len(occurrences)} Image References From {len(unique)} Sources", flush=True)
    with ThreadPoolExecutor(max_workers=10) as pool:
        fetched = dict(zip(unique, pool.map(lambda candidates: _fetch_one(candidates, cache), unique)))

    assets: list[dict[str, Any]] = []
    missing: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    by_hash: dict[str, str] = {}
    edits: dict[int, list[tuple[int, int, str]]] = {}
    for occurrence in occurrences:
        document = documents[occurrence.document_index]
        result = fetched[occurrence.candidates]
        source_path = str(document["source_path"])
        original_reference = occurrence.destination
        if original_reference.startswith("data:"):
            original_reference = "embedded-data:sha256:" + hashlib.sha256(original_reference.encode()).hexdigest()
        if "error" in result:
            fallback = next((value for value in occurrence.candidates if value.startswith(("https://", "http://"))), "")
            description = occurrence.alt or "Figure"
            if fallback:
                replacement = f"[Image Source — {description}](<{fallback}>)\n\n> Image Import Unavailable: See the linked source."
            else:
                replacement = f"> Image Import Unavailable: {description}. See the original chapter source."
            missing.append({"source_path": source_path, "original": original_reference,
                            "alt": occurrence.alt, "error": result["error"],
                            "source_url": fallback})
        else:
            digest = result["sha256"]
            if digest not in by_hash:
                source = PurePosixPath(source_path)
                volume_match = re.search(r"(?:^|/)vol([1-4])(?:/|$)", source_path)
                volume = "Volume " + {"1": "I", "2": "II", "3": "III", "4": "IV"}.get(volume_match.group(1), volume_match.group(1)) if volume_match else "Shared"
                chapter_match = next((part for part in source.parts if re.match(r"\d{2}_", part)), "Shared Figures")
                folder = _title(chapter_match)
                original_name = PurePosixPath(urlparse(occurrence.destination).path).stem
                if occurrence.destination.startswith("data:"):
                    original_name = "Embedded Figure"
                elif re.fullmatch(r"[0-9a-fA-F]{24,}", original_name):
                    original_name = occurrence.alt or "Generated Figure"
                friendly_name = _title(original_name)
                local = (Path("90 Assets") / volume / folder /
                         f"{friendly_name} {digest[:10]}{result['extension']}").as_posix()
                destination_file = vault / local
                destination_file.parent.mkdir(parents=True, exist_ok=True)
                if not destination_file.exists() or hashlib.sha256(destination_file.read_bytes()).hexdigest() != digest:
                    destination_file.write_bytes(result["data"])
                by_hash[digest] = local
                provenance_url = result["source_url"]
                if provenance_url.startswith("file:"):
                    local_source = Path(unquote(urlparse(provenance_url).path)).resolve()
                    provenance_url = (f"https://raw.githubusercontent.com/{repository}/{source_commit}/"
                                      + quote(local_source.relative_to(repo.resolve()).as_posix(), safe="/"))
                elif provenance_url.startswith("data:"):
                    provenance_url = "embedded-data:sha256:" + digest
                asset = {"path": local, "source_url": provenance_url,
                         "source_path": source_path, "original": original_reference,
                         "sha256": digest, "mime": result["mime"], "bytes": len(result["data"])}
                assets.append(asset)
            local = by_hash[digest]
            replacement = f"![[{local}]]"
            # Keep alternative descriptions available to the reader.  Do not use
            # wiki aliases as alt text: Obsidian treats those as sizing controls.
            if occurrence.alt:
                caption = occurrence.alt.replace("\n", " ").replace("*", r"\*")
                caption = re.sub(r"\s+", " ", caption)
                replacement += "\n\n*" + caption + "*"
            for warning in result["warnings"]:
                warnings.append({"source_path": source_path, "asset_path": local, "warning": warning})
        # A source image can itself own a cross-reference identifier.  Preserve
        # that target while removing Pandoc's nonportable attribute syntax.
        attribute_id = re.search(r"\{[^}\n]*#([A-Za-z][A-Za-z0-9_-]*)[^}\n]*\}\s*$", occurrence.original)
        if attribute_id:
            replacement += "\n^" + attribute_id.group(1)
        edits.setdefault(occurrence.document_index, []).append((occurrence.start, occurrence.end, replacement))
    for index, changes in edits.items():
        body = str(documents[index]["body"])
        for start, end, replacement in reversed(changes):
            body = body[:start] + replacement + body[end:]
        documents[index]["body"] = body
    return {"stats": {"image_references": len(occurrences), "source_images": len(unique),
                       "local_assets": len(assets), "missing_references": len(missing),
                       "total_bytes": sum(asset["bytes"] for asset in assets)},
            "assets": assets, "missing": missing, "warnings": warnings}


def prune_unused_generated_assets(vault: Path) -> dict[str, Any]:
    """Remove only verified generated files unreferenced by any Markdown note.

    Call after all converted and personal notes have been written.  Manually
    modified files, files without this importer's SHA filename signature, and
    shorthand/relative personal-note references are preserved.
    """
    vault = Path(vault).resolve()
    assets_directory = vault / "90 Assets"
    references: set[str] = set()
    shorthand: set[str] = set()
    for note in vault.rglob("*.md"):
        body = note.read_text(encoding="utf-8")
        for match in re.finditer(r"!?\[\[([^\]\n]+)\]\]", body):
            target = unquote(match.group(1).split("|", 1)[0].split("#", 1)[0]).strip()
            if "/" not in target:
                shorthand.add(target)
            else:
                references.add(target.lstrip("/"))
                resolved = (note.parent / target).resolve()
                if resolved.is_relative_to(vault):
                    references.add(resolved.relative_to(vault).as_posix())
        for match in re.finditer(r"!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))", body):
            target = unquote(html.unescape(match.group(1) or match.group(2))).split("#", 1)[0]
            if urlparse(target).scheme:
                continue
            references.add(target.lstrip("/"))
            resolved = (note.parent / target).resolve()
            if resolved.is_relative_to(vault):
                references.add(resolved.relative_to(vault).as_posix())
    removed: list[dict[str, Any]] = []
    kept_unreferenced: list[str] = []
    for attachment in sorted(assets_directory.rglob("*")):
        if not attachment.is_file() or attachment.is_symlink():
            continue
        relative = attachment.relative_to(vault).as_posix()
        if relative in references or attachment.name in shorthand or attachment.stem in shorthand:
            continue
        signature = re.search(r" ([0-9a-f]{10})\.[a-z0-9]+$", attachment.name)
        if not signature:
            kept_unreferenced.append(relative)
            continue
        content = attachment.read_bytes()
        digest = hashlib.sha256(content).hexdigest()
        if not digest.startswith(signature.group(1)):
            kept_unreferenced.append(relative)
            continue
        removed.append({"path": relative, "sha256": digest, "bytes": len(content)})
        attachment.unlink()
    for directory in sorted(assets_directory.rglob("*"), reverse=True):
        if directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()
    return {"removed": removed, "removed_files": len(removed),
            "removed_bytes": sum(item["bytes"] for item in removed),
            "preserved_unreferenced": kept_unreferenced}

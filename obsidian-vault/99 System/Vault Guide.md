---
title: Vault Guide
type: Index
tags:
- Type/Index
---

# Vault Guide

Open this `obsidian-vault` folder as a vault in Obsidian. Start at [[Home]]. Core links, backlinks, tags, search, and Graph View work without community plugins.

## Reading Structure

Books retain volume and part order. Chapter overview notes link to section notes; each section links back to its chapter. Source headings and original identifiers are retained as exact Obsidian block references. Titles and prose headings use Title Case, preserving technical acronyms.

## Concepts and Themes

Canonical concept notes use the repository taxonomy and retain its draft status, stable identifiers, and relationship conditions. Related passages are not assertions of prerequisite order or complete coverage. Theme notes are curated reading lenses. Obsidian computes backlinks from the explicit links in these notes.

## Tables, Images, and Mathematics

Tables use Markdown pipe tables or HTML tables for structures that require merged cells. Images are imported locally under `90 Assets`. Source-specific LaTeX notation is expanded or supplied as MathJax-compatible definitions. The import manifest records image provenance, rendering mode, and explicit fallbacks for content that cannot be represented faithfully.

## Rebuilding

Run `python obsidian_tools/build_vault.py`, then `python obsidian_tools/link_vault.py --repo .`, then `python obsidian_tools/validate_vault.py` from the repository root. Rebuilding replaces generated notes; personal notes and reading progress are preserved. Source and rendering snapshots are recorded separately, because a published rendering can differ from the pinned repository commit.

## Naming and Tags

File names and headings use Title Case. Source identifiers keep their original machine-readable spelling for stable references. Tags use slash-separated namespaces and underscores where spaces would otherwise be required.

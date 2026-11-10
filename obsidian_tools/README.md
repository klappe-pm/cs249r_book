# Obsidian Vault Importer

Imports the four-volume *Machine Learning Systems* curriculum into `obsidian-vault/`.

## Open the Vault

In Obsidian, choose **Open Folder as Vault**, select `obsidian-vault`, and open `Home.md`. Core plugins provide links, backlinks, tags, search, and Graph View. No community plugins are required.

## Rebuild

Requirements: Python 3.12, Pandoc 3.1 or newer, `curl`, Git, and the packages in `requirements.txt`.

```sh
python -m pip install -r obsidian_tools/requirements.txt
python obsidian_tools/build_vault.py --repo .
python obsidian_tools/link_vault.py --repo . --audit-round 2
python obsidian_tools/validate_vault.py --json /tmp/vault-validation.json
```

The importer reads the checked-out book source and canonical taxonomy. Source-correlated published HTML supplies executed numerical values and generated diagrams; missing headings are restored only when their source prose matches. The manifest records the pinned repository commit, rendered-page SHA-256 hashes, prose coverage, restored headings, and attachment hashes separately. It never executes textbook code cells.

`06 My Notes`, reading progress, and Obsidian preferences are preserved. Source identities repair links when generated titles change. Rebuilding replaces generated book and concept notes. Verified, unreferenced generated attachments are pruned; manual attachments remain.

## Review Evidence

The vault includes the original Round One findings, corrected Round Two content and formatting reviews, both independent semantic backlink audits, and a media integrity audit. Validation checks all source headings, exact page/block links, YAML, table columns, footnotes, image files, and source metadata. The semantic audit compares all canonical definitions and conditional relationships to the pinned taxonomy and checks every explicit passage alignment.

## Source Rights

Attribution and the original component license notices are in `99 System/Sources and Attribution.md`. The taxonomy and book prose have different licenses; source provenance remains explicit.

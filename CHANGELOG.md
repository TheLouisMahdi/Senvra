# Changelog

All notable public changes to Senvra are documented here.

## 1.2.0 — 2026-08-09

### Added

- Standard Base64 can now be used as a normal input, not only as an output.
- Raw Base64 can be pasted in **Convert** and turned into Senvra, TXT, ZIP, or Base64 output.
- Raw Base64 can be pasted in **Restore** and converted back to file bytes.
- Supports common Base64 forms including optional `Senvra` / `Base64:` labels and `data:...;base64,...` values.
- Common file types can be inferred from decoded bytes when Base64 does not contain filename metadata.
- `.b64` and `.base64` text files are accepted in Restore.

### Changed

- Base64 is now presented as one of Senvra's general file representations instead of a developer-specific feature.
- Base64 output button now follows the same visual hierarchy as the other output buttons.
- README now documents the general `File ↔ Base64 ↔ Senvra` workflow.

### Compatibility

- Existing `.senvra`, TXT, ZIP, password-protected files, and supported legacy `.poimu` restore paths remain supported.

## 1.1.0 — 2026-08-09

### Added

- Standard Base64 output for the original selected file.
- Base64 could be copied directly to the clipboard.

## 1.0.0 — 2026-08-08

Initial public release.

### Added

- Local browser-based file conversion and restoration.
- Native `.senvra` output.
- TXT transport output for copy/paste and text-friendly channels.
- ZIP transport output for broader uploader compatibility.
- Optional password protection and random password generation.
- English and Persian interface.
- Restore support for supported legacy `.poimu` files.
- Single-file application with no build step or runtime package dependency.

### Notes

- ZIP output is provided mainly as a compatibility wrapper and is not intended to guarantee smaller file size.
- TXT and Base64 change how data is represented but are not confidential by themselves; use password protection when privacy is required.

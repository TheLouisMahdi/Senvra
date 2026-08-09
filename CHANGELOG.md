# Changelog

All notable public changes to Senvra are documented here.

## 1.1.0 — 2026-08-09

### Added

- Dedicated **Base64** action for copying the original selected file as standard Base64 text.
- Developer workflow for embedding small images, icons, templates, fixtures, and other assets directly inside Python, HTML, JSON, or single-file utilities.
- Python Base64 embedding example under `examples/base64_embed.py`.

### Changed

- Public documentation now treats Base64 as a first-class developer use case alongside Senvra, TXT, and ZIP transport workflows.
- UI copy and version label updated for Senvra 1.1.

### Notes

- Base64 represents the original file bytes directly; it is separate from Senvra password protection.
- Base64 is not hashing, encryption, or compression and is normally larger than the original binary file.

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
- TXT output changes the representation of a file but is not confidential by itself; use password protection when privacy is required.

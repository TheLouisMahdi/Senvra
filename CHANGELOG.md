# Changelog

All notable public changes to Senvra are documented here.

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

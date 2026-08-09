"""Minimal example for embedding a small file as Base64 in Python."""

import base64
from pathlib import Path

# Paste the value copied from Senvra's Base64 action here.
ASSET_B64 = "PASTE_BASE64_HERE"

asset_bytes = base64.b64decode(ASSET_B64)

# Use asset_bytes directly with APIs that accept bytes,
# or restore the file only when you actually need it on disk.
Path("restored_asset.bin").write_bytes(asset_bytes)

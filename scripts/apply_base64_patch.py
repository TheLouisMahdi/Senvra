from __future__ import annotations

import base64
import hashlib
import re
from pathlib import Path

PATH = Path("index.html")
s = PATH.read_text(encoding="utf-8")

if 'id="copyBase64"' in s:
    print("Base64 feature already present; nothing to patch.")
    raise SystemExit(0)


def rep(old: str, new: str, count: int = 1) -> None:
    global s
    if old not in s:
        raise RuntimeError(f"Patch anchor not found: {old[:100]!r}")
    s = s.replace(old, new, count)


rep(
    '.actions{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:7px;margin-top:8px}.actions.three{grid-template-columns:repeat(3,minmax(0,1fr))}.action{',
    '.actions{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:7px;margin-top:8px}.actions.three{grid-template-columns:repeat(3,minmax(0,1fr))}#copyBase64{grid-column:1/-1}.action{',
)

rep(
    '<div class="actions"><button class="action" id="copyCode" type="button" data-i18n="copyPoimu"></button><button class="action primary" id="downloadPoimu" type="button" data-i18n="downloadPoimu"></button><button class="action" id="startLargeEncode" type="button" data-i18n="startLarge"></button><button class="action" id="downloadZip" type="button" data-i18n="downloadZip"></button></div>',
    '<div class="actions"><button class="action" id="copyCode" type="button" data-i18n="copyPoimu"></button><button class="action primary" id="downloadPoimu" type="button" data-i18n="downloadPoimu"></button><button class="action" id="startLargeEncode" type="button" data-i18n="startLarge"></button><button class="action" id="downloadZip" type="button" data-i18n="downloadZip"></button><button class="action" id="copyBase64" type="button" data-i18n="copyBase64"></button></div>',
)

rep("SENVRA 1.0 — PUBLIC RELEASE", "SENVRA 1.1 — PUBLIC RELEASE")

rep(
    'startLargeEncode: $("startLargeEncode"), copyCode: $("copyCode"), downloadPoimu: $("downloadPoimu"),\n  downloadZip: $("downloadZip"), encodeStatus: $("encodeStatus"), decodeInput: $("decodeInput"),',
    'startLargeEncode: $("startLargeEncode"), copyCode: $("copyCode"), downloadPoimu: $("downloadPoimu"),\n  downloadZip: $("downloadZip"), copyBase64: $("copyBase64"), encodeStatus: $("encodeStatus"), decodeInput: $("decodeInput"),',
)

rep('  textCache: "",\n  outputBaseName: "file",', '  textCache: "",\n  sourceFile: null,\n  outputBaseName: "file",')

rep(
    'heroSubtitle: "فایلت را با Senvra به یک فایل قابل‌حمل، TXT یا ZIP تبدیل کن و هر وقت خواستی دوباره برگردان.",',
    'heroSubtitle: "فایلت را با Senvra به یک فایل قابل‌حمل، TXT، ZIP یا Base64 تبدیل کن و هر وقت خواستی دوباره برگردان.",',
)
rep('containerHint: "خروجی Senvra، TXT و ZIP در دسترس است.",', 'containerHint: "خروجی Senvra، TXT، ZIP و Base64 در دسترس است.",')
rep(
    'copyPoimu: "کپی متن", downloadPoimu: "دانلود Senvra", startLarge: "دانلود TXT", downloadZip: "دانلود ZIP",',
    'copyPoimu: "کپی متن", downloadPoimu: "دانلود Senvra", startLarge: "دانلود TXT", downloadZip: "دانلود ZIP", copyBase64: "Base64",',
)
rep(
    'secDownloadTitle: "سه خروجی", secDownloadText: "می‌توانی فایل را به صورت Senvra، TXT یا ZIP دانلود کنی.",',
    'secDownloadTitle: "چند روش خروجی", secDownloadText: "می‌توانی فایل را به صورت Senvra، TXT یا ZIP بگیری یا Base64 فایل اصلی را کپی کنی.",',
)

rep(
    'heroSubtitle: "Use Senvra to turn a file into a portable file, TXT or ZIP, then restore it whenever you need it.",',
    'heroSubtitle: "Use Senvra to turn a file into a portable file, TXT, ZIP or Base64, then restore it whenever you need it.",',
)
rep('containerHint: "Senvra, TXT and ZIP outputs are available.",', 'containerHint: "Senvra, TXT, ZIP and Base64 outputs are available.",')
rep(
    'copyPoimu: "Copy text", downloadPoimu: "Download Senvra", startLarge: "Download TXT", downloadZip: "Download ZIP",',
    'copyPoimu: "Copy text", downloadPoimu: "Download Senvra", startLarge: "Download TXT", downloadZip: "Download ZIP", copyBase64: "Base64",',
)
rep(
    'secDownloadTitle: "Three outputs", secDownloadText: "Download your file as Senvra, TXT or ZIP.",',
    'secDownloadTitle: "Flexible outputs", secDownloadText: "Download Senvra, TXT or ZIP, or copy the original file as Base64.",',
)

s = s.replace('signature: "Senvra 1.0 · by POIMU · TheLouisMahdi"', 'signature: "Senvra 1.1 · by POIMU · TheLouisMahdi"')

rep(
    'function wipeEncodeState() {\n  wipeBytes(state.containerBytes); state.containerBytes = null; state.senvraBlob = null; state.zipBlob = null; state.textCache = "";\n}',
    'function wipeEncodeState() {\n  wipeBytes(state.containerBytes); state.containerBytes = null; state.senvraBlob = null; state.zipBlob = null; state.textCache = ""; state.sourceFile = null;\n}',
)

rep(
    'state.containerBytes = built.container; state.senvraBlob = new Blob([built.container], { type: "application/octet-stream" }); state.outputBaseName = baseName(file.name);',
    'state.containerBytes = built.container; state.senvraBlob = new Blob([built.container], { type: "application/octet-stream" }); state.sourceFile = file; state.outputBaseName = baseName(file.name);',
)

rep(
    'dom.encodePath.textContent = encrypted ? "FILE → PASSWORD → SENVRA / TXT / ZIP" : "FILE → SENVRA / TXT / ZIP";',
    'dom.encodePath.textContent = encrypted ? "FILE → PASSWORD → SENVRA / TXT / ZIP · BASE64 (ORIGINAL)" : "FILE → SENVRA / TXT / ZIP / BASE64";',
)

rep(
    'function ensureTextCache() { if (!state.containerBytes) throw new Error(uiText("اول یک فایل انتخاب کن.", "Choose a file first.")); if (!state.textCache) state.textCache = containerToText(state.containerBytes); return state.textCache; }\nfunction downloadBlob(blob, name) {',
    'function ensureTextCache() { if (!state.containerBytes) throw new Error(uiText("اول یک فایل انتخاب کن.", "Choose a file first.")); if (!state.textCache) state.textCache = containerToText(state.containerBytes); return state.textCache; }\nasync function copyOriginalBase64() {\n  if (!(state.sourceFile instanceof File)) throw new Error(uiText("اول یک فایل انتخاب کن.", "Choose a file first."));\n  let raw = new Uint8Array(await state.sourceFile.arrayBuffer());\n  try {\n    const base64Text = bytesToBase64(raw);\n    await copyTextToClipboard(base64Text);\n    setStatus(dom.encodeStatus, uiText("Base64 فایل اصلی در Clipboard کپی شد.", "Base64 for the original file was copied to the clipboard."), "good");\n  } finally { wipeBytes(raw); raw = null; }\n}\nfunction downloadBlob(blob, name) {',
)

rep(
    'dom.downloadZip.addEventListener("click", () => { if (!state.zipBlob) return; downloadBlob(state.zipBlob, state.outputBaseName + ".zip"); });\ndom.loadPoimu.addEventListener("click", () => dom.poimuInput.click());',
    'dom.downloadZip.addEventListener("click", () => { if (!state.zipBlob) return; downloadBlob(state.zipBlob, state.outputBaseName + ".zip"); });\ndom.copyBase64.addEventListener("click", async () => { try { await copyOriginalBase64(); } catch (e) { setStatus(dom.encodeStatus, String(e?.message || e), "warn"); } });\ndom.loadPoimu.addEventListener("click", () => dom.poimuInput.click());',
)

style = re.search(r"<style>(.*?)</style>", s, re.S)
script = re.search(r"<script>(.*?)</script>", s, re.S)
if not style or not script:
    raise RuntimeError("Could not locate inline style/script")

style_hash = base64.b64encode(hashlib.sha256(style.group(1).encode()).digest()).decode()
script_hash = base64.b64encode(hashlib.sha256(script.group(1).encode()).digest()).decode()

s = re.sub(r"style-src 'sha256-[^']+'", f"style-src 'sha256-{style_hash}'", s, count=1)
s = re.sub(r"script-src 'sha256-[^']+'", f"script-src 'sha256-{script_hash}'", s, count=1)

if s.count('id="copyBase64"') != 1:
    raise RuntimeError("Base64 button validation failed")
if 'copyOriginalBase64' not in s or 'sourceFile: null' not in s:
    raise RuntimeError("Base64 logic validation failed")

PATH.write_text(s, encoding="utf-8")
print("Applied Senvra 1.1 Base64 patch")
print("style sha256:", style_hash)
print("script sha256:", script_hash)

# Senvra

**A simple, local-first way to convert, protect, send, embed, and restore files — directly in your browser.**

> *“The file asked: If I’m never uploaded, do I still exist? — Senvra replied: Easy, Descartes. You’re just being converted.”*

Senvra is a single-file browser tool for turning ordinary files into formats that can be easier to store, move, paste, send, or embed in code. It runs locally in the browser and is designed for people who want a simple workflow without installing an application or uploading their file to a processing server.

**Created by POIMU · [TheLouisMahdi](https://github.com/TheLouisMahdi)**

---

## Why Senvra?

Sometimes the hard part is not the file itself — it is getting the file through the place you need to send it, or keeping a small asset inside a project without carrying another external file.

Messaging apps, upload forms, email gateways, corporate systems, educational portals, and other services may reject certain file extensions or make some file types inconvenient to transfer. This can be especially noticeable for users in Iran, where people may regularly move files through a mix of local and international services with different upload restrictions.

Senvra gives the same file several practical ways to travel or live inside a project:

- **Senvra file (`.senvra`)** — the native portable form.
- **ZIP (`.zip`)** — useful when an uploader accepts ZIP more easily than the original file type. Senvra uses ZIP as a compatibility wrapper; it is not a promise of smaller file size.
- **Text (`.txt`)** — represents the Senvra package as ordinary text, so it can be saved, copied, pasted, or sent through text-friendly channels.
- **Base64** — copies the original file bytes as standard Base64 text, useful for embedding small assets directly inside source code, configuration, JSON, HTML, test fixtures, or scripts.
- **Optional password protection** — add a password before creating Senvra/TXT/ZIP output when the contents should stay private between sender and receiver.

## Common uses

### Embed an image or file directly in source code

The **Base64** action is useful when a project should not depend on a separate small asset file.

For example, copy an image as Base64 with Senvra and place it directly in a Python variable:

```python
import base64

ASSET_B64 = "PASTE_BASE64_HERE"
asset_bytes = base64.b64decode(ASSET_B64)
```

Now `asset_bytes` contains the original file bytes and can be passed to code that accepts in-memory bytes, or written back only when needed:

```python
from pathlib import Path

Path("asset.png").write_bytes(asset_bytes)
```

This can be useful for:

- small icons and images
- embedded templates or configuration files
- certificates or public test assets
- fixtures used by automated tests
- single-file Python utilities
- HTML/CSS data assets
- small resources that should travel with the source code

For an HTML image data URI, add the appropriate MIME prefix yourself, for example:

```html
<img src="data:image/png;base64,PASTE_BASE64_HERE" alt="Embedded image">
```

> **Base64 is not a hash, encryption, or compression.** It is a reversible text representation of the original bytes and is usually about one-third larger than the binary file. Use it mainly for portability and embedding small files.

### Send a file through a restrictive uploader

If a service refuses the original extension, create a **ZIP output** with Senvra. ZIP is accepted by many upload forms and messaging systems, so it can be a practical compatibility option when direct upload is difficult.

This is particularly useful in everyday workflows in Iran, where different local and international uploaders can have inconsistent extension policies. Senvra does not bypass a service's rules; it simply gives you standard transport formats that may already be accepted by that service.

### Send a file as text

A file can also be exported as **TXT**. This is useful when you want to move data through a text-friendly channel, paste it into a message, or store it somewhere that handles text more easily than arbitrary files.

The receiver opens the text with Senvra and restores the original file.

> Text mode changes how the file is represented; by itself it is not a secrecy mechanism. If privacy matters, enable password protection before creating the output.

### Protect a file before sending it

Enable password protection, create the Senvra/TXT/ZIP output, and share the password separately with the intended receiver. The recipient can then restore the original file using Senvra.

Base64 is intentionally separate from this protected transport workflow: the Base64 action represents the **original file** directly for developer use.

### Keep processing local

Senvra performs its conversion in the browser. The application itself does not need to upload your selected file to a remote processing service.

---

## How to use

1. Open `index.html` in a modern browser.
2. Choose **Convert**.
3. Select or drop a file.
4. Choose what you need:
   - **Download Senvra** for the native portable format.
   - **Download TXT** when a text representation is easier to send.
   - **Download ZIP** for broad uploader compatibility.
   - **Base64** to copy the original file as standard Base64 text for embedding in code.
5. Optionally enable password protection or generate a **Random Pass** before creating Senvra/TXT/ZIP output.
6. To restore a Senvra/TXT/ZIP package, switch to **Restore**, load the received file or paste its text, enter the password if one was used, and restore the original file.

No installation is required.

---

## Privacy & security

Senvra is built around a straightforward idea: **keep the file under the user's control as much as possible.**

- File processing is performed locally in the browser.
- Password protection is optional for the Senvra transport formats.
- Passwords are not meant to be embedded into the protected file.
- The application includes integrity checks when restoring supported Senvra files.
- Base64 is a developer/transport representation and should not be treated as a security feature.
- Senvra does not claim to hide operating-system history, browser history, clipboard history, downloaded files, screenshots, malware, or access by someone who already controls your device.

Public documentation intentionally describes the security model at a high level. See [`SECURITY.md`](SECURITY.md) for reporting guidance.

---

## Compatibility

Senvra 1.x creates the `.senvra` format and can also restore supported legacy `.poimu` files from the earlier project version.

The interface is available in **English and Persian**.

## What Senvra is not

Senvra is not a cloud drive, anonymous communication network, malware-hiding tool, or a way to bypass laws or platform policies. It is a local file conversion, transport, and developer utility. Users remain responsible for the files they process and for the rules of the services they use.

## Project structure

```text
Senvra/
├── index.html                  # Complete application — HTML, CSS and JavaScript in one file
├── examples/
│   └── base64_embed.py         # Minimal Python Base64 embedding example
├── README.md                   # Project overview and usage
├── SECURITY.md                 # Security policy
├── CHANGELOG.md                # Release history
├── LICENSE                     # MIT License
└── .nojekyll                   # Keeps GitHub Pages serving the files as-is
```

## Running locally

Clone or download this repository, then open:

```text
index.html
```

in a modern browser.

There is no build step, package manager, framework, CDN, or external runtime dependency required for the application itself.

## Version

**Senvra 1.1**

## License

Senvra is released under the **MIT License**. See [`LICENSE`](LICENSE).

---

## فارسی

**Senvra** ابزاری ساده و محلی برای تبدیل، رمزدار کردن، ارسال، بازیابی و استفاده از فایل‌ها در پروژه‌های برنامه‌نویسی است که مستقیماً داخل مرورگر اجرا می‌شود.

یکی از کاربردهای اصلی آن زمانی است که ارسال نوع خاصی از فایل سخت است. این موضوع به‌خصوص برای کاربران داخل ایران می‌تواند کاربردی باشد، چون سرویس‌ها و آپلودرهای مختلف محدودیت‌های متفاوتی روی پسوند فایل دارند.

- اگر فایل اصلی آپلود نمی‌شود، می‌توانید خروجی **ZIP** بگیرید؛ ZIP معمولاً توسط آپلودرهای بیشتری پذیرفته می‌شود.
- می‌توانید فایل را به شکل **TXT** تبدیل کنید و آن را مثل متن ذخیره، کپی یا ارسال کنید؛ دریافت‌کننده با Senvra فایل اصلی را برمی‌گرداند.
- اگر فایل خصوصی است، قبل از خروجی گرفتن **رمز** بگذارید و رمز را از یک مسیر جداگانه برای دریافت‌کننده بفرستید.
- با گزینه **Base64** می‌توانید بایت‌های فایل اصلی را به متن Base64 تبدیل و کپی کنید. این قابلیت برای قرار دادن عکس، آیکن یا فایل‌های کوچک مستقیماً داخل کد Python، HTML، JSON یا پروژه‌های تک‌فایلی کاربردی است و وابستگی به فایل جانبی را کم می‌کند.
- پردازش فایل داخل مرورگر انجام می‌شود و خود Senvra برای تبدیل فایل نیازی به ارسال آن به سرور پردازشی ندارد.

**نکته:** Base64 هش، رمزگذاری یا فشرده‌سازی نیست و برای امنیت طراحی نشده است؛ یک نمایش متنی برگشت‌پذیر از بایت‌های فایل است. همچنین خروجی TXT به‌تنهایی به معنی محرمانه‌بودن نیست. اگر فقط شما و دریافت‌کننده باید بتوانید محتوای فایل را بازیابی کنید، از حالت رمزدار استفاده کنید.

---

**Senvra · by POIMU**

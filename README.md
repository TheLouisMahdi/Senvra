# Senvra

**A simple, local-first way to convert, protect, send, represent, and restore files directly in your browser.**

> *“The file asked: If I’m never uploaded, do I still exist? — Senvra replied: Easy, Descartes. You’re just being converted.”*

Senvra is a single-file browser tool for working with ordinary files, `.senvra` packages, TXT, ZIP, and standard Base64. It runs locally in the browser and is designed to keep everyday file conversion simple without requiring an installed application or a processing server.

**Created by POIMU · [TheLouisMahdi](https://github.com/TheLouisMahdi)**

---

## What Senvra does

Senvra lets the same file move between several practical forms:

- **Normal file → Senvra** — create a portable `.senvra` file.
- **Normal file → Base64** — copy the original file as standard Base64 text.
- **Base64 → Senvra** — paste ordinary Base64 and create a `.senvra` file from it.
- **Base64 → file** — paste Base64 and restore the underlying file bytes.
- **Senvra → TXT** — carry a Senvra package as ordinary text.
- **Senvra → ZIP** — wrap it in a widely supported ZIP container.
- **Optional password** — protect Senvra/TXT/ZIP output when privacy matters.

Base64 is treated as a normal input/output format rather than a separate developer-only feature.

## Why Senvra?

Sometimes the difficult part is not creating a file — it is getting that file through the service where you need to send it.

Messaging apps, upload forms, email systems, educational portals, company systems, and other services may reject certain extensions or handle some file types poorly. This can be especially noticeable for users in Iran, where a file may need to pass through several local and international services with different upload rules.

Senvra gives you alternative representations without changing the original contents.

### Use ZIP when the original extension is difficult to upload

If an uploader refuses the original file type, Senvra can create a **ZIP** output. ZIP is broadly supported by uploaders and messaging services, so it is often easier to send than an unusual or blocked extension.

Senvra uses ZIP mainly for compatibility. It does not promise that ZIP will make the file smaller, and it does not claim that every service will accept every ZIP file.

### Send a file as text

Senvra can create a **TXT** representation of a Senvra package. This is useful when a text-friendly channel is easier to use than a binary-file upload.

The receiver can paste or open that text in Senvra and restore the original file.

> TXT changes how the data is carried. By itself, it is not a secrecy feature. Use password protection when the contents need to stay private.

### Work directly with ordinary Base64

You can paste standard Base64 into Senvra and use it like another form of the file.

For example, this is accepted:

```text
Senvra
iVBORw0KGgoAAAANSUhEUg...
```

The first line can simply be a label. Raw Base64, `Base64:` labels, and common `data:...;base64,...` values are also supported.

When possible, Senvra recognizes common file types from the decoded bytes, such as PNG, JPEG, GIF, WebP, PDF, ZIP, audio, and video formats. If the original filename or type is not available, Senvra uses a safe generic name and falls back to `.bin` when the type cannot be identified.

Base64 can also be copied from any normal file selected in Senvra. This can be useful for sending text, storing small resources in source code or configuration, or moving a file through a text-only workflow.

> Base64 is not a hash, encryption, or compression. It is a reversible text representation of the original bytes and normally takes more space than the binary file.

### Protect a file before sending it

Password protection can be enabled before creating Senvra, TXT, or ZIP output. Share the password separately with the intended receiver.

The receiver opens the protected output in Senvra, enters the password, and restores the original file.

### Keep processing local

Senvra performs its work inside the browser. The application itself does not need to upload the selected file to a remote processing service.

---

## How to use

### Start from a normal file

1. Open `index.html` in a modern browser.
2. Choose **Convert file**.
3. Select or drop any supported-size file.
4. Optionally enable a password or create a **Random Pass**.
5. Choose the output you need:
   - **Download Senvra**
   - **Download TXT**
   - **Download ZIP**
   - **Copy Base64**

### Start from Base64

1. Open **Convert file**.
2. Paste standard Base64 into the text-input box.
3. Press **Use text**.
4. Senvra reconstructs the bytes and treats them like a normal input file.
5. Create Senvra/TXT/ZIP output or copy Base64 again as needed.

### Restore Senvra or Base64

Open **Restore file** and either:

- load `.senvra`, supported legacy `.poimu`, TXT, ZIP, `.b64`, or `.base64`; or
- paste Senvra text or raw Base64 directly.

For raw Base64, Senvra restores the decoded file bytes and detects common file types where possible.

For a protected Senvra package, enter the password before restoring.

No installation or build step is required.

---

## Privacy & security

Senvra follows a simple principle: **keep file processing under the user's control as much as possible.**

- File conversion is performed locally in the browser.
- Password protection is optional for Senvra transport formats.
- The password is kept separate from the protected output.
- Restored Senvra files are checked for integrity.
- Base64 and TXT should be treated as representations or transport formats, not as security by themselves.
- Senvra cannot protect data from someone who already controls your device, browser session, clipboard, downloads, screenshots, backups, or operating-system history.

Public documentation intentionally keeps security implementation details high-level. The source code remains available for review.

See [`SECURITY.md`](SECURITY.md) for reporting guidance.

---

## Compatibility

Senvra 1.2 creates the `.senvra` format and supports:

- `.senvra`
- supported legacy `.poimu`
- Senvra TXT
- Senvra ZIP
- standard Base64 text
- `.b64` and `.base64` text files
- common Base64 data URIs

The interface is available in **Persian and English**.

## What Senvra is not

Senvra is not a cloud drive, anonymous communication network, malware-hiding tool, or a promise that a service will accept a file that violates its rules. It is a local file conversion and transport utility. Users remain responsible for the files they process and for the policies of the services they use.

## Project structure

```text
Senvra/
├── index.html      # Complete application — HTML, CSS and JavaScript in one file
├── README.md       # Project overview and usage
├── SECURITY.md     # Security policy
├── CHANGELOG.md    # Release history
├── LICENSE         # MIT License
└── .nojekyll       # Keeps GitHub Pages serving the files as-is
```

## Running locally

Clone or download the repository and open:

```text
index.html
```

in a modern browser.

There is no package manager, framework, CDN, build step, or external runtime dependency required for the application itself.

## Version

**Senvra 1.2**

## License

Senvra is released under the **MIT License**. See [`LICENSE`](LICENSE).

---

## فارسی

**Senvra** یک ابزار ساده و محلی برای تبدیل، رمزدار کردن، ارسال و بازگردانی فایل است که مستقیماً داخل مرورگر اجرا می‌شود.

ورودی فقط فایل نیست؛ **Base64 معمولی هم یک ورودی عادی Senvra است.** می‌توانید یک فایل را انتخاب کنید یا Base64 آن را Paste کنید و بعد از همان داده خروجی Senvra، TXT، ZIP یا Base64 بگیرید.

### کاربردهای مهم

- اگر یک سایت یا پیام‌رسان پسوند فایل اصلی را قبول نمی‌کند، می‌توانید خروجی **ZIP** بگیرید. ZIP توسط سرویس‌های بسیار بیشتری پشتیبانی می‌شود و مخصوصاً در بعضی روندهای ارسال فایل داخل ایران می‌تواند کاربردی باشد.
- می‌توانید فایل را به شکل **TXT** منتقل کنید و دریافت‌کننده آن را دوباره با Senvra بازگرداند.
- می‌توانید **Base64 خام** را مستقیم Paste کنید؛ حتی متنی مثل `Senvra` یا `Base64:` در خط اول قابل قبول است.
- می‌توانید از یک فایل معمولی **Base64 استاندارد** بگیرید.
- اگر فایل خصوصی است، قبل از ساخت Senvra/TXT/ZIP روی آن **رمز** بگذارید و رمز را جداگانه برای دریافت‌کننده بفرستید.
- پردازش فایل برای تبدیل و بازگردانی داخل مرورگر انجام می‌شود و Senvra برای این کار نیازی به آپلود فایل به سرور پردازشی ندارد.

**نکته:** Base64 و TXT به‌تنهایی امنیت ایجاد نمی‌کنند. اگر محتوا باید محرمانه بماند، از قابلیت رمز Senvra استفاده کنید.

---

**Senvra · by POIMU**

# Senvra

**A simple, local-first way to convert, protect, send, and restore files — directly in your browser.**

> *“The file asked: If I’m never uploaded, do I still exist? — Senvra replied: Easy, Descartes. You’re just being converted.”*

Senvra is a single-file browser tool for turning ordinary files into formats that can be easier to store, move, paste, or send. It runs locally in the browser and is designed for people who want a simple workflow without installing an application or uploading their file to a processing server.

**Created by POIMU · [TheLouisMahdi](https://github.com/TheLouisMahdi)**

---

## Why Senvra?

Sometimes the hard part is not the file itself — it is getting the file through the place you need to send it.

Messaging apps, upload forms, email gateways, corporate systems, educational portals, and other services may reject certain file extensions or make some file types inconvenient to transfer. This can be especially noticeable for users in Iran, where people may regularly move files through a mix of local and international services with different upload restrictions.

Senvra gives the same file several practical ways to travel:

- **Senvra file (`.senvra`)** — the native portable form.
- **ZIP (`.zip`)** — useful when an uploader accepts ZIP more easily than the original file type. Senvra uses ZIP as a compatibility wrapper; it is not intended as a promise of smaller file size.
- **Text (`.txt`)** — represents the file as ordinary text, so it can be saved, copied, pasted, or sent through places where binary files are inconvenient.
- **Optional password protection** — add a password before creating the output when the contents should stay private between sender and receiver.

## Common uses

### Send a file through a restrictive uploader

If a service refuses the original extension, create a **ZIP output** with Senvra. ZIP is widely accepted by upload forms and messaging systems, so it can be a practical compatibility option when direct upload is difficult.

### Send a file as text

A file can also be exported as **TXT**. This is useful when you want to move data through a text-friendly channel, paste it into a message, or store it somewhere that handles text more easily than arbitrary files.

The receiver opens the text with Senvra and restores the original file.

> Text mode changes how the file is represented; by itself it is not a secrecy mechanism. If privacy matters, enable password protection before creating the output.

### Protect a file before sending it

Enable password protection, create the Senvra/TXT/ZIP output, and share the password separately with the intended receiver. The recipient can then restore the original file using Senvra.

### Keep processing local

Senvra performs its conversion in the browser. The application itself does not need to upload your selected file to a remote processing service.

---

## How to use

1. Open `index.html` in a modern browser.
2. Choose **Convert**.
3. Select or drop a file.
4. Optionally enable a password or generate a **Random Pass**.
5. Download the format that fits your situation:
   - `.senvra`
   - `.txt`
   - `.zip`
6. Send the output to the receiver.
7. The receiver opens Senvra, switches to **Restore**, loads the received file or pastes the text, enters the password if one was used, and restores the original file.

No installation is required.

---

## Privacy & security

Senvra is built around a straightforward idea: **keep the file under the user's control as much as possible.**

- File processing is performed locally in the browser.
- Password protection is optional.
- Passwords are not meant to be embedded into the protected file.
- The application includes integrity checks when restoring supported Senvra files.
- Senvra does not claim to hide operating-system history, browser history, clipboard history, downloaded files, screenshots, malware, or access by someone who already controls your device.

For implementation-level security details, please review the source code. Public documentation intentionally describes the security model at a high level rather than publishing a step-by-step internal design.

See [`SECURITY.md`](SECURITY.md) for security reporting guidance.

---

## Compatibility

Senvra v1.0 creates the new `.senvra` format and can also restore supported legacy `.poimu` files from the earlier project version.

The interface is available in **English and Persian**.

## What Senvra is not

Senvra is not a cloud drive, anonymous communication network, malware-hiding tool, or a way to bypass laws or platform policies. It is a local file conversion and transport utility. Users remain responsible for the files they process and for the rules of the services they use.

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

Clone or download this repository, then open:

```text
index.html
```

in a modern browser.

There is no build step, package manager, framework, CDN, or external runtime dependency required for the application itself.

## Version

**Senvra 1.0**

## License

Senvra is released under the **MIT License**. See [`LICENSE`](LICENSE).

---

## فارسی

**Senvra** ابزاری ساده و محلی برای تبدیل، رمزدار کردن، ارسال و بازیابی فایل است که مستقیماً داخل مرورگر اجرا می‌شود.

یکی از کاربردهای اصلی آن زمانی است که ارسال نوع خاصی از فایل سخت است. این موضوع به‌خصوص برای کاربران داخل ایران می‌تواند کاربردی باشد، چون سرویس‌ها و آپلودرهای مختلف محدودیت‌های متفاوتی روی پسوند فایل دارند.

- اگر فایل اصلی آپلود نمی‌شود، می‌توانید خروجی **ZIP** بگیرید؛ ZIP معمولاً توسط آپلودرهای بیشتری پذیرفته می‌شود.
- می‌توانید فایل را به شکل **TXT** تبدیل کنید و آن را مثل متن ذخیره، کپی یا ارسال کنید؛ دریافت‌کننده با Senvra فایل اصلی را برمی‌گرداند.
- اگر فایل خصوصی است، قبل از خروجی گرفتن **رمز** بگذارید و رمز را از یک مسیر جداگانه برای دریافت‌کننده بفرستید.
- پردازش فایل داخل مرورگر انجام می‌شود و خود Senvra برای تبدیل فایل نیازی به ارسال آن به سرور پردازشی ندارد.

**نکته:** خروجی TXT به‌تنهایی به معنی محرمانه‌بودن نیست. اگر فقط شما و دریافت‌کننده باید بتوانید محتوای فایل را بازیابی کنید، از حالت رمزدار استفاده کنید.

---

**Senvra · by POIMU**

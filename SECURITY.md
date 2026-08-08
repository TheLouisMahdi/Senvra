# Security Policy

Senvra is designed as a local-first browser tool. Its public documentation intentionally keeps implementation details high-level while the source remains available for review.

## Supported version

| Version | Supported |
| --- | --- |
| 1.x | Yes |

## Security principles

- Keep file processing local to the browser whenever possible.
- Make password protection optional and easy to use.
- Keep the password separate from the protected output.
- Check restored files for unexpected modification or corruption.
- Avoid external runtime dependencies in the application itself.
- Keep the application usable as a single local HTML file.

## Important limitations

Senvra cannot protect a file from someone who already controls your device, browser session, clipboard, downloaded files, screenshots, backups, or operating-system history.

Text export is a transport format, not a confidentiality feature by itself. Use password protection when the contents need to remain private.

## Reporting a security issue

Please do not publish sensitive exploit details in a public issue.

If GitHub private vulnerability reporting is available for this repository, use it. Otherwise, contact the maintainer privately through the contact information associated with the GitHub account before publishing technical details.

When reporting a problem, include the affected Senvra version, browser/OS, a minimal reproduction, and the expected versus observed behavior. Do not include real private files, real passwords, or personal data in a report.

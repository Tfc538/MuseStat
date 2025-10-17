# Security Policy

## Supported Versions

We currently support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of MuseStat seriously. If you discover a security vulnerability, please follow these steps:

### How to Report

**Please DO NOT report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of the following methods:

1. **Email**: Send details to [post@tim-gatzke.de](mailto:post@tim-gatzke.de)
2. **GitHub Security Advisory**: Use the [Security tab](https://github.com/Tfc538/MuseStat/security/advisories) to privately report vulnerabilities

### What to Include

When reporting a vulnerability, please include:

- **Description**: Clear description of the vulnerability
- **Impact**: What an attacker could potentially do
- **Steps to Reproduce**: Detailed steps to reproduce the issue
- **Affected Versions**: Which versions are affected
- **Proposed Fix**: If you have suggestions for fixing it
- **Your Contact Info**: So we can follow up with questions

### What to Expect

- **Acknowledgment**: Within 48 hours of your report
- **Initial Assessment**: Within 5 business days
- **Status Updates**: Regular updates on progress
- **Resolution Timeline**: We aim to resolve critical issues within 30 days
- **Credit**: Public acknowledgment (unless you prefer to remain anonymous)

## Security Considerations

### File Handling

MuseStat reads and processes manuscript files. While the tool is designed to be safe:

- **Untrusted Files**: Be cautious when analyzing files from unknown sources
- **File Formats**: DOCX and RTF files are parsed by third-party libraries (python-docx, striprtf)
- **Permissions**: MuseStat does not require elevated permissions

### Data Privacy

- **No Data Collection**: MuseStat does not send your manuscript data anywhere
- **Local Processing**: All analysis happens locally on your machine
- **Version Checking**: Only checks GitHub API for latest version (no manuscript data sent)
- **Export Files**: Export files (JSON, CSV, HTML) are saved locally only

### Dependencies

MuseStat relies on several third-party packages:
- `rich` - Terminal formatting
- `python-docx` - Word document reading
- `striprtf` - RTF file reading
- `langdetect` - Language detection
- `textstat` - Readability metrics
- `requests` - Version checking
- `questionary` - Interactive TUI

We regularly monitor these dependencies for known vulnerabilities.

## Best Practices for Users

- **Keep Updated**: Always use the latest version
- **Verify Downloads**: Download executables only from official GitHub releases
- **Check Hashes**: Verify file integrity (when provided)
- **Source Installation**: If building from source, use official repository

## Disclosure Policy

- Security vulnerabilities will be disclosed after a fix is available
- Critical vulnerabilities will be disclosed with security advisories
- Users will be notified through GitHub releases
- CHANGELOG will document security fixes

## Acknowledgments

We appreciate the security research community's efforts to responsibly disclose vulnerabilities.

---

Thank you for helping keep MuseStat and its users safe!


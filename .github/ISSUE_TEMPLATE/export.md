---
name: Export/Output Issue
about: Report problems with exports (JSON, CSV) or terminal output
title: '[EXPORT] '
labels: export, output
assignees: ''
---

## Export Issue

A clear description of the export or output problem.

## Issue Type

What kind of output issue is this?
- [ ] Export fails with error
- [ ] Exported file is corrupted/unreadable
- [ ] Missing data in export
- [ ] Incorrect data in export
- [ ] Formatting issues in export
- [ ] Terminal output incorrect
- [ ] Terminal display issues
- [ ] Unicode/encoding problems
- [ ] Colors/formatting not showing correctly
- [ ] Other: ___________

## Export Format

Which output format is affected?
- [ ] JSON export
- [ ] CSV export
- [ ] Terminal display (compact mode)
- [ ] Terminal display (semi-compact mode)
- [ ] Terminal display (full mode)
- [ ] Verification mode output

## Environment

- **OS**: [e.g., Windows 11, Ubuntu 22.04, macOS 14]
- **MuseStat Version**: [run `musestat --version`]
- **Terminal/Shell**: [e.g., PowerShell 7, Windows Terminal, bash, zsh, iTerm2]
- **Terminal Encoding**: [if known, e.g., UTF-8]

## Manuscript Details

- **File Format**: [.md / .txt / .docx / .rtf]
- **File Size**: [e.g., 500KB]
- **Word Count**: [approximate]
- **Special Characters**: [Unicode, emojis, accented characters, non-English text]

## Command Used

```bash
# The exact command you ran
musestat -f mybook.docx --export json --output stats.json
```

## Expected Output

What should the output look like or contain?

```
# Describe or show expected format/content
```

## Actual Output

What does it actually look like?

```
# Paste actual output, error message, or attach exported file
```

## Error Messages

```
# Paste any error messages or warnings
```

## Terminal Display Issues (if applicable)

For terminal display problems, please describe:
- [ ] Colors not showing
- [ ] Tables misaligned
- [ ] Text truncated
- [ ] Unicode characters showing as boxes/question marks
- [ ] Progress bars not working
- [ ] Panels not rendering correctly
- [ ] Charts/graphs not displaying

## Screenshots

<!-- For display issues, screenshots are very helpful -->

## Exported File Issues (if applicable)

If exporting to file:
- **Can file be opened?**: [yes / no]
- **File size**: [e.g., 0 bytes, too large, normal]
- **File permissions**: [can you read it?]
- **Output path**: [absolute or relative path used]

### JSON Export Issues
- [ ] Invalid JSON syntax
- [ ] Missing fields
- [ ] Incorrect data types
- [ ] Encoding errors
- [ ] Cannot parse with JSON tools

### CSV Export Issues
- [ ] Delimiter problems
- [ ] Missing headers
- [ ] Missing rows
- [ ] Incorrect formatting
- [ ] Cannot open in Excel/LibreOffice

## Reproducibility

Does this happen:
- [ ] Every time with this file
- [ ] Every time with any file
- [ ] Only with certain file formats
- [ ] Only with certain display modes
- [ ] Only with certain export formats
- [ ] Intermittently

## Steps to Reproduce

1. 
2. 
3. 

## Comparison

Have you tested:
- [ ] Different export formats (which ones work?)
- [ ] Different display modes (which ones work?)
- [ ] Different files (does it happen with all?)
- [ ] Different terminal emulators (same issue?)

## Terminal Configuration

### Windows
- [ ] Windows Terminal
- [ ] PowerShell (version: _____)
- [ ] Command Prompt
- [ ] WSL (Ubuntu/other: _____)
- [ ] Git Bash
- [ ] Other: ___________

### macOS
- [ ] Terminal.app
- [ ] iTerm2
- [ ] Hyper
- [ ] Alacritty
- [ ] Other: ___________

### Linux
- [ ] gnome-terminal
- [ ] konsole
- [ ] xterm
- [ ] Alacritty
- [ ] Terminator
- [ ] Other: ___________

## Encoding Settings

Have you checked your terminal encoding?
- **Current encoding**: [e.g., UTF-8, ISO-8859-1, Windows-1252]
- **Can be changed?**: [yes / no / don't know]

## Workarounds

Have you found any workarounds?

## Expected Files

<!-- If applicable, attach: -->
- [ ] Sample exported file (with issue)
- [ ] Screenshot of terminal output
- [ ] Example of what correct output should be

## Additional Context

<!-- Any other relevant information -->

## Checklist

- [ ] I have specified which export format/display mode has issues
- [ ] I have included the exact command used
- [ ] I have provided error messages or actual output
- [ ] I have described what the output should be
- [ ] I have tested with the latest version



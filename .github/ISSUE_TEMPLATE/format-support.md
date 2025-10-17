---
name: File Format Support Request
about: Request support for a new file format or improve existing format handling
title: '[FORMAT] '
labels: enhancement, file-format
assignees: ''
---

## File Format Request

Which file format do you want supported or improved?

- **Format**: [e.g., .epub, .odt, .pages, .scrivener]
- **Full Name**: [e.g., EPUB (Electronic Publication)]
- **MIME Type**: [if known, e.g., application/epub+zip]

## Current Status

Is this format:
- [ ] Not supported at all (new format request)
- [ ] Partially supported (what works? what doesn't?)
- [ ] Supported but has issues (describe issues)

## Use Case

Why do you need this format supported?

**Example:**
> As a writer using [software name], my manuscripts are in [format]. I need MuseStat to analyze them without converting to another format first.

## Format Details

### Technical Information

- **Open Standard**: [yes / no / partially]
- **Proprietary**: [yes / no]
- **Text-based**: [yes / no / mixed]
- **Structured**: [yes / no - XML, JSON, binary, etc.]
- **Documentation**: [is format specification publicly available?]

### Common Tools

What tools create/use this format?
- **Creation tools**: [e.g., Scrivener, Microsoft Word, Google Docs]
- **Popular with**: [e.g., fiction writers, technical writers, academic writers]
- **Platform**: [Windows / macOS / Linux / Web / All]

## Format Characteristics

What makes this format unique or challenging?
- [ ] Contains metadata
- [ ] Supports rich formatting
- [ ] Includes images/media
- [ ] Multi-file/container format
- [ ] Compressed archive
- [ ] Encrypted/protected
- [ ] Multiple document sections
- [ ] Version differences
- [ ] Custom styles/themes
- [ ] Embedded fonts
- [ ] Comments/annotations
- [ ] Track changes
- [ ] Other: ___________

## Current Workflow

How do you currently work around this limitation?
- [ ] Manually convert to .txt/.md/.docx
- [ ] Use external conversion tools
- [ ] Export from original software
- [ ] Copy and paste
- [ ] No workaround (can't use MuseStat)

What conversion tools do you use?
- **Tool**: [e.g., Pandoc, Calibre, LibreOffice]
- **Quality**: [does conversion preserve text accurately?]
- **Issues**: [what gets lost in conversion?]

## What Should Be Preserved

When reading this format, what's important to preserve?
- [ ] Plain text content
- [ ] Chapter divisions
- [ ] Paragraph breaks
- [ ] Dialogue formatting
- [ ] Emphasis (bold/italic)
- [ ] Headers/titles
- [ ] Scene breaks
- [ ] Comments/notes
- [ ] Metadata (author, title, etc.)
- [ ] Custom tags/markers

## Python Libraries

Do you know of Python libraries that can read this format?
- **Library name**: [e.g., ebooklib, python-docx]
- **PyPI link**: [if available]
- **License**: [if known]
- **Quality**: [is it well-maintained?]

## Sample Files

Can you provide sample files in this format?
- [ ] Yes, I can attach a sample
- [ ] Yes, available online at: [URL]
- [ ] Can create a sample
- [ ] Cannot share due to privacy
- [ ] Available in format specification

<!-- If you can share, attach or link sample files -->

## Expected Behavior

How should MuseStat handle this format?
<!-- Describe what you expect to happen when analyzing this format -->

## Parsing Challenges

Are there known challenges with this format?
- [ ] Complex binary structure
- [ ] Proprietary/undocumented
- [ ] Requires specialized libraries
- [ ] Format varies by version
- [ ] Compressed/encrypted
- [ ] Contains non-text content
- [ ] Multiple parsing methods needed

## Priority

How important is this to your workflow?
- [ ] Critical - can't use MuseStat without it
- [ ] High - significant inconvenience
- [ ] Medium - would be nice to have
- [ ] Low - rarely need it

## User Base

Who else might benefit from this?
- [ ] Scrivener users
- [ ] Academic writers (LaTeX, etc.)
- [ ] E-book authors (EPUB, MOBI)
- [ ] Technical writers
- [ ] Business writers
- [ ] Specific writing community: ___________

## Alternative Solutions

Are there alternatives you've considered?
- [ ] Pre-processing script
- [ ] Format conversion workflow
- [ ] Plugin system
- [ ] External tool integration

## Implementation Willingness

Are you willing to:
- [ ] Help test format support
- [ ] Provide sample files
- [ ] Review documentation
- [ ] Contribute code (if possible)
- [ ] Fund development
- [ ] Research format specifications

## Compatibility

Should this work with:
- [ ] All MuseStat features
- [ ] Basic analysis only
- [ ] Specific features: ___________

## Related Formats

Are there related formats to consider?
<!-- e.g., .doc and .docx, .mobi and .epub -->

## Additional Context

<!-- Any other relevant information, links, or resources -->

## Checklist

- [ ] I have clearly specified the file format
- [ ] I have explained why this format is needed
- [ ] I have researched available Python libraries (if any)
- [ ] I have described the current workaround (if any)
- [ ] I understand this may require significant development effort



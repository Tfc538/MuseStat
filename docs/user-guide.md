# 📚 MuseStat v2.1 - Complete Guide

**Your comprehensive manuscript analysis & verification toolkit**

---

## 🚀 Quick Start

```bash
# Daily writing check (RECOMMENDED)
python musestat.py -sc

# Verify for publishing
python musestat.py -v

# Full analysis
python musestat.py

# Help
python musestat.py --help
```

---

## 📖 Table of Contents

1. [Installation](#installation)
2. [All Display Modes](#all-display-modes)
3. [Verification Mode](#verification-mode-new)
4. [Ignore Patterns](#ignore-patterns-new)
5. [Export & Compare](#export--compare)
6. [Advanced Features](#advanced-features)
7. [Achievement System](#achievement-system)
8. [CLI Reference](#cli-reference)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

---

## 📦 Installation

### Basic Installation
```bash
# Install base requirements
pip install rich

# Or from requirements.txt
pip install -r requirements.txt
```

### Optional Dependencies
```bash
# For .docx support
pip install python-docx

# For .rtf support
pip install striprtf

# For advanced features
pip install langdetect textstat
```

---

## 🎨 All Display Modes

### 1. Semi-Compact (`-sc`) ⭐ **RECOMMENDED**
```bash
python musestat.py -sc
```

**Shows:**
- Overview statistics (words, pages, reading time)
- Milestone progress bars
- Achievement badge
- Motivational quote
- Chapter statistics summary

**Best for**: Daily writing routine, evening check-ins

**Output Preview:**
```
╔═══ MuseStat - Manuscript Analytics ═══╗

Manuscript Overview  |  Writing Milestones Progress
─────────────────────┼─────────────────────────────
Words: 112,800       |  ✓ 📘 Novel (Standard)
Pages: 376 avg       |  ████████████████ 100%
Reading Time: 6-9h   |  
Chapters: 33         |  ○ 📚 Epic Novel
                     |  ██████████████░░ 94%

╔═ Achievement ══════╗  ╭─ Writer's Wisdom ──╮
║ ✨ Expanded Novel   ║  │ Motivational quote │
╚════════════════════╝  ╰────────────────────╯
```

---

### 2. Verify (`-v`) 🆕 **FOR PUBLISHING**
```bash
python musestat.py -v
```

**Shows:**
- 12 comprehensive check categories
- Errors, warnings, info
- Top issues summary
- Detailed issue tables
- Ignore patterns status

**Best for**: Pre-submission, quality control, final review

**Output Preview:**
```
╭─ Verification Checks ─────╮  ╭─ Results Summary ───╮
│ 12 Comprehensive Checks:  │  │ 🔴 Errors:     12   │
│ 1. Markdown Formatting    │  │ ⚠️  Warnings:    3   │
│ 2. Pre-publish Markers    │  │ ℹ️  Info:        8   │
│ 3. Repeated Words         │  │                     │
│ ...                       │  │ Top Issues:         │
╰───────────────────────────╯  │ • Pre-publish: 11   │
                                ╰─────────────────────╯

🔴 ERRORS (12)
[Detailed issue table with line numbers, suggestions]
```

---

### 3. Compact (`-c`) **QUICK CHECK**
```bash
python musestat.py -c
```

**Shows:**
- Essential stats only
- Inline badge
- Milestone indicator
- Quick motivational quote

**Best for**: Ultra-fast checks, multiple files

---

### 4. Full (default) **DEEP ANALYSIS**
```bash
python musestat.py
```

**Shows:**
- Complete overview
- All milestones
- ALL chapters (detailed)
- Word frequency (top 15)
- Achievement badge
- Motivational quote

**Best for**: Weekly reviews, comprehensive analysis

---

### 5. Advanced (`-a`) **EDITORIAL REVIEW**
```bash
python musestat.py -a
```

**Shows Everything from Full PLUS:**
- 5 Readability scores
- Pacing analysis
- Dialogue statistics
- Language detection

**Best for**: Editorial review, submission preparation

---

### 6. Minimalist (`-m`) **AUTOMATION**
```bash
python musestat.py -m
```

**Output:**
```
Words: 112,800
Characters: 609,595
Sentences: 8,621
Paragraphs: 3,513
Chapters: 33
Reading Time: 6h 16m - 9h 24m
Pages: 322-451 pages (~376 avg)
Chapter Avg: 3414 ± 1691 words
```

**Best for**: Scripts, editor integration, CI/CD

---

## 🔍 Verification Mode (NEW!)

### What Gets Checked

**12 Comprehensive Categories:**

1. ✅ **Markdown Formatting**
   - Unmatched `*`, `**`, `_`
   - Triple asterisks
   - Bold/italic completeness

2. ✅ **Pre-publish Markers**
   - TODO, FIXME, HACK, NOTE:
   - TK, TBD, PLACEHOLDER, XXX

3. ✅ **Repeated Words**
   - the the, a a, and and
   - to to, of of, in in, it it

4. ✅ **Punctuation**
   - Multiple !!/??
   - Space before punctuation
   - Ellipsis issues (4+ dots)
   - Em-dash vs hyphen

5. ✅ **Whitespace**
   - Trailing whitespace
   - Multiple spaces
   - Tab characters

6. ✅ **Heading Structure**
   - Missing space after #
   - Skipped levels (H1 → H3)
   - Proper hierarchy

7. ✅ **Smart Quotes**
   - Consistency checking
   - Mixed straight/curly

8. ✅ **Markdown Links**
   - Unmatched brackets []
   - Link completeness

9. ✅ **Paragraph Spacing**
   - Excessive blank lines (3+)

10. ✅ **Line Length**
    - Very long lines (>1000 chars)

11. ✅ **Dialogue Quotes**
    - Quote consistency

12. ✅ **Incomplete Content**
    - [INSERT...] placeholders
    - Lorem Ipsum text

### Issue Levels

**🔴 ERRORS** - Critical, must fix before publishing
**⚠️ WARNINGS** - Quality issues, should review
**ℹ️ INFO** - Style suggestions, optional

### Running Verification

```bash
# Basic verification
python musestat.py -v

# With specific file
python musestat.py -f mybook.md -v

# Export verification results
python musestat.py -v --export html
```

---

## 🚫 Ignore Patterns (NEW!)

### Creating `.musestatignore`

```bash
# Copy example file
cp .musestatignore.example .musestatignore

# Edit to your needs
nano .musestatignore
```

### Example Patterns

```gitignore
# .musestatignore

# ===== COMMENTS =====
# Lines starting with # are comments

# ===== FOREIGN LANGUAGES =====
# Ignore Korean text
\b[가-힣]+\b

# Ignore Japanese text
[ぁ-んァ-ン]+

# Ignore Chinese text
[\u4e00-\u9fff]+

# ===== CHARACTER NAMES =====
# Ignore names with underscores
_Minho_
_Jisoo_
_Character_Name_

# ===== INTENTIONAL GRAMMAR =====
# Past perfect tense
\bhad\s+had\b

# Emphatic repetition
\bthat\s+that\b

# ===== STYLE CHOICES =====
# I prefer spaced hyphens
 - 

# Author notes are intentional
\[Author's Note\]
\[Editor's Note\]

# ===== SECTIONS TO SKIP =====
# Appendix
^##\s+Appendix

# References
^##\s+References

# Glossary
^##\s+Glossary

# ===== TECHNICAL CONTENT =====
# URLs
https?://

# Code blocks (auto-handled, but you can add)
```
```

### Pattern Syntax

- **Regex Patterns**: Full regex support
- **Literal Matching**: Falls back if regex fails
- **Line-by-Line**: Checks each pattern per line
- **Comments**: `#` at start of line

### Testing Ignore Patterns

```bash
# Check if patterns are loaded
python musestat.py -v
# Will show: "5 patterns loaded from .musestatignore"
```

---

## 📤 Export & Compare

### Export Formats

```bash
# HTML (beautiful, shareable)
python musestat.py --export html

# JSON (machine-readable)
python musestat.py --export json

# CSV (spreadsheet-compatible)
python musestat.py --export csv

# Custom output file
python musestat.py --export json -o mystats.json
```

### Progress Tracking

```bash
# Save current state
python musestat.py --save-snapshot
# Creates: manuscript_2025-10-16.stats.json

# Compare with previous
python musestat.py --compare manuscript_2025-10-15.stats.json
```

**Comparison Shows:**
- Word count delta (+/- words)
- Chapter changes
- Time since last analysis
- Progress percentage

---

## 🚀 Advanced Features

### Enable Advanced Analysis

```bash
python musestat.py -a
```

### Readability Metrics (5 Scores)

1. **Flesch Reading Ease** (0-100)
   - Higher = easier
   - 60-70 = standard

2. **Flesch-Kincaid Grade** (0-18)
   - US grade level
   - 8-10 = typical

3. **Gunning Fog Index** (6-17)
   - Years of education
   - 7-8 = easy

4. **SMOG Index** (6-18)
   - Readability grade
   - 12-14 = difficult

5. **Coleman-Liau Index** (1-16)
   - Grade level
   - 6-10 = accessible

### Dialogue Analysis

- Dialogue line count
- Dialogue ratio (percentage)
- Fiction-specific insights

### Pacing Analysis

- Long sentences (>50 words)
- Long paragraphs (>300 words)
- Pacing recommendations

### Language Detection

- Auto-detect manuscript language
- Language-specific analysis

---

## 🏆 Achievement System

### 9 Badge Levels

| Threshold | Badge | Icon | Message |
|-----------|-------|------|---------|
| 1,000 | First Thousand | 🌱 | Every journey begins with a single word |
| 5,000 | Sprint Champion | 🏃 | You're building momentum! |
| 10,000 | Committed Writer | 📝 | You've crossed into serious territory |
| 25,000 | Novella Territory | 📗 | You could publish this as a novella! |
| 50,000 | Novelist | 📘 | Congratulations! You've written a novel! |
| 75,000 | Expanded Novel | ✨ | Your story is growing beautifully |
| 120,000 | Epic Writer | 📙 | You've entered epic novel territory! |
| 135,000 | Master Storyteller | 📚 | An epic masterpiece is forming |
| 150,000 | Trilogy Material | 🏆 | You could split this into multiple books! |

### Milestones

- 📗 Novel (Short): 50,000 words
- 📘 Novel (Standard): 80,000 words
- 📙 Novel (Long): 100,000 words
- 📚 Epic Novel: 120,000 words

### Motivational Quotes

20 inspiring quotes from famous authors including:
- Maya Angelou
- Terry Pratchett
- Stephen King
- Kurt Vonnegut
- And more!

---

## 🔧 CLI Reference

### File Options
```bash
-f, --file PATH       Specify manuscript file
-l, --list            List all manuscript files
--formats             Show supported formats
```

### Display Modes
```bash
# No flag              Full analysis (default)
-sc, --semi-compact   Semi-compact (RECOMMENDED)
-c, --compact         Compact summary
-m, --minimalist      Plain text output
-a, --advanced        Enable advanced features
-v, --verify          Verification mode
--chapters-only       Chapter breakdown only
```

### Export & Output
```bash
--export {json,csv,html}   Export to format
-o, --output FILE          Save to file
--save-snapshot, -s        Save current stats
--compare FILE             Compare with previous
```

### Control Options
```bash
--no-animation        Skip loading animations
-h, --help            Show help message
```

---

## 💡 Best Practices

### Daily Workflow

**Morning: Quick Check**
```bash
python musestat.py -m
```

**Evening: Progress Review**
```bash
python musestat.py -sc
```

### Weekly Workflow

**Monday: Save Baseline**
```bash
python musestat.py --save-snapshot
```

**Friday: Review Progress**
```bash
python musestat.py -sc --compare monday.stats.json
```

### Pre-Submission Workflow

**Step 1: Full Analysis**
```bash
python musestat.py -a
```

**Step 2: Verify Quality**
```bash
python musestat.py -v
```

**Step 3: Export Report**
```bash
python musestat.py --export html -o submission_report.html
```

**Step 4: Fix Issues**
- Address errors (🔴)
- Review warnings (⚠️)
- Consider suggestions (ℹ️)

**Step 5: Final Check**
```bash
python musestat.py -v
# Goal: ✨ Manuscript is ready for publishing! ✨
```

---

## 🔍 Troubleshooting

### Issue: Too Many Whitespace Warnings

**Solution**: Add to `.musestatignore`:
```gitignore
# Trailing whitespace is intentional
\s+$
```

### Issue: Character Names Flagged

**Solution**: Add to `.musestatignore`:
```gitignore
_CharacterName_|_AnotherName_
```

### Issue: Foreign Language False Positives

**Solution**: Add to `.musestatignore`:
```gitignore
# Korean
[가-힣]+
# Japanese
[ぁ-んァ-ン]+
```

### Issue: Intentional Em-dash Style

**Solution**: Add to `.musestatignore`:
```gitignore
 -  # Spaced hyphen
```

### Issue: Past Perfect Grammar

**Solution**: Add to `.musestatignore`:
```gitignore
\bhad\s+had\b
```

### Issue: File Not Found

**Solution**: Check file location:
```bash
# List available files
python musestat.py --list

# Use correct path
python musestat.py -f path/to/file.md
```

### Issue: Module Not Found (docx/rtf)

**Solution**: Install optional dependencies:
```bash
pip install python-docx striprtf
```

---

## 📚 Documentation Files

- **README.md** - Getting started guide
- **QUICK_START.md** - Quick reference
- **VERIFICATION_GUIDE.md** - Complete verification guide
- **FEATURES_V2.md** - Detailed feature list
- **COMPLETE_GUIDE.md** - This comprehensive guide
- **CHANGELOG.md** - Version history
- **.musestatignore.example** - Example ignore patterns

---

## 🎯 Use Cases

### Fiction Writer
```bash
# Daily writing
python musestat.py -sc

# Weekly review
python musestat.py -a

# Pre-submission
python musestat.py -v
```

### Non-Fiction Writer
```bash
# Track chapters
python musestat.py --chapters-only

# Readability check
python musestat.py -a

# Quality check
python musestat.py -v
```

### Student/Thesis
```bash
# Word count target
python musestat.py -c

# Progress tracking
python musestat.py --save-snapshot
python musestat.py --compare baseline.json

# Final review
python musestat.py -v
```

### Editor/Beta Reader
```bash
# Quick overview
python musestat.py -sc

# Detailed analysis
python musestat.py -a

# Issue detection
python musestat.py -v --export html
```

---

## 🚀 Quick Command Reference

```bash
# MOST USED COMMANDS
python musestat.py -sc          # Daily check
python musestat.py -v           # Verify quality
python musestat.py -a           # Deep analysis
python musestat.py -c           # Quick check

# EXPORT & TRACKING
python musestat.py --export html
python musestat.py --save-snapshot
python musestat.py --compare old.json

# FILE OPERATIONS
python musestat.py -f book.md
python musestat.py --list
python musestat.py --formats

# SPECIAL MODES
python musestat.py -m           # Minimalist
python musestat.py --chapters-only  # Chapters
python musestat.py --no-animation   # Fast
```

---

## ✨ What's New in v2.1

### Major Features
- ✅ **Verification Mode**: 12 comprehensive check categories
- ✅ **`.musestatignore`**: Regex pattern-based ignoring
- ✅ **Enhanced Verification**: Much more thorough checks
- ✅ **Issue Categorization**: Errors/Warnings/Info with counts
- ✅ **Top Issues Summary**: Quick breakdown by category
- ✅ **Ignore Status Display**: Shows loaded patterns
- ✅ **Side-by-Side Displays**: Better visual layout

### Improvements
- ✅ Better achievement badge logic
- ✅ 20 motivational quotes
- ✅ Enhanced semi-compact mode
- ✅ Category breakdown in verification
- ✅ More thorough punctuation checks
- ✅ Heading hierarchy validation
- ✅ Smart quote consistency
- ✅ Incomplete content detection

---

## 📞 Need Help?

```bash
# Show help
python musestat.py --help

# List files
python musestat.py --list

# Check supported formats
python musestat.py --formats
```

---

**MuseStat v2.1** - Your complete manuscript analysis & verification toolkit! 📚✨

**Created with ❤️ for writers everywhere**


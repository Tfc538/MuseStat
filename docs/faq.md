# ❓ Frequently Asked Questions

Common questions and quick answers about MuseStat.

---

## 📦 Installation & Setup

### Q: What do I need to run MuseStat?

**A:** Python 3.7+ and the `rich` library:
```bash
pip install rich
```

Optional dependencies for additional formats:
```bash
pip install python-docx striprtf langdetect textstat
```

---

### Q: Can I use MuseStat without installing extra packages?

**A:** Yes! MuseStat works with `.md` and `.txt` files using only `rich`. Install optional packages only if you need:
- `.docx` support → `python-docx`
- `.rtf` support → `striprtf`
- Advanced features → `langdetect textstat`

---

### Q: Does MuseStat work on Windows/Mac/Linux?

**A:** Yes! MuseStat works on all platforms that support Python 3.7+.

---

## 🎯 Basic Usage

### Q: What's the best mode for daily use?

**A:** Semi-compact mode (`-sc`):
```bash
python musestat.py -sc
```

It shows everything important without being overwhelming.

---

### Q: How do I analyze my manuscript?

**A:** Navigate to the MuseStat folder and run:
```bash
# If your file is in the same folder
python musestat.py -f yourfile.md

# If your file is elsewhere
python musestat.py -f ../path/to/yourfile.md
```

---

### Q: What files can MuseStat analyze?

**A:** 
- ✅ `.md` (Markdown) - native support
- ✅ `.txt` (Plain text) - native support
- ✅ `.docx` (Word) - requires `python-docx`
- ✅ `.rtf` (Rich Text) - requires `striprtf`

---

### Q: How do I see available files?

**A:**
```bash
python musestat.py --list
```

---

## 📊 Features & Statistics

### Q: What counts as a "word"?

**A:** MuseStat counts any sequence of characters separated by whitespace, after removing markdown formatting. It ignores code blocks and cleans markdown syntax for accurate counts.

---

### Q: How is reading time calculated?

**A:** Based on average reading speeds:
- Fast readers: 300 WPM
- Average readers: 200 WPM  
- Slow readers: 120 WPM

The range shows from fast to slow: "3h 20m - 5h 0m"

---

### Q: How are pages estimated?

**A:** Using 250-350 words per page:
- Low estimate: 350 words/page (dense)
- High estimate: 250 words/page (spacious)
- Average: ~300 words/page

Result: "143-200 pages (~167 avg)"

---

### Q: What are achievement badges?

**A:** Gamified milestones celebrating your writing progress! From 🌱 "First Thousand" (1,000 words) to 🏆 "Trilogy Material" (150,000 words).

---

### Q: Can I turn off the badges/quotes?

**A:** Yes! Use minimalist mode:
```bash
python musestat.py -m
```

---

## 🔍 Verification Mode

### Q: What does verification check?

**A:** 12 categories including:
- Markdown formatting errors
- Pre-publish markers (TODO, FIXME)
- Repeated words
- Punctuation issues
- And more!

See [Verification Guide](verification-guide.md) for details.

---

### Q: How do I ignore false positives?

**A:** Create a `.musestatignore` file with patterns to skip:
```gitignore
# Ignore Korean text
[가-힣]+

# Ignore character name
_MyCharacter_

# Ignore intentional grammar
\bhad\s+had\b
```

See [Ignore Patterns](ignore-patterns.md) for more.

---

### Q: What's the difference between errors, warnings, and info?

**A:**
- 🔴 **ERRORS**: Critical issues that must be fixed before publishing
- ⚠️ **WARNINGS**: Quality issues you should review
- ℹ️ **INFO**: Optional style suggestions

---

## 📤 Export & Tracking

### Q: How do I export my statistics?

**A:**
```bash
# HTML (beautiful, shareable)
python musestat.py --export html

# JSON (machine-readable)
python musestat.py --export json

# CSV (spreadsheet)
python musestat.py --export csv
```

---

### Q: How do I track progress over time?

**A:**
```bash
# Save current stats
python musestat.py --save-snapshot

# Compare with previous
python musestat.py --compare old.stats.json
```

---

### Q: Where are snapshots saved?

**A:** In the same folder as your manuscript, named:
```
manuscript_2025-10-16.stats.json
```

---

## ⚙️ Advanced Features

### Q: What are readability metrics?

**A:** Professional scores measuring how easy your text is to read:
- Flesch Reading Ease (0-100, higher = easier)
- Flesch-Kincaid Grade (US grade level)
- Gunning Fog, SMOG, Coleman-Liau indices

Enable with `-a` flag. Requires `textstat`.

---

### Q: What's dialogue analysis?

**A:** Counts lines containing quoted text and calculates the dialogue ratio (percentage). Useful for fiction writers.

Enable with `-a` flag.

---

### Q: Can MuseStat detect my manuscript's language?

**A:** Yes! With the `-a` flag and `langdetect` installed, it auto-detects the language and shows it in the output.

---

## 🎨 Display Modes

### Q: What's the difference between modes?

**A:**
- **Full**: Everything (default)
- **Semi-Compact** (`-sc`): Daily routine ⭐
- **Compact** (`-c`): Ultra-quick
- **Minimalist** (`-m`): Plain text
- **Verify** (`-v`): Quality checks
- **Advanced** (`-a`): + Readability

---

### Q: Can I combine modes?

**A:** Not all, but you can combine some options:
```bash
# Semi-compact with file
python musestat.py -f book.md -sc

# Advanced with export
python musestat.py -a --export html
```

---

## 🔧 Troubleshooting

### Q: "Module 'rich' not found"

**A:**
```bash
pip install rich
```

---

### Q: "File not found"

**A:** Either:
1. Specify full path: `python musestat.py -f /path/to/file.md`
2. Navigate to the file's folder first
3. List files: `python musestat.py --list`

---

### Q: Can't read my .docx file

**A:**
```bash
pip install python-docx
```

---

### Q: MuseStat is slow on large files

**A:**
1. Use `--no-animation` to skip loading screens
2. Use `-c` or `-m` for faster modes
3. Avoid `-a` (advanced) for routine checks

---

### Q: Too many verification warnings

**A:** Create `.musestatignore` to skip intentional patterns. See [Ignore Patterns](ignore-patterns.md).

---

## 💡 Best Practices

### Q: How often should I run MuseStat?

**A:**
- **Daily**: Use `-sc` mode after writing
- **Weekly**: Use `-a` for deep analysis
- **Pre-submission**: Use `-v` for verification

---

### Q: Should I fix all verification issues?

**A:**
- 🔴 **ERRORS**: Yes, fix before publishing
- ⚠️ **WARNINGS**: Review and decide
- ℹ️ **INFO**: Optional improvements

---

### Q: What's the best workflow for tracking progress?

**A:**
```bash
# Monday: Save baseline
python musestat.py --save-snapshot

# Daily: Check progress
python musestat.py -sc

# Friday: Review week
python musestat.py -sc --compare monday.stats.json
```

---

### Q: How do I share statistics with others?

**A:** Export to HTML:
```bash
python musestat.py --export html
```

Then share the generated HTML file. It's beautiful and works in any browser!

---

## 🎯 Specific Use Cases

### Q: I'm a fiction writer - what features should I use?

**A:**
- Daily: `-sc` mode
- Weekly: `-a` for dialogue analysis
- Pre-submission: `-v` for quality

---

### Q: I'm writing a thesis - what's most useful?

**A:**
- Word count tracking: `-c` mode
- Progress tracking: `--save-snapshot` and `--compare`
- Readability: `-a` mode

---

### Q: I'm an editor - how can I use MuseStat?

**A:**
- Quality check: `-v` mode
- Detailed analysis: `-a` mode
- Generate report: `--export html`

---

### Q: Can I use MuseStat for blog posts?

**A:** Absolutely! MuseStat works great for:
- Word count goals
- Readability checking
- Verification before publishing

---

## 🔗 Integration

### Q: Can I integrate MuseStat with my editor?

**A:** Yes! Use minimalist mode:
```bash
python musestat.py -m
```

Then create a keyboard shortcut or task in your editor.

---

### Q: Can I use MuseStat in scripts?

**A:** Yes! Minimalist mode outputs plain text perfect for parsing:
```bash
python musestat.py -m | grep "Words:"
```

---

### Q: Can I use MuseStat in CI/CD?

**A:** Yes! Run verification in your pipeline:
```bash
python musestat.py -v --minimalist
```

Returns exit code 0 if no critical errors.

---

## 📚 Learning

### Q: Where do I start as a beginner?

**A:** Read [Getting Started](getting-started.md), then try:
```bash
python musestat.py -sc
```

---

### Q: What's the complete learning path?

**A:**
1. [Getting Started](getting-started.md) - Day 1
2. [User Guide](user-guide.md) - Week 1
3. [Verification Guide](verification-guide.md) - Month 1
4. [Advanced Features](advanced-features.md) - Ongoing

---

### Q: Is there a cheat sheet?

**A:** Yes! See [Quick Reference](quick-reference.md) for a one-page command list.

---

## 🆘 Still Need Help?

1. Check [Troubleshooting](troubleshooting.md)
2. Review [Examples](examples.md)
3. Read the full [User Guide](user-guide.md)

---

**Can't find your answer?** Check the [User Guide](user-guide.md) for comprehensive documentation.


# ⚡ Quick Reference Cheat Sheet

One-page reference for all MuseStat commands.

---

## 🎯 Most Used Commands

```bash
# Daily writing check (RECOMMENDED)
python musestat.py -sc

# Verify before publishing
python musestat.py -v

# Quick word count
python musestat.py -c

# Full detailed analysis
python musestat.py

# Advanced features
python musestat.py -a
```

---

## 📊 Display Modes

| Command | Mode | Use When |
|---------|------|----------|
| `python musestat.py` | Full | Weekly review, deep analysis |
| `python musestat.py -sc` | Semi-Compact | **Daily routine** ⭐ |
| `python musestat.py -c` | Compact | Ultra-quick check |
| `python musestat.py -m` | Minimalist | Scripts, automation |
| `python musestat.py -v` | Verify | Pre-submission check |
| `python musestat.py -a` | Advanced | Editorial review |
| `python musestat.py --chapters-only` | Chapters | Structure review |

---

## 📁 File Operations

```bash
# Analyze specific file
python musestat.py -f mybook.md

# List all manuscript files
python musestat.py --list

# Show supported formats
python musestat.py --formats
```

---

## 📤 Export & Save

```bash
# Export to HTML
python musestat.py --export html

# Export to JSON
python musestat.py --export json

# Export to CSV
python musestat.py --export csv

# Save to specific file
python musestat.py --export json -o mystats.json

# Save snapshot for tracking
python musestat.py --save-snapshot

# Compare with previous
python musestat.py --compare old.stats.json
```

---

## 🔍 Verification

```bash
# Run all checks
python musestat.py -v

# Verify specific file
python musestat.py -f mybook.md -v

# Export verification results
python musestat.py -v --export html
```

---

## ⚙️ Control Options

```bash
# Skip loading animation
python musestat.py --no-animation

# Get help
python musestat.py --help

# Show version info
python musestat.py --formats
```

---

## 🎨 Combining Options

```bash
# Semi-compact with specific file
python musestat.py -f chapter01.md -sc

# Advanced analysis with export
python musestat.py -a --export html

# Verify and save results
python musestat.py -v --export json -o report.json

# Compact with no animation
python musestat.py -c --no-animation

# Compare progress in semi-compact
python musestat.py -sc --compare yesterday.json
```

---

## 📋 Common Workflows

### Daily Writing
```bash
# Morning
python musestat.py -m

# Evening
python musestat.py -sc
```

### Weekly Review
```bash
# Monday
python musestat.py --save-snapshot

# Friday
python musestat.py -sc --compare monday.stats.json
```

### Pre-Submission
```bash
# Step 1: Full analysis
python musestat.py -a

# Step 2: Verify
python musestat.py -v

# Step 3: Export
python musestat.py --export html
```

---

## 🔤 Short Forms

| Short | Long | Description |
|-------|------|-------------|
| `-f` | `--file` | Specify file |
| `-c` | `--compact` | Compact mode |
| `-sc` | `--semi-compact` | Semi-compact mode |
| `-m` | `--minimalist` | Minimalist mode |
| `-v` | `--verify` | Verify mode |
| `-a` | `--advanced` | Advanced mode |
| `-l` | `--list` | List files |
| `-s` | `--save-snapshot` | Save snapshot |
| `-o` | `--output` | Output file |

---

## 📝 File Formats

| Extension | Support | Requires |
|-----------|---------|----------|
| `.md` | ✅ Native | None |
| `.txt` | ✅ Native | None |
| `.docx` | ✅ Optional | `python-docx` |
| `.rtf` | ✅ Optional | `striprtf` |

```bash
# Install optional deps
pip install python-docx striprtf
```

---

## 🏆 Achievement Milestones

| Words | Badge | Icon |
|-------|-------|------|
| 1,000 | First Thousand | 🌱 |
| 5,000 | Sprint Champion | 🏃 |
| 10,000 | Committed Writer | 📝 |
| 25,000 | Novella Territory | 📗 |
| 50,000 | Novelist | 📘 |
| 75,000 | Expanded Novel | ✨ |
| 120,000 | Epic Writer | 📙 |
| 135,000 | Master Storyteller | 📚 |
| 150,000 | Trilogy Material | 🏆 |

---

## 🚫 .musestatignore Patterns

Create a `.musestatignore` file with regex patterns:

```gitignore
# Ignore foreign language
[가-힣]+              # Korean
[ぁ-んァ-ン]+         # Japanese

# Ignore character names
_Character_Name_

# Ignore intentional grammar
\bhad\s+had\b        # Past perfect

# Ignore em-dash preference
 - 

# Ignore sections
^##\s+Appendix
```

---

## 🔍 Verification Check Categories

1. Markdown Formatting (*, **, _)
2. Pre-publish Markers (TODO, FIXME)
3. Repeated Words (the the, etc.)
4. Punctuation (!!, ??)
5. Whitespace (trailing, tabs)
6. Heading Structure (hierarchy)
7. Smart Quotes (consistency)
8. Markdown Links (brackets)
9. Paragraph Spacing (blanks)
10. Line Length (>1000 chars)
11. Dialogue Quotes (consistency)
12. Incomplete Content (placeholders)

---

## 💡 Pro Tips

```bash
# Create an alias (Mac/Linux)
alias wc='python ~/path/to/musestat.py -sc'

# Create an alias (Windows PowerShell)
function wc { python C:\path\to\musestat.py -sc }

# Then just type:
wc
```

---

## ⚠️ Common Fixes

```bash
# Module not found
pip install rich

# Can't read .docx
pip install python-docx

# Can't read .rtf
pip install striprtf

# File not found
python musestat.py --list      # See available files
python musestat.py -f yourfile.md
```

---

## 📊 Output Examples

### Minimalist (`-m`)
```
Words: 50,000
Chapters: 20
Reading Time: 3h 20m - 5h 0m
```

### Compact (`-c`)
```
╭─ MuseStat Quick Summary ─╮
│ Words: 50,000            │
│ Badge: 📘 Novelist       │
│ "Keep writing!"          │
╰──────────────────────────╯
```

### Semi-Compact (`-sc`)
```
╔═══ MuseStat ═══╗

Overview | Milestones
─────────┼──────────
Stats... | Progress...

Badge | Quote
──────┼──────
🎉    | "..."
```

---

## 🔗 Quick Links

- [Full User Guide](user-guide.md)
- [Verification Guide](verification-guide.md)
- [Display Modes](display-modes.md)
- [Examples](examples.md)
- [FAQ](faq.md)
- [Troubleshooting](troubleshooting.md)

---

## 📞 Need More Help?

```bash
# Show help
python musestat.py --help

# Show formats
python musestat.py --formats

# List files
python musestat.py --list
```

Read the [User Guide](user-guide.md) for detailed explanations.

---

**Print this page for quick reference!** 📄



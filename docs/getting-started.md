# 🚀 Getting Started with MuseStat

Welcome! This guide will have you analyzing your manuscript in 5 minutes.

---

## 📦 Installation

### Step 1: Install Python Requirements

MuseStat requires Python 3.7+ and the `rich` library.

```bash
# Install base requirement
pip install rich
```

### Step 2: Optional Dependencies

For additional file format support:

```bash
# For Word documents (.docx)
pip install python-docx

# For Rich Text Format (.rtf)
pip install striprtf

# For advanced features (readability, language detection)
pip install langdetect textstat
```

**Or install everything at once:**

```bash
pip install -r requirements.txt
```

---

## 🎯 Your First Analysis

### 1. Basic Analysis

Navigate to the MuseStat folder and run:

```bash
python musestat.py
```

**Expected output:**
```
╔══════════════════════════════════════╗
║ 📊 MuseStat - Manuscript Analytics   ║
╚══════════════════════════════════════╝

[Beautiful tables with your manuscript statistics]
```

### 2. With Your Own File

```bash
python musestat.py -f mybook.md
```

Supported formats: `.md`, `.txt`, `.docx`, `.rtf`

### 3. See Available Files

```bash
python musestat.py --list
```

Lists all manuscript files in the current directory.

---

## 🎨 Try Different Modes

### Semi-Compact (Recommended for Daily Use)

```bash
python musestat.py -sc
```

Perfect for your daily writing routine!

### Quick Check

```bash
python musestat.py -c
```

Ultra-fast overview.

### Verify Quality

```bash
python musestat.py -v
```

Check for issues before publishing.

---

## 📚 Understanding Your First Results

When you run MuseStat, you'll see:

### 1. **Word Count**
```
Words: 50,000
```
Your total manuscript word count.

### 2. **Reading Time**
```
Reading Time: 3h 20m - 5h 0m
```
How long it takes to read (slow to fast readers).

### 3. **Pages**
```
Pages: 143-200 pages (~167 avg)
```
Estimated book pages (250-350 words per page).

### 4. **Chapters**
```
Chapters: 20
Avg Chapter: 2,500 words
```
Chapter count and average length.

### 5. **Milestones**
```
✓ 📗 Novel (Short) (50,000 words)
  ████████████████████ 100.0%
```
Progress toward standard novel lengths.

### 6. **Achievement Badge**
```
╔═ Achievement ════════════════╗
║ 📘 Novelist                  ║
║ Congratulations! You've      ║
║ written a novel!             ║
╚══════════════════════════════╝
```
Your current achievement level!

### 7. **Motivational Quote**
```
╭─ Writer's Wisdom ──────────────╮
│ "Keep writing! One paragraph   │
│  at a time."                   │
╰────────────────────────────────╯
```
Daily inspiration for your writing journey.

---

## ⚡ Quick Commands Cheat Sheet

```bash
# Full analysis (default)
python musestat.py

# Daily check (recommended)
python musestat.py -sc

# Quick check
python musestat.py -c

# Verify for publishing
python musestat.py -v

# Advanced analysis
python musestat.py -a

# Minimalist output
python musestat.py -m

# With specific file
python musestat.py -f mybook.md

# List available files
python musestat.py --list

# Get help
python musestat.py --help
```

---

## 🎯 Recommended Daily Workflow

### Morning
```bash
python musestat.py -m
```
Quick word count to see where you left off.

### Evening
```bash
python musestat.py -sc
```
Review your progress with motivation!

### Weekly
```bash
python musestat.py -a
```
Deep dive into your manuscript statistics.

---

## 🚦 Next Steps

Now that you've run your first analysis, explore:

1. **[Display Modes](display-modes.md)** - Choose the right view
2. **[User Guide](user-guide.md)** - Learn all features
3. **[Verification Guide](verification-guide.md)** - Check quality
4. **[Quick Reference](quick-reference.md)** - Command cheat sheet

---

## 🔧 Troubleshooting First Run

### Issue: "Command not found: python"

**Solution:** Try `python3` instead:
```bash
python3 musestat.py
```

### Issue: "Module 'rich' not found"

**Solution:** Install rich:
```bash
pip install rich
# or
pip3 install rich
```

### Issue: "File not found: manuscript.md"

**Solution:** Specify your file:
```bash
python musestat.py -f yourfile.md
# or list available files
python musestat.py --list
```

### Issue: Can't read .docx files

**Solution:** Install optional dependency:
```bash
pip install python-docx
```

### Issue: Can't read .rtf files

**Solution:** Install optional dependency:
```bash
pip install striprtf
```

---

## 💡 Pro Tips for Beginners

### 1. Start Simple
Don't worry about all the features - start with:
```bash
python musestat.py -sc
```

### 2. Use the Right Mode
- Writing daily? → `-sc`
- Quick check? → `-c`
- Before submission? → `-v`

### 3. Check Supported Formats
```bash
python musestat.py --formats
```

### 4. Create an Alias
Make it easy to run:

**On Mac/Linux (.bashrc or .zshrc):**
```bash
alias wc='python ~/path/to/musestat.py -sc'
```

**On Windows (PowerShell profile):**
```powershell
function wc { python C:\path\to\musestat.py -sc }
```

Then just type:
```bash
wc
```

### 5. Explore Gradually
Week 1: Use `-sc` mode  
Week 2: Try `-v` verification  
Week 3: Explore `-a` advanced features  
Week 4: Setup progress tracking  

---

## 📊 What Each Flag Means

| Flag | Name | Best For |
|------|------|----------|
| *(none)* | Full | Complete analysis |
| `-sc` | Semi-Compact | Daily routine ⭐ |
| `-c` | Compact | Quick checks |
| `-v` | Verify | Pre-publishing |
| `-a` | Advanced | Deep analysis |
| `-m` | Minimalist | Scripting |

---

## 🎓 Learning Resources

### Documentation
- [User Guide](user-guide.md) - Complete feature guide
- [Display Modes](display-modes.md) - All view modes explained
- [Verification Guide](verification-guide.md) - Quality checking

### Quick Help
- [Quick Reference](quick-reference.md) - Command cheat sheet
- [Examples](examples.md) - Real-world usage
- [FAQ](faq.md) - Common questions

### Advanced
- [Ignore Patterns](ignore-patterns.md) - Customize verification
- [Export & Tracking](export-tracking.md) - Save progress
- [Advanced Features](advanced-features.md) - Readability & more

---

## ✅ Installation Checklist

- [ ] Python 3.7+ installed
- [ ] `rich` library installed (`pip install rich`)
- [ ] Optional: `python-docx` for .docx files
- [ ] Optional: `striprtf` for .rtf files
- [ ] Optional: `langdetect textstat` for advanced features
- [ ] Ran first analysis: `python musestat.py`
- [ ] Tried semi-compact mode: `python musestat.py -sc`
- [ ] Located your manuscript file
- [ ] Read [User Guide](user-guide.md)

---

## 🎉 Congratulations!

You're now ready to use MuseStat for your manuscript analysis!

**Next:** Check out the [User Guide](user-guide.md) to learn about all features.

---

**Questions?** See [FAQ](faq.md) or [Troubleshooting](troubleshooting.md)



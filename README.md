# 📊 MuseStat - Manuscript Statistics Analyzer

Beautiful terminal UI for comprehensive manuscript analysis with advanced features for fiction writers.

![Version](https://img.shields.io/badge/version-1.0.1-blue)
![Python](https://img.shields.io/badge/python-3.7+-green)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

### Core Statistics
- 📝 **Word & Character Count**: Accurate counts with markdown cleaning
- 📖 **Chapter Analysis**: Automatic detection with smart patterns
- ⏱️ **Reading Time**: Estimated based on average reading speed
- 🎯 **Writing Milestones**: Track progress towards novel length goals
- 🏆 **Achievement Badges**: Unlock titles as you cross word count thresholds
- ✍️ **Writer's Wisdom**: Motivational quotes from famous authors
- 📄 **Multiple Format Support**: .md, .txt, .docx, .rtf files

### Advanced Features
- 🌐 **Language Detection**: Auto-detect language and use appropriate stop words
- 📊 **Readability Metrics**: Flesch-Kincaid, Gunning Fog, Coleman-Liau, and more
- 💬 **Dialogue Analysis**: Count dialogue lines and calculate dialogue ratio
- ⚡ **Pacing Detection**: Identify long sentences/paragraphs that may affect pacing
- 📈 **Progress Tracking**: Compare with previous analyses to track your writing progress
- 🎭 **Scene Detection**: Count scene breaks within chapters
- 🔤 **Word Frequency**: Most common words with language-aware stop word filtering

### Smart Chapter Detection
Recognizes multiple chapter formats:
- `# Chapter Title` (Markdown H1)
- `## Chapter Title` (Markdown H2)
- `Chapter 1: Title`
- `CHAPTER 1: Title`
- `Ch. 1: Title`

## 🚀 Installation

### From Releases (Recommended)

Download the latest executable for your platform from the [Releases](https://github.com/Tfc538/MuseStat/releases) page:
- **Windows**: `musestat-windows-x64.exe`
- **Linux**: `musestat-linux-x64`
- **macOS**: `musestat-macos-x64`

**No Python installation required!**

✨ **Interactive Mode**: Simply double-click the executable to launch an interactive menu that guides you through:
- File selection
- Analysis type selection
- Beautiful results display
- Perfect for first-time users!

### From Source

1. **Install Python 3.7+**

2. **Clone the repository:**
```bash
git clone https://github.com/Tfc538/MuseStat.git
cd MuseStat
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run MuseStat:**
```bash
python main.py
# or
python -m musestat.cli.commands
```

### Development Setup

For development and building executables:

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install in editable mode
pip install -e .

# Run tests (when available)
pytest

# Build executable
pyinstaller --onefile --name musestat --console main.py
```

## 📖 Usage

### Interactive Mode (Easiest!)

Simply double-click the executable or run without arguments:

```bash
# Windows
musestat.exe

# Linux/macOS
./musestat
```

You'll see a beautiful welcome screen with:
1. List of all manuscript files in the current directory
2. File selection menu
3. Analysis type menu (quick, standard, full, advanced, verify)
4. Results that stay on screen until you press Enter

### Command-Line Mode (For Power Users)

```bash
# Analyze default file
python main.py

# Analyze specific file
python main.py -f mybook.docx
python main.py --file manuscript.txt

# Quick summary
python main.py --compact
python main.py -c
```

*Note: If you're using the compiled executable, replace `python main.py` with `musestat` (or `./musestat` on Linux/macOS).*

### Advanced Features

```bash
# Enable all advanced features (language detection, readability, dialogue, pacing)
python main.py --advanced
python main.py -a

# Save snapshot for future comparison
python main.py --save-snapshot
python main.py -s

# Compare with previous analysis
python main.py --compare mybook.stats.json

# Combine options
python main.py -f mybook.docx --advanced --save-snapshot
```

### Discovery & Information

```bash
# List all manuscript files in current directory
python main.py --list
python main.py -l

# Show supported formats and features
python main.py --formats

# Show only chapter breakdown
python main.py --chapters-only

# Check version
python main.py --version
```

### Performance

```bash
# Skip loading animation for instant results
python main.py --no-animation

# Fast word count check
python main.py -c --no-animation
```

## 🎯 CLI Options

| Option | Short | Description |
|--------|-------|-------------|
| `--file PATH` | `-f` | Specify file to analyze |
| `--compact` | `-c` | Display compact summary |
| `--advanced` | `-a` | Enable advanced features |
| `--list` | `-l` | List all manuscript files |
| `--formats` | | Show supported formats |
| `--chapters-only` | | Show only chapter breakdown |
| `--no-animation` | | Skip loading animation |
| `--save-snapshot` | `-s` | Save stats for comparison |
| `--compare FILE` | | Compare with previous stats |
| `--help` | `-h` | Show help message |

## 📊 What You'll See

### Full Mode (Default)
```
📊 MuseStat - Manuscript Analytics
═══════════════════════════════════

┌─────────────────────────────────┐
│  📊 Overview Statistics         │
│  - Total Words: 107,638         │
│  - Characters: 582,576          │
│  - Chapters: 33                 │
│  - Reading Time: 7h 10m         │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  📖 Chapter Breakdown           │
│  - Individual chapter stats     │
│  - Word counts & percentages    │
│  - Scene counts per chapter     │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  🔤 Most Frequent Words         │
│  - Top 15 common words          │
│  - Visual bar charts            │
└─────────────────────────────────┘
```

### Advanced Mode (`--advanced`)
Includes everything from Full Mode plus:

```
┌─────────────────────────────────┐
│  📖 Readability Metrics         │
│  - Flesch Reading Ease: 72.3    │
│  - Flesch-Kincaid Grade: 7.8    │
│  - Gunning Fog Index: 10.2      │
│  - Coleman-Liau Index: 8.5      │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  ⚡ Pacing Analysis              │
│  - Avg Sentence Length: 15.2    │
│  - Avg Paragraph Length: 87     │
│  - Long Sentences: 12           │
│  - Long Paragraphs: 8           │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  💬 Dialogue Statistics         │
│  - Dialogue Lines: 1,247        │
│  - Dialogue Ratio: 32.5%        │
└─────────────────────────────────┘
```

### Comparison Mode (`--compare`)
```
┌─────────────────────────────────┐
│  📈 Changes Since Last Analysis │
│  Words: +1,523 ✓                │
│  Characters: +8,234 ✓            │
│  Sentences: +89 ✓                │
│  Paragraphs: +45 ✓               │
│  ⏰ Last analyzed: 2 days ago   │
└─────────────────────────────────┘
```

## 💡 Use Cases & Workflows

### Daily Writing Progress
```bash
# Quick word count after your writing session
python main.py -c --no-animation
```

### Deep Manuscript Analysis
```bash
# Full analysis with all advanced features
python main.py -f manuscript.docx --advanced
```

### Track Your Writing Progress
```bash
# First analysis - save a snapshot
python main.py --save-snapshot

# Later - compare with previous
python main.py --compare manuscript.stats.json
```

### Editor Review
```bash
# Analyze readability and pacing
python main.py --advanced

# Focus on chapter structure
python main.py --chapters-only

# Verify manuscript for publishing
python main.py --verify
```

### Multiple Format Management
```bash
# See all manuscript versions
python main.py --list

# Compare different versions
python main.py -f draft.md -c
python main.py -f final.docx -c
```

## 📊 Readability Scores Explained

### Flesch Reading Ease (0-100)
- **90-100**: Very Easy (5th grade)
- **80-90**: Easy (6th grade)
- **70-80**: Fairly Easy (7th grade)
- **60-70**: Standard (8-9th grade) - **Most novels**
- **50-60**: Fairly Difficult (10-12th grade)
- **30-50**: Difficult (College)
- **0-30**: Very Difficult (Graduate)

### Flesch-Kincaid Grade
- Indicates US grade level required to understand the text
- Most popular fiction: **Grade 6-8**
- Literary fiction: **Grade 8-10**

### Gunning Fog Index
- Estimates years of formal education needed
- Ideal for most writing: **8-10**

## 🎨 Features Comparison

| Feature | Basic | With --advanced |
|---------|-------|----------------|
| Word Count | ✓ | ✓ |
| Character Count | ✓ | ✓ |
| Chapter Breakdown | ✓ | ✓ with scenes |
| Reading Time | ✓ | ✓ |
| Word Frequency | ✓ | ✓ language-aware |
| Milestones | ✓ | ✓ |
| Language Detection | ✗ | ✓ |
| Readability Metrics | ✗ | ✓ |
| Dialogue Analysis | ✗ | ✓ |
| Pacing Analysis | ✗ | ✓ |

## 📝 Supported File Formats

| Format | Extension | Requires | Status |
|--------|-----------|----------|--------|
| Markdown | .md, .markdown | Built-in | ✓ |
| Plain Text | .txt | Built-in | ✓ |
| Word Document | .docx | python-docx | ✓ |
| Rich Text Format | .rtf | striprtf | ✓ |

## 🔧 Dependencies

### Core (Required)
- **rich** >= 13.0.0 - Beautiful terminal UI

### File Formats (Optional)
- **python-docx** >= 0.8.11 - Word documents
- **striprtf** >= 0.0.26 - RTF files

### Advanced Features (Optional)
- **langdetect** >= 1.0.9 - Language detection
- **textstat** >= 0.7.3 - Readability metrics

*Note: The tool works without optional dependencies but with reduced functionality.*

## 📈 Todo List

### ✅ Completed Features
- [x] **Flexible file input**: `--file <path>` for any manuscript
- [x] **Multiple format support**: Auto-detect .docx, .txt, .md, .rtf
- [x] **Language detection**: With language-specific stop words
- [x] **Readability metrics**: Flesch-Kincaid, Gunning Fog, Coleman-Liau
- [x] **Smarter chapter detection**: Multiple patterns including `##`, scene markers
- [x] **Dialogue counting**: Lines and ratio analysis
- [x] **Pacing detection**: Long sentences/paragraphs flagging
- [x] **Progress tracking**: `--compare` with previous stats

### 🚀 Future Enhancements
- [ ] Export reports to PDF/HTML
- [ ] Word cloud visualization
- [ ] Character name frequency tracking
- [ ] Time-of-day analysis (morning/evening writing patterns)
- [ ] Writing streak tracking
- [ ] Sentiment analysis
- [ ] Genre-specific benchmarks

## 🎯 Tips for Fiction Writers

### Dialogue Ratio
- **Heavy dialogue** (50%+): Fast-paced, character-driven
- **Moderate dialogue** (30-50%): Balanced narrative
- **Light dialogue** (< 30%): Description/introspection heavy

### Sentence Length
- **Short** (< 15 words): Creates tension, fast pacing
- **Medium** (15-20 words): Standard, easy reading
- **Long** (> 25 words): Slower, more literary

### Paragraph Length
- **Short** (< 50 words): Modern, fast-paced
- **Medium** (50-150 words): Standard
- **Long** (> 200 words): May lose reader attention

### Readability
- **Commercial fiction**: Aim for Flesch-Kincaid Grade 6-8
- **Literary fiction**: Grade 8-10 is acceptable
- **YA fiction**: Grade 5-7

## 🤝 Contributing

Suggestions and contributions are welcome! This tool is designed for writers, by writers.

## 📄 License

MIT License - Use freely for your writing projects!

## 🙏 Acknowledgments

Built with:
- [Rich](https://github.com/Textualize/rich) - Beautiful terminal formatting
- [python-docx](https://python-docx.readthedocs.io/) - Word document support
- [textstat](https://github.com/textstat/textstat) - Readability metrics
- [langdetect](https://github.com/Mimino666/langdetect) - Language detection

---

**Happy Writing! 📚✨**

*MuseStat - Because every word counts*

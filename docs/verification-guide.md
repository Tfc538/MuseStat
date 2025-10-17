# 🔍 MuseStat Verification Guide

Comprehensive manuscript verification for publishing readiness.

## Quick Start

```bash
# Run verification on your manuscript
python musestat.py --verify
python musestat.py -v

# With specific file
python musestat.py -f mybook.md --verify
```

---

## 📋 What Gets Checked

### 12 Comprehensive Check Categories

#### 1. **Markdown Formatting**
- Unmatched single asterisks `*` (italic)
- Unmatched double asterisks `**` (bold)
- Triple asterisks `***` (likely error)
- Unmatched underscores `_` (emphasis)

**Example Issues:**
```markdown
❌ This is *italic text                    (unmatched)
✓ This is *italic* text                   (correct)

❌ This is **bold text                     (unmatched)
✓ This is **bold** text                   (correct)
```

---

#### 2. **Pre-publish Markers**
Detects markers that should be resolved before publishing:
- `TODO` - Tasks to complete
- `FIXME` - Code/content to fix
- `HACK` - Temporary workarounds
- `NOTE:` - Author notes
- `XXX` - Attention needed
- `TK` - "To Come" (journalism)
- `TBD` - "To Be Determined"
- `PLACEHOLDER` - Temporary content

**Example:**
```markdown
❌ TODO: Add more description here
❌ FIXME: This chapter needs work  
❌ [PLACEHOLDER - write conclusion]
```

---

####3. **Repeated Words**
Catches accidental word repetitions:
- the the
- a a
- and and
- to to
- of of
- in in
- it it

**Example:**
```markdown
❌ He went to to the store.
✓ He went to the store.

❌ The the sun was setting.
✓ The sun was setting.
```

---

#### 4. **Punctuation Issues**

**Multiple Punctuation Marks:**
```markdown
❌ What are you doing!?!?
❌ Really??
✓ What are you doing?
```

**Space Before Punctuation:**
```markdown
❌ Hello there !
❌ What is this ?
✓ Hello there!
✓ What is this?
```

**Ellipsis Issues:**
```markdown
❌ And then....         (4+ dots)
✓ And then...          (3 dots)
✓ And then…            (unicode ellipsis)
```

**Em-dash vs Hyphen:**
```markdown
ℹ️  She said - pausing - never mind
✓ She said—pausing—never mind
```

---

#### 5. **Whitespace Issues**

**Trailing Whitespace:**
```markdown
❌ "Hello world    "    (spaces at end)
✓ "Hello world"        (clean)
```

**Multiple Consecutive Spaces:**
```markdown
❌ "Hello    world"     (4 spaces)
✓ "Hello world"        (1 space)
```

**Tabs in Content:**
```markdown
❌ Uses tab    character
✓ Uses space character
```

---

#### 6. **Heading Structure**

**Missing Space After #:**
```markdown
❌ #Chapter One
✓ # Chapter One

❌ ##Section Title
✓ ## Section Title
```

**Skipped Heading Levels:**
```markdown
❌ # H1
   ### H3 (skipped H2)

✓ # H1
  ## H2
  ### H3
```

---

#### 7. **Smart Quotes Consistency**
Checks for mixed straight and curly quotes:

```markdown
Mixed quotes detected:
- Straight: " (234 found)
- Curly: " " (456 found)

Suggestion: Use consistent style throughout
```

---

#### 8. **Markdown Links**
Validates bracket matching:

```markdown
❌ [This is a link text
❌ This has a ]broken bracket
✓ [This is a link](url)
```

---

#### 9. **Paragraph Spacing**
Detects excessive blank lines:

```markdown
❌ Paragraph one.


   (3+ blank lines)


   Paragraph two.

✓ Paragraph one.

  Paragraph two.
```

---

#### 10. **Line Length**
Warns about very long lines (>1000 characters):

```markdown
⚠️  Very long line (1234 characters)
Suggestion: Consider breaking into multiple lines
```

---

#### 11. **Dialogue Quotes**
Checks quote consistency in dialogue:

```markdown
If most of your document uses curly quotes:
ℹ️  "Straight quote found in dialogue"
Suggestion: Consider using curly quotes for consistency
```

---

#### 12. **Incomplete Content**

**Placeholder Text:**
```markdown
❌ [INSERT SCENE HERE]
❌ [ADD MORE DETAILS]
❌ [EDIT THIS SECTION]
```

**Lorem Ipsum:**
```markdown
❌ Lorem ipsum dolor sit amet...
```

---

## 🚫 The `.musestatignore` File

### What Is It?

A file that tells MuseStat to **ignore** certain patterns during verification. Useful for:
- Intentional formatting choices
- Foreign language text
- Character names with underscores
- Specific sections you don't want checked

### Creating `.musestatignore`

Create a file named `.musestatignore` in your project directory:

```bash
# In your manuscript directory
touch .musestatignore
```

### Pattern Syntax

Each line is a **regular expression** pattern:
```gitignore
# Lines starting with # are comments

# Ignore lines containing "Author's Note"
\[Author's Note\]

# Ignore character names with underscores
_Character_Name_

# Ignore foreign language markers
\b(Korean|Japanese):\s

# Ignore specific sections
^##\s+Appendix

# Ignore em-dash warnings
 - 

# Ignore intentional repeated words
\bhad\s+had\b

# Ignore URLs
https?://

# Ignore code blocks (automatically handled, but you can add)
```

### Example `.musestatignore`

```gitignore
# .musestatignore for Seoul Mate manuscript

# Ignore Korean romanization lines
\b한글\b
\b[가-힣]+\b

# Ignore character names
_Minho_
_Jisoo_

# Ignore author notes section
^##\s+Author's Notes

# Ignore intentional em-dash usage
 - 

# Ignore TODO in HTML comments
<!--.*TODO.*-->

# Ignore repeated "had had" (past perfect)
\bhad\s+had\b

# Ignore repeated "that that"
\bthat\s+that\b
```

---

## 📊 Verification Output

### Summary Panel

```
╭─ Results Summary ─────────────────────╮
│                                       │
│  Verification Summary                 │
│                                       │
│  🔴 Errors:     12                    │
│  ⚠️  Warnings:    3                    │
│  ℹ️  Info:        8                    │
│                                       │
│  Top Issues:                          │
│    • Pre-publish: 11                  │
│    • Punctuation: 2                   │
│    • Whitespace: 8                    │
│                                       │
│  ❌ Critical issues found             │
│                                       │
╰───────────────────────────────────────╯
```

### Issue Levels

**🔴 ERRORS (Critical):**
- Must be fixed before publishing
- Formatting errors
- Pre-publish markers
- Incomplete content
- Malformed syntax

**⚠️ WARNINGS (Quality):**
- Should be reviewed
- Style inconsistencies
- Repeated words
- Multiple punctuation
- Whitespace issues

**ℹ️ INFO (Suggestions):**
- Optional improvements
- Style recommendations
- Minor whitespace
- Em-dash suggestions

---

## 🎯 Best Practices

### 1. **Run Verification Regularly**

```bash
# During writing (check progress)
python musestat.py -v

# Before submission
python musestat.py --verify --file final_draft.md
```

### 2. **Create `.musestatignore` Early**

Start with a basic ignore file and add patterns as needed:
```bash
cp .musestatignore.example .musestatignore
# Edit to match your needs
```

### 3. **Fix in Priority Order**

1. **Errors first** (🔴)
   - Fix formatting issues
   - Remove pre-publish markers
   - Complete placeholder content

2. **Warnings next** (⚠️)
   - Review repeated words
   - Check punctuation
   - Clean whitespace

3. **Info last** (ℹ️)
   - Consider suggestions
   - Apply style improvements

### 4. **Use Ignore Patterns Wisely**

```gitignore
# Good: Ignore intentional choices
\bhad\s+had\b        # Past perfect tense

# Good: Ignore foreign languages
\b[한글]+\b           # Korean text

# Bad: Ignore all errors
TODO                 # Don't ignore all TODOs!
```

---

## 🔧 Advanced Usage

### Combine with Export

```bash
# Verify and export results
python musestat.py -v --export html
# Creates report with verification results
```

### Check Specific Files

```bash
# Check multiple chapters
python musestat.py -f chapter01.md -v
python musestat.py -f chapter02.md -v
python musestat.py -f chapter03.md -v
```

### Script for Batch Checking

```bash
#!/bin/bash
# check_all.sh

for file in chapters/*.md; do
    echo "Checking $file..."
    python musestat.py -f "$file" -v
    echo "---"
done
```

---

## 📈 Verification Workflow

### Step 1: First Pass
```bash
python musestat.py -v
```
- Review all errors
- Note patterns
- Create `.musestatignore` if needed

### Step 2: Fix Critical Issues
```bash
# Fix errors marked as 🔴
# Remove TODO/FIXME markers
# Complete placeholder content
```

### Step 3: Re-verify
```bash
python musestat.py -v
```
- Confirm errors are fixed
- Review warnings

### Step 4: Polish
```bash
# Address warnings (⚠️)
# Consider info suggestions (ℹ️)
# Final verification
python musestat.py -v
```

### Step 5: Ready for Publishing!
```
✨ Manuscript is ready for publishing! ✨
```

---

## 🆘 Common Issues & Solutions

### Issue: Too Many Whitespace Warnings

**Solution:** Add to `.musestatignore`:
```gitignore
# Ignore trailing whitespace (if intentional)
\s+$
```

### Issue: Character Names Flagged

**Solution:** Add to `.musestatignore`:
```gitignore
# Ignore character names with underscores
_Minho_|_Jisoo_|_Character_
```

### Issue: Foreign Language False Positives

**Solution:** Add to `.musestatignore`:
```gitignore
# Ignore Korean text
[가-힣]+

# Ignore Japanese text
[ぁ-んァ-ン]+

# Ignore Chinese text  
[\u4e00-\u9fff]+
```

### Issue: Intentional Em-dash Style

**Solution:** Add to `.musestatignore`:
```gitignore
# I prefer spaced hyphens
 - 
```

### Issue: Past Perfect "had had"

**Solution:** Add to `.musestatignore`:
```gitignore
# Grammatically correct past perfect
\bhad\s+had\b
```

---

## 📝 Tips for Fiction Writers

### 1. **Dialogue Tags**
Verify checks for consistent quote marks in dialogue.

### 2. **Scene Breaks**
`***` is recognized as valid for scene breaks.

### 3. **Chapter Headings**
Maintains proper heading hierarchy.

### 4. **Character Thoughts**
Check your italic formatting is consistent.

### 5. **Manuscript Markers**
Remove all TODO/FIXME before submission.

---

## 🎓 Pro Tips

1. **Run after every chapter** - Catch issues early
2. **Use `.musestatignore`** - For intentional style choices
3. **Fix errors first** - Then warnings, then info
4. **Export results** - Share with beta readers/editors
5. **Check before submission** - Final quality pass

---

## 🔗 Related Commands

```bash
# Full analysis
python musestat.py

# Semi-compact view
python musestat.py -sc

# Verify only
python musestat.py -v

# Advanced analysis
python musestat.py -a

# Export verification
python musestat.py -v --export html
```

---

**Ready to verify?** Run `python musestat.py --verify` now! 🚀


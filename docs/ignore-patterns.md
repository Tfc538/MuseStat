# 🚫 Ignore Patterns Guide

**User-friendly guide to `.musestatignore` for writers**

---

## 🎯 What is `.musestatignore`?

A file that tells MuseStat to **skip** certain lines when checking your manuscript. Perfect for:

- ✅ Intentional style choices
- ✅ Character names with special formatting
- ✅ Foreign language text
- ✅ Technical terms
- ✅ Section headers you want to keep

---

## ⚡ Quick Start (3 steps)

### 1. Create the File

```bash
# Copy the example file
cp .musestatignore.example .musestatignore

# Or create from scratch
touch .musestatignore
```

### 2. Add Patterns

Open `.musestatignore` in any text editor and add patterns:

```gitignore
# Ignore my character's name
_Minho_

# Ignore author notes
*Author's Note*

# Ignore appendix section
^## Appendix
```

### 3. Test It

```bash
python musestat.py -v
```

You'll see: "5 patterns loaded from .musestatignore"

---

## 📝 Pattern Types (3 simple ways!)

### 1. **Plain Text** (Easiest!)

Just write the text you want to ignore. MuseStat will find it anywhere in a line.

**Examples:**
```gitignore
# Ignore any line with "TODO:"
TODO:

# Ignore character name
Protagonist_Name

# Ignore Korean text
한글
```

**What it matches:**
- Case-insensitive (TODO: = todo: = ToDo:)
- Anywhere in the line
- Exact text match

---

### 2. **Wildcards** (Flexible!)

Use `*` to match anything, `?` to match one character.

**Examples:**
```gitignore
# Match any author note
*Author*

# Match "had had" or "had  had" (with extra space)
had*had

# Match any Korean marker
*[Korean]*

# Match character name variations
_Character?Name_
```

**What `*` does:**
- `*Author*` matches: "Author's Note", "Author Note:", "[AUTHOR]"
- `*TODO*` matches: "TODO:", "[TODO]", "**TODO**"
- `Character*` matches: "Character_Name", "Character123"

**What `?` does:**
- `Chapt?r` matches: "Chapter", "Chaptr"
- `had ?ad` matches: "had had", "had bad"

---

### 3. **Starts With** (Specific!)

Use `^` at the start to only match lines that begin with that pattern.

**Examples:**
```gitignore
# Only match lines starting with "## Appendix"
^## Appendix

# Only match chapter numbers at line start
^Chapter [0-9]

# Only match TODO at the very beginning
^TODO:
```

**Difference:**
- `TODO:` matches anywhere: "Note: TODO: fix this"
- `^TODO:` only matches at start: "TODO: fix this"

---

## 🎨 Real-World Examples

### Fiction Writer

```gitignore
# .musestatignore for Fiction

# My character names have underscores
_Minho_
_Jisoo_

# Ignore my intentional em-dash style
 - 

# Ignore past perfect tense
had had

# Ignore author notes
*Author's Note*

# Ignore Korean dialogue
*[Korean]*

# Ignore character thought markers
*_thought_*
```

---

### Non-Fiction Writer

```gitignore
# .musestatignore for Non-Fiction

# Ignore citations
(20[0-9][0-9])
et al.

# Ignore figure captions
^Figure [0-9]
^Table [0-9]

# Ignore technical terms
API
JSON
URL

# Ignore references section
^## References

# Ignore footnote markers
[^[0-9]]
```

---

### Student/Thesis Writer

```gitignore
# .musestatignore for Thesis

# Ignore bibliography section
^## Bibliography
^## Works Cited

# Ignore citations
(Author, [0-9]
et al.

# Ignore technical notation
^[A-Z]+ =

# Ignore table/figure labels
^Table [0-9]
^Figure [0-9]

# Keep my TODOs during drafting
TODO: (expand)
NOTE: (cite)
```

---

## 💡 Common Patterns Library

### Character Names
```gitignore
# Underscored names
_Character_Name_
*_Protagonist*

# Special formatting
**Character**
*Character*
```

### Foreign Languages
```gitignore
# Korean
한글
*[Korean:*

# Japanese
*[Japanese:*

# Spanish
*[Spanish:*

# Generic
*[Language:*
```

### Intentional Grammar
```gitignore
# Past perfect
had had

# Emphatic repetition
that that
it it

# Dialogue quirks
said said
```

### Style Choices
```gitignore
# Em-dash preference
 - 

# Ellipsis style
....

# Multiple punctuation (in dialogue)
!?
```

### Sections to Skip
```gitignore
# Back matter
^## Appendix
^## Glossary
^## Notes
^## References

# Front matter
^## Dedication
^## Acknowledgments
```

### Technical Content
```gitignore
# Code blocks
```
`code`

# URLs
http
https
www.

# Email addresses
@
```

---

## 🔍 Pattern Matching Rules

### Case Sensitivity
**All patterns are CASE-INSENSITIVE**

```gitignore
TODO: matches todo:, ToDo:, TODO:
Author matches author, AUTHOR, Author
```

### Where It Matches
- **Plain text**: Anywhere in line
- **Wildcards**: Anywhere (unless starting with ^)
- **Starts with (^)**: Beginning of line only

### Multiple Matches
If ANY pattern matches, the line is ignored. Patterns work together!

```gitignore
# Both patterns will ignore the line
*Author*
TODO:
```

---

## ✅ Testing Your Patterns

### Step 1: Add Pattern
```gitignore
# Ignore my character's name
_Minho_
```

### Step 2: Run Verification
```bash
python musestat.py -v
```

### Step 3: Check Results
Look for:
```
Ignore patterns: 1 patterns loaded from .musestatignore
```

### Step 4: Verify It Works
If your pattern works, you'll see fewer issues!

**Before:**
```
🔴 Errors: 10
  - Unmatched underscore (_) - "_Minho_"
```

**After:**
```
🔴 Errors: 9
(No more _Minho_ errors!)
```

---

## 🎯 Best Practices

### 1. Start Simple
```gitignore
# ✅ Good: Simple and clear
Author's Note

# ❌ Avoid: Too complex at first
\[Author'?s?\s+Note\].*
```

### 2. Add Comments
```gitignore
# ✅ Good: Explained
# Ignore my character's special name format
_Minho_

# ❌ Avoid: No explanation
_Minho_
```

### 3. Test One at a Time
Add patterns gradually and test each time:

```bash
# Add one pattern
echo "_Minho_" >> .musestatignore

# Test it
python musestat.py -v

# Add another
echo "*Author*" >> .musestatignore

# Test again
python musestat.py -v
```

### 4. Use Wildcards Wisely
```gitignore
# ✅ Good: Specific
*Author's Note*

# ⚠️ Careful: Very broad
*Note*
```

### 5. Document Your Choices
```gitignore
# Why I'm ignoring this:
# My writing style uses spaced hyphens for em-dashes
# This is intentional and not an error
 - 
```

---

## 🆘 Troubleshooting

### Pattern Not Working?

**Problem**: Pattern doesn't match

**Solutions**:
1. Check for typos
2. Try adding wildcards: `*pattern*`
3. Check case (remember: case-insensitive)
4. Test with simpler version

**Example:**
```gitignore
# Not working?
^## Appendix: References

# Try simpler:
Appendix

# Or with wildcard:
*Appendix*
```

---

### Too Many Lines Ignored?

**Problem**: Pattern too broad

**Solution**: Make it more specific

```gitignore
# ❌ Too broad (ignores ALL "Note")
Note

# ✅ More specific
Author's Note

# ✅ Even more specific
*[Author's Note]*
```

---

### Pattern Seems Ignored?

**Problem**: File not loaded

**Check**:
```bash
python musestat.py -v
```

Should see:
```
Ignore patterns: X patterns loaded
```

**Fixes**:
1. Make sure file is named `.musestatignore` (note the dot!)
2. Make sure it's in the same folder as your manuscript
3. Make sure lines don't start with #

---

## 📚 Examples by Issue Type

### For "Pre-publish Markers"
```gitignore
# Keep TODOs during drafting
TODO: (expand)
FIXME: (later)
NOTE: (check)
```

### For "Repeated Words"
```gitignore
# Intentional grammar
had had
that that
```

### For "Markdown Formatting"
```gitignore
# Character names with underscores
_Character_Name_
*_Name_*
```

### For "Punctuation"
```gitignore
# Style choice for em-dash
 - 

# Ellipsis style
....
```

### For "Smart Quotes"
```gitignore
# Technical terms with straight quotes
"API"
"JSON"
```

---

## 💪 Power User Tips

### Combine Patterns
```gitignore
# Ignore multiple variations
*Author*
*[Author]*
Author's Note
```

### Use Wildcards Creatively
```gitignore
# Match any character name with underscores
*_*_*

# Match any foreign language marker
*[*:*

# Match any figure caption
*Figure *:*
```

### Section-Based Ignoring
```gitignore
# Skip entire sections
^## Appendix
^## References
^## Glossary
^## Index
```

---

## 📖 Complete Example

Here's a complete `.musestatignore` for a fiction manuscript:

```gitignore
# .musestatignore for "Seoul Mate" Novel
# ======================================

# --- Character Names ---
# My characters have underscored names
_Minho_
_Jisoo_
_Sarah_

# --- Foreign Language ---
# Korean dialogue sections
*[Korean:*
한글

# --- Style Choices ---
# I prefer spaced hyphens
 - 

# --- Intentional Grammar ---
# Past perfect tense usage
had had

# Emphatic repetition (dialogue)
that that

# --- Author Notes ---
# Keep during drafting
*[Author's Note]*
*[Editor's Note]*

# --- Sections to Skip ---
# Back matter
^## Appendix
^## Author's Notes
^## Glossary

# --- Technical ---
# URLs in references
http
https

# --- Dialogue Quirks ---
# Character stuttering (intentional)
*"B-but*

# Character trailing (intentional)
*...*

# END OF FILE
```

---

## 🎓 Learning Path

**Day 1**: Create file, add simple text patterns
```gitignore
TODO:
Author's Note
```

**Week 1**: Add wildcards for flexibility
```gitignore
*Author*
*Character*
```

**Week 2**: Use "starts with" for precision
```gitignore
^## Appendix
^Chapter
```

**Month 1**: Build complete custom ignore file for your manuscript

---

## 🔗 Related Documentation

- [Verification Guide](verification-guide.md) - What gets checked
- [FAQ](faq.md) - Common questions
- [User Guide](user-guide.md) - Complete MuseStat guide

---

**Ready to customize?** Copy `.musestatignore.example` and start adding your patterns! 🚀



"""
Manuscript verification and quality checking.

Provides comprehensive validation of manuscript formatting, typos, and readiness for publishing.
"""

import re
from pathlib import Path
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional


class IssueType(Enum):
    """Types of verification issues."""
    ERROR = ("ERROR", "red")
    WARNING = ("WARNING", "yellow")
    INFO = ("INFO", "cyan")


@dataclass
class Issue:
    """Represents a validation issue."""
    type: IssueType
    category: str
    message: str
    line_number: Optional[int] = None
    line_preview: Optional[str] = None
    suggestion: Optional[str] = None


def load_ignore_patterns() -> List[str]:
    """
    Load ignore patterns from .musestatignore file.
    
    Returns:
        List of ignore patterns
    """
    ignore_file = Path('.musestatignore')
    patterns = []
    
    if ignore_file.exists():
        try:
            with open(ignore_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # Skip empty lines and comments
                    if line and not line.startswith('#'):
                        patterns.append(line)
        except Exception:
            # Silently fail if we can't read the file
            pass
    
    return patterns


def should_ignore_line(line: str, line_number: int, ignore_patterns: List[str]) -> bool:
    """
    Check if a line should be ignored based on .musestatignore patterns.
    
    Supports multiple pattern types:
    - Plain text: "TODO:" matches lines containing TODO:
    - Wildcards: "*Author*" matches any line with Author  
    - Starts with: "^## Chapter" matches lines starting with ## Chapter
    - Regex: Advanced users can still use regex patterns
    
    Args:
        line: The line to check
        line_number: Line number (not used currently but kept for future use)
        ignore_patterns: List of patterns to match against
        
    Returns:
        True if the line should be ignored, False otherwise
    """
    line_lower = line.lower()
    
    for pattern in ignore_patterns:
        # Handle simple wildcards (* and ?)
        if '*' in pattern or '?' in pattern:
            # Use simple string matching for wildcards instead of regex
            # This is much faster and avoids catastrophic backtracking
            pattern_lower = pattern.lower()
            
            # Split by * to get parts that must appear in order
            parts = pattern_lower.split('*')
            
            # Check if all parts appear in order
            pos = 0
            match = True
            for part in parts:
                if not part:  # Empty part from leading/trailing *
                    continue
                # Handle ? wildcards in this part
                if '?' in part:
                    # Convert to simple regex for single character matching
                    part_regex = part.replace('?', '.')
                    try:
                        found = re.search(part_regex, line_lower[pos:])
                        if found:
                            pos += found.end()
                        else:
                            match = False
                            break
                    except Exception:
                        match = False
                        break
                else:
                    # Simple text search
                    idx = line_lower.find(part, pos)
                    if idx == -1:
                        match = False
                        break
                    pos = idx + len(part)
            
            if match:
                return True
                
        # Handle "starts with" pattern (^)
        elif pattern.startswith('^'):
            check_pattern = pattern[1:].lower()
            if line_lower.startswith(check_pattern):
                return True
                
        # Plain text or regex
        else:
            # Try simple text match first (fast)
            if pattern.lower() in line_lower:
                return True
            # Try as regex for advanced users (only if text match fails)
            try:
                if re.search(pattern, line, re.IGNORECASE):
                    return True
            except (re.error, Exception):
                pass
    
    return False


def verify_manuscript(text: str, ignore_patterns: Optional[List[str]] = None) -> List[Issue]:
    """
    Run comprehensive verification checks on manuscript.
    
    Args:
        text: Full manuscript text
        ignore_patterns: Optional list of patterns to ignore (loaded from file if None)
        
    Returns:
        List of Issue objects found during verification
    """
    if ignore_patterns is None:
        ignore_patterns = load_ignore_patterns()
    
    # Cache for ignored lines to avoid repeated checks
    ignored_lines_cache = {}
    has_patterns = len(ignore_patterns) > 0
    
    def is_line_ignored(line: str, line_num: int) -> bool:
        """Check if line should be ignored (with caching)."""
        if not has_patterns:
            return False
        if line_num in ignored_lines_cache:
            return ignored_lines_cache[line_num]
        result = should_ignore_line(line, line_num, ignore_patterns)
        ignored_lines_cache[line_num] = result
        return result
    
    issues = []
    lines = text.split('\n')
    in_code_block = False
    
    # 1. Check for unmatched emphasis markers (*, **, _)
    for i, line in enumerate(lines, 1):
        if is_line_ignored(line, i):
            continue
        
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
        
        if in_code_block:
            continue
        
        # Check for unmatched single asterisks
        single_asterisks = len(re.findall(r'(?<!\*)\*(?!\*)', line))
        if single_asterisks % 2 != 0 and not re.match(r'^\s*\*\s', line):  # Not a bullet point
            preview = line.strip()[:70]
            issues.append(Issue(
                type=IssueType.ERROR,
                category="Markdown Formatting",
                message="Unmatched asterisk (*) - italic formatting incomplete",
                line_number=i,
                line_preview=preview,
                suggestion="Ensure all * have matching pairs"
            ))
        
        # Check for unmatched double asterisks
        double_asterisks = len(re.findall(r'(?<!\*)\*\*(?!\*)', line))
        if double_asterisks % 2 != 0:
            preview = line.strip()[:70]
            issues.append(Issue(
                type=IssueType.ERROR,
                category="Markdown Formatting",
                message="Unmatched double asterisk (**) - bold formatting incomplete",
                line_number=i,
                line_preview=preview,
                suggestion="Ensure all ** have matching pairs"
            ))
        
        # Check for triple asterisks (likely error)
        if '***' in line and not re.match(r'^\s*\*\*\*\s*$', line):
            preview = line.strip()[:70]
            issues.append(Issue(
                type=IssueType.WARNING,
                category="Markdown Formatting",
                message="Triple asterisk (***) found - may be formatting error",
                line_number=i,
                line_preview=preview,
                suggestion="Use ** for bold or * for italic, or *** for scene break"
            ))
        
        # Check for unmatched underscores
        underscores = len(re.findall(r'(?<!_)_(?!_)', line))
        if underscores % 2 != 0 and not re.search(r'\w+_\w+', line):  # Not snake_case
            preview = line.strip()[:70]
            issues.append(Issue(
                type=IssueType.WARNING,
                category="Markdown Formatting",
                message="Unmatched underscore (_) - incomplete emphasis",
                line_number=i,
                line_preview=preview,
                suggestion="Ensure all _ have matching pairs"
            ))
    
    # 2. Check for TODO/FIXME markers
    for i, line in enumerate(lines, 1):
        if is_line_ignored(line, i):
            continue
        
        for keyword in ['TODO', 'FIXME', 'XXX', 'HACK', 'NOTE:', 'TK', 'TBD', 'PLACEHOLDER']:
            if keyword in line.upper():
                preview = line.strip()[:70]
                issues.append(Issue(
                    type=IssueType.ERROR,
                    category="Pre-publish",
                    message=f"'{keyword}' marker found - should be resolved before publishing",
                    line_number=i,
                    line_preview=preview,
                    suggestion="Complete or remove this marker"
                ))
                break
    
    # 3. Check for common typos and repeated words
    for i, line in enumerate(lines, 1):
        if is_line_ignored(line, i):
            continue
        
        line_lower = line.lower()
        for pattern, msg in [
            (r'\bthe\s+the\b', "Repeated 'the the'"),
            (r'\ba\s+a\b', "Repeated 'a a'"),
            (r'\band\s+and\b', "Repeated 'and and'"),
            (r'\bto\s+to\b', "Repeated 'to to'"),
            (r'\bof\s+of\b', "Repeated 'of of'"),
            (r'\bin\s+in\b', "Repeated 'in in'"),
            (r'\bit\s+it\b', "Repeated 'it it'"),
        ]:
            if re.search(pattern, line_lower):
                preview = line.strip()[:70]
                issues.append(Issue(
                    type=IssueType.WARNING,
                    category="Typos",
                    message=msg,
                    line_number=i,
                    line_preview=preview,
                    suggestion="Remove duplicate word"
                ))
    
    # 4. Check punctuation issues
    for i, line in enumerate(lines, 1):
        if is_line_ignored(line, i):
            continue
        
        # Multiple exclamation/question marks
        if re.search(r'[!?]{2,}', line):
            preview = line.strip()[:70]
            issues.append(Issue(
                type=IssueType.WARNING,
                category="Punctuation",
                message="Multiple consecutive exclamation/question marks",
                line_number=i,
                line_preview=preview,
                suggestion="Use single punctuation for professional writing"
            ))
        
        # Space before punctuation
        if re.search(r'\s[.,!?;:]', line):
            preview = line.strip()[:70]
            issues.append(Issue(
                type=IssueType.ERROR,
                category="Punctuation",
                message="Space before punctuation mark",
                line_number=i,
                line_preview=preview,
                suggestion="Remove space before punctuation"
            ))
        
        # Check for ellipsis issues
        if re.search(r'\.{4,}', line):
            preview = line.strip()[:70]
            issues.append(Issue(
                type=IssueType.WARNING,
                category="Punctuation",
                message="Too many dots in ellipsis (should be 3)",
                line_number=i,
                line_preview=preview,
                suggestion="Use three dots (...) or unicode ellipsis (…)"
            ))
        
        # Check for em-dash vs hyphen
        if ' - ' in line:
            preview = line.strip()[:70]
            issues.append(Issue(
                type=IssueType.INFO,
                category="Punctuation",
                message="Spaced hyphen found - consider em-dash",
                line_number=i,
                line_preview=preview,
                suggestion="Use em-dash (—) without spaces for professional formatting"
            ))
    
    # 5. Check for whitespace issues
    for i, line in enumerate(lines, 1):
        if is_line_ignored(line, i):
            continue
        
        # Trailing whitespace
        if line and (line[-1] == ' ' or line[-1] == '\t'):
            issues.append(Issue(
                type=IssueType.INFO,
                category="Whitespace",
                message="Trailing whitespace at end of line",
                line_number=i,
                suggestion="Remove trailing spaces/tabs"
            ))
        
        # Multiple consecutive spaces (not indentation)
        if '  ' in line.strip():
            spaces = re.findall(r' {2,}', line.strip())
            if spaces:
                max_spaces = max(len(s) for s in spaces)
                if max_spaces > 2:
                    preview = line.strip()[:70]
                    issues.append(Issue(
                        type=IssueType.WARNING,
                        category="Whitespace",
                        message=f"Multiple consecutive spaces ({max_spaces}) found",
                        line_number=i,
                        line_preview=preview,
                        suggestion="Use single spaces between words"
                    ))
        
        # Tabs in content
        if '\t' in line and line.strip():
            preview = line.strip()[:70]
            issues.append(Issue(
                type=IssueType.INFO,
                category="Whitespace",
                message="Tab character found in content",
                line_number=i,
                line_preview=preview,
                suggestion="Use spaces instead of tabs"
            ))
    
    # 6. Check heading structure
    prev_level = 0
    
    for i, line in enumerate(lines, 1):
        if is_line_ignored(line, i):
            continue
        
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        
        if heading_match:
            level = len(heading_match.group(1))
            
            # Check for proper spacing after #
            if not re.match(r'^#{1,6}\s+\S', line):
                issues.append(Issue(
                    type=IssueType.ERROR,
                    category="Heading Format",
                    message="Missing space after # in heading",
                    line_number=i,
                    line_preview=line.strip(),
                    suggestion="Add space: '# Title' not '#Title'"
                ))
            
            # Check for skipped levels
            if prev_level > 0 and level > prev_level + 1:
                issues.append(Issue(
                    type=IssueType.WARNING,
                    category="Heading Hierarchy",
                    message=f"Heading level skipped (H{prev_level} to H{level})",
                    line_number=i,
                    line_preview=line.strip(),
                    suggestion="Use proper heading hierarchy without skipping levels"
                ))
            
            prev_level = level
    
    # 7. Check for smart quotes consistency
    straight_double = text.count('"')
    curly_double = text.count(""") + text.count(""")
    
    if straight_double > 10 and curly_double > 10:
        issues.append(Issue(
            type=IssueType.WARNING,
            category="Smart Quotes",
            message=f"Mixed straight ({straight_double}) and curly ({curly_double}) quotes",
            suggestion="Use consistent quote style throughout manuscript"
        ))
    
    # 8. Check for markdown links
    for i, line in enumerate(lines, 1):
        if is_line_ignored(line, i):
            continue
        
        # Malformed links
        if '[' in line and ']' in line:
            open_brackets = line.count('[')
            close_brackets = line.count(']')
            if open_brackets != close_brackets:
                preview = line.strip()[:70]
                issues.append(Issue(
                    type=IssueType.ERROR,
                    category="Markdown Links",
                    message="Unmatched square brackets [ ]",
                    line_number=i,
                    line_preview=preview,
                    suggestion="Ensure all brackets are properly paired"
                ))
    
    # 9. Check for paragraph spacing
    consecutive_blanks = 0
    for i, line in enumerate(lines, 1):
        if not line.strip():
            consecutive_blanks += 1
        else:
            if consecutive_blanks > 2:
                issues.append(Issue(
                    type=IssueType.INFO,
                    category="Spacing",
                    message=f"{consecutive_blanks} consecutive blank lines",
                    line_number=i-1,
                    suggestion="Use single blank line between paragraphs"
                ))
            consecutive_blanks = 0
    
    # 10. Check for very long lines (> 1000 characters - potential formatting issue)
    for i, line in enumerate(lines, 1):
        if len(line) > 1000:
            issues.append(Issue(
                type=IssueType.WARNING,
                category="Line Length",
                message=f"Very long line ({len(line)} characters)",
                line_number=i,
                suggestion="Consider breaking into multiple lines"
            ))
    
    # 11. Check for inconsistent dialogue quotes
    for i, line in enumerate(lines, 1):
        if is_line_ignored(line, i):
            continue
        
        # Check for dialogue with straight quotes in otherwise curly quote document
        if curly_double > straight_double * 2:  # Mostly curly
            if '"' in line and re.search(r'\w+\s+"[^"]+"\s+\w+', line):
                preview = line.strip()[:70]
                issues.append(Issue(
                    type=IssueType.INFO,
                    category="Smart Quotes",
                    message="Straight quote in primarily curly-quote document",
                    line_number=i,
                    line_preview=preview,
                    suggestion="Consider using curly quotes for consistency"
                ))
    
    # 12. Check for common manuscript issues
    for i, line in enumerate(lines, 1):
        if is_line_ignored(line, i):
            continue
        
        # Check for placeholder text
        if '[INSERT' in line.upper() or '[ADD' in line.upper() or '[EDIT' in line.upper():
            preview = line.strip()[:70]
            issues.append(Issue(
                type=IssueType.ERROR,
                category="Incomplete Content",
                message="Placeholder text found",
                line_number=i,
                line_preview=preview,
                suggestion="Replace with actual content before publishing"
            ))
        
        # Check for Lorem Ipsum
        if 'lorem ipsum' in line.lower():
            preview = line.strip()[:70]
            issues.append(Issue(
                type=IssueType.ERROR,
                category="Incomplete Content",
                message="Lorem Ipsum placeholder text found",
                line_number=i,
                line_preview=preview,
                suggestion="Replace with actual content"
            ))
    
    return issues


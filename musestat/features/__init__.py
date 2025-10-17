"""Feature modules for advanced manuscript analysis."""

from .language import detect_language, get_language_stopwords
from .dialogue import count_dialogue
from .readability import calculate_readability, detect_pacing_issues
from .verification import (
    verify_manuscript,
    load_ignore_patterns,
    should_ignore_line,
    Issue,
    IssueType
)

__all__ = [
    'detect_language',
    'get_language_stopwords',
    'count_dialogue',
    'calculate_readability',
    'detect_pacing_issues',
    'verify_manuscript',
    'load_ignore_patterns',
    'should_ignore_line',
    'Issue',
    'IssueType',
]


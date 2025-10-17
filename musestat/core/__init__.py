"""Core manuscript analysis modules."""

from .analyzer import analyze_manuscript
from .text_processing import (
    clean_markdown,
    count_words,
    count_characters,
    count_sentences,
    count_paragraphs,
    get_most_common_words
)
from .chapter import extract_chapters, calculate_chapter_statistics

__all__ = [
    'analyze_manuscript',
    'clean_markdown',
    'count_words',
    'count_characters',
    'count_sentences',
    'count_paragraphs',
    'get_most_common_words',
    'extract_chapters',
    'calculate_chapter_statistics',
]


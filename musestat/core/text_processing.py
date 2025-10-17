"""
Text processing utilities for manuscript analysis.

Handles text cleaning, word/character counting, and keyword extraction.
"""

import re
from collections import Counter
from typing import List, Tuple


def clean_markdown(text: str) -> str:
    """
    Remove markdown formatting for accurate word counting.
    
    Args:
        text: Raw text with markdown formatting
        
    Returns:
        Cleaned text without markdown syntax
    """
    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    # Remove inline code
    text = re.sub(r'`[^`]+`', '', text)
    # Remove markdown links but keep text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove images
    text = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', '', text)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove markdown headers symbols
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
    # Remove emphasis markers
    text = re.sub(r'[*_]{1,3}([^*_]+)[*_]{1,3}', r'\1', text)
    return text


def count_words(text: str) -> int:
    """
    Count words in text.
    
    Args:
        text: Text to count words in
        
    Returns:
        Number of words
    """
    clean_text = clean_markdown(text)
    words = re.findall(r'\b\w+\b', clean_text)
    return len(words)


def count_characters(text: str, include_spaces: bool = True) -> int:
    """
    Count characters in text.
    
    Args:
        text: Text to count characters in
        include_spaces: Whether to include spaces in the count
        
    Returns:
        Number of characters
    """
    clean_text = clean_markdown(text)
    if include_spaces:
        return len(clean_text)
    return len(re.sub(r'\s', '', clean_text))


def count_sentences(text: str) -> int:
    """
    Count sentences in text.
    
    Args:
        text: Text to count sentences in
        
    Returns:
        Number of sentences
    """
    clean_text = clean_markdown(text)
    sentences = re.split(r'[.!?]+', clean_text)
    return len([s for s in sentences if s.strip()])


def count_paragraphs(text: str) -> int:
    """
    Count paragraphs in text.
    
    Args:
        text: Text to count paragraphs in
        
    Returns:
        Number of paragraphs
    """
    paragraphs = re.split(r'\n\s*\n', text)
    return len([p for p in paragraphs if p.strip()])


def get_most_common_words(text: str, n: int = 20, stop_words: set = None, min_length: int = 3) -> List[Tuple[str, int]]:
    """
    Get the most common words (excluding stop words).
    
    Args:
        text: Text to analyze
        n: Number of top words to return
        stop_words: Set of words to exclude (if None, uses empty set)
        min_length: Minimum word length to include (default: 3)
        
    Returns:
        List of (word, count) tuples for the most common words
    """
    if stop_words is None:
        stop_words = set()
    
    clean_text = clean_markdown(text).lower()
    words = re.findall(r'\b\w+\b', clean_text)
    words = [w for w in words if w not in stop_words and len(w) >= min_length]
    
    return Counter(words).most_common(n)


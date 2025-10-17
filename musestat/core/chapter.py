"""
Chapter extraction and analysis for manuscripts.
"""

import re
from typing import List, Dict, Optional
from .text_processing import count_words


def extract_chapters(text: str) -> List[Dict]:
    """
    Extract chapter information with smart detection.
    
    Recognizes multiple chapter formats:
    - # Chapter Title (Markdown H1)
    - ## Chapter Title (Markdown H2)
    - Chapter 1: Title
    - CHAPTER 1: Title
    - Ch. 1: Title
    
    Args:
        text: Full manuscript text
        
    Returns:
        List of chapter dictionaries with title, content, words, and scenes
    """
    chapters = []
    lines = text.split('\n')
    
    # Patterns for chapter detection
    patterns = [
        r'^#\s+(.+)$',  # Markdown H1
        r'^##\s+(.+)$',  # Markdown H2
        r'^Chapter\s+\d+[:\s]+(.+)',  # "Chapter 1: Title"
        r'^CHAPTER\s+\d+[:\s]+(.+)',  # "CHAPTER 1: Title"
        r'^Ch\.\s*\d+[:\s]+(.+)',  # "Ch. 1: Title"
    ]
    
    current_chapter = None
    chapter_content = []
    scene_break_count = 0
    
    for line in lines:
        # Check for scene breaks (*** or ---)
        if re.match(r'^\s*\*\*\*\s*$', line) or re.match(r'^\s*---\s*$', line):
            scene_break_count += 1
        
        # Check all chapter patterns
        matched = False
        for pattern in patterns:
            match = re.match(pattern, line)
            if match:
                # Save previous chapter if exists
                if current_chapter:
                    chapters.append({
                        'title': current_chapter,
                        'content': '\n'.join(chapter_content),
                        'words': count_words('\n'.join(chapter_content)),
                        'scenes': scene_break_count
                    })
                
                current_chapter = match.group(1).strip()
                chapter_content = []
                scene_break_count = 0
                matched = True
                break
        
        if not matched and current_chapter:
            chapter_content.append(line)
    
    # Add final chapter if exists
    if current_chapter:
        chapters.append({
            'title': current_chapter,
            'content': '\n'.join(chapter_content),
            'words': count_words('\n'.join(chapter_content)),
            'scenes': scene_break_count
        })
    
    return chapters


def calculate_chapter_statistics(chapters: List[Dict]) -> Optional[Dict]:
    """
    Calculate statistical measures for chapter lengths.
    
    Args:
        chapters: List of chapter dictionaries from extract_chapters()
        
    Returns:
        Dictionary with mean, std_dev, min, max, range, and chapter names,
        or None if no chapters provided
    """
    if not chapters:
        return None
    
    word_counts = [ch['words'] for ch in chapters]
    
    if not word_counts:
        return None
    
    # Calculate statistics
    mean = sum(word_counts) / len(word_counts)
    
    # Standard deviation
    variance = sum((x - mean) ** 2 for x in word_counts) / len(word_counts)
    std_dev = variance ** 0.5
    
    # Min and max
    min_words = min(word_counts)
    max_words = max(word_counts)
    
    # Find chapters
    shortest = min(chapters, key=lambda x: x['words'])
    longest = max(chapters, key=lambda x: x['words'])
    
    return {
        'mean': mean,
        'std_dev': std_dev,
        'min': min_words,
        'max': max_words,
        'range': max_words - min_words,
        'shortest_chapter': shortest['title'],
        'longest_chapter': longest['title'],
        'coefficient_of_variation': (std_dev / mean * 100) if mean > 0 else 0
    }


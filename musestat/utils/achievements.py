"""
Achievement badges, quotes, and reading time estimation.
"""

import random
from typing import Dict
from .constants import (
    WRITER_QUOTES,
    ACHIEVEMENT_MILESTONES,
    READING_SPEED_FAST,
    READING_SPEED_AVERAGE,
    READING_SPEED_SLOW,
    WORDS_PER_PAGE_DENSE,
    WORDS_PER_PAGE_STANDARD,
    WORDS_PER_PAGE_LOOSE
)


def get_achievement_badge(word_count: int, prev_word_count: int = 0) -> Dict:
    """
    Get achievement badge based on word count milestones.
    
    Args:
        word_count: Current word count
        prev_word_count: Previous word count (for detecting newly unlocked badges)
        
    Returns:
        Dictionary with badge information (threshold, title, icon, message, unlocked status)
    """
    # Find current milestone
    current_badge = None
    for threshold, title, icon, message in ACHIEVEMENT_MILESTONES:
        if word_count >= threshold:
            current_badge = {
                'threshold': threshold,
                'title': title,
                'icon': icon,
                'message': message,
                'unlocked': True
            }
            # Continue to find the highest milestone
    
    # Check if just crossed a threshold (find highest newly crossed)
    newly_unlocked_badge = None
    for threshold, title, icon, message in ACHIEVEMENT_MILESTONES:
        if prev_word_count < threshold <= word_count:
            newly_unlocked_badge = {
                'threshold': threshold,
                'title': title,
                'icon': icon,
                'message': message,
                'unlocked': True,
                'newly_unlocked': True
            }
            # Continue to find the highest newly unlocked
    
    # If we found a newly unlocked badge, use that instead
    if newly_unlocked_badge:
        current_badge = newly_unlocked_badge
    
    if not current_badge:
        # No milestone yet
        next_milestone = ACHIEVEMENT_MILESTONES[0]
        return {
            'threshold': next_milestone[0],
            'title': next_milestone[1],
            'icon': next_milestone[2],
            'message': f"Keep writing! {next_milestone[0] - word_count:,} words to '{next_milestone[1]}'",
            'unlocked': False
        }
    
    return current_badge


def get_random_quote() -> str:
    """
    Get a random motivational quote for writers.
    
    Returns:
        Random quote string
    """
    return random.choice(WRITER_QUOTES)


def estimate_reading_time(word_count: int) -> Dict:
    """
    Estimate reading time with range based on reading speed.
    
    Uses research-backed reading speeds:
    - Fast readers: 300 wpm
    - Average readers: 250 wpm  
    - Slow/careful readers: 200 wpm
    
    Args:
        word_count: Total word count
        
    Returns:
        Dictionary with reading time estimates and page counts
    """
    # Calculate for different speeds
    fast_minutes = word_count / READING_SPEED_FAST
    avg_minutes = word_count / READING_SPEED_AVERAGE
    slow_minutes = word_count / READING_SPEED_SLOW
    
    # Convert to hours and minutes
    def to_hours_mins(minutes):
        return int(minutes // 60), int(minutes % 60)
    
    fast_h, fast_m = to_hours_mins(fast_minutes)
    avg_h, avg_m = to_hours_mins(avg_minutes)
    slow_h, slow_m = to_hours_mins(slow_minutes)
    
    # Estimate pages (assuming ~300 words per page for fiction)
    pages_min = int(word_count / WORDS_PER_PAGE_DENSE)  # Dense pages
    pages_max = int(word_count / WORDS_PER_PAGE_LOOSE)  # Loose pages
    pages_avg = int(word_count / WORDS_PER_PAGE_STANDARD)  # Standard
    
    return {
        'fast': (fast_h, fast_m),
        'average': (avg_h, avg_m),
        'slow': (slow_h, slow_m),
        'pages_min': pages_min,
        'pages_max': pages_max,
        'pages_avg': pages_avg,
        'range_str': f"{fast_h}h {fast_m}m - {slow_h}h {slow_m}m",
        'pages_str': f"{pages_min}-{pages_max} pages (~{pages_avg} avg)"
    }


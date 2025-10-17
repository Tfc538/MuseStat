"""
Main manuscript analysis orchestration.
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, Optional
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from ..io.readers import read_manuscript
from .text_processing import (
    count_words,
    count_characters,
    count_sentences,
    count_paragraphs,
    get_most_common_words
)
from .chapter import extract_chapters, calculate_chapter_statistics
from ..features.language import detect_language, get_language_stopwords
from ..features.dialogue import count_dialogue
from ..features.readability import calculate_readability, detect_pacing_issues
from ..utils.achievements import get_achievement_badge, estimate_reading_time

console = Console()


def analyze_manuscript(file_path: str, enable_advanced: bool = False, show_progress: bool = True) -> Optional[Dict]:
    """
    Analyze the manuscript and return comprehensive statistics.
    
    Args:
        file_path: Path to manuscript file
        enable_advanced: Enable advanced features (readability, dialogue, pacing)
        show_progress: Show progress indicators during analysis
        
    Returns:
        Dictionary with all statistics, or None if analysis failed
    """
    if show_progress:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("[cyan]Reading file...", total=100)
            text = read_manuscript(file_path)
            progress.update(task, advance=20)
            
            if not text:
                return None
            
            progress.update(task, description="[cyan]Counting words...", advance=20)
            total_words = count_words(text)
            total_chars = count_characters(text, include_spaces=True)
            total_chars_no_spaces = count_characters(text, include_spaces=False)
            
            progress.update(task, description="[cyan]Analyzing structure...", advance=20)
            total_sentences = count_sentences(text)
            total_paragraphs = count_paragraphs(text)
            chapters = extract_chapters(text)
            
            progress.update(task, description="[cyan]Extracting keywords...", advance=20)
            language = detect_language(text) if enable_advanced else 'en'
            stop_words = get_language_stopwords(language)
            common_words = get_most_common_words(text, n=20, stop_words=stop_words)
            
            progress.update(task, description="[cyan]Finalizing...", advance=20)
    else:
        text = read_manuscript(file_path)
        if not text:
            return None
        
        total_words = count_words(text)
        total_chars = count_characters(text, include_spaces=True)
        total_chars_no_spaces = count_characters(text, include_spaces=False)
        total_sentences = count_sentences(text)
        total_paragraphs = count_paragraphs(text)
        chapters = extract_chapters(text)
        language = detect_language(text) if enable_advanced else 'en'
        stop_words = get_language_stopwords(language)
        common_words = get_most_common_words(text, n=20, stop_words=stop_words)
    
    # Build statistics dictionary
    stats = {
        'file_path': file_path,
        'file_size': Path(file_path).stat().st_size,
        'modified_date': datetime.fromtimestamp(Path(file_path).stat().st_mtime),
        'language': language,
        'total_words': total_words,
        'total_characters': total_chars,
        'total_characters_no_spaces': total_chars_no_spaces,
        'total_sentences': total_sentences,
        'total_paragraphs': total_paragraphs,
        'chapters': chapters,
        'common_words': common_words,
    }
    
    # Calculate derived statistics
    if stats['total_sentences'] > 0:
        stats['avg_words_per_sentence'] = stats['total_words'] / stats['total_sentences']
    else:
        stats['avg_words_per_sentence'] = 0
    
    stats['reading_time'] = estimate_reading_time(stats['total_words'])
    stats['chapter_stats'] = calculate_chapter_statistics(chapters)
    stats['badge'] = get_achievement_badge(stats['total_words'])
    
    # Advanced features
    if enable_advanced:
        if show_progress:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
                transient=True
            ) as progress:
                task = progress.add_task("[cyan]Advanced analysis...", total=100)
                
                progress.update(task, description="[cyan]Analyzing dialogue...", advance=33)
                stats['dialogue'] = count_dialogue(text)
                
                progress.update(task, description="[cyan]Checking pacing...", advance=33)
                stats['pacing'] = detect_pacing_issues(text)
                
                progress.update(task, description="[cyan]Calculating readability...", advance=34)
                stats['readability'] = calculate_readability(text)
        else:
            stats['dialogue'] = count_dialogue(text)
            stats['pacing'] = detect_pacing_issues(text)
            stats['readability'] = calculate_readability(text)
    
    return stats


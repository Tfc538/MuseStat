"""
Table creation functions for Rich UI display.
"""

from pathlib import Path
from typing import Dict, List, Optional
from rich.table import Table
from rich.text import Text
from rich import box

from .visualizations import (
    get_readability_indicator,
    create_horizontal_bar,
    create_sparkline
)


def create_overview_table(stats: Dict) -> Table:
    """Create overview statistics table."""
    table = Table(
        title="Overview Statistics",
        box=box.ROUNDED,
        border_style="cyan",
        header_style="bold cyan",
        show_header=True,
        title_style="bold cyan"
    )
    
    table.add_column("Metric", style="bold yellow", width=30)
    table.add_column("Value", style="bold green", justify="right", width=20)
    
    # File info
    table.add_row("File Name", Path(stats['file_path']).name)
    table.add_row("File Size", f"{stats['file_size']:,} bytes")
    table.add_row("Last Modified", stats['modified_date'].strftime("%Y-%m-%d %H:%M:%S"))
    
    if stats.get('language') and stats['language'] != 'unknown':
        table.add_row("Language", stats['language'].upper())
    
    table.add_row("", "")  # Spacer
    
    # Word counts
    table.add_row("Total Words", f"{stats['total_words']:,}", style="bold bright_green")
    table.add_row("Characters (with spaces)", f"{stats['total_characters']:,}")
    table.add_row("Characters (no spaces)", f"{stats['total_characters_no_spaces']:,}")
    table.add_row("", "")  # Spacer
    
    # Structure
    table.add_row("Sentences", f"{stats['total_sentences']:,}")
    table.add_row("Paragraphs", f"{stats['total_paragraphs']:,}")
    table.add_row("Chapters", f"{len(stats['chapters']):,}")
    table.add_row("", "")  # Spacer
    
    # Averages
    table.add_row("Avg Words/Sentence", f"{stats['avg_words_per_sentence']:.1f}")
    if len(stats['chapters']) > 0:
        avg_chapter_words = stats['total_words'] / len(stats['chapters'])
        table.add_row("Avg Words/Chapter", f"{avg_chapter_words:,.0f}")
    
    # Reading time
    rt = stats['reading_time']
    table.add_row("", "")  # Spacer
    table.add_row("Estimated Reading Time", rt['range_str'], style="bold bright_cyan")
    table.add_row(" Estimated Pages", rt['pages_str'], style="bold bright_cyan")
    
    # Dialogue stats if available
    if stats.get('dialogue'):
        table.add_row("", "")  # Spacer
        table.add_row("Dialogue Lines", f"{stats['dialogue']['lines']:,}")
        table.add_row("Dialogue Ratio", f"{stats['dialogue']['ratio']:.1f}%")
    
    return table


def create_readability_table(readability: Dict) -> Optional[Table]:
    """Create readability metrics table with color-coded indicators."""
    if not readability:
        return None
    
    table = Table(
        title="Readability Metrics",
        box=box.ROUNDED,
        border_style="green",
        header_style="bold green",
        title_style="bold green"
    )
    
    table.add_column("Metric", style="bold cyan", width=35)
    table.add_column("Score", style="bold yellow", justify="right", width=10)
    table.add_column("Indicator", justify="center", width=5)
    table.add_column("Interpretation", style="dim", width=30)
    
    # Flesch Reading Ease
    fre = readability['flesch_reading_ease']
    if fre >= 90:
        fre_level = "Very Easy (5th grade)"
    elif fre >= 80:
        fre_level = "Easy (6th grade)"
    elif fre >= 70:
        fre_level = "Fairly Easy (7th grade)"
    elif fre >= 60:
        fre_level = "Standard (8-9th grade)"
    elif fre >= 50:
        fre_level = "Fairly Difficult (10-12th)"
    elif fre >= 30:
        fre_level = "Difficult (College)"
    else:
        fre_level = "Very Difficult (Graduate)"
    
    # Get color-coded indicators
    fre_symbol, fre_color, fre_status = get_readability_indicator(fre, "flesch")
    fk_symbol, fk_color, fk_status = get_readability_indicator(readability['flesch_kincaid_grade'], "grade")
    gf_symbol, gf_color, gf_status = get_readability_indicator(readability['gunning_fog'], "fog")
    cl_symbol, cl_color, cl_status = get_readability_indicator(readability['coleman_liau_index'], "grade")
    ar_symbol, ar_color, ar_status = get_readability_indicator(readability['automated_readability_index'], "grade")
    
    # Create Text objects for colored indicators
    fre_indicator = Text(fre_symbol, style=fre_color)
    fk_indicator = Text(fk_symbol, style=fk_color)
    gf_indicator = Text(gf_symbol, style=gf_color)
    cl_indicator = Text(cl_symbol, style=cl_color)
    ar_indicator = Text(ar_symbol, style=ar_color)
    
    table.add_row("Flesch Reading Ease", f"{fre:.1f}", fre_indicator, fre_level)
    table.add_row("Flesch-Kincaid Grade", f"{readability['flesch_kincaid_grade']:.1f}", fk_indicator, f"{fk_status} - US Grade Level")
    table.add_row("Gunning Fog Index", f"{readability['gunning_fog']:.1f}", gf_indicator, f"{gf_status} - Years of education")
    table.add_row("Coleman-Liau Index", f"{readability['coleman_liau_index']:.1f}", cl_indicator, f"{cl_status} - US Grade Level")
    table.add_row("Automated Readability Index", f"{readability['automated_readability_index']:.1f}", ar_indicator, f"{ar_status} - US Grade Level")
    
    return table


def create_pacing_table(pacing: Dict) -> Optional[Table]:
    """Create pacing analysis table."""
    if not pacing:
        return None
    
    table = Table(
        title="Pacing Analysis",
        box=box.ROUNDED,
        border_style="yellow",
        header_style="bold yellow",
        title_style="bold yellow"
    )
    
    table.add_column("Metric", style="bold cyan", width=30)
    table.add_column("Value", style="bold green", justify="right", width=15)
    table.add_column("Notes", style="dim", width=40)
    
    table.add_row("Avg Sentence Length", f"{pacing['avg_sentence_length']:.1f} words", 
                  "Ideal: 15-20 words")
    table.add_row("Avg Paragraph Length", f"{pacing['avg_paragraph_length']:.0f} words",
                  "Ideal: 50-150 words")
    
    table.add_row("", "", "")
    table.add_row("Long Sentences (>40 words)", f"{len(pacing['long_sentences'])}", 
                  "May slow pacing")
    table.add_row("Long Paragraphs (>200 words)", f"{len(pacing['long_paragraphs'])}", 
                  "May lose reader attention")
    table.add_row("Short Paragraphs (<10 words)", f"{len(pacing['short_paragraphs'])}", 
                  "Creates fast pacing")
    
    return table


def create_chapters_table(chapters: List[Dict], max_chapters: Optional[int] = None, sparkline_width: int = 40) -> Table:
    """
    Create chapters breakdown table with visual enhancements.
    
    Args:
        chapters: List of chapter dictionaries
        max_chapters: Maximum number of chapters to display (default: all)
        sparkline_width: Width of the sparkline chart (default: 40)
    """
    # Determine which chapters to display
    display_chapters = chapters if max_chapters is None else chapters[:max_chapters]
    
    # Create sparkline from all chapter word counts (for overall trend)
    chapter_lengths = [ch['words'] for ch in chapters]
    sparkline_w = min(sparkline_width, len(chapters) * 2)
    sparkline = create_sparkline(chapter_lengths, width=sparkline_w)
    
    table_title = f"Chapter Breakdown   Trend: {sparkline}"
    if max_chapters and len(chapters) > max_chapters:
        table_title += f"   (Showing {max_chapters} of {len(chapters)})"
    
    table = Table(
        title=table_title,
        box=box.ROUNDED,
        border_style="magenta",
        header_style="bold magenta",
        title_style="bold magenta"
    )
    
    table.add_column("#", style="dim", width=5, justify="right")
    table.add_column("Chapter Title", style="bold cyan", width=40)
    table.add_column("Words", style="bold yellow", justify="right", width=10)
    table.add_column("% of Total", style="green", justify="right", width=10)
    table.add_column("Bar", style="bright_blue", width=15)
    table.add_column("Scenes", style="dim", justify="right", width=8)
    
    total_words = sum(ch['words'] for ch in chapters)
    max_words = max(chapter_lengths) if chapter_lengths else 1
    
    for i, chapter in enumerate(display_chapters, 1):
        percentage = (chapter['words'] / total_words * 100) if total_words > 0 else 0
        
        # Truncate long titles
        title = chapter['title']
        if len(title) > 37:
            title = title[:34] + "..."
        
        # Create mini bar for visual representation
        bar_length = int((chapter['words'] / max_words) * 12)
        bar = "█" * bar_length
        
        table.add_row(
            str(i),
            title,
            f"{chapter['words']:,}",
            f"{percentage:.1f}%",
            bar,
            str(chapter.get('scenes', 0))
        )
    
    return table


def create_word_frequency_table(common_words: List[tuple], max_words: Optional[int] = None) -> Table:
    """
    Create most common words table.
    
    Args:
        common_words: List of (word, count) tuples
        max_words: Maximum number of words to display (default: all words up to 15, or len(common_words))
    """
    # Determine how many words to show
    if max_words is None:
        display_count = min(15, len(common_words))
    else:
        display_count = min(max_words, len(common_words))
    
    table = Table(
        title=f"Most Frequent Words (Top {display_count})",
        box=box.ROUNDED,
        border_style="yellow",
        header_style="bold yellow",
        title_style="bold yellow"
    )
    
    table.add_column("Rank", style="dim", width=6, justify="right")
    table.add_column("Word", style="bold cyan", width=20)
    table.add_column("Count", style="bold green", justify="right", width=10)
    table.add_column("Bar", style="bright_blue", width=30)
    
    max_count = common_words[0][1] if common_words else 1
    
    for i, (word, count) in enumerate(common_words[:display_count], 1):
        bar_length = int((count / max_count) * 25)
        bar = "█" * bar_length
        
        table.add_row(
            str(i),
            word,
            f"{count:,}",
            bar
        )
    
    return table


def create_top_chapters_table(chapters: List[Dict], n: int = 5) -> Table:
    """Create a table showing top N chapters by word count."""
    # Sort chapters by word count
    sorted_chapters = sorted(chapters, key=lambda x: x['words'], reverse=True)[:n]
    
    table = Table(
        title=f"Top {n} Longest Chapters",
        box=box.ROUNDED,
        border_style="magenta",
        header_style="bold magenta",
        title_style="bold magenta"
    )
    
    table.add_column("Rank", style="dim", width=6, justify="right")
    table.add_column("Chapter Title", style="bold cyan", width=40)
    table.add_column("Words", style="bold yellow", justify="right", width=12)
    table.add_column("Bar", style="bright_blue", width=25)
    
    max_words = sorted_chapters[0]['words'] if sorted_chapters else 1
    
    for i, chapter in enumerate(sorted_chapters, 1):
        bar_length = int((chapter['words'] / max_words) * 20)
        bar = "█" * bar_length
        
        # Truncate long titles
        title = chapter['title']
        if len(title) > 37:
            title = title[:34] + "..."
        
        table.add_row(
            str(i),
            title,
            f"{chapter['words']:,}",
            bar
        )
    
    return table


def create_semi_compact_overview(stats: Dict) -> Table:
    """Create semi-compact overview with key metrics."""
    table = Table(
        title="Manuscript Overview",
        box=box.ROUNDED,
        border_style="cyan",
        header_style="bold cyan",
        title_style="bold cyan",
        show_header=False
    )
    
    table.add_column("Metric", style="bold yellow", width=25)
    table.add_column("Value", style="bold green", justify="right", width=30)
    
    total_words = stats['total_words']
    rt = stats['reading_time']
    
    # File info
    table.add_row("File", Path(stats['file_path']).name)
    table.add_row("", "")
    
    # Key stats
    table.add_row("Words", f"{total_words:,}", style="bold bright_green")
    table.add_row("Chapters", f"{len(stats['chapters'])}")
    table.add_row("Paragraphs", f"{stats['total_paragraphs']:,}")
    table.add_row("", "")
    
    # Reading & pages
    table.add_row("Reading Time", rt['range_str'])
    table.add_row("Pages", rt['pages_str'])
    table.add_row("", "")
    
    # Averages
    table.add_row("Avg Sentence", f"{stats['avg_words_per_sentence']:.1f} words")
    if len(stats['chapters']) > 0:
        avg_chapter_words = total_words / len(stats['chapters'])
        table.add_row("Avg Chapter", f"{avg_chapter_words:,.0f} words")
    
    # Chapter stats if available
    if stats.get('chapter_stats'):
        cs = stats['chapter_stats']
        table.add_row("", "")
        table.add_row("Chapter Range", f"{cs['min']:,} - {cs['max']:,} words")
        table.add_row("Std Deviation", f"± {cs['std_dev']:,.0f} words")
    
    return table


def create_verification_table(issues, issue_type, limit: int = 20) -> Optional[Table]:
    """Create table showing verification issues of a specific type."""
    from ..features.verification import IssueType
    
    # Filter issues by type
    filtered_issues = [i for i in issues if i.type == issue_type]
    
    if not filtered_issues:
        return None
    
    # Determine table style based on issue type
    if issue_type == IssueType.ERROR:
        border_color = "red"
        title_prefix = "🔴 Errors"
    elif issue_type == IssueType.WARNING:
        border_color = "yellow"
        title_prefix = "⚠️  Warnings"
    else:
        border_color = "cyan"
        title_prefix = "ℹ️  Info"
    
    table = Table(
        title=f"{title_prefix} ({len(filtered_issues)} found)",
        box=box.ROUNDED,
        border_style=border_color,
        header_style=f"bold {border_color}",
        title_style=f"bold {border_color}"
    )
    
    table.add_column("Line", style="dim", width=6, justify="right")
    table.add_column("Category", style="bold cyan", width=18)
    table.add_column("Issue", style="white", width=35)
    table.add_column("Preview", style="dim", width=35)
    
    for issue in filtered_issues[:limit]:
        line_str = str(issue.line_number) if issue.line_number else "-"
        preview = issue.line_preview if issue.line_preview else ""
        if len(preview) > 32:
            preview = preview[:29] + "..."
        
        table.add_row(
            line_str,
            issue.category,
            issue.message,
            preview
        )
    
    if len(filtered_issues) > limit:
        table.caption = f"Showing first {limit} of {len(filtered_issues)} issues"
    
    return table


"""
Panel creation functions for Rich UI display.
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, Optional, List
from rich.panel import Panel
from rich.text import Text
from rich import box

from ..utils.achievements import get_random_quote
from .visualizations import (
    create_sparkline,
    create_trend_arrow,
    create_horizontal_bar,
    create_heat_map_line,
    create_multi_line_heat_map
)


def create_header() -> Panel:
    """Create a beautiful header panel."""
    title = Text()
    title.append("📊 MuseStat ", style="bold magenta")
    title.append("- Manuscript Analytics", style="bold cyan")
    
    subtitle = Text("\nComprehensive Statistics Dashboard", style="italic dim")
    
    header = Text()
    header.append(title)
    header.append(subtitle)
    
    return Panel(
        header,
        box=box.DOUBLE_EDGE,
        border_style="bright_magenta",
        padding=(1, 2)
    )


def create_comparison_panel(stats: Dict, old_stats: Dict) -> Panel:
    """Create comparison panel showing changes since last analysis with trend arrows."""
    content = Text()
    content.append("Changes Since Last Analysis\n\n", style="bold underline cyan")
    
    word_diff = stats['total_words'] - old_stats.get('total_words', 0)
    char_diff = stats['total_characters'] - old_stats.get('total_characters', 0)
    sent_diff = stats['total_sentences'] - old_stats.get('total_sentences', 0)
    para_diff = stats['total_paragraphs'] - old_stats.get('total_paragraphs', 0)
    chap_diff = len(stats['chapters']) - old_stats.get('chapters', 0)
    
    # Get trend arrows for each metric
    metrics = [
        (stats['total_words'], old_stats.get('total_words', 0), "Words", word_diff, True),
        (stats['total_characters'], old_stats.get('total_characters', 0), "Characters", char_diff, True),
        (stats['total_sentences'], old_stats.get('total_sentences', 0), "Sentences", sent_diff, True),
        (stats['total_paragraphs'], old_stats.get('total_paragraphs', 0), "Paragraphs", para_diff, True),
        (len(stats['chapters']), old_stats.get('chapters', 0), "Chapters", chap_diff, True)
    ]
    
    for current, previous, label, diff, higher_is_better in metrics:
        arrow, arrow_color = create_trend_arrow(current, previous, higher_is_better)
        
        if diff > 0:
            content.append(f"{arrow} ", style=arrow_color)
            content.append(f"{label}: +{diff:,}\n", style="bold green")
        elif diff < 0:
            content.append(f"{arrow} ", style=arrow_color)
            content.append(f"{label}: {diff:,}\n", style="bold red")
        else:
            content.append(f"{arrow} ", style=arrow_color)
            content.append(f"{label}: No change\n", style="dim")
    
    # Time since last analysis
    if 'timestamp' in old_stats:
        old_time = datetime.fromisoformat(old_stats['timestamp'])
        time_diff = datetime.now() - old_time
        days = time_diff.days
        hours = time_diff.seconds // 3600
        content.append(f"\nLast analyzed: ", style="dim")
        if days > 0:
            content.append(f"{days} day{'s' if days != 1 else ''} ago", style="cyan")
        else:
            content.append(f"{hours} hour{'s' if hours != 1 else ''} ago", style="cyan")
    
    return Panel(
        content,
        box=box.ROUNDED,
        border_style="bright_green" if word_diff >= 0 else "bright_yellow",
        padding=(1, 2),
        title="[bold]Comparison[/bold]",
        title_align="left"
    )


def create_chapter_stats_panel(chapter_stats: Dict, chapter_lengths: Optional[List[int]] = None, sparkline_width: int = 40) -> Optional[Panel]:
    """
    Create panel showing chapter length statistics with visual enhancements.
    
    Args:
        chapter_stats: Chapter statistics dictionary
        chapter_lengths: Optional list of chapter word counts for sparkline
        sparkline_width: Width of the sparkline chart (default: 40)
    """
    if not chapter_stats:
        return None
    
    content = Text()
    content.append("Chapter Length Analysis\n\n", style="bold underline cyan")
    
    # Add sparkline if chapter lengths provided
    if chapter_lengths and len(chapter_lengths) > 0:
        width = min(sparkline_width, len(chapter_lengths) * 2)
        sparkline = create_sparkline(chapter_lengths, width=width)
        content.append("Trend:     ", style="bold white")
        content.append(f"{sparkline}\n\n", style="bright_cyan")
    
    content.append(f"Mean:      {chapter_stats['mean']:,.0f} words\n", style="white")
    content.append(f"Std Dev:   {chapter_stats['std_dev']:,.0f} words\n", style="white")
    
    # Add balance indicator based on coefficient of variation
    cv = chapter_stats['coefficient_of_variation']
    if cv < 15:
        balance_text = "Very Consistent"
        balance_color = "bright_green"
        balance_symbol = "●"
    elif cv < 30:
        balance_text = "Moderately Consistent"
        balance_color = "yellow"
        balance_symbol = "●"
    else:
        balance_text = "Variable"
        balance_color = "red"
        balance_symbol = "●"
    
    content.append(f"CV:        {cv:.1f}% ", style="white")
    content.append(f"{balance_symbol} ", style=balance_color)
    content.append(f"{balance_text}\n\n", style=balance_color)
    
    content.append("Shortest:  ", style="bold yellow")
    content.append(f"{chapter_stats['min']:,} words\n", style="yellow")
    content.append(f"           {chapter_stats['shortest_chapter']}\n\n", style="dim yellow")
    
    content.append("Longest:   ", style="bold green")
    content.append(f"{chapter_stats['max']:,} words\n", style="green")
    content.append(f"           {chapter_stats['longest_chapter']}\n\n", style="dim green")
    
    content.append(f"Range:     {chapter_stats['range']:,} words", style="cyan")
    
    return Panel(
        content,
        box=box.ROUNDED,
        border_style="magenta",
        padding=(1, 2),
        title="[bold]Chapter Statistics[/bold]",
        title_align="left"
    )


def create_achievement_badge_panel(badge: Dict) -> Panel:
    """Create achievement badge panel."""
    content = Text()
    
    if badge.get('newly_unlocked'):
        # Just unlocked!
        content.append("🎉 ACHIEVEMENT UNLOCKED! 🎉\n\n", style="bold bright_yellow")
        content.append(f"{badge['icon']} {badge['title']}\n", style="bold bright_green")
        content.append(f"{badge['message']}\n", style="italic cyan")
    elif badge['unlocked']:
        # Already achieved
        content.append("Current Status\n\n", style="bold underline cyan")
        content.append(f"{badge['icon']} {badge['title']}\n", style="bold bright_green")
        content.append(f"{badge['message']}", style="italic dim")
    else:
        # Not yet achieved
        content.append("Next Milestone\n\n", style="bold underline cyan")
        content.append(f"{badge['icon']} {badge['title']}\n", style="bold yellow")
        content.append(f"{badge['message']}", style="italic dim")
    
    border_color = "bright_yellow" if badge.get('newly_unlocked') else ("bright_green" if badge['unlocked'] else "yellow")
    
    return Panel(
        content,
        box=box.DOUBLE if badge.get('newly_unlocked') else box.ROUNDED,
        border_style=border_color,
        padding=(1, 2),
        title="[bold]Achievement[/bold]" if badge['unlocked'] else "[bold]Next Goal[/bold]",
        title_align="left"
    )


def create_motivation_panel() -> Panel:
    """Create motivational quote panel."""
    quote = get_random_quote()
    
    content = Text()
    content.append(quote, style="italic white")
    
    return Panel(
        content,
        box=box.ROUNDED,
        border_style="dim",
        padding=(1, 2),
        title="[dim]Writer's Wisdom[/dim]",
        title_align="center"
    )


def create_milestone_panel(stats: Dict) -> Panel:
    """Create writing milestones panel."""
    total_words = stats['total_words']
    
    milestones = [
        (50000, "Novel (Short)", "📗"),
        (80000, "Novel (Standard)", "📘"),
        (100000, "Novel (Long)", "📙"),
        (120000, "Epic Novel", "📚"),
    ]
    
    content = Text()
    content.append("Writing Milestones Progress\n\n", style="bold underline cyan")
    
    for milestone, label, icon in milestones:
        percentage = min((total_words / milestone) * 100, 100)
        bar_length = int(percentage / 5)
        bar = "█" * bar_length + "░" * (20 - bar_length)
        
        status = "✓" if total_words >= milestone else "○"
        style = "bold green" if total_words >= milestone else "dim"
        
        content.append(f"{status} {icon} {label} ({milestone:,} words)\n", style=style)
        content.append(f"   {bar} {percentage:.1f}%\n", style=style)
        content.append(f"   {total_words:,} / {milestone:,}\n\n", style=style)
    
    return Panel(
        content,
        box=box.ROUNDED,
        border_style="bright_green",
        padding=(1, 2)
    )


def create_compact_display(stats: Dict) -> Panel:
    """Create a compact summary panel with essential statistics."""
    total_words = stats['total_words']
    rt = stats['reading_time']
    
    content = Text()
    
    # Title
    content.append("MuseStat Quick Summary\n\n", style="bold cyan")
    
    # Essential stats
    content.append("Words:       ", style="bold")
    content.append(f"{total_words:,}\n", style="bold bright_yellow")
    
    content.append("Characters:  ", style="bold")
    content.append(f"{stats['total_characters']:,}\n", style="cyan")
    
    content.append("Chapters:    ", style="bold")
    content.append(f"{len(stats['chapters'])}\n", style="cyan")
    
    content.append("Paragraphs:  ", style="bold")
    content.append(f"{stats['total_paragraphs']:,}\n", style="cyan")
    
    content.append("Read Time:   ", style="bold")
    content.append(f"{rt['range_str']}\n", style="cyan")
    
    content.append("Pages:       ", style="bold")
    content.append(f"{rt['pages_str']}\n", style="cyan")
    
    if stats.get('dialogue'):
        content.append("Dialogue:    ", style="bold")
        content.append(f"{stats['dialogue']['ratio']:.1f}%\n", style="cyan")
    
    content.append("\n")
    
    # Milestone indicator
    milestones = [(50000, "Novel (Short)", "📗"), (80000, "Novel (Standard)", "📘"), 
                  (100000, "Novel (Long)", "📙"), (120000, "Epic Novel", "📚")]
    
    content.append("Progress:    ", style="bold")
    achieved = [m for m in milestones if total_words >= m[0]]
    if achieved:
        last = achieved[-1]
        content.append(f"{last[2]} {last[1]} ", style="bold bright_green")
        if len(achieved) < len(milestones):
            next_milestone = milestones[len(achieved)]
            remaining = next_milestone[0] - total_words
            content.append(f"({remaining:,} to {next_milestone[1]})", style="dim")
    else:
        remaining = 50000 - total_words
        content.append(f"{remaining:,} words to Novel (Short)", style="yellow")
    
    # Add badge if available
    if stats.get('badge'):
        badge = stats['badge']
        content.append("\n\n")
        content.append(f"{badge['icon']} ", style="bold")
        content.append(f"{badge['title']}", style="bold bright_green" if badge['unlocked'] else "bold yellow")
        if badge.get('newly_unlocked'):
            content.append(" 🎉", style="bold bright_yellow")
    
    return Panel(
        content,
        box=box.ROUNDED,
        border_style="bright_cyan",
        padding=(1, 2),
        title="[bold]Quick Stats[/bold]",
        title_align="left"
    )


def create_verification_checks_info() -> Panel:
    """Create panel showing what verification checks are performed."""
    content = Text()
    content.append("12 Comprehensive Check Categories:\n\n", style="bold underline cyan")
    
    checks = [
        ("1", "Markdown Formatting", "Unmatched *, **, _"),
        ("2", "Pre-publish Markers", "TODO, FIXME, HACK, etc."),
        ("3", "Repeated Words", "the the, and and, etc."),
        ("4", "Punctuation", "Spacing, multiples, ellipsis"),
        ("5", "Whitespace", "Trailing, tabs, spacing"),
        ("6", "Heading Structure", "Hierarchy and formatting"),
        ("7", "Smart Quotes", "Consistency checking"),
        ("8", "Markdown Links", "Bracket matching"),
        ("9", "Paragraph Spacing", "Consecutive blanks"),
        ("10", "Line Length", "Very long lines"),
        ("11", "Dialogue Quotes", "Quote consistency"),
        ("12", "Incomplete Content", "Placeholders, Lorem Ipsum"),
    ]
    
    for num, cat, desc in checks:
        content.append(f"{num}. ", style="bold bright_white")
        content.append(f"{cat}: ", style="bold cyan")
        content.append(f"{desc}\n", style="dim")
    
    return Panel(
        content,
        box=box.ROUNDED,
        border_style="cyan",
        padding=(1, 2),
        title="[bold]Verification Checks[/bold]",
        title_align="left"
    )


def create_verification_summary(issues) -> Panel:
    """Create verification summary panel."""
    from ..features.verification import IssueType
    
    errors = sum(1 for i in issues if i.type == IssueType.ERROR)
    warnings = sum(1 for i in issues if i.type == IssueType.WARNING)
    info = sum(1 for i in issues if i.type == IssueType.INFO)
    
    content = Text()
    content.append("Verification Summary\n\n", style="bold underline white")
    
    # Errors
    error_style = "bold red" if errors > 0 else "dim"
    content.append(f"{'🔴' if errors > 0 else '✓'} Errors:   {errors:>4}\n", style=error_style)
    
    # Warnings
    warning_style = "bold yellow" if warnings > 0 else "dim"
    content.append(f"{'⚠️ ' if warnings > 0 else '✓'} Warnings: {warnings:>4}\n", style=warning_style)
    
    # Info
    info_style = "bold cyan" if info > 0 else "dim"
    content.append(f"{'ℹ️ ' if info > 0 else '✓'} Info:     {info:>4}\n\n", style=info_style)
    
    # Category breakdown
    if issues:
        categories = {}
        for issue in issues:
            categories[issue.category] = categories.get(issue.category, 0) + 1
        
        content.append("Top Issues:\n", style="bold dim")
        sorted_cats = sorted(categories.items(), key=lambda x: x[1], reverse=True)[:5]
        for cat, count in sorted_cats:
            content.append(f"  • {cat}: {count}\n", style="dim")
        content.append("\n")
    
    # Overall status
    if errors == 0 and warnings == 0 and info == 0:
        content.append("✨ Manuscript is ready for publishing! ✨", style="bold bright_green")
    elif errors == 0 and warnings == 0:
        content.append("✓ No critical issues - minor suggestions only", style="bold green")
    elif errors == 0:
        content.append("⚠️  Some warnings found - review recommended", style="bold yellow")
    else:
        content.append("🔴 Critical issues require attention", style="bold red")
    
    return Panel(
        content,
        box=box.ROUNDED,
        border_style="bright_yellow" if errors > 0 else "bright_green",
        padding=(1, 2),
        title="[bold]Summary[/bold]",
        title_align="left"
    )


def create_density_heat_map_panel(chapters: List[Dict]) -> Optional[Panel]:
    """
    Create a heat map panel showing sentence and paragraph density across chapters.
    
    Args:
        chapters: List of chapter dictionaries with 'words' and optionally 'sentences'
        
    Returns:
        Panel with heat map visualization or None if insufficient data
    """
    if not chapters or len(chapters) < 2:
        return None
    
    content = Text()
    content.append("Chapter Density Analysis\n\n", style="bold underline cyan")
    
    # Extract data for heat map
    chapter_lengths = [ch.get('words', 0) for ch in chapters]
    
    # Create heat map for chapter word counts
    if chapter_lengths:
        heatmap = create_heat_map_line(chapter_lengths, width=50)
        content.append("Word Density:  ", style="bold white")
        content.append(f"{heatmap}\n", style="bright_cyan")
        
        # Add legend
        min_words = min(chapter_lengths)
        max_words = max(chapter_lengths)
        content.append(f"               [{min_words:,} words", style="dim")
        content.append(" " * 30, style="dim")
        content.append(f"{max_words:,} words]\n\n", style="dim")
    
    # If we have sentence data, show that too
    if chapters and 'sentences' in chapters[0]:
        sentence_counts = [ch.get('sentences', 0) for ch in chapters]
        if any(sentence_counts):
            heatmap = create_heat_map_line(sentence_counts, width=50)
            content.append("Sentence Count:", style="bold white")
            content.append(f"{heatmap}\n", style="bright_yellow")
            
            min_sent = min(sentence_counts) if sentence_counts else 0
            max_sent = max(sentence_counts) if sentence_counts else 0
            content.append(f"               [{min_sent:,} sentences", style="dim")
            content.append(" " * 25, style="dim")
            content.append(f"{max_sent:,} sentences]\n\n", style="dim")
    
    # Add interpretation
    content.append("\nInterpretation:\n", style="bold dim")
    content.append("  █ = High density  |  ░ = Low density", style="dim")
    
    return Panel(
        content,
        box=box.ROUNDED,
        border_style="cyan",
        padding=(1, 2),
        title="[bold]Density Heat Map[/bold]",
        title_align="left"
    )


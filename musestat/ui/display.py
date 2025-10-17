"""
Main display logic for manuscript statistics.
"""

import time
from pathlib import Path
from typing import Dict, Optional, List
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text
from rich import box

from .panels import (
    create_header,
    create_compact_display,
    create_motivation_panel,
    create_comparison_panel,
    create_achievement_badge_panel,
    create_milestone_panel,
    create_chapter_stats_panel,
    create_density_heat_map_panel
)
from .tables import (
    create_semi_compact_overview,
    create_overview_table,
    create_readability_table,
    create_pacing_table,
    create_chapters_table,
    create_word_frequency_table
)
from ..utils.achievements import get_achievement_badge

console = Console()


def display_statistics(
    stats: Dict,
    compact: bool = False,
    semi_compact: bool = False,
    comparison_stats: Optional[Dict] = None,
    show_advanced: bool = False,
    display_options: Optional[Dict] = None
):
    """
    Display all statistics in a beautiful layout.
    
    Args:
        stats: Statistics dictionary from analyzer
        compact: Use compact display mode
        semi_compact: Use semi-compact display mode
        comparison_stats: Optional previous stats for comparison
        show_advanced: Show advanced metrics (readability, pacing)
        display_options: Optional dictionary with display customization:
            - top_words: Number of frequent words to show
            - max_chapters: Maximum chapters to display
            - sparkline_width: Width of sparkline charts
            - hide_word_frequency: Hide word frequency table
            - hide_heat_map: Hide density heat map
            - hide_chapter_details: Hide chapter breakdown table
            - show_top_chapters: Show top N longest chapters
    """
    if display_options is None:
        display_options = {}
    
    top_words = display_options.get('top_words', 15)
    max_chapters = display_options.get('max_chapters')
    sparkline_width = display_options.get('sparkline_width', 40)
    hide_word_frequency = display_options.get('hide_word_frequency', False)
    hide_heat_map = display_options.get('hide_heat_map', False)
    hide_chapter_details = display_options.get('hide_chapter_details', False)
    show_top_chapters = display_options.get('show_top_chapters')
    console.clear()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True
    ) as progress:
        task = progress.add_task("[cyan]Analyzing manuscript...", total=100)
        steps = 20 if (compact or semi_compact) else 100
        sleep_time = 0.005 if (compact or semi_compact) else 0.01
        for i in range(steps):
            progress.update(task, advance=100//steps)
            time.sleep(sleep_time)
    
    if semi_compact:
        console.print(create_header())
        console.print()
        
        if comparison_stats:
            console.print(Columns([
                create_semi_compact_overview(stats),
                create_comparison_panel(stats, comparison_stats)
            ], equal=True, expand=True))
            
            prev_words = comparison_stats.get('total_words', 0)
            badge = get_achievement_badge(stats['total_words'], prev_words)
            if badge.get('newly_unlocked'):
                console.print()
                console.print(create_achievement_badge_panel(badge))
        else:
            console.print(Columns([
                create_semi_compact_overview(stats),
                create_milestone_panel(stats)
            ], equal=True, expand=True))
        
        console.print()
        
        if stats.get('badge'):
            console.print(Columns([
                create_achievement_badge_panel(stats['badge']),
                create_motivation_panel()
            ], equal=True, expand=True))
            console.print()
        
        # Footer
        footer = Text()
        footer.append("✨ Analysis Complete! ", style="bold bright_green")
        footer.append(f"Total: {stats['total_words']:,} words", style="bold bright_yellow")
        footer.append(" • Use -c for quick or no flag for full details", style="dim")
        footer.append(" ✨", style="bold bright_green")
        
        console.print(Panel(
            footer,
            box=box.DOUBLE_EDGE,
            border_style="bright_green",
            padding=(0, 2)
        ))
    
    elif compact:
        console.print(create_compact_display(stats))
        console.print()
        
        if comparison_stats:
            prev_words = comparison_stats.get('total_words', 0)
            badge = get_achievement_badge(stats['total_words'], prev_words)
            
            if badge.get('newly_unlocked'):
                console.print(create_achievement_badge_panel(badge))
                console.print()
            
            console.print(create_comparison_panel(stats, comparison_stats))
            console.print()
        
        console.print(create_motivation_panel())
        console.print()
        
        # Footer
        footer = Text()
        footer.append("✨ ", style="bold bright_green")
        footer.append(f"{stats['total_words']:,} words", style="bold bright_yellow")
        footer.append(" • Run without --compact for detailed stats", style="dim")
        footer.append(" ✨", style="bold bright_green")
        
        console.print(Panel(
            footer,
            box=box.ROUNDED,
            border_style="bright_green",
            padding=(0, 1)
        ))
    else:
        console.print(create_header())
        console.print()
        
        if comparison_stats:
            console.print(Columns([
                create_overview_table(stats),
                create_comparison_panel(stats, comparison_stats)
            ], equal=True, expand=True))
        else:
            console.print(Columns([
                create_overview_table(stats),
                create_milestone_panel(stats)
            ], equal=True, expand=True))
        
        console.print()
        
        if show_advanced:
            if stats.get('readability'):
                table = create_readability_table(stats['readability'])
                if table:
                    console.print(table)
                    console.print()
            
            if stats.get('pacing'):
                table = create_pacing_table(stats['pacing'])
                if table:
                    console.print(table)
                    console.print()
        
        if stats.get('chapter_stats') and stats['chapter_stats']:
            chapter_lengths = [ch['words'] for ch in stats['chapters']] if stats.get('chapters') else None
            panel = create_chapter_stats_panel(stats['chapter_stats'], chapter_lengths, sparkline_width=sparkline_width)
            if panel:
                console.print(panel)
                console.print()
        
        if not hide_heat_map and stats.get('chapters') and len(stats['chapters']) > 1:
            heat_map_panel = create_density_heat_map_panel(stats['chapters'])
            if heat_map_panel:
                console.print(heat_map_panel)
                console.print()
        
        if show_top_chapters and stats['chapters']:
            from .tables import create_top_chapters_table
            console.print(create_top_chapters_table(stats['chapters'], n=show_top_chapters))
            console.print()
        
        if not hide_chapter_details and stats['chapters']:
            console.print(create_chapters_table(stats['chapters'], max_chapters=max_chapters, sparkline_width=sparkline_width))
            console.print()
        
        if not hide_word_frequency:
            console.print(create_word_frequency_table(stats['common_words'], max_words=top_words))
            console.print()
        
        if stats.get('badge'):
            badge = stats['badge']
            if comparison_stats:
                prev_words = comparison_stats.get('total_words', 0)
                badge = get_achievement_badge(stats['total_words'], prev_words)
                stats['badge'] = badge
            
            console.print(Columns([
                create_achievement_badge_panel(badge),
                create_motivation_panel()
            ], equal=True, expand=True))
            console.print()
        
        # Footer
        footer = Text()
        footer.append("✨ Analysis Complete! ", style="bold bright_green")
        footer.append(f"Total: {stats['total_words']:,} words", style="bold bright_yellow")
        footer.append(" ✨", style="bold bright_green")
        
        console.print(Panel(
            footer,
            box=box.DOUBLE_EDGE,
            border_style="bright_green",
            padding=(0, 2)
        ))


def print_minimalist(stats: Dict):
    """Print minimalist output for editor integration."""
    rt = stats['reading_time']
    output = f"""Words: {stats['total_words']:,}
Characters: {stats['total_characters']:,}
Sentences: {stats['total_sentences']:,}
Paragraphs: {stats['total_paragraphs']:,}
Chapters: {len(stats['chapters'])}
Reading Time: {rt['range_str']}
Pages: {rt['pages_str']}
"""
    
    if stats.get('chapter_stats'):
        cs = stats['chapter_stats']
        output += f"""Chapter Avg: {cs['mean']:.0f} ± {cs['std_dev']:.0f} words
"""
    
    console.print(output.strip())


def list_manuscript_files(directory: str = ".") -> List[Path]:
    """
    List all potential manuscript files in a directory.
    
    Args:
        directory: Directory to search (default: current directory)
        
    Returns:
        List of Path objects for manuscript files, sorted by modification time
    """
    path = Path(directory)
    extensions = ['.md', '.txt', '.docx', '.rtf', '.markdown']
    files = []
    
    for ext in extensions:
        files.extend(path.glob(f'*{ext}'))
    
    return sorted(files, key=lambda x: x.stat().st_mtime, reverse=True)


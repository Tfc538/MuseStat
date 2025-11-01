"""
Command-line interface for MuseStat.
"""

import sys
import argparse
import os
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box

try:
    import questionary
    from questionary import Style
    QUESTIONARY_AVAILABLE = True
except ImportError:
    QUESTIONARY_AVAILABLE = False

from ..config import __version__
from ..core.analyzer import analyze_manuscript
from ..io.readers import read_manuscript, get_supported_formats_info
from ..io.exporters import export_to_json, export_to_csv, export_to_html
from ..io.badges import generate_badges
from ..utils.stats import save_stats_snapshot, load_comparison_stats
from ..utils.version_check import check_for_updates, get_update_message
from ..features.verification import (
    verify_manuscript,
    load_ignore_patterns,
    IssueType
)
from ..ui.display import display_statistics, print_minimalist, list_manuscript_files
from ..ui.panels import (
    create_header,
    create_compact_display,
    create_comparison_panel,
    create_motivation_panel,
    create_achievement_badge_panel,
    create_milestone_panel,
    create_verification_checks_info,
    create_verification_summary
)
from ..ui.tables import (
    create_chapters_table,
    create_overview_table,
    create_readability_table,
    create_pacing_table,
    create_word_frequency_table,
    create_semi_compact_overview,
    create_verification_table
)

console = Console()


def interactive_mode():
    """
    Interactive TUI mode for when executable is run without arguments.
    Provides a user-friendly interface for first-time users.
    """
    console.clear()
    
    # Welcome screen
    navigation_hint = "Use ↑↓ arrow keys to navigate, Enter to select" if QUESTIONARY_AVAILABLE else "Type numbers to select options"
    
    welcome = Panel(
        Text.from_markup(
            "[bold magenta]📊 Welcome to MuseStat![/bold magenta]\n\n"
            "[cyan]Manuscript Statistics Analyzer for Fiction Writers[/cyan]\n\n"
            "This tool provides comprehensive analysis of your manuscript including:\n"
            "• Word counts and chapter breakdowns\n"
            "• Reading time estimates\n"
            "• Readability metrics\n"
            "• Dialogue and pacing analysis\n"
            "• Manuscript verification\n\n"
            f"[dim]{navigation_hint}[/dim]\n"
            "[dim]Press Ctrl+C at any time to exit[/dim]"
        ),
        box=box.DOUBLE_EDGE,
        border_style="bright_magenta",
        padding=(1, 2)
    )
    console.print(welcome)
    console.print()
    
    # List available files
    files = list_manuscript_files()
    
    if not files:
        console.print("[yellow]No manuscript files found in current directory.[/yellow]")
        console.print("\n[dim]Supported formats: .md, .txt, .docx, .rtf[/dim]")
        console.print("\n[bold]Please:[/bold]")
        console.print("1. Place your manuscript file in this directory, or")
        console.print("2. Run with: [cyan]musestat -f /path/to/your/manuscript.md[/cyan]")
        console.print("\nFor more options, run: [cyan]musestat --help[/cyan]")
        input("\nPress Enter to exit...")
        return None, {}
    
    # Show available files
    table = Table(title="📚 Available Manuscript Files", box=box.ROUNDED, border_style="cyan")
    table.add_column("#", style="bold yellow", width=4, justify="right")
    table.add_column("File Name", style="bold cyan")
    table.add_column("Type", style="yellow", width=8)
    table.add_column("Size", style="green", justify="right", width=12)
    
    for i, file in enumerate(files, 1):
        size_kb = file.stat().st_size / 1024
        size_str = f"{size_kb:.1f} KB" if size_kb < 1024 else f"{size_kb/1024:.1f} MB"
        table.add_row(
            str(i),
            file.name,
            file.suffix.upper().replace('.', ''),
            size_str
        )
    
    console.print(table)
    console.print()
    
    # Prompt for file selection
    if QUESTIONARY_AVAILABLE:
        # Use arrow keys for navigation
        custom_style = Style([
            ('qmark', 'fg:#673ab7 bold'),
            ('question', 'bold'),
            ('answer', 'fg:#00ff00 bold'),
            ('pointer', 'fg:#673ab7 bold'),
            ('highlighted', 'fg:#673ab7 bold'),
            ('selected', 'fg:#00ff00'),
        ])
        
        file_choices = [
            {
                'name': f"{i}. {file.name} ({file.suffix.upper().replace('.', '')}, "
                        f"{file.stat().st_size/1024:.1f} KB)" 
                        if file.stat().st_size < 1024*1024 
                        else f"{i}. {file.name} ({file.suffix.upper().replace('.', '')}, "
                             f"{file.stat().st_size/1024/1024:.1f} MB)",
                'value': str(file)
            }
            for i, file in enumerate(files, 1)
        ]
        
        try:
            selected_file = questionary.select(
                "Select a manuscript file (use arrow keys):",
                choices=file_choices,
                style=custom_style,
                use_indicator=True,
                use_shortcuts=True
            ).ask()
            
            if not selected_file:
                console.print("\n[yellow]Cancelled.[/yellow]")
                return None, {}
        except KeyboardInterrupt:
            console.print("\n[yellow]Cancelled.[/yellow]")
            return None, {}
    else:
        # Fallback to number input
        while True:
            try:
                choice = console.input("[bold cyan]Select a file number (or press Enter for #1):[/bold cyan] ").strip()
                
                if choice == "":
                    choice = "1"
                
                file_index = int(choice) - 1
                
                if 0 <= file_index < len(files):
                    selected_file = str(files[file_index])
                    break
                else:
                    console.print(f"[red]Please enter a number between 1 and {len(files)}[/red]")
            except ValueError:
                console.print("[red]Please enter a valid number[/red]")
            except KeyboardInterrupt:
                console.print("\n[yellow]Cancelled.[/yellow]")
                return None, {}
    
    console.print(f"\n[green]✓ Selected:[/green] [bold]{Path(selected_file).name}[/bold]")
    console.print()
    
    # Analysis options menu
    if QUESTIONARY_AVAILABLE:
        # Use arrow keys for navigation
        analysis_choices = [
            questionary.Choice("Quick Summary (compact view)", value="1"),
            questionary.Choice("Standard Analysis (recommended)", value="2"),
            questionary.Choice("Full Analysis (with chapters and word frequency)", value="3"),
            questionary.Choice("Advanced Analysis (readability, dialogue, pacing)", value="4"),
            questionary.Choice("Verify Manuscript (check for publishing)", value="5"),
        ]
        
        try:
            analysis_choice = questionary.select(
                "Choose analysis type (use arrow keys):",
                choices=analysis_choices,
                default="2",
                style=custom_style,
                use_indicator=True
            ).ask()
            
            if not analysis_choice:
                console.print("\n[yellow]Cancelled.[/yellow]")
                return None, {}
        except KeyboardInterrupt:
            console.print("\n[yellow]Cancelled.[/yellow]")
            return None, {}
    else:
        # Fallback to number input
        options_panel = Panel(
            "[bold]Analysis Options:[/bold]\n\n"
            "[cyan]1.[/cyan] Quick Summary (compact view)\n"
            "[cyan]2.[/cyan] Standard Analysis (recommended)\n"
            "[cyan]3.[/cyan] Full Analysis (with chapters and word frequency)\n"
            "[cyan]4.[/cyan] Advanced Analysis (readability, dialogue, pacing)\n"
            "[cyan]5.[/cyan] Verify Manuscript (check for issues before publishing)",
            title="📊 Choose Analysis Type",
            border_style="cyan",
            box=box.ROUNDED
        )
        console.print(options_panel)
        console.print()
        
        # Prompt for analysis type
        while True:
            try:
                analysis_choice = console.input("[bold cyan]Select analysis type (or press Enter for #2):[/bold cyan] ").strip()
                
                if analysis_choice == "":
                    analysis_choice = "2"
                
                if analysis_choice in ["1", "2", "3", "4", "5"]:
                    break
                else:
                    console.print("[red]Please enter a number between 1 and 5[/red]")
            except KeyboardInterrupt:
                console.print("\n[yellow]Cancelled.[/yellow]")
                return None, {}
    
    console.print()
    
    # Map choice to options
    options = {
        'compact': analysis_choice == "1",
        'semi_compact': analysis_choice == "2",
        'full': analysis_choice == "3",
        'advanced': analysis_choice == "4",
        'verify': analysis_choice == "5"
    }

    # Badge selection (interactive only)
    if QUESTIONARY_AVAILABLE:
        try:
            badge_choices = [
                questionary.Choice("Achievement (milestone)", value='achievement'),
                questionary.Choice("Word Count", value='wordcount'),
                questionary.Choice("Chapters", value='chapters'),
                questionary.Choice("Reading Pages", value='reading_time'),
            ]

            selected_badges = questionary.checkbox(
                "Select badges to generate (space to toggle, Enter to continue):",
                choices=badge_choices,
                style=custom_style
            ).ask()

            if selected_badges:
                options['badges'] = selected_badges

                format_choices = [
                    questionary.Choice("SVG", value='svg'),
                    questionary.Choice("PNG (requires cairosvg)", value='png')
                ]

                selected_formats = questionary.checkbox(
                    "Select output formats:",
                    choices=format_choices,
                    style=custom_style
                ).ask()

                options['badge_formats'] = selected_formats or ['svg']
        except Exception:
            # If any interactive badge selection fails, ignore and continue
            pass
    
    return selected_file, options


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description=f"MuseStat v{__version__} - Manuscript Statistics Analyzer with Advanced Features",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
               "  %(prog)s                                 # Full detailed analysis\n"
               "  %(prog)s -sc                             # Semi-compact view (RECOMMENDED)\n"
               "  %(prog)s --verify                        # Check for formatting issues\n"
               "  %(prog)s -f mybook.docx                  # Analyze specific file\n"
               "  %(prog)s --advanced                      # Enable all advanced features\n"
               "  %(prog)s --minimalist                    # Plain text output (editor integration)\n"
               "  %(prog)s --export html                   # Export to HTML report\n"
               "  %(prog)s --export json -o stats.json     # Export to custom file\n"
               "  %(prog)s --compare old.stats.json        # Compare with previous\n"
               "  %(prog)s --save-snapshot                 # Save stats for later comparison\n"
               "  %(prog)s --list                          # List available files\n"
               "\n"
               "Display Customization:\n"
               "  %(prog)s --top-words 25                  # Show 25 most frequent words\n"
               "  %(prog)s --max-chapters 10               # Display only first 10 chapters\n"
               "  %(prog)s --sparkline-width 60            # Wider sparkline charts\n"
               "  %(prog)s --hide-word-frequency           # Hide word frequency table\n"
               "  %(prog)s --show-top-chapters 5           # Show 5 longest chapters\n"
               "\n"
               "Display Modes: full, -sc (semi-compact), -c (compact), -m (minimalist), -v (verify)\n"
               "Supported formats: .md, .txt, .docx, .rtf\n"
               "Advanced features require: langdetect, textstat questionary\n"
               "Export formats: json, csv, html"
    )
    
    parser.add_argument(
        '--file', '-f',
        metavar='PATH',
        help='Path to manuscript file (default: manuscript.md)'
    )
    
    parser.add_argument(
        '--compact', '-c',
        action='store_true',
        help='Display compact summary (minimal info)'
    )
    
    parser.add_argument(
        '--semi-compact', '-sc',
        action='store_true',
        help='Display semi-compact view (balanced detail - recommended for daily use)'
    )
    
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='List all manuscript files in current directory'
    )
    
    parser.add_argument(
        '--formats',
        action='store_true',
        help='Show supported file formats and their availability'
    )
    
    parser.add_argument(
        '--no-animation',
        action='store_true',
        help='Skip loading animation for faster output'
    )
    
    parser.add_argument(
        '--chapters-only',
        action='store_true',
        help='Show only chapter breakdown (implied compact mode)'
    )
    
    parser.add_argument(
        '--advanced', '-a',
        action='store_true',
        help='Enable advanced features (language detection, readability, dialogue, pacing)'
    )
    
    parser.add_argument(
        '--compare',
        metavar='STATS_FILE',
        help='Compare with previous stats from JSON file'
    )
    
    parser.add_argument(
        '--save-snapshot', '-s',
        action='store_true',
        help='Save statistics snapshot for future comparison'
    )
    
    parser.add_argument(
        '--export',
        choices=['json', 'csv', 'html'],
        help='Export statistics to specified format (json, csv, or html)'
    )

    parser.add_argument(
        '--badges',
        metavar='BADGES',
        help='Comma-separated list of badges to generate (achievement,wordcount,chapters,reading_time)'
    )

    parser.add_argument(
        '--badge-formats',
        metavar='FORMATS',
        default='svg',
        help='Comma-separated badge output formats (svg,png). png requires cairosvg.'
    )

    parser.add_argument(
        '--badge-dir',
        metavar='DIR',
        help='Directory to save generated badges (default: ./musestat/badges)'
    )
    
    parser.add_argument(
        '--output', '-o',
        metavar='FILE',
        help='Save output/report to file instead of displaying to terminal'
    )
    
    parser.add_argument(
        '--minimalist', '-m',
        action='store_true',
        help='Minimalist output mode for editor integration (plain text, no colors)'
    )
    
    parser.add_argument(
        '--verify', '-v',
        action='store_true',
        help='Verify manuscript for publishing readiness (check formatting, typos, etc.)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s {__version__}'
    )
    
    # Display customization options
    display_group = parser.add_argument_group('Display Customization')
    
    display_group.add_argument(
        '--top-words',
        type=int,
        metavar='N',
        default=15,
        help='Number of most frequent words to display (default: 15)'
    )
    
    display_group.add_argument(
        '--max-chapters',
        type=int,
        metavar='N',
        help='Maximum number of chapters to display in detail (default: all)'
    )
    
    display_group.add_argument(
        '--min-word-length',
        type=int,
        metavar='N',
        default=1,
        help='Minimum word length for frequency analysis (default: 3)'
    )
    
    display_group.add_argument(
        '--sparkline-width',
        type=int,
        metavar='N',
        default=40,
        help='Width of sparkline charts in characters (default: 40)'
    )
    
    display_group.add_argument(
        '--hide-word-frequency',
        action='store_true',
        help='Hide the word frequency table'
    )
    
    display_group.add_argument(
        '--hide-heat-map',
        action='store_true',
        help='Hide the density heat map visualization'
    )
    
    display_group.add_argument(
        '--hide-chapter-details',
        action='store_true',
        help='Hide individual chapter breakdown table'
    )
    
    display_group.add_argument(
        '--show-top-chapters',
        type=int,
        metavar='N',
        help='Show top N longest chapters in a summary table'
    )
    
    args = parser.parse_args()
    
    # Check for updates (silent, non-blocking)
    update_info = check_for_updates(silent=True)
    if update_info:
        console.print()
        console.print(Panel(
            Text.from_markup(
                f"[bold bright_green]🎉 New version available: v{update_info['latest_version']}[/bold bright_green]\n"
                f"[dim]Current version: v{update_info['current_version']}[/dim]\n\n"
                f"[cyan]Download:[/cyan] {update_info['release_url']}\n"
                f"[dim]Run with --version to see current version[/dim]"
            ),
            title="[bold yellow]⚡ Update Available[/bold yellow]",
            border_style="bright_yellow",
            box=box.ROUNDED,
            padding=(1, 2)
        ))
        console.print()
    
    # Check if running in interactive mode (no file specified and no special flags)
    is_interactive = (
        not args.file and
        not args.list and
        not args.formats and
        not args.verify and
        len(sys.argv) == 1  # No arguments at all
    )
    
    if is_interactive:
        selected_file, options = interactive_mode()
        
        if not selected_file:
            return  # User cancelled or no files found
        
        # Set args based on interactive choices
        args.file = selected_file
        if options.get('verify'):
            args.verify = True
        elif options.get('compact'):
            args.compact = True
        elif options.get('semi_compact'):
            args.semi_compact = True
        elif options.get('advanced'):
            args.advanced = True
        # else: full mode (default)
        # Pass badge options from interactive mode into args
        if options.get('badges'):
            # store lists directly on args for later handling
            args.badges = options.get('badges')
            args.badge_formats = options.get('badge_formats', ['svg'])
            # default output directory
            args.badge_dir = None
    
    # Handle special commands
    if args.formats:
        console.print(Panel(
            get_supported_formats_info(),
            title="[bold cyan]Supported File Formats & Features[/bold cyan]",
            border_style="cyan",
            box=box.ROUNDED
        ))
        return
    
    if args.list:
        files = list_manuscript_files()
        if not files:
            console.print("[yellow]No manuscript files found in current directory.[/yellow]")
            return
        
        table = Table(title="Available Manuscript Files", box=box.ROUNDED, border_style="cyan")
        table.add_column("#", style="dim", width=4)
        table.add_column("File Name", style="cyan")
        table.add_column("Type", style="yellow", width=8)
        table.add_column("Size", style="green", justify="right", width=12)
        table.add_column("Modified", style="dim")
        
        for i, file in enumerate(files, 1):
            size_kb = file.stat().st_size / 1024
            size_str = f"{size_kb:.1f} KB" if size_kb < 1024 else f"{size_kb/1024:.1f} MB"
            modified = datetime.fromtimestamp(file.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
            table.add_row(
                str(i),
                file.name,
                file.suffix.upper().replace('.', ''),
                size_str,
                modified
            )
        
        console.print(table)
        console.print("\n[dim]Use -f <filename> to analyze a specific file[/dim]")
        return
    
    # Determine file path (interactive mode already sets args.file)
    file_path = args.file
    
    if not file_path:
        # If still no file (shouldn't happen after interactive mode)
        file_path = "manuscript.md"
    
    if not Path(file_path).exists():
        console.print(f"[bold red]Error:[/bold red] File '{file_path}' not found!")
        console.print("\n[dim]Tip: Use --list to see available files or run without arguments for interactive mode[/dim]")
        return
    
    # Load comparison stats if requested
    comparison_stats = None
    if args.compare:
        comparison_stats = load_comparison_stats(args.compare)
    
    # Analyze manuscript (with progress bar unless minimalist or output to file)
    show_progress = not (args.minimalist or args.output or args.no_animation)
    stats = analyze_manuscript(
        file_path, 
        enable_advanced=args.advanced, 
        show_progress=show_progress,
        top_words_count=max(args.top_words, 1),  # Ensure at least 1
        min_word_length=max(args.min_word_length, 1)  # Ensure at least 1
    )
    
    if not stats:
        console.print("[bold red]Failed to analyze manuscript.[/bold red]")
        return
    
    # Handle export first if requested
    if args.export:
        export_file = args.output if args.output else f"{Path(file_path).stem}.{args.export}"
        
        if args.export == 'json':
            export_to_json(stats, export_file)
        elif args.export == 'csv':
            export_to_csv(stats, export_file)
        elif args.export == 'html':
            export_to_html(stats, export_file)
        
        # If export mode, don't display terminal output
        if not args.output:
            return
    
    # Save snapshot if requested
    if args.save_snapshot:
        snapshot_file = save_stats_snapshot(stats, file_path)
        if snapshot_file:
            console.print(f"[green]✓ Snapshot saved: {snapshot_file}[/green]\n")

    # Badge generation (CLI or interactive)
    badge_request = None
    if hasattr(args, 'badges') and args.badges:
        # args.badges from argparse is a comma-separated string
        if isinstance(args.badges, str):
            badge_request = [b.strip() for b in args.badges.split(',') if b.strip()]
        else:
            # from interactive mode (already a list)
            badge_request = args.badges

    if badge_request:
        # Determine formats
        if hasattr(args, 'badge_formats') and isinstance(args.badge_formats, (list, tuple)):
            formats = args.badge_formats
        else:
            formats = [f.strip() for f in (args.badge_formats or 'svg').split(',') if f.strip()]

        out_dir = args.badge_dir if args.badge_dir else None

        try:
            created = generate_badges(stats, badge_request, formats, out_dir=out_dir)
            if created:
                for p in created:
                    console.print(f"[green]Saved:[/green] {p}")
        except Exception as e:
            console.print(f"[red]Error generating badges: {e}[/red]")
    
    # Handle verify mode
    if args.verify:
        console.clear()
        console.print(create_header())
        console.print()
        
        # Load ignore patterns
        ignore_patterns = load_ignore_patterns()
        
        # Run verification
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("[cyan]Running comprehensive verification...", total=100)
            text = read_manuscript(file_path)
            progress.update(task, advance=30)
            issues = verify_manuscript(text, ignore_patterns)
            progress.update(task, advance=70)
        
        # Display file info and ignore patterns status
        file_info = Text()
        file_info.append("File: ", style="bold")
        file_info.append(file_path, style="cyan")
        
        if ignore_patterns:
            file_info.append(f"\nIgnore patterns: ", style="bold")
            file_info.append(f"{len(ignore_patterns)} patterns loaded from .musestatignore", style="green")
        else:
            file_info.append(f"\nIgnore patterns: ", style="bold")
            file_info.append("None (create .musestatignore to ignore patterns)", style="dim")
        
        console.print(Panel(file_info, box=box.ROUNDED, border_style="blue"))
        console.print()
        
        # Display checks info and summary side by side
        console.print(Columns([
            create_verification_checks_info(),
            create_verification_summary(issues)
        ], equal=True, expand=True))
        console.print()
        
        if issues:
            # Display detailed issues by type
            for issue_type in [IssueType.ERROR, IssueType.WARNING, IssueType.INFO]:
                table = create_verification_table(issues, issue_type, limit=20)
                if table:
                    console.print(table)
                    console.print()
        
        # Footer
        errors = sum(1 for i in issues if i.type == IssueType.ERROR)
        footer = Text()
        if errors > 0:
            footer.append(f"⚠️  {errors} critical issue(s) require attention before publishing", style="bold red")
        else:
            footer.append("✓ All critical checks passed!", style="bold green")
        
        console.print(Panel(
            footer,
            box=box.DOUBLE_EDGE,
            border_style="bright_yellow" if errors > 0 else "bright_green",
            padding=(0, 2)
        ))
        return
    
    # Handle minimalist mode
    if args.minimalist:
        print_minimalist(stats)
        return
    
    # Handle output to file
    if args.output and not args.export:
        console.print(f"[yellow]Note: Use --export html/json/csv to save formatted reports.[/yellow]")
        console.print(f"[yellow]Terminal output capture coming soon. Displaying to terminal for now.[/yellow]\n")
    
    # Display results based on mode
    if args.chapters_only:
        console.clear()
        if stats['chapters']:
            console.print(create_chapters_table(
                stats['chapters'], 
                max_chapters=args.max_chapters,
                sparkline_width=args.sparkline_width
            ))
        else:
            console.print("[yellow]No chapters found in manuscript.[/yellow]")
    else:
        # Override animation preference
        if args.no_animation:
            console.clear()
            if args.compact:
                console.print(create_compact_display(stats))
                if comparison_stats:
                    console.print()
                    console.print(create_comparison_panel(stats, comparison_stats))
            elif args.semi_compact:
                # Semi-compact with no animation
                console.print(create_header())
                console.print()
                
                console.print(Columns([
                    create_semi_compact_overview(stats),
                    create_milestone_panel(stats) if not comparison_stats else create_comparison_panel(stats, comparison_stats)
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
                footer.append(" ✨", style="bold bright_green")
                
                console.print(Panel(
                    footer,
                    box=box.DOUBLE_EDGE,
                    border_style="bright_green",
                    padding=(0, 2)
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
                
                if args.advanced:
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
                
                if stats['chapters']:
                    console.print(create_chapters_table(stats['chapters']))
                    console.print()
                console.print(create_word_frequency_table(stats['common_words']))
        else:
            # Build display options dictionary
            display_options = {
                'top_words': args.top_words,
                'max_chapters': args.max_chapters,
                'sparkline_width': args.sparkline_width,
                'hide_word_frequency': args.hide_word_frequency,
                'hide_heat_map': args.hide_heat_map,
                'hide_chapter_details': args.hide_chapter_details,
                'show_top_chapters': args.show_top_chapters
            }
            
            display_statistics(
                stats, 
                compact=args.compact, 
                semi_compact=args.semi_compact, 
                comparison_stats=comparison_stats, 
                show_advanced=args.advanced,
                display_options=display_options
            )
    
    # If in interactive mode, wait for user before exiting
    if is_interactive:
        console.print()
        console.print("[dim italic]Analysis complete. Press Enter to exit...[/dim italic]")
        try:
            input()
        except (KeyboardInterrupt, EOFError):
            pass


if __name__ == "__main__":
    main()


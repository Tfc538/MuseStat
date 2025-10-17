"""
Statistics snapshot and comparison utilities.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional
from rich.console import Console

console = Console()


def save_stats_snapshot(stats: Dict, file_path: str) -> Optional[Path]:
    """
    Save statistics snapshot for comparison.
    
    Args:
        stats: Statistics dictionary from analyzer
        file_path: Original manuscript file path
        
    Returns:
        Path to saved snapshot file, or None on error
    """
    snapshot_file = Path(file_path).with_suffix('.stats.json')
    
    snapshot = {
        'timestamp': datetime.now().isoformat(),
        'file': file_path,
        'total_words': stats['total_words'],
        'total_characters': stats['total_characters'],
        'total_sentences': stats['total_sentences'],
        'total_paragraphs': stats['total_paragraphs'],
        'chapters': len(stats['chapters']),
        'dialogue_words': stats.get('dialogue', {}).get('words', 0),
    }
    
    try:
        with open(snapshot_file, 'w', encoding='utf-8') as f:
            json.dump(snapshot, f, indent=2)
        return snapshot_file
    except Exception as e:
        console.print(f"[yellow]Warning: Could not save snapshot: {e}[/yellow]")
        return None


def load_comparison_stats(file_path: str) -> Optional[Dict]:
    """
    Load previous statistics for comparison.
    
    Args:
        file_path: Path to saved stats file
        
    Returns:
        Dictionary with previous stats, or None on error
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        console.print(f"[yellow]Warning: Could not load comparison file: {e}[/yellow]")
        return None


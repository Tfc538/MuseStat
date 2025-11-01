"""
Badge generation utilities for MuseStat.

Creates simple SVG badges (and optionally PNG if cairosvg is installed)
and saves them to the badges directory.
"""
from pathlib import Path
import os
import re
from typing import List, Dict
from ..utils.achievements import get_achievement_badge
from rich.console import Console

console = Console()


def _sanitize_name(name: str) -> str:
    # Replace spaces with underscores and remove unsafe characters
    name = name.strip()
    name = re.sub(r"\s+", "_", name)
    name = re.sub(r"[^A-Za-z0-9_\-\.]+", "", name)
    return name


def _render_svg_badge(label: str, value: str, color: str = "#4c1") -> str:
    # Modern, polished badge design with gradients, shadows, and web fonts
    # Color scheme: darker label background, vibrant value background
    label_w = max(9 * len(label) + 28, 90)
    value_w = max(9 * len(value) + 28, 90)
    height = 36
    total_w = label_w + value_w
    label_bg = "#2c3e50"
    value_color = color
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="{height}" viewBox="0 0 {total_w} {height}">
  <defs>
    <linearGradient id="labelGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#34495e;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#2c3e50;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="valueGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{color};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{color}dd;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.15"/>
    </filter>
  </defs>
  
  <!-- Background with shadow -->
  <g filter="url(#shadow)">
    <!-- Label section -->
    <rect x="0" y="0" width="{label_w}" height="{height}" rx="6" fill="url(#labelGrad)"/>
    
    <!-- Value section -->
    <rect x="{label_w}" y="0" width="{value_w}" height="{height}" rx="6" fill="url(#valueGrad)"/>
  </g>
  
  <!-- Highlight effect on top -->
  <rect x="0" y="0" width="{total_w}" height="{height}" rx="6" fill="#fff" opacity="0.08"/>
  
  <!-- Label text -->
  <text x="{label_w/2}" y="24" font-family="Arial, Helvetica, sans-serif" 
        font-size="13" font-weight="600" text-anchor="middle" fill="#ecf0f1" letter-spacing="-0.3">
    {label}
  </text>
  
  <!-- Value text -->
  <text x="{label_w + value_w/2}" y="24" font-family="Arial, Helvetica, sans-serif" 
        font-size="14" font-weight="700" text-anchor="middle" fill="#fff" letter-spacing="-0.2">
    {value}
  </text>
</svg>'''
    return svg


def _save_svg(svg: str, path: Path) -> bool:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(svg)
        return True
    except Exception as e:
        console.print(f"[red]Error saving SVG badge {path}: {e}[/red]")
        return False


def _svg_to_png(svg_path: Path, png_path: Path) -> bool:
    try:
        import cairosvg
    except Exception:
        console.print("[yellow]cairosvg not installed; PNG export skipped. Install with: pip install cairosvg[/yellow]")
        return False

    try:
        png_path.parent.mkdir(parents=True, exist_ok=True)
        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path))
        return True
    except Exception as e:
        console.print(f"[red]Error converting SVG to PNG: {e}[/red]")
        return False


def _badge_values_from_stats(stats: Dict, badge_type: str) -> Dict:
    # Map badge_type to (label, value, color) with beautiful, modern color palette
    # Colors: vibrant, saturated, accessible contrast on dark background
    if badge_type == 'achievement':
        badge = stats.get('badge') or get_achievement_badge(stats.get('total_words', 0))
        label = 'Achievement'
        value = badge.get('title', 'Writer')
        color = '#3b82f6'  # Vibrant blue
    elif badge_type == 'wordcount':
        label = 'Words'
        value = f"{stats.get('total_words', 0):,}"
        color = '#10b981'  # Emerald green
    elif badge_type == 'chapters':
        label = 'Chapters'
        value = str(len(stats.get('chapters', [])))
        color = '#a78bfa'  # Purple/lavender
    elif badge_type == 'reading_time':
        rt = stats.get('reading_time', {})
        value = rt.get('pages_avg') if isinstance(rt, dict) else ''
        label = 'Pages'
        value = str(value)
        color = '#f59e0b'  # Amber/gold
    else:
        label = badge_type.capitalize()
        value = ''
        color = '#6366f1'  # Indigo fallback

    return {'label': label, 'value': value, 'color': color}


def generate_badges(stats: Dict, badge_types: List[str], formats: List[str], out_dir: str = None) -> List[Path]:
    """
    Generate badges for the provided stats.

    Args:
        stats: analysis stats dictionary
        badge_types: list of badge type strings (e.g., ['achievement','wordcount'])
        formats: list of formats to output (e.g., ['svg','png'])
        out_dir: optional output directory (defaults to ./musestat/badges)

    Returns:
        List of created file Paths
    """
    created = []
    if out_dir is None:
        out_dir = os.path.join('musestat', 'badges')

    novel = Path(stats.get('file_path', 'manuscript')).stem
    novel = _sanitize_name(novel)

    for btype in badge_types:
        info = _badge_values_from_stats(stats, btype)
        label = info['label']
        value = info['value']
        color = info['color']

        # Don't sanitize badge_type—keep the original name (e.g. 'reading_time')
        filename_base = f"{novel}_{btype}"

        if 'svg' in formats:
            svg = _render_svg_badge(label, value, color)
            svg_path = Path(out_dir) / f"{filename_base}.svg"
            if _save_svg(svg, svg_path):
                created.append(svg_path)

        if 'png' in formats:
            # prefer converting from svg if available (created above)
            png_path = Path(out_dir) / f"{filename_base}.png"
            svg_path = Path(out_dir) / f"{filename_base}.svg"
            if svg_path.exists():
                if _svg_to_png(svg_path, png_path):
                    created.append(png_path)
            else:
                # render svg string and convert without saving first
                svg = _render_svg_badge(label, value, color)
                tmp_svg = Path(out_dir) / f"{filename_base}._tmp.svg"
                if _save_svg(svg, tmp_svg):
                    if _svg_to_png(tmp_svg, png_path):
                        created.append(png_path)
                    try:
                        tmp_svg.unlink()
                    except Exception:
                        pass

    if created:
        console.print(f"[green]✓ Generated {len(created)} badge(s) in {out_dir}[/green]")
    else:
        console.print("[yellow]No badges were generated.[/yellow]")

    return created

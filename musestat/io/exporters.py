"""
Export manuscript statistics to various formats.

Supports JSON, CSV, and HTML export.
"""

import json
import csv
from pathlib import Path
from datetime import datetime
from typing import Dict
from rich.console import Console

console = Console()


def export_to_json(stats: Dict, output_file: str) -> bool:
    """
    Export statistics to JSON format.
    
    Args:
        stats: Statistics dictionary from analyzer
        output_file: Output file path
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Make stats JSON-serializable
        export_stats = stats.copy()
        export_stats['modified_date'] = stats['modified_date'].isoformat()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export_stats, f, indent=2, ensure_ascii=False)
        
        console.print(f"[green]✓ Exported to JSON: {output_file}[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error exporting to JSON: {e}[/red]")
        return False


def export_to_csv(stats: Dict, output_file: str) -> bool:
    """
    Export statistics to CSV format.
    
    Args:
        stats: Statistics dictionary from analyzer
        output_file: Output file path
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write overview stats
            writer.writerow(['Metric', 'Value'])
            writer.writerow(['File', Path(stats['file_path']).name])
            writer.writerow(['Total Words', stats['total_words']])
            writer.writerow(['Characters', stats['total_characters']])
            writer.writerow(['Sentences', stats['total_sentences']])
            writer.writerow(['Paragraphs', stats['total_paragraphs']])
            writer.writerow(['Chapters', len(stats['chapters'])])
            writer.writerow(['Avg Words/Sentence', f"{stats['avg_words_per_sentence']:.1f}"])
            
            # Reading time
            rt = stats['reading_time']
            writer.writerow(['Reading Time (Range)', rt['range_str']])
            writer.writerow(['Estimated Pages', rt['pages_str']])
            
            # Chapter stats
            if stats.get('chapter_stats'):
                cs = stats['chapter_stats']
                writer.writerow([''])
                writer.writerow(['Chapter Statistics', ''])
                writer.writerow(['Mean Length', f"{cs['mean']:.0f} words"])
                writer.writerow(['Std Deviation', f"{cs['std_dev']:.0f} words"])
                writer.writerow(['Shortest Chapter', f"{cs['shortest_chapter']} ({cs['min']} words)"])
                writer.writerow(['Longest Chapter', f"{cs['longest_chapter']} ({cs['max']} words)"])
            
            # Chapter breakdown
            writer.writerow([''])
            writer.writerow(['Chapter', 'Words', 'Percentage'])
            for ch in stats['chapters']:
                pct = (ch['words'] / stats['total_words'] * 100) if stats['total_words'] > 0 else 0
                writer.writerow([ch['title'], ch['words'], f"{pct:.1f}%"])
        
        console.print(f"[green]✓ Exported to CSV: {output_file}[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error exporting to CSV: {e}[/red]")
        return False


def export_to_html(stats: Dict, output_file: str) -> bool:
    """
    Export statistics to HTML format with styled report.
    
    Args:
        stats: Statistics dictionary from analyzer
        output_file: Output file path
        
    Returns:
        True if successful, False otherwise
    """
    try:
        rt = stats['reading_time']
        cs = stats.get('chapter_stats', {})
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MuseStat Report - {Path(stats['file_path']).name}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
            color: #333;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 20px;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
        }}
        .header p {{
            margin: 10px 0 0;
            opacity: 0.9;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .stat-card h3 {{
            margin: 0 0 10px;
            color: #667eea;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .stat-value {{
            font-size: 2em;
            font-weight: bold;
            color: #333;
        }}
        .section {{
            background: white;
            padding: 25px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .section h2 {{
            margin-top: 0;
            color: #667eea;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }}
        th, td {{
            text-align: left;
            padding: 12px;
            border-bottom: 1px solid #e0e0e0;
        }}
        th {{
            background: #f8f9fa;
            font-weight: 600;
            color: #667eea;
        }}
        tr:hover {{
            background: #f8f9fa;
        }}
        .progress-bar {{
            background: #e0e0e0;
            border-radius: 10px;
            height: 8px;
            overflow: hidden;
            margin-top: 8px;
        }}
        .progress-fill {{
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            height: 100%;
            transition: width 0.3s ease;
        }}
        .footer {{
            text-align: center;
            color: #999;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 MuseStat Report</h1>
        <p>{Path(stats['file_path']).name} • Generated {datetime.now().strftime('%B %d, %Y at %H:%M')}</p>
    </div>
    
    <div class="stats-grid">
        <div class="stat-card">
            <h3>Total Words</h3>
            <div class="stat-value">{stats['total_words']:,}</div>
        </div>
        <div class="stat-card">
            <h3>Chapters</h3>
            <div class="stat-value">{len(stats['chapters'])}</div>
        </div>
        <div class="stat-card">
            <h3>Reading Time</h3>
            <div class="stat-value" style="font-size: 1.3em;">{rt['range_str']}</div>
        </div>
        <div class="stat-card">
            <h3>Estimated Pages</h3>
            <div class="stat-value" style="font-size: 1.5em;">{rt['pages_avg']}</div>
            <p style="margin: 5px 0 0; font-size: 0.9em; color: #666;">{rt['pages_str']}</p>
        </div>
    </div>
    
    <div class="section">
        <h2>Overview</h2>
        <table>
            <tr><td><strong>Characters:</strong></td><td>{stats['total_characters']:,}</td></tr>
            <tr><td><strong>Sentences:</strong></td><td>{stats['total_sentences']:,}</td></tr>
            <tr><td><strong>Paragraphs:</strong></td><td>{stats['total_paragraphs']:,}</td></tr>
            <tr><td><strong>Avg Words/Sentence:</strong></td><td>{stats['avg_words_per_sentence']:.1f}</td></tr>
        </table>
    </div>
"""
        
        # Chapter statistics
        if cs:
            html += f"""
    <div class="section">
        <h2>Chapter Statistics</h2>
        <table>
            <tr><td><strong>Average Length:</strong></td><td>{cs['mean']:.0f} words</td></tr>
            <tr><td><strong>Standard Deviation:</strong></td><td>{cs['std_dev']:.0f} words</td></tr>
            <tr><td><strong>Shortest:</strong></td><td>{cs['shortest_chapter']} ({cs['min']:,} words)</td></tr>
            <tr><td><strong>Longest:</strong></td><td>{cs['longest_chapter']} ({cs['max']:,} words)</td></tr>
            <tr><td><strong>Range:</strong></td><td>{cs['range']:,} words</td></tr>
        </table>
    </div>
"""
        
        # Chapter breakdown
        html += """
    <div class="section">
        <h2>Chapter Breakdown</h2>
        <table>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Chapter</th>
                    <th>Words</th>
                    <th>Percentage</th>
                </tr>
            </thead>
            <tbody>
"""
        
        for i, ch in enumerate(stats['chapters'], 1):
            pct = (ch['words'] / stats['total_words'] * 100) if stats['total_words'] > 0 else 0
            html += f"""
                <tr>
                    <td>{i}</td>
                    <td>{ch['title']}</td>
                    <td>{ch['words']:,}</td>
                    <td>
                        {pct:.1f}%
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: {pct}%"></div>
                        </div>
                    </td>
                </tr>
"""
        
        html += """
            </tbody>
        </table>
    </div>
    
    <div class="footer">
        <p>Generated by <strong>MuseStat</strong> - Manuscript Analytics</p>
        <p>Because every word counts</p>
    </div>
</body>
</html>
"""
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        console.print(f"[green]✓ Exported to HTML: {output_file}[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error exporting to HTML: {e}[/red]")
        return False


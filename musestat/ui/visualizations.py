"""
Visual enhancements for terminal UI including sparklines, charts, heat maps, and indicators.
"""

from typing import List, Dict, Optional, Tuple
from rich.text import Text


def create_sparkline(values: List[float], width: int = 20, height: int = 8) -> str:
    """
    Create a sparkline chart from a list of values.
    
    Args:
        values: List of numeric values to plot
        width: Maximum width of the sparkline
        height: Height resolution (number of possible bar heights)
        
    Returns:
        Unicode sparkline string
    """
    if not values:
        return "─" * width
    
    min_val = min(values)
    max_val = max(values)
    value_range = max_val - min_val if max_val != min_val else 1
    
    if len(values) > width:
        step = len(values) / width
        sampled_values = [values[int(i * step)] for i in range(width)]
    else:
        sampled_values = values
    
    blocks = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
    
    sparkline = ""
    for val in sampled_values:
        normalized = (val - min_val) / value_range
        block_index = int(normalized * (len(blocks) - 1))
        sparkline += blocks[block_index]
    
    return sparkline


def create_horizontal_bar(percentage: float, width: int = 20, filled_char: str = "█", empty_char: str = "░") -> str:
    """
    Create a horizontal progress bar.
    
    Args:
        percentage: Percentage filled (0-100)
        width: Width of the bar
        filled_char: Character for filled portion
        empty_char: Character for empty portion
        
    Returns:
        Bar string
    """
    filled = int((percentage / 100) * width)
    return filled_char * filled + empty_char * (width - filled)


def create_vertical_bar_chart(data: List[Tuple[str, float]], max_height: int = 10, max_width: int = 60) -> List[str]:
    """
    Create a vertical ASCII bar chart.
    
    Args:
        data: List of (label, value) tuples
        max_height: Maximum height of bars
        max_width: Maximum width for labels
        
    Returns:
        List of strings representing the chart lines
    """
    if not data:
        return ["No data to display"]
    
    max_val = max(val for _, val in data)
    if max_val == 0:
        max_val = 1
    
    lines = []
    
    for h in range(max_height, 0, -1):
        line = ""
        for label, value in data:
            normalized_height = int((value / max_val) * max_height)
            if normalized_height >= h:
                line += "█ "
            else:
                line += "  "
        lines.append(line)
    
    value_line = ""
    for label, value in data:
        value_str = f"{value:,.0f}"[:2]
        value_line += value_str + " " * (2 - len(value_str) + 1)
    lines.append(value_line)
    
    lines.append("─" * (len(data) * 2))
    
    label_line = ""
    for label, _ in data:
        truncated = label[:2] if len(label) >= 2 else label + " "
        label_line += truncated + " "
    lines.append(label_line)
    
    return lines


def create_simple_pie_chart(data: List[Tuple[str, float]], width: int = 40) -> List[str]:
    """
    Create a simple ASCII pie chart representation.
    
    Args:
        data: List of (label, value) tuples
        width: Width of the chart
        
    Returns:
        List of strings representing the chart
    """
    if not data:
        return ["No data to display"]
    
    total = sum(val for _, val in data)
    if total == 0:
        return ["No data to display"]
    
    lines = []
    pie_chars = ['█', '▓', '▒', '░', '▪', '▫', '●', '○', '◆', '◇']
    
    bar_width = width - 20
    for i, (label, value) in enumerate(data):
        percentage = (value / total) * 100
        filled = int((percentage / 100) * bar_width)
        char = pie_chars[i % len(pie_chars)]
        bar = char * filled
        
        label_truncated = label[:15] if len(label) > 15 else label
        line = f"{label_truncated:<15} {bar} {percentage:>5.1f}%"
        lines.append(line)
    
    return lines


def create_heat_map_line(values: List[float], width: int = 50) -> str:
    """
    Create a single line heat map using color gradients.
    
    Args:
        values: List of values to map
        width: Width of the heat map
        
    Returns:
        String representing heat intensity
    """
    if not values:
        return "─" * width
    
    min_val = min(values)
    max_val = max(values)
    value_range = max_val - min_val if max_val != min_val else 1
    
    if len(values) > width:
        step = len(values) / width
        sampled = [values[int(i * step)] for i in range(width)]
    else:
        sampled = values + [values[-1]] * (width - len(values))
    
    intensities = [' ', '░', '▒', '▓', '█']
    
    heatmap = ""
    for val in sampled:
        normalized = (val - min_val) / value_range
        intensity_index = int(normalized * (len(intensities) - 1))
        heatmap += intensities[intensity_index]
    
    return heatmap


def create_multi_line_heat_map(data: List[List[float]], labels: Optional[List[str]] = None, width: int = 50) -> List[str]:
    """
    Create a multi-line heat map.
    
    Args:
        data: List of lists of values (each inner list is a row)
        labels: Optional labels for each row
        width: Width of each heat map line
        
    Returns:
        List of strings representing the heat map
    """
    if not data:
        return ["No data to display"]
    
    lines = []
    for i, row_values in enumerate(data):
        label = labels[i] if labels and i < len(labels) else f"Row {i+1}"
        heatmap = create_heat_map_line(row_values, width - 20)
        line = f"{label:<15} │ {heatmap}"
        lines.append(line)
    
    return lines


def get_readability_indicator(score: float, metric_type: str = "flesch") -> Tuple[str, str, str]:
    """
    Get color-coded indicator for readability scores.
    
    Args:
        score: Readability score
        metric_type: Type of metric ("flesch", "grade", "fog")
        
    Returns:
        Tuple of (symbol, color, interpretation)
    """
    if metric_type == "flesch":
        if score >= 70:
            return "●", "bright_green", "Easy"
        elif score >= 50:
            return "●", "yellow", "Fair"
        else:
            return "●", "red", "Difficult"
    
    elif metric_type in ["grade", "fog"]:
        if score <= 8:
            return "●", "bright_green", "Easy"
        elif score <= 12:
            return "●", "yellow", "Fair"
        else:
            return "●", "red", "Difficult"
    
    return "●", "white", "Unknown"


def create_trend_arrow(current: float, previous: float, higher_is_better: bool = True) -> Tuple[str, str]:
    """
    Create a trend arrow showing if a metric improved or declined.
    
    Args:
        current: Current value
        previous: Previous value
        higher_is_better: Whether higher values are better
        
    Returns:
        Tuple of (arrow symbol, color)
    """
    if current == previous:
        return "→", "dim"
    
    is_increase = current > previous
    
    if higher_is_better:
        if is_increase:
            return "↑", "bright_green"
        else:
            return "↓", "red"
    else:
        if is_increase:
            return "↑", "red"
        else:
            return "↓", "bright_green"


def create_chapter_balance_visualization(chapter_lengths: List[int], target_length: Optional[int] = None) -> List[str]:
    """
    Create a visual representation of chapter length balance/consistency.
    
    Args:
        chapter_lengths: List of word counts for each chapter
        target_length: Optional target length to compare against
        
    Returns:
        List of strings representing the visualization
    """
    if not chapter_lengths:
        return ["No chapters to display"]
    
    lines = []
    
    mean_length = sum(chapter_lengths) / len(chapter_lengths)
    min_length = min(chapter_lengths)
    max_length = max(chapter_lengths)
    
    if target_length is None:
        target_length = mean_length
    
    sparkline = create_sparkline(chapter_lengths, width=40)
    lines.append(f"Trend: {sparkline}")
    lines.append("")
    
    lines.append("Chapter Balance:")
    for i, length in enumerate(chapter_lengths, 1):
        deviation = abs(length - target_length) / target_length if target_length else 0
        
        if deviation < 0.15:
            indicator = "●"
            color = "bright_green"
            status = "Balanced"
        elif deviation < 0.30:  # Within 30%
            indicator = "●"
            color = "yellow"
            status = "Acceptable"
        else:
            indicator = "●"
            color = "red"
            status = "Unbalanced"
        
        normalized = length / max_length if max_length else 0
        bar_length = int(normalized * 20)
        bar = "█" * bar_length
        
        lines.append(f"Ch {i:>2}: {indicator} {bar:<20} {length:>6,} words ({status})")
    
    lines.append("")
    lines.append(f"Mean: {mean_length:,.0f} | Range: {min_length:,} - {max_length:,}")
    
    return lines


def create_progress_forecast(current_words: int, target_words: int, days_worked: int, words_per_day: Optional[float] = None) -> Text:
    """
    Create a progress forecast visualization.
    
    Args:
        current_words: Current word count
        target_words: Target word count
        days_worked: Number of days worked so far
        words_per_day: Average words per day (calculated if None)
        
    Returns:
        Rich Text object with forecast
    """
    if words_per_day is None and days_worked > 0:
        words_per_day = current_words / days_worked
    elif words_per_day is None:
        words_per_day = 0
    
    remaining = target_words - current_words
    
    content = Text()
    
    progress_pct = (current_words / target_words * 100) if target_words > 0 else 0
    bar = create_horizontal_bar(progress_pct, width=30)
    content.append(f"{bar} {progress_pct:.1f}%\n\n", style="cyan")
    
    content.append(f"Current:  {current_words:>8,} words\n", style="white")
    content.append(f"Target:   {target_words:>8,} words\n", style="white")
    content.append(f"Remaining:{remaining:>8,} words\n\n", style="yellow")
    
    if words_per_day > 0 and remaining > 0:
        days_remaining = int(remaining / words_per_day)
        content.append(f"Velocity: {words_per_day:>8,.0f} words/day\n", style="cyan")
        content.append(f"Est. Days:{days_remaining:>8} days to finish\n", style="bright_green")
    elif remaining <= 0:
        content.append("🎉 Target reached!\n", style="bold bright_green")
    else:
        content.append("Track progress over time for forecasts\n", style="dim")
    
    return content


def create_mini_histogram(values: List[float], bins: int = 10, width: int = 40) -> List[str]:
    """
    Create a mini histogram visualization.
    
    Args:
        values: List of values to plot
        bins: Number of bins/buckets
        width: Width of the histogram
        
    Returns:
        List of strings representing the histogram
    """
    if not values:
        return ["No data to display"]
    
    min_val = min(values)
    max_val = max(values)
    value_range = max_val - min_val if max_val != min_val else 1
    bin_size = value_range / bins
    
    bin_counts = [0] * bins
    for val in values:
        bin_index = min(int((val - min_val) / bin_size), bins - 1)
        bin_counts[bin_index] += 1
    
    max_count = max(bin_counts) if bin_counts else 1
    lines = []
    
    for i, count in enumerate(bin_counts):
        bin_start = min_val + (i * bin_size)
        bin_end = min_val + ((i + 1) * bin_size)
        
        bar_length = int((count / max_count) * (width - 25))
        bar = "█" * bar_length
        
        line = f"{bin_start:>6.0f}-{bin_end:<6.0f} │ {bar} {count}"
        lines.append(line)
    
    return lines


def get_metric_color(value: float, thresholds: Tuple[float, float], reverse: bool = False) -> str:
    """
    Get color for a metric based on thresholds.
    
    Args:
        value: Metric value
        thresholds: Tuple of (good_threshold, fair_threshold)
        reverse: If True, lower is better
        
    Returns:
        Rich color string
    """
    good_threshold, fair_threshold = thresholds
    
    if not reverse:
        if value >= good_threshold:
            return "bright_green"
        elif value >= fair_threshold:
            return "yellow"
        else:
            return "red"
    else:
        if value <= good_threshold:
            return "bright_green"
        elif value <= fair_threshold:
            return "yellow"
        else:
            return "red"


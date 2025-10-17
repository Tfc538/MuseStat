"""
Dialogue analysis for manuscripts.
"""

import re
from typing import Dict


def count_dialogue(text: str) -> Dict:
    """
    Count dialogue lines and calculate dialogue ratio.
    
    Args:
        text: Full manuscript text
        
    Returns:
        Dictionary with lines, words, and ratio statistics
    """
    lines = text.split('\n')
    dialogue_lines = 0
    total_lines = len([l for l in lines if l.strip()])
    dialogue_words = 0
    
    # Patterns for dialogue detection
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check for quoted dialogue (supports various quote styles)
        if '"' in line or '"' in line or '"' in line or "'" in line or "'" in line:
            # Count as dialogue if it has substantial quoted content
            quotes = re.findall(r'["\'](.*?)["\']', line)
            if quotes:
                dialogue_lines += 1
                dialogue_words += sum(len(q.split()) for q in quotes)
    
    dialogue_ratio = (dialogue_lines / total_lines * 100) if total_lines > 0 else 0
    
    return {
        'lines': dialogue_lines,
        'words': dialogue_words,
        'ratio': dialogue_ratio
    }


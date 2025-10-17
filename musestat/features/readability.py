"""
Readability metrics and pacing analysis.
"""

import re
from typing import Dict, Optional, List, Tuple
from ..core.text_processing import clean_markdown

# Optional import for readability metrics
try:
    import textstat
    READABILITY_SUPPORT = True
except ImportError:
    READABILITY_SUPPORT = False


def calculate_readability(text: str) -> Optional[Dict]:
    """
    Calculate readability metrics.
    
    Args:
        text: Full manuscript text
        
    Returns:
        Dictionary with various readability scores, or None if textstat not available
    """
    if not READABILITY_SUPPORT:
        return None
    
    try:
        clean_text = clean_markdown(text)
        
        return {
            'flesch_reading_ease': textstat.flesch_reading_ease(clean_text),
            'flesch_kincaid_grade': textstat.flesch_kincaid_grade(clean_text),
            'gunning_fog': textstat.gunning_fog(clean_text),
            'coleman_liau_index': textstat.coleman_liau_index(clean_text),
            'automated_readability_index': textstat.automated_readability_index(clean_text),
        }
    except Exception:
        return None


def detect_pacing_issues(text: str) -> Dict:
    """
    Detect long sentences and paragraphs that may affect pacing.
    
    Args:
        text: Full manuscript text
        
    Returns:
        Dictionary with pacing statistics including long sentences/paragraphs
    """
    clean_text = clean_markdown(text)
    
    # Analyze sentences
    sentences = [s.strip() for s in re.split(r'[.!?]+', clean_text) if s.strip()]
    sentence_lengths = [len(s.split()) for s in sentences]
    
    # Find long sentences (>40 words)
    long_sentences = [(i+1, len(s.split())) for i, s in enumerate(sentences) if len(s.split()) > 40]
    
    # Analyze paragraphs
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    paragraph_lengths = [len(p.split()) for p in paragraphs]
    
    # Find long paragraphs (>200 words) and short paragraphs (<10 words)
    long_paragraphs = [(i+1, len(p.split())) for i, p in enumerate(paragraphs) if len(p.split()) > 200]
    short_paragraphs = [(i+1, len(p.split())) for i, p in enumerate(paragraphs) if 0 < len(p.split()) < 10]
    
    return {
        'long_sentences': long_sentences[:10],  # Top 10
        'long_paragraphs': long_paragraphs[:10],  # Top 10
        'short_paragraphs': short_paragraphs[:10],  # Top 10
        'avg_sentence_length': sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0,
        'avg_paragraph_length': sum(paragraph_lengths) / len(paragraph_lengths) if paragraph_lengths else 0
    }


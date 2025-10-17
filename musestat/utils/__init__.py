"""Utility modules for stats, achievements, and version checking."""

from .stats import save_stats_snapshot, load_comparison_stats
from .achievements import get_achievement_badge, get_random_quote, estimate_reading_time
from .constants import WRITER_QUOTES, ACHIEVEMENT_MILESTONES
from .version_check import check_for_updates, get_update_message

__all__ = [
    'save_stats_snapshot',
    'load_comparison_stats',
    'get_achievement_badge',
    'get_random_quote',
    'estimate_reading_time',
    'WRITER_QUOTES',
    'ACHIEVEMENT_MILESTONES',
    'check_for_updates',
    'get_update_message',
]


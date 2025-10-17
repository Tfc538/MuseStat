"""
Version checking against GitHub releases.
"""

import json
import requests
from typing import Optional, Dict
from pathlib import Path
from datetime import datetime, timedelta
from ..config import __version__, GITHUB_API_URL, GITHUB_REPO_URL


# Cache file location
CACHE_FILE = Path.home() / '.musestat_version_cache.json'
CACHE_DURATION = timedelta(hours=24)


def check_for_updates(silent: bool = True) -> Optional[Dict]:
    """
    Check if a newer version is available on GitHub.
    
    Args:
        silent: If True, suppress error messages (default: True)
        
    Returns:
        Dictionary with update information if newer version exists, None otherwise
    """
    # Check cache first
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                cache = json.load(f)
            
            # Check if cache is still valid
            cache_time = datetime.fromisoformat(cache['timestamp'])
            if datetime.now() - cache_time < CACHE_DURATION:
                # Use cached result
                if cache.get('has_update'):
                    return cache['update_info']
                return None
        except Exception:
            # If cache is corrupted, continue with fresh check
            pass
    
    # Fetch latest release from GitHub
    try:
        response = requests.get(GITHUB_API_URL, timeout=3)
        response.raise_for_status()
        
        release_data = response.json()
        latest_version = release_data['tag_name'].lstrip('v')
        release_url = release_data['html_url']
        release_notes = release_data.get('body', '')[:200]  # First 200 chars
        
        # Compare versions (simple string comparison works for semver)
        current_parts = [int(x) for x in __version__.split('.')]
        latest_parts = [int(x) for x in latest_version.split('.')]
        
        has_update = latest_parts > current_parts
        
        update_info = None
        if has_update:
            update_info = {
                'current_version': __version__,
                'latest_version': latest_version,
                'release_url': release_url,
                'release_notes': release_notes
            }
        
        # Cache the result
        try:
            cache_data = {
                'timestamp': datetime.now().isoformat(),
                'has_update': has_update,
                'update_info': update_info
            }
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, indent=2)
        except Exception:
            # Silently fail if we can't write cache
            pass
        
        return update_info
    
    except Exception as e:
        # Network error, timeout, or API issue - silently fail unless not silent
        if not silent:
            from rich.console import Console
            console = Console()
            console.print(f"[dim]Could not check for updates: {e}[/dim]")
        return None


def get_update_message(update_info: Dict) -> str:
    """
    Format an update message for display.
    
    Args:
        update_info: Update information dictionary from check_for_updates()
        
    Returns:
        Formatted message string
    """
    return (
        f"🎉 New version available: v{update_info['latest_version']} "
        f"(current: v{update_info['current_version']})\n"
        f"Download: {update_info['release_url']}"
    )


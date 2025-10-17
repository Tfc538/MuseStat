"""
File readers for various manuscript formats.

Supports .md, .txt, .docx, and .rtf files.
"""

from pathlib import Path
from rich.console import Console

# Optional imports for different file formats
try:
    from docx import Document
    DOCX_SUPPORT = True
except ImportError:
    DOCX_SUPPORT = False

try:
    from striprtf.striprtf import rtf_to_text
    RTF_SUPPORT = True
except ImportError:
    RTF_SUPPORT = False

console = Console()


def read_docx(file_path: str) -> str:
    """
    Read a Word document (.docx).
    
    Args:
        file_path: Path to .docx file
        
    Returns:
        Text content of the document, or empty string on error
    """
    if not DOCX_SUPPORT:
        console.print("[bold red]Error:[/bold red] python-docx not installed. Install with: pip install python-docx")
        return ""
    
    try:
        doc = Document(file_path)
        paragraphs = [para.text for para in doc.paragraphs]
        return '\n'.join(paragraphs)
    except Exception as e:
        console.print(f"[bold red]Error reading DOCX file:[/bold red] {e}")
        return ""


def read_rtf(file_path: str) -> str:
    """
    Read a Rich Text Format (.rtf) file.
    
    Args:
        file_path: Path to .rtf file
        
    Returns:
        Text content of the file, or empty string on error
    """
    if not RTF_SUPPORT:
        console.print("[bold red]Error:[/bold red] striprtf not installed. Install with: pip install striprtf")
        return ""
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            rtf_content = f.read()
        return rtf_to_text(rtf_content)
    except Exception as e:
        console.print(f"[bold red]Error reading RTF file:[/bold red] {e}")
        return ""


def read_text(file_path: str) -> str:
    """
    Read a plain text or markdown file (.txt, .md).
    
    Args:
        file_path: Path to text file
        
    Returns:
        Text content of the file, or empty string on error
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        console.print(f"[bold red]Error reading file:[/bold red] {e}")
        return ""


def read_manuscript(file_path: str) -> str:
    """
    Read the manuscript file (auto-detects format from extension).
    
    Args:
        file_path: Path to manuscript file
        
    Returns:
        Text content of the file, or empty string on error
    """
    path = Path(file_path)
    
    if not path.exists():
        console.print(f"[bold red]Error:[/bold red] File '{file_path}' not found!")
        return ""
    
    extension = path.suffix.lower()
    
    # Route to appropriate reader based on file extension
    if extension == '.docx':
        return read_docx(file_path)
    elif extension == '.rtf':
        return read_rtf(file_path)
    elif extension in ['.txt', '.md', '.markdown']:
        return read_text(file_path)
    else:
        console.print(f"[bold yellow]Warning:[/bold yellow] Unknown file extension '{extension}'. Attempting to read as plain text...")
        return read_text(file_path)


def get_supported_formats_info() -> str:
    """
    Get information about supported file formats and their availability.
    
    Returns:
        Formatted string with format support information
    """
    formats = [
        "File Formats:",
        "✓ Markdown (.md, .markdown) - Built-in",
        "✓ Plain Text (.txt) - Built-in",
    ]
    
    if DOCX_SUPPORT:
        formats.append("✓ Word Document (.docx) - Available")
    else:
        formats.append("✗ Word Document (.docx) - install python-docx")
    
    if RTF_SUPPORT:
        formats.append("✓ Rich Text Format (.rtf) - Available")
    else:
        formats.append("✗ Rich Text Format (.rtf) - install striprtf")
    
    return "\n".join(formats)


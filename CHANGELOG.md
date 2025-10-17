# Changelog

All notable changes to MuseStat will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 2025-10-17

### Fixed
- GitHub Actions workflow now correctly generates platform-specific executables
- Linux executable: `musestat-linux-x64`
- macOS executable: `musestat-macos-x64`
- Windows executable: `musestat-windows-x64.exe`
- Previous releases had Linux/macOS executables overwriting each other

### Improved
- Added pip dependency caching to GitHub Actions (40-60% faster builds)
- Added PyInstaller build caching (20-30% faster subsequent builds)
- Build times reduced from ~2 minutes to ~30-60 seconds on cache hits

## [1.0.1] - 2025-10-17

### Added
- Interactive TUI mode when executable is run without arguments
- Welcome screen with feature overview
- Automatic file discovery and selection menu
- Analysis type selection menu (quick, standard, full, advanced, verify)
- "Press Enter to exit" prompt to prevent executable window from closing immediately
- Improved first-time user experience

### Changed
- Executables now user-friendly for non-technical users
- No longer immediately closes when double-clicked
- Enhanced user guidance for first-time users

## [1.0.0] - 2025-10-17

### Added
- Initial public release
- Complete refactoring from monolithic script to modular package structure
- Core analysis features:
  - Word, character, sentence, and paragraph counting
  - Chapter detection with multiple format support
  - Reading time estimation
  - Page count estimation
- Advanced features:
  - Language detection with language-specific stop words
  - Readability metrics (Flesch-Kincaid, Gunning Fog, Coleman-Liau, etc.)
  - Dialogue analysis and ratio calculation
  - Pacing detection (long sentences/paragraphs)
- Verification system:
  - 12 comprehensive check categories
  - Markdown formatting validation
  - Typo detection (repeated words)
  - Punctuation checking
  - Smart quotes consistency
  - Pre-publish marker detection (TODO, FIXME, etc.)
  - Support for `.musestatignore` patterns
- Display modes:
  - Full detailed analysis
  - Semi-compact view (recommended for daily use)
  - Compact summary
  - Minimalist mode (editor integration)
  - Chapters-only view
- Export formats:
  - JSON
  - CSV
  - HTML with styled reports
- Comparison features:
  - Save statistics snapshots
  - Compare with previous analyses
  - Track writing progress over time
- Achievement system:
  - Word count milestones
  - Motivational quotes from famous authors
  - Writing progress tracking
- Version checking:
  - Automatic update notifications from GitHub
  - Release information display
- File format support:
  - Markdown (.md, .markdown)
  - Plain text (.txt)
  - Word documents (.docx)
  - Rich Text Format (.rtf)
- Cross-platform executable builds:
  - Windows (x64)
  - Linux (x64)
  - macOS (x64)
- Comprehensive documentation
- GitHub Actions workflow for automated releases

### Technical
- Modular package structure with clear separation of concerns
- Type hints throughout the codebase
- Comprehensive docstrings
- PEP8 compliant code
- Error handling and graceful degradation
- Optional dependencies for extended features
- Beautiful Rich terminal UI
- Progress indicators for long operations

### Future Enhancements
- Export reports to PDF
- Word cloud visualization
- Character name frequency tracking
- Writing streak tracking
- Sentiment analysis
- Genre-specific benchmarks
- Time-of-day analysis for writing patterns

[1.0.0]: https://github.com/Tfc538/MuseStat/releases/tag/v1.0.0

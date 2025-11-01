# Changelog

All notable changes to MuseStat will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2025-11-01

### Added

#### Badge Generation System
- **Dynamic Badge Generation**: Generate beautiful, modern SVG and PNG badges for your manuscript
- **Multiple Badge Types**:
  - **Word Count Badge**: Shows total word count with emerald green gradient
  - **Achievement Badge**: Displays milestone achievements with vibrant blue gradient
  - **Chapters Badge**: Shows chapter count with purple/lavender gradient
  - **Reading Pages Badge**: Shows estimated page count with amber/gold gradient
- **Multiple Output Formats**:
  - SVG badges (~1.5 KB each): lightweight, scalable, perfect for web/README
  - PNG badges (~2–4 KB each): raster format for direct embedding
- **CLI Support**: 
  - `--badges` flag: comma-separated list (e.g., `--badges wordcount,achievement,chapters`)
  - `--badge-formats` flag: choose output formats (svg, png, or both)
  - `--badge-dir` flag: customize output directory (default: `./musestat/badges`)
- **Interactive Mode Support**:
  - Multi-select checkbox interface for badge types
  - Multi-select for output formats
  - Seamless integration with existing interactive TUI
- **Dependencies**: Added optional `cairosvg` for PNG conversion

### Technical
- New `musestat/io/badges.py` module with badge generation utilities
- Enhanced CLI argument parsing for badge options
- Interactive mode extended with questionary checkbox support
- SVG rendering with linearGradient, filter effects, and modern styling

## [1.2.1] - 2025-10-17

### Fixed
- **Version Update Notifications**: Fixed critical bug where update notifications were never displayed to users
  - The version check infrastructure existed but was never called in the CLI
  - Now displays beautiful panel notification when updates are available
  - Non-blocking, silent check with 24-hour caching
  - Shows current version, latest version, and download link

### Changed
- Updated all documentation references from v1.2.0 to v1.2.1
- Enhanced SECURITY.md with improved disclosure policy and version history section
- Improved cross-references between documentation files in CONTRIBUTING.md

## [1.2.0] - 2025-10-17

### Added

#### Display Customization CLI Options
- **`--top-words N`**: Specify number of most frequent words to display (default: 15)
- **`--max-chapters N`**: Limit number of chapters shown in detail view
- **`--min-word-length N`**: Set minimum word length for frequency analysis (default: 1)
- **`--sparkline-width N`**: Customize width of sparkline charts (default: 40)
- **`--hide-word-frequency`**: Hide the word frequency table from display
- **`--hide-heat-map`**: Hide the density heat map visualization
- **`--hide-chapter-details`**: Hide individual chapter breakdown table
- **`--show-top-chapters N`**: Display a summary table of the top N longest chapters

#### UI/UX Visual Enhancements
- **Sparkline Charts**: Inline sparklines showing chapter length trends in chapter breakdown table titles and chapter stats panel
- **Color-Coded Indicators**: Traffic light system (●) for readability scores
  - Green = Easy/Good
  - Yellow = Fair/Moderate
  - Red = Difficult/Needs Work
- **Trend Arrows**: Directional arrows (↑↓→) in comparison panels showing if metrics improved or declined
- **Visual Progress Bars**: Enhanced horizontal bars with unicode characters (█░) for visual progress representation
- **Chapter Balance Visualization**: Color-coded consistency indicators in chapter statistics panel
  - Very Consistent (CV < 15%): Green
  - Moderately Consistent (CV < 30%): Yellow
  - Variable (CV ≥ 30%): Red
- **Chapter Density Heat Maps**: Visual representation of word and sentence density across chapters
  - High density areas shown as █
  - Low density areas shown as ░
  - Helps identify pacing variations at a glance
- **Mini-Bars in Tables**: Visual bars added to chapter breakdown table for quick length comparison

### Improved
- Readability table now includes color-coded indicators for at-a-glance assessment
- Chapter stats panel now displays sparkline trends for chapter lengths
- Comparison panel now shows directional trend arrows for each metric
- Chapter breakdown table includes sparkline in title and mini-bars per chapter
- Enhanced visual feedback throughout the UI for better data comprehension

### Technical
- New `visualizations.py` module with reusable visualization components:
  - `create_sparkline()`: Generate unicode sparklines from data
  - `create_horizontal_bar()`: Create progress bars
  - `create_heat_map_line()`: Generate heat map visualizations
  - `get_readability_indicator()`: Color-code readability scores
  - `create_trend_arrow()`: Show metric trends with arrows
  - `create_chapter_balance_visualization()`: Visualize chapter consistency
  - Additional helper functions for charts and graphs

## [1.1.0] - 2025-10-17

### Added
- **Arrow key navigation** in interactive mode using questionary library
- Visual selection highlighting with custom styling
- Better keyboard navigation (↑↓ arrows + Enter to select)
- Graceful fallback to number input if questionary not available
- Project governance files:
  - CODE_OF_CONDUCT.md (Contributor Covenant v2.0)
  - CONTRIBUTING.md (development guidelines)
  - SECURITY.md (vulnerability reporting process)
  - GitHub issue templates (bug report, feature request, question)
  - Pull request template with comprehensive testing checklist
  - Issue template config with documentation links

### Improved
- Much more intuitive interactive TUI experience
- File selection with arrow keys instead of typing numbers
- Analysis type selection with visual highlighting
- Better first-time user onboarding

### Changed
- Contact information updated throughout project files
- Author details: Tim Gatzke <post@tim-gatzke.de>
- Website: tim-gatzke.de

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

[1.3.0]: https://github.com/Tfc538/MuseStat/releases/tag/v1.3.0
[1.2.1]: https://github.com/Tfc538/MuseStat/releases/tag/v1.2.1
[1.2.0]: https://github.com/Tfc538/MuseStat/releases/tag/v1.2.0
[1.1.0]: https://github.com/Tfc538/MuseStat/releases/tag/v1.1.0
[1.0.2]: https://github.com/Tfc538/MuseStat/releases/tag/v1.0.2
[1.0.1]: https://github.com/Tfc538/MuseStat/releases/tag/v1.0.1
[1.0.0]: https://github.com/Tfc538/MuseStat/releases/tag/v1.0.0

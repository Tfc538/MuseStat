# Contributing to MuseStat

Thank you for your interest in contributing to MuseStat! This document provides guidelines for contributing to the project.

## Code of Conduct

This project adheres to the Contributor Covenant [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the [existing issues](https://github.com/Tfc538/MuseStat/issues) to avoid duplicates.

When creating a bug report, include:
- **Description**: Clear description of the issue
- **Steps to Reproduce**: Detailed steps to reproduce the behavior
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Environment**: 
  - OS (Windows/Linux/macOS)
  - Python version (if running from source)
  - MuseStat version
- **Manuscript Details** (if relevant):
  - File format (.md, .txt, .docx, .rtf)
  - Approximate size
- **Screenshots**: If applicable

### Suggesting Features

Feature suggestions are welcome! Please:
- Check [existing feature requests](https://github.com/Tfc538/MuseStat/issues?q=is%3Aissue+label%3Aenhancement)
- Provide a clear description of the feature
- Explain why it would be useful for fiction writers
- Consider implementation complexity

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Follow the code style**:
   - PEP8 compliant
   - Type hints for function parameters and returns
   - Docstrings for all public functions and classes
   - Clear, descriptive variable names
3. **Test your changes**:
   - Test with various file formats (.md, .txt, .docx, .rtf)
   - Test with different manuscript sizes
   - Ensure all existing features still work
4. **Update documentation** if needed:
   - Update README.md for new features
   - Update CHANGELOG.md
   - Add/update docstrings
5. **Keep commits clean**:
   - Use conventional commit messages (feat:, fix:, docs:, etc.)
   - One logical change per commit
   - Descriptive commit messages

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/MuseStat.git
cd MuseStat

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install in editable mode
pip install -e .

# Run tests (when available)
pytest

# Run MuseStat
python main.py --help
```

## Project Structure

```
musestat/
├── core/         # Core analysis logic
├── features/     # Advanced features (readability, dialogue, etc.)
├── io/           # File readers and exporters
├── ui/           # Terminal UI components
├── utils/        # Utility functions
└── cli/          # Command-line interface
```

## Code Style Guidelines

- **Imports**: Organize as stdlib, third-party, local
- **Line Length**: Maximum 100 characters (soft limit)
- **Docstrings**: Use Google or NumPy style
- **Type Hints**: Use for all function parameters and returns
- **Error Handling**: Use specific exceptions, not bare `except`
- **Console Output**: Use Rich library for beautiful formatting

## Testing Guidelines

When adding new features:
- Test with manuscripts of varying sizes (small, medium, large)
- Test all supported file formats
- Test edge cases (empty files, very long chapters, etc.)
- Ensure error messages are helpful and clear
- Test both interactive and CLI modes

## Adding New Features

### For Analysis Features:
- Add to appropriate module in `features/`
- Update `core/analyzer.py` to integrate
- Add CLI flag if needed
- Update UI to display results
- Document in README.md

### For UI Components:
- Add to `ui/panels.py` or `ui/tables.py`
- Follow existing Rich UI patterns
- Ensure responsive to terminal width
- Test with different color schemes

## Commit Message Guidelines

Use conventional commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `perf:` Performance improvements
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Examples:
```
feat: Add character name frequency tracking
fix: Correct dialogue ratio calculation for curly quotes
docs: Update README with new --export-pdf option
perf: Optimize chapter detection for large manuscripts
```

## Questions?

Feel free to:
- Open an issue for questions
- Start a discussion in GitHub Discussions (if enabled)
- Check the [FAQ](docs/faq.md)

## License

By contributing, you agree that your contributions will be licensed under the same [MIT License](LICENSE) that covers the project.

---

Thank you for contributing to MuseStat! 🎉


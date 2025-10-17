---
name: Performance Issue
about: Report slow performance, high memory usage, or optimization opportunities
title: '[PERFORMANCE] '
labels: performance
assignees: ''
---

## Performance Issue

A clear description of the performance problem.

## Performance Impact

How does this affect your usage?
- [ ] Makes MuseStat unusable
- [ ] Significantly slows down analysis
- [ ] Causes system slowdown
- [ ] High memory consumption
- [ ] Takes longer than expected
- [ ] Minor inconvenience

## Environment

- **OS**: [e.g., Windows 11, Ubuntu 22.04, macOS 14]
- **MuseStat Version**: [run `musestat --version`]
- **Installation Method**: [executable / pip install / from source]
- **Python Version** (if from source): [e.g., 3.11]
- **System Specs**:
  - **CPU**: [e.g., Intel i7-10700K, AMD Ryzen 5 5600X]
  - **RAM**: [e.g., 16GB]
  - **Storage**: [HDD / SSD / NVMe]

## Manuscript Details

- **File Format**: [.md / .txt / .docx / .rtf]
- **File Size**: [e.g., 500KB, 2MB, 50MB]
- **Word Count**: [approximate, e.g., 50,000 words]
- **Number of Chapters**: [if applicable]
- **Special Characters**: [Unicode, emojis, non-English text, etc.]

## Command Used

```bash
# The exact command you ran
musestat -f mybook.docx --advanced
```

## Performance Metrics

### Timing
- **Actual Duration**: [e.g., 2 minutes 30 seconds]
- **Expected Duration**: [e.g., 30 seconds or less]
- **Operation**: [e.g., initial analysis, export, verification]

### Resource Usage
<!-- If you can measure these -->
- **Peak Memory**: [e.g., 4GB]
- **CPU Usage**: [e.g., 100% on all cores]
- **Disk I/O**: [Did disk usage spike?]

## Reproducibility

How often does this occur?
- [ ] Always with this specific file
- [ ] Always with files of this size
- [ ] Always with this file format
- [ ] Intermittently
- [ ] Only on first run
- [ ] Gets worse over time

## Steps to Reproduce

1. Prepare manuscript: [describe file]
2. Run command: [exact command]
3. Observe: [what happens]

## Comparison

Have you tested with:
- [ ] Smaller files (faster/slower?)
- [ ] Different file formats (faster/slower?)
- [ ] Different display modes (faster/slower?)
- [ ] Different flags/options (faster/slower?)

## Expected Performance

What performance would be acceptable?
<!-- e.g., "Should complete in under 10 seconds for a 50k word manuscript" -->

## Potential Causes

Do you have any insight into what might be causing this?
- [ ] Large file size
- [ ] Complex formatting
- [ ] Specific feature (dialogue analysis, readability, etc.)
- [ ] Export operation
- [ ] Memory leak
- [ ] Inefficient algorithm
- [ ] External dependencies
- [ ] No idea

## Profiling Data

If you've done any profiling, paste results here:

```
# Profiling output or observations
```

## Workarounds

Have you found any workarounds?

## Additional Context

<!-- Any other relevant information, logs, or observations -->

## Checklist

- [ ] I have tested with the latest version
- [ ] I have provided detailed performance metrics
- [ ] I have checked if this is a known issue
- [ ] I have described the expected performance



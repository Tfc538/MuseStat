---
name: Refactoring Suggestion
about: Suggest code improvements, better architecture, or technical debt reduction
title: '[REFACTOR] '
labels: refactoring, technical-debt
assignees: ''
---

## Refactoring Goal

What is the main objective of this refactoring?

<!-- Describe what you want to improve -->

## Current State

Describe the current implementation that needs refactoring.

### Affected Files/Modules

- `path/to/file.py`
- `path/to/another/file.py`

### Current Code

```python
# Paste relevant code that needs refactoring
# Or describe the current structure
```

## Issues with Current Implementation

What problems does the current code have?
- [ ] Code duplication
- [ ] Poor maintainability
- [ ] Unclear naming
- [ ] Too complex / needs simplification
- [ ] Violates SOLID principles
- [ ] Tight coupling
- [ ] Inefficient algorithm
- [ ] Poor type hints
- [ ] Missing docstrings
- [ ] Inconsistent patterns
- [ ] Technical debt
- [ ] Hard to test
- [ ] Other: ___________

## Proposed Refactoring

How should the code be restructured?

### Approach

<!-- Describe your proposed approach -->

### Proposed Code Structure

```python
# Show what the refactored code might look like
# Or outline the new structure
```

## Benefits

What improvements would this refactoring provide?
- [ ] Better readability
- [ ] Easier maintenance
- [ ] Improved performance
- [ ] Better testability
- [ ] Reduced complexity
- [ ] Better separation of concerns
- [ ] Easier to extend
- [ ] Consistent with project patterns
- [ ] Reduces technical debt
- [ ] Other: ___________

## Breaking Changes

Would this refactoring introduce breaking changes?
- [ ] No breaking changes
- [ ] Internal changes only (no API changes)
- [ ] Minor API changes
- [ ] Major API changes (would need major version bump)

If yes, describe:

## Testing Strategy

How should this refactoring be tested?
- [ ] Existing tests should still pass
- [ ] New unit tests needed
- [ ] Integration tests needed
- [ ] Manual testing required
- [ ] Performance benchmarks needed

## Implementation Plan

Suggested steps for implementing this refactoring:

1. 
2. 
3. 

## Scope

How extensive is this refactoring?
- [ ] Single function/method
- [ ] Single class
- [ ] Single module
- [ ] Multiple related modules
- [ ] Affects multiple features
- [ ] Large-scale architectural change

## Priority

How important is this refactoring?
- [ ] Low - nice to have
- [ ] Medium - would improve codebase
- [ ] High - significant technical debt
- [ ] Critical - blocking other improvements

## Risks

What are the potential risks of this refactoring?
- [ ] May introduce bugs
- [ ] Could break existing functionality
- [ ] Large scope, difficult to review
- [ ] Might affect performance
- [ ] Could confuse users if API changes
- [ ] Other: ___________

## Alternative Approaches

Are there alternative ways to achieve the same goal?

## Related Issues/PRs

<!-- Link to related issues or PRs -->

## Examples

Are there examples in the codebase of the pattern you're suggesting?
Or examples from other projects?

## Backwards Compatibility

If this would change APIs:
- [ ] Can provide deprecation warnings
- [ ] Can maintain backwards compatibility
- [ ] Would require breaking change
- [ ] Can create migration guide

## Documentation Impact

What documentation would need updating?
- [ ] Code comments/docstrings
- [ ] README
- [ ] User guide
- [ ] Contributing guide
- [ ] API documentation
- [ ] None

## Discussion

Do you want to discuss this before implementation?
- [ ] Would like feedback on approach
- [ ] Ready to implement if approved
- [ ] Just suggesting, not planning to implement
- [ ] Need help with implementation

## Checklist

- [ ] I have clearly described the current problem
- [ ] I have suggested a specific improvement
- [ ] I have considered the impact and risks
- [ ] I have checked if this aligns with project goals
- [ ] I have searched for similar refactoring suggestions



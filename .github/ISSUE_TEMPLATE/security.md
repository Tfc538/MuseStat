---
name: Security Vulnerability
about: Report a security vulnerability (PLEASE USE PRIVATE REPORTING FOR CRITICAL ISSUES)
title: '[SECURITY] '
labels: security
assignees: ''
---

<!-- 
⚠️ IMPORTANT: For critical security vulnerabilities, please use GitHub's private
vulnerability reporting feature instead of creating a public issue.

Go to: Security tab → Report a vulnerability

For non-critical security suggestions or general security improvements,
you can use this template.
-->

## Security Issue Type

What type of security concern is this?
- [ ] Code execution vulnerability
- [ ] Dependency vulnerability
- [ ] Information disclosure
- [ ] Path traversal
- [ ] Input validation issue
- [ ] Security best practice suggestion
- [ ] Documentation security clarification
- [ ] Other: ___________

## Severity Assessment

How severe do you consider this issue?
- [ ] Critical (immediate action required)
- [ ] High (significant impact)
- [ ] Medium (moderate impact)
- [ ] Low (minor concern)
- [ ] Informational (suggestion)

## Description

<!-- Provide a clear description of the security issue or suggestion -->

## Affected Component

- **Module**: [e.g., io/readers.py, features/verification.py]
- **Feature**: [e.g., file reading, export, CLI parsing]
- **Version**: [affected version(s)]

## Potential Impact

What could happen if this is exploited?
<!-- Describe potential attack scenarios and impact -->

## Steps to Reproduce (if applicable)

<!-- Only if this is safe to share publicly -->

1. 
2. 
3. 

## Proof of Concept

<!-- Only include if this is not a critical vulnerability -->

```python
# Example code demonstrating the issue (if safe to share)
```

## Suggested Mitigation

How could this be fixed or improved?

## References

<!-- Link to CVEs, security advisories, or relevant documentation -->

- 
- 

## Environment (if relevant)

- **MuseStat Version**: 
- **Python Version**: 
- **OS**: 
- **Installation Method**: 

## Discovery Method

How was this discovered?
- [ ] Code review
- [ ] Security scanner
- [ ] Dependency alert
- [ ] User report
- [ ] Security research
- [ ] Other: ___________

## Checklist

- [ ] I have not disclosed critical vulnerabilities publicly
- [ ] I have provided enough detail for the maintainers to understand the issue
- [ ] I have suggested potential mitigations
- [ ] I am willing to discuss this issue privately if needed

## Disclosure Timeline

If you have a disclosure timeline or deadline, please specify:

<!-- Note: We aim to address security issues promptly -->



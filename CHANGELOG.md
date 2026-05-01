# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-04-30

### Added
- Complete SHACL shapes (Person, Project, Action, Zet) following schema.org
- Multi-template support (`default`, `minimal`, `full`)
- `wiki init` command with `--list-templates` flag
- Framework test suite (21 tests across 4 test files)
- Ruff linter configuration and CI integration
- Mypy type checking configuration
- Documentation overhaul with badges and CLI reference
- `.pre-commit-config.yaml` for automated code quality checks

### Fixed
- Typos in pyproject.toml (hatchling build system)
- Mypy type errors in sparql and frontmatter modules
- SHACL validation now fails gracefully with warnings when no shapes exist
- CI workflows updated to use correct paths

### Changed
- SHACL validation returns True with warning instead of raising RuntimeError when no shapes
- Updated README with PyPI version badge, CI status badge, and License badge
- Improved CLI help text and documentation

### Security
- No security changes in this release

## [Unreleased]

### Planned
- `wiki sync` command for template updates from framework repo
- API reference documentation
- Performance caching for large wikis
- PyPI publication

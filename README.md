# wiki-framework

[![PyPI version](https://badge.fury.io/py/wiki-framework.svg)](https://pypi.org/project/wiki-framework/)
[![CI Status](https://github.com/EthanThatOneKid/wiki/actions/workflows/shacl-validation.yml/badge.svg)](https://github.com/EthanThatOneKid/wiki/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An opinionated, engine-agnostic, and agent-friendly wiki framework with SHACL validation and SPARQL querying.

## Overview

This framework provides the core architecture, rules, and skills for maintaining a structured knowledge base (Second Brain). It is designed to be used as a template or a shared core for personal wiki instances.

## Architecture

The framework follows a three-layer stack:
1. **`raw/`**: Immutable primary sources and atomic captures.
2. **`wiki/`**: Curated, evergreen knowledge records.
3. **`RULES.md`**: The "Operating System" — guidelines for human and AI collaboration.

## Core Features

- **Semantic Integrity**: Standardized JSON-LD frontmatter rooted in Schema.org.
- **SHACL Validation**: Enforces canonical schemas for Person, Project, Action, and CreativeWork types.
- **SPARQL Querying**: Query your wiki as an RDF graph with OWL-RL inference.
- **Agent-Ready**: Explicit guidelines and workflows for AI coding assistants.
- **Portable Skills**: Automations for dailies, ingestion, and link auditing.
- **Template System**: Scaffold new wiki instances with `wiki init`.

## Installation

### As a CLI tool
```bash
pip install wiki-framework
# or with uv
uv tool install wiki-framework
```

### As a project dependency
```bash
uv add wiki-framework
```

## Quickstart

### 1. Initialize a new wiki
```bash
python -m wiki init my-wiki
cd my-wiki
```

This creates:
- `wiki/` — Your knowledge base
- `shapes/` — SHACL shapes for validation
- `.github/workflows/shacl-validation.yml` — CI pipeline
- `pyproject.toml` — Project configuration

### 2. Create your first page
```bash
cat > wiki/hello.md << 'EOF'
---
"@context":
  "@vocab": "https://schema.org/"
"@type": Person
givenName: John
familyName: Doe
context: A friendly neighbor.
status: permanent
dateCreated: "2026-04-30"
---

# John Doe

Welcome to my wiki page!
EOF
```

### 3. Validate your wiki
```bash
python -m wiki shacl validate
# With detailed report:
python -m wiki shacl validate --verbose
# Summary view:
python -m wiki shacl validate --summary
```

### 4. Query your wiki
```bash
python -m wiki sparql "PREFIX schema: <https://schema.org/> SELECT ?name WHERE { ?s a schema:Person ; schema:givenName ?name }"
```

## CLI Reference

### `wiki init`
Initialize a new wiki from a template.
```bash
python -m wiki init [-t template-id] [-d target-dir]
```
- `-t, --template`: Template to use (default: `default`)
- `-d, --dir`: Target directory (default: current directory)

### `wiki shacl validate`
Validate wiki pages against SHACL shapes.
```bash
python -m wiki shacl validate [file] [--summary] [--verbose]
```
- `file`: Validate a single file (by name or path)
- `--summary`: Print per-file conformance summary
- `--verbose`: Print full validation report

### `wiki sparql`
Run SPARQL SELECT or CONSTRUCT queries.
```bash
python -m wiki sparql "query" [-f format] [-o output] [--construct] [--no-inference]
```
- `-f, --format`: Output format (table, json, csv, tsv, turtle, nt)
- `-o, --output`: Write output to file
- `--construct`: Shorthand for `-f turtle`
- `--no-inference`: Skip OWL-RL inference
- `--dry-run`: Load graph and print stats without querying

### `wiki frontmatter`
Frontmatter conversion and normalization.
```bash
python -m wiki frontmatter normalize [--dry-run]
python -m wiki frontmatter convert
```

## SHACL Shapes

The framework includes SHACL shapes for:
- **Person** (`schema:Person`): givenName, familyName, context, status, dateCreated
- **Project** (`schema:Project`): name, description, status, dateCreated
- **Action** (`schema:Action`): name, actionStatus, priority, dateCreated
- **CreativeWork/Zet** (`schema:CreativeWork`): name, keywords, dateCreated

Customize `shapes/*.ttl` to enforce your own schemas.

## Rules & Guidelines

See [RULES.md](RULES.md) for detailed guidelines on:
- Single Source of Truth (SSoT) principles
- Vault organization rules
- Semantic inference with OWL-RL
- Self-healing and link auditing
- Task management with Actions

## Examples

See the `examples/` directory for sample wiki pages:
- [person.md](examples/person.md) — Person record template
- [project.md](examples/project.md) — Project record template

## Development

```bash
git clone https://github.com/EthanThatOneKid/wiki.git
cd wiki
uv sync
uv run python -m wiki --help
```

Run tests:
```bash
uv run pytest
```

## License

MIT License — see [LICENSE](LICENSE) for details.

---

Managed by **EthanThatOneKid**

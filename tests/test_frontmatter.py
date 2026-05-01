"""Tests for frontmatter module."""

from pathlib import Path
from wiki.frontmatter import frontmatter_from_path, frontmatter_to_graph, normalize_all, convert_all


def test_frontmatter_from_path_valid(tmp_path):
    """Test parsing valid frontmatter from markdown file."""
    md_file = tmp_path / "test.md"
    content = """---
name: Test
"@type": Thing
---

# Test Page
"""
    md_file.write_text(content)
    
    data = frontmatter_from_path(md_file)
    assert data is not None
    assert "name" in data
    assert data["name"] == "Test"


def test_frontmatter_from_path_no_frontmatter(tmp_path):
    """Test parsing file without frontmatter."""
    md_file = tmp_path / "test.md"
    content = "# Test Page\n\nNo frontmatter here.\n"
    md_file.write_text(content)
    
    data = frontmatter_from_path(md_file)
    assert data is None


def test_frontmatter_to_graph():
    """Test converting frontmatter to RDF graph."""
    data = {
        "@type": "Thing",
        "name": "Test Page",
        "@id": "test"
    }
    
    graph = frontmatter_to_graph(data, file_id="test")
    triples = list(graph.triples((None, None, None)))
    assert len(triples) > 0


def test_normalize_all_dry_run(tmp_path):
    """Test normalize_all with dry_run flag."""
    wiki_dir = tmp_path / "wiki"
    wiki_dir.mkdir()
    
    # Create a file with non-canonical property
    md_file = wiki_dir / "test.md"
    content = """---
title: Test
---

# Test
"""
    md_file.write_text(content)
    
    results = normalize_all(wiki_dir=wiki_dir, dry_run=True)
    assert "fixed" in results
    assert results["fixed"] >= 0


def test_convert_all(tmp_path):
    """Test convert_all function."""
    wiki_dir = tmp_path / "wiki"
    wiki_dir.mkdir()
    
    # Create a file with frontmatter
    md_file = wiki_dir / "test.md"
    content = """---
name: Test
---

# Test
"""
    md_file.write_text(content)
    
    results = convert_all(wiki_dir=wiki_dir)
    assert "converted" in results
    assert "no_frontmatter" in results

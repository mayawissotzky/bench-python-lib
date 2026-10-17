from tabfmt import render, render_csv, render_markdown

ROWS = [{"name": "alpha", "size": 3}, {"name": "be", "size": None}]


def test_render_aligns_columns():
    lines = render(ROWS).splitlines()
    assert lines[0] == "name   size"
    assert lines[2] == "alpha  3"


def test_markdown_escapes_pipes():
    assert "a\\|b" in render_markdown([{"x": "a|b"}])


def test_csv_header():
    assert render_csv(ROWS).splitlines()[0] == "name,size"

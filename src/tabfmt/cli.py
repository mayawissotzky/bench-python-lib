import json
import sys

import click

from .render import render, render_csv, render_markdown

FORMATS = {"text": render, "md": render_markdown, "csv": render_csv}


@click.command()
@click.argument("source", default="-")
@click.option("--format", "fmt", type=click.Choice(sorted(FORMATS)), default="text")
def main(source, fmt):
    """Render a JSON array of objects from SOURCE (a file, a URL or - for stdin)."""
    if source.startswith(("http://", "https://")):
        from .remote import load_json

        rows = load_json(source)
    elif source == "-":
        rows = json.load(sys.stdin)
    else:
        with open(source, encoding="utf-8") as fh:
            rows = json.load(fh)
    click.echo(FORMATS[fmt](rows))

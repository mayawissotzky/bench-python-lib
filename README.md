# tabfmt

Render a list of dicts as an aligned plain-text, Markdown or CSV table.

```python
from tabfmt import render

print(render([{"name": "alpha", "size": 3}, {"name": "beta", "size": 12}]))
```

```
name   size
-----  ----
alpha  3
beta   12
```

## Install

```
pip install tabfmt            # library
pip install "tabfmt[cli]"     # adds the `tabfmt` command
pip install "tabfmt[http]"    # lets the command read from a URL
```

## Command line

```
tabfmt data.json --format md
cat data.json | tabfmt -
```

## Releasing

Bump the version in `pyproject.toml` and `src/tabfmt/__init__.py`, then run `scripts/release.sh`.

## License

MIT

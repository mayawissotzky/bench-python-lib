import csv
import io

from wcwidth import wcswidth


def _columns(rows):
    cols = []
    for row in rows:
        for key in row:
            if key not in cols:
                cols.append(key)
    return cols


def _cell(value):
    return "" if value is None else str(value)


def _pad(text, width):
    return text + " " * (width - max(wcswidth(text), 0))


def _widths(cols, rows):
    widths = {c: wcswidth(c) for c in cols}
    for row in rows:
        for c in cols:
            widths[c] = max(widths[c], wcswidth(_cell(row.get(c))))
    return widths


def render(rows, sep="  "):
    rows = list(rows)
    if not rows:
        return ""
    cols = _columns(rows)
    widths = _widths(cols, rows)
    lines = [sep.join(_pad(c, widths[c]) for c in cols).rstrip()]
    lines.append(sep.join("-" * widths[c] for c in cols))
    for row in rows:
        lines.append(sep.join(_pad(_cell(row.get(c)), widths[c]) for c in cols).rstrip())
    return "\n".join(lines)


def render_markdown(rows):
    rows = list(rows)
    if not rows:
        return ""
    cols = _columns(rows)
    out = ["| " + " | ".join(cols) + " |", "|" + "|".join("---" for _ in cols) + "|"]
    for row in rows:
        cells = (_cell(row.get(c)).replace("|", "\\|") for c in cols)
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def render_csv(rows):
    rows = list(rows)
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=_columns(rows), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()

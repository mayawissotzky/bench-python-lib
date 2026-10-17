import re
import sys

PREFIXES = ("feat", "fix", "docs", "chore", "refactor", "ci")

title = sys.argv[1] if len(sys.argv) > 1 else ""
if not re.match(r"^(%s)(\([\w-]+\))?: .+" % "|".join(PREFIXES), title):
    sys.exit("PR title must look like 'fix: short summary'")

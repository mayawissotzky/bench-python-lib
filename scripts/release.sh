#!/usr/bin/env bash
# Build and upload a release. Credentials come from ~/.pypirc.
set -euo pipefail

cd "$(dirname "$0")/.."
rm -rf dist build
python -m build
python -m twine check dist/*
python -m twine upload dist/*

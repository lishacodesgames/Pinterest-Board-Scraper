#!/usr/bin/env bash

set -e

# dirname gives the parent directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$REPO_ROOT"

# verify anyways
if [ ! -f ".gitignore" ]; then
   echo "ERROR: Repository root not found!"
   exit 1
fi

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Upgrading pip..."
.venv/bin/python -m pip install --upgrade pip

echo
echo "Setup complete"
echo
echo "To activate venv in your terminal instance, run:"
echo "source .venv/bin/activate"
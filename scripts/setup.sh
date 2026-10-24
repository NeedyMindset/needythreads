#!/usr/bin/env sh
# NeedyThreads setup for Mac and Linux: installs Python if missing, then the
# two packages the publishing layer needs, then saves your Publora keys in
# ~/.needythreads/.env. Safe to run again.
# Writing posts does not need any of this; only publishing and images do.
#
# Run from a terminal:  sh scripts/setup.sh

set -eu

root="$(cd "$(dirname "$0")/.." && pwd)"

if command -v python3 >/dev/null 2>&1; then
    echo "Python is already installed."
elif command -v brew >/dev/null 2>&1; then
    echo "Installing Python with Homebrew..."
    brew install python
else
    echo "Python 3 was not found. Install it from https://www.python.org/downloads/"
    echo "(Linux: your package manager, for example 'sudo apt install python3 python3-pip'),"
    echo "then run this script again."
    exit 1
fi

echo "Installing the Python packages..."
if [ -f "$root/requirements.txt" ]; then
    set -- -r "$root/requirements.txt"
else
    set -- "requests>=2.31.0" "python-dotenv>=1.2.4"
fi

if ! python3 -m pip install --quiet --user "$@" 2>/dev/null; then
    # Newer Python builds refuse a global install. Use a virtual environment.
    echo "Global install refused, using a virtual environment in .venv instead."
    python3 -m venv "$root/.venv"
    "$root/.venv/bin/python" -m pip install --quiet "$@"
    echo "Run the scripts with: $root/.venv/bin/python"
fi

py=python3
[ -x "$root/.venv/bin/python" ] && py="$root/.venv/bin/python"

echo ""
echo "Connecting Publora (press Enter to skip, posts then stay in draft mode)..."
"$py" "$root/scripts/configure_env.py" || true

echo ""
echo "Done. Python and the packages are ready."

#!/usr/bin/env bash
# Runs validate_archive.py with whichever Python the runner has: Windows
# images do not guarantee a working `python3`.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
# Git Bash on Windows would rewrite the --require regexes as POSIX paths.
export MSYS_NO_PATHCONV=1 MSYS2_ARG_CONV_EXCL='*'
script="$here/validate_archive.py"
command -v cygpath >/dev/null 2>&1 && script="$(cygpath -m "$script")"
for py in python3 python py; do
  if "$py" -c "import sys" >/dev/null 2>&1; then
    exec "$py" "$script" "$@"
  fi
done
echo "::error::no Python interpreter found to validate archives" >&2
exit 1

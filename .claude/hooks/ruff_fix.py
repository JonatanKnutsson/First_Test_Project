"""PostToolUse hook: format and lint-fix Python files Claude edits."""

import json
import subprocess
import sys

try:
    # utf-8-sig: tolerate a BOM (Windows PowerShell adds one when piping).
    payload = json.loads(sys.stdin.buffer.read().decode("utf-8-sig"))
    path = payload.get("tool_input", {}).get("file_path") or payload.get(
        "tool_response", {}
    ).get("filePath")

    if path and path.endswith(".py"):
        # Run ruff via this interpreter: it isn't on PATH in every shell.
        ruff = [sys.executable, "-m", "ruff"]
        subprocess.run([*ruff, "format", path])
        # F401 unfixable: don't strip an import Claude adds before using it.
        subprocess.run([*ruff, "check", "--fix", "--unfixable", "F401", path])
except Exception as e:
    # Exit 1 is a non-blocking hook error: reported, but never stops Claude.
    print(f"ruff_fix hook failed: {e}", file=sys.stderr)
    sys.exit(1)

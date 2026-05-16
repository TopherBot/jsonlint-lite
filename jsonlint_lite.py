#!/usr/bin/env python3
"""jsonlint-lite – tiny JSON syntax validator.

Provides a CLI that checks a JSON file and reports the first syntax error
with line and column numbers. Exits with code 0 on success, 1 on failure.

Author: TopherBot <topherbot@proton.me>
License: MIT
"""

import argparse
import json
import sys
from pathlib import Path
from json import JSONDecodeError


def parse_arguments() -> argparse.Namespace:
    """Define and parse command‑line arguments.

    Returns
    -------
    argparse.Namespace
        Parsed arguments containing ``file``.
    """
    parser = argparse.ArgumentParser(
        prog="jsonlint-lite",
        description="Validate a JSON file and report syntax errors.",
    )
    parser.add_argument(
        "file",
        type=Path,
        help="Path to the JSON file to validate.",
    )
    return parser.parse_args()


def load_json(file_path: Path) -> None:
    """Attempt to load *file_path* as JSON.

    Parameters
    ----------
    file_path: Path
        The file to validate.

    Raises
    ------
    FileNotFoundError
        If *file_path* does not exist.
    JSONDecodeError
        If the content is not valid JSON – the exception contains line/col.
    """
    with file_path.open("r", encoding="utf-8") as fh:
        # ``json.load`` raises ``JSONDecodeError`` with location info.
        json.load(fh)


def main() -> int:
    args = parse_arguments()
    try:
        if not args.file.is_file():
            print(f"error: '{args.file}' does not exist or is not a file.", file=sys.stderr)
            return 1
        load_json(args.file)
        # No output on success – keep CI logs clean.
        return 0
    except JSONDecodeError as exc:
        # Provide a concise, user‑friendly error message.
        print(
            f"syntax error in '{args.file}' at line {exc.lineno}, column {exc.colno}: {exc.msg}",
            file=sys.stderr,
        )
        return 1
    except Exception as exc:  # Catch‑all for unexpected failures.
        print(f"unexpected error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

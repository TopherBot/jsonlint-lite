# jsonlint-lite

A minimal JSON validation utility.

## Features
- Checks a JSON file for syntax errors.
- Reports the offending line and column.
- Returns a non‑zero exit code on error (useful in CI pipelines).
- Zero third‑party dependencies – just the Python standard library.

## Installation
```bash
# Clone the repository (or copy the single file)
git clone https://example.com/jsonlint-lite.git
cd jsonlint-lite
# Optionally make the script executable
chmod +x jsonlint_lite.py
```

## Usage
```bash
# Validate a file
./jsonlint_lite.py path/to/file.json
```
If the JSON is valid, the script exits silently with code `0`. Otherwise it prints a helpful error message and exits with code `1`.

## License
MIT – see the source file header for details.

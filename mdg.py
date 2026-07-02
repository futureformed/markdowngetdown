#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

from markitdown import MarkItDown

SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".doc"}


def convert_file(input_path: Path, output_path: Path | None) -> str:
    md = MarkItDown()
    result = md.convert(str(input_path))
    text = result.text_content

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text, encoding="utf-8")
        print(f"Converted: {input_path} -> {output_path}")
    else:
        print(text)

    return text


def cmd_convert(args):
    input_path = Path(args.input).resolve()

    if input_path.is_file():
        if input_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            print(f"Error: Unsupported file type '{input_path.suffix}'. Supported: {', '.join(SUPPORTED_EXTENSIONS)}", file=sys.stderr)
            sys.exit(1)

        if args.output:
            output_path = Path(args.output).resolve()
        else:
            output_path = input_path.with_suffix(".md")

        convert_file(input_path, output_path)

    elif input_path.is_dir():
        output_dir = Path(args.output).resolve() if args.output else input_path / "output"
        output_dir.mkdir(parents=True, exist_ok=True)

        files = sorted(f for f in input_path.iterdir() if f.suffix.lower() in SUPPORTED_EXTENSIONS)
        if not files:
            print(f"No supported files found in {input_path}", file=sys.stderr)
            sys.exit(1)

        for f in files:
            out = output_dir / f.with_suffix(".md").name
            convert_file(f, out)

        print(f"\nConverted {len(files)} file(s) -> {output_dir}")
    else:
        print(f"Error: '{input_path}' not found", file=sys.stderr)
        sys.exit(1)


def cmd_merge(args):
    input_files = []
    for p in args.files:
        path = Path(p).resolve()
        if path.is_dir():
            input_files.extend(sorted(path.glob("*.md")))
        elif path.is_file() and path.suffix.lower() == ".md":
            input_files.append(path)
        else:
            print(f"Warning: Skipping '{p}' (not a .md file or directory)", file=sys.stderr)

    if not input_files:
        print("Error: No Markdown files found to merge", file=sys.stderr)
        sys.exit(1)

    parts = []
    for f in input_files:
        content = f.read_text(encoding="utf-8").strip()
        parts.append(f"<!-- source: {f.name} -->\n\n{content}")

    merged = "\n\n---\n\n".join(parts) + "\n"

    if args.output:
        output_path = Path(args.output).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(merged, encoding="utf-8")
        print(f"Merged {len(input_files)} file(s) -> {output_path}")
    else:
        print(merged)


def main():
    parser = argparse.ArgumentParser(
        prog="mdg",
        description="Markdown Get Down - Convert PDF/DOCX to Markdown and merge Markdown files",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    convert_parser = subparsers.add_parser("convert", help="Convert PDF or DOCX to Markdown")
    convert_parser.add_argument("input", help="Input file or directory")
    convert_parser.add_argument("-o", "--output", help="Output file or directory (default: same name with .md extension)")

    merge_parser = subparsers.add_parser("merge", help="Merge multiple Markdown files")
    merge_parser.add_argument("files", nargs="+", help="Markdown files or directories to merge")
    merge_parser.add_argument("-o", "--output", help="Output file (default: print to stdout)")

    args = parser.parse_args()

    if args.command == "convert":
        cmd_convert(args)
    elif args.command == "merge":
        cmd_merge(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

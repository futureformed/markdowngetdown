# mdg (Markdown Get Down)

A lightweight CLI tool to convert PDF and Word documents to Markdown, and merge multiple Markdown files together.

No LLMs. No cloud APIs. Zero tokens burned. Just fast, local document conversion.

## Features

- **Convert PDF to Markdown** - preserves headings, lists, tables, and structure
- **Convert DOCX to Markdown** - maintains document formatting
- **Merge Markdown files** - combine multiple files with source markers and separators
- **Batch processing** - convert entire directories at once
- **Lightweight** - uses Microsoft's markitdown library, no heavy dependencies

## Installation

### Option 1: pipx (Recommended)

[pipx](https://pipx.pypa.io/) installs Python CLI tools in isolated environments and makes them globally available.

```bash
# Install pipx if you don't have it
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Install mdg
pipx install git+https://github.com/futureformed/markdowngetdown.git
```

### Option 2: pip

```bash
pip install git+https://github.com/futureformed/markdowngetdown.git
```

### Option 3: From source

```bash
git clone https://github.com/futureformed/markdowngetdown.git
cd markdowngetdown
pip install .
```

## Usage

### Convert a document

```bash
# Convert a PDF
mdg convert document.pdf

# Convert a Word document
mdg convert document.docx

# Specify output location
mdg convert document.pdf -o output.md

# Convert all documents in a folder
mdg convert ./documents/
```

### Merge Markdown files

```bash
# Merge specific files
mdg merge file1.md file2.md file3.md -o combined.md

# Merge all files in a folder
mdg merge ./chapters/ -o book.md

# Preview merged output (prints to screen)
mdg merge file1.md file2.md
```

## Examples

### Convert meeting notes and merge them

```bash
mdg convert ~/Documents/meetings/ -o ~/Documents/meetings-md/
mdg merge ~/Documents/meetings-md/ -o ~/Documents/all-meetings.md
```

### Batch convert reports

```bash
mdg convert ./reports/ -o ./reports-md/
mdg merge ./reports-md/Q1.md ./reports-md/Q2.md ./reports-md/Q3.md ./reports-md/Q4.md -o annual-report.md
```

## Uninstall

```bash
# If installed with pipx
pipx uninstall mdg

# If installed with pip
pip uninstall mdg
```

## Requirements

- Python 3.10 or higher
- macOS, Linux, or Windows

## How it works

mdg uses Microsoft's [markitdown](https://github.com/microsoft/markitdown) library for document conversion. It extracts text, preserves structure (headings, lists, tables), and outputs clean Markdown. No AI or LLM is involved - it's pure text extraction.

## Limitations

- Scanned/image-based PDFs may not convert well (no OCR)
- Complex formatting may require manual cleanup
- Only supports PDF and DOCX formats currently

## License

MIT

## Contributing

Issues and pull requests welcome at [github.com/futureformed/markdowngetdown](https://github.com/futureformed/markdowngetdown).

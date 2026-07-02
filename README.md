# mdg (Markdown Get Down)

A lightweight CLI tool to convert PDF and Word documents to Markdown, and merge multiple Markdown files together.

No LLMs. No cloud APIs. Zero tokens burned. Just fast, local document conversion.

## Features

- **Convert PDF to Markdown** - preserves headings, lists, tables, and structure
- **Convert DOCX to Markdown** - maintains document formatting
- **Merge Markdown files** - combine multiple files with source markers and separators
- **Batch processing** - convert entire directories at once
- **Lightweight** - uses Microsoft's markitdown library, no heavy dependencies

## Getting Started: Opening Terminal

If you've never used Terminal before, don't worry — it's simpler than it looks. Terminal is just a text-based way to give your computer instructions.

<img width="1610" height="1018" alt="terminal" src="https://github.com/user-attachments/assets/c04e18b3-fa97-4099-bce7-b4add017d8d9" />

### On Mac

1. Press **Command + Space** to open Spotlight Search
2. Type **Terminal**
3. Press **Enter** or click on Terminal.app

A window will open with a blinking cursor. That's your terminal — you're ready to type commands.

### On Windows

1. Press the **Windows key** on your keyboard
2. Type **cmd** or **PowerShell**
3. Press **Enter**

A window will open with a blinking cursor. That's your terminal — you're ready to type commands.

**Tip:** You can also right-click the Start button and select "Windows PowerShell" or "Terminal".

### How to use Terminal

- **Type a command** and press **Enter** to run it
- **Copy/paste** works normally (Command+C/V on Mac, Ctrl+C/V on Windows)
- **To stop a command** that's running, press **Ctrl+C**
- **To clear the screen**, type `clear` (Mac) or `cls` (Windows) and press Enter

That's it! You're ready to install and use mdg.

## Installation

### Prerequisites

You need Python 3.10 or higher installed on your computer.

**Check if you have Python:**
```bash
python --version
```

If you see "Python 3.10" or higher, you're good. If not:
- **Mac:** Download from [python.org](https://www.python.org/downloads/) or run `brew install python`
- **Windows:** Download from [python.org](https://www.python.org/downloads/) (check "Add Python to PATH" during installation)

### Option 1: pipx (Recommended)

[pipx](https://pipx.pypa.io/) installs Python CLI tools in isolated environments and makes them globally available.

```bash
# Install pipx if you don't have it
python -m pip install --user pipx
python -m pipx ensurepath

# Restart your terminal, then install mdg
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

### Verify installation

After installing, close and reopen your terminal, then run:
```bash
mdg --help
```

If you see usage information, you're ready to go!

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

**Mac/Linux:**
```bash
mdg convert ~/Documents/meetings/ -o ~/Documents/meetings-md/
mdg merge ~/Documents/meetings-md/ -o ~/Documents/all-meetings.md
```

**Windows:**
```powershell
mdg convert C:\Users\YourName\Documents\meetings\ -o C:\Users\YourName\Documents\meetings-md\
mdg merge C:\Users\YourName\Documents\meetings-md\ -o C:\Users\YourName\Documents\all-meetings.md
```

### Batch convert reports

```bash
mdg convert ./reports/ -o ./reports-md/
mdg merge ./reports-md/Q1.md ./reports-md/Q2.md ./reports-md/Q3.md ./reports-md/Q4.md -o annual-report.md
```

## Troubleshooting

### "mdg: command not found" (Mac/Linux) or "'mdg' is not recognized" (Windows)

This means mdg isn't in your system PATH. Try these steps:

1. **Close and reopen your terminal** — sometimes PATH changes need a fresh terminal
2. **Check if pipx installed correctly:**
   ```bash
   pipx list
   ```
   You should see `mdg` in the list
3. **Reinstall with pip instead:**
   ```bash
   pip install git+https://github.com/futureformed/markdowngetdown.git
   ```

### "python: command not found" (Mac/Linux) or "'python' is not recognized" (Windows)

Python isn't installed or isn't in your PATH:
- **Mac:** Run `brew install python` or download from [python.org](https://www.python.org/downloads/)
- **Windows:** Download from [python.org](https://www.python.org/downloads/) and **make sure to check "Add Python to PATH"** during installation, then restart your terminal

### Permission errors on Mac/Linux

If you get permission errors, try adding `--user` to pip commands:
```bash
pip install --user git+https://github.com/futureformed/markdowngetdown.git
```

### Windows: "Execution Policy" error in PowerShell

If you see an error about execution policy, run this command first:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try installing again.

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

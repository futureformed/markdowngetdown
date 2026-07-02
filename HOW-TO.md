# Markdown Get Down (mdg) - How To Guide

A lightweight tool to convert PDF and Word documents to Markdown, and merge multiple Markdown files together.

---

## What This Tool Does

**Convert documents to Markdown:**
- PDF files → Markdown
- Word documents (.docx, .doc) → Markdown

**Merge Markdown files:**
- Combine multiple `.md` files into one
- Adds source file markers and separators between files

---

## Setup (One-Time Only)

### Step 1: Open Terminal

Open the Terminal app on your Mac.

### Step 2: Navigate to the project folder

```bash
cd ~/Documents/development/markdowngetdown
```

### Step 3: Activate the virtual environment

Every time you want to use the tool, you need to activate its environment first:

```bash
source .venv/bin/activate
```

You'll know it worked when you see `(.venv)` at the start of your terminal prompt.

### Step 4: Verify it's working

```bash
python mdg.py --help
```

You should see usage information displayed.

---

## How to Convert Documents

### Convert a single PDF

```bash
python mdg.py convert /path/to/document.pdf
```

This creates `document.md` in the same folder as the PDF.

### Convert a single Word document

```bash
python mdg.py convert /path/to/document.docx
```

This creates `document.md` in the same folder as the DOCX.

### Specify a custom output location

```bash
python mdg.py convert /path/to/document.pdf -o /path/to/output/result.md
```

### Convert all documents in a folder

```bash
python mdg.py convert /path/to/folder
```

This converts all PDF and DOCX files in the folder and saves them to a subfolder called `output`.

### Convert all documents to a specific folder

```bash
python mdg.py convert /path/to/folder -o /path/to/results
```

---

## How to Merge Markdown Files

### Merge specific files

```bash
python mdg.py merge file1.md file2.md file3.md -o combined.md
```

This creates `combined.md` with all three files merged together.

### Merge all files in a folder

```bash
python mdg.py merge /path/to/folder -o combined.md
```

This merges all `.md` files in the folder (sorted alphabetically) into `combined.md`.

### Preview merged output without saving

```bash
python mdg.py merge file1.md file2.md
```

This prints the merged content to the screen instead of saving to a file.

---

## Real-World Examples

### Example 1: Convert meeting notes and merge them

```bash
# Convert all meeting PDFs to Markdown
python mdg.py convert ~/Documents/meetings -o ~/Documents/meetings-md

# Merge them into one file
python mdg.py merge ~/Documents/meetings-md -o ~/Documents/all-meetings.md
```

### Example 2: Convert a contract and review it

```bash
# Convert the contract
python mdg.py convert ~/Downloads/contract.pdf -o ~/Desktop/contract.md

# Open it in your text editor
open ~/Desktop/contract.md
```

### Example 3: Batch convert and merge reports

```bash
# Convert all quarterly reports
python mdg.py convert ~/Documents/reports -o ~/Documents/reports-md

# Merge them chronologically
python mdg.py merge ~/Documents/reports-md/Q1.md ~/Documents/reports-md/Q2.md ~/Documents/reports-md/Q3.md ~/Documents/reports-md/Q4.md -o ~/Documents/annual-report.md
```

---

## Understanding the Output

### Converted files

When you convert a document, the tool:
- Preserves headings, lists, and tables
- Extracts text content
- Maintains document structure
- Saves as clean Markdown

### Merged files

When you merge files, the tool:
- Adds a comment showing the source filename: `<!-- source: filename.md -->`
- Separates each file with a horizontal rule: `---`
- Preserves all original content exactly

Example merged output:
```markdown
<!-- source: chapter1.md -->

# Chapter 1

Content here...

---

<!-- source: chapter2.md -->

# Chapter 2

More content...
```

---

## Troubleshooting

### "command not found: python"

Make sure you've activated the virtual environment:
```bash
source .venv/bin/activate
```

### "No module named 'markitdown'"

The dependencies aren't installed. Reinstall them:
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### "Unsupported file type"

The tool only supports `.pdf`, `.docx`, and `.doc` files. Other formats (like `.pptx`, `.xlsx`) are not currently supported.

### "No supported files found"

The folder you specified doesn't contain any PDF or DOCX files. Check the path and try again.

### Conversion quality is poor

Some PDFs (especially scanned documents or image-based PDFs) may not convert well. This tool uses text extraction, not OCR. For scanned documents, you'd need a different approach.

---

## Tips

1. **Always activate the virtual environment** before running commands
2. **Use absolute paths** (starting with `/` or `~`) to avoid confusion
3. **Batch convert folders** instead of individual files when possible
4. **Check the output** after conversion - complex documents may need manual cleanup
5. **Merge in order** - files are merged in the order you specify them

---

## Quick Reference

| Task | Command |
|------|---------|
| Convert one PDF | `python mdg.py convert file.pdf` |
| Convert one DOCX | `python mdg.py convert file.docx` |
| Convert with custom output | `python mdg.py convert file.pdf -o output.md` |
| Convert entire folder | `python mdg.py convert /path/to/folder` |
| Merge specific files | `python mdg.py merge a.md b.md -o combined.md` |
| Merge folder contents | `python mdg.py merge /path/to/folder -o combined.md` |
| Get help | `python mdg.py --help` |

---

## Need More Help?

Run the help command to see all options:
```bash
python mdg.py --help
python mdg.py convert --help
python mdg.py merge --help
```

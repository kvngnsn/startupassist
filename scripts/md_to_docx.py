#!/usr/bin/env python3
"""Convert a startupassist Markdown draft into a Word (.docx) document.

  python3 scripts/md_to_docx.py draft.md [-o draft.docx] [--keep-notes]

Formatting follows common law-firm conventions: Times New Roman 12 pt, 1-inch
margins, justified body text, centered bold title and article headings,
run-in bold section captions, and page numbers centered in the footer.

If the file is a template (it has a "## Form" heading), only the form is
converted. Drafting and Verify notes are dropped unless --keep-notes is given,
in which case they are kept as shaded italic paragraphs for review drafts.
A Markdown horizontal rule ("---" on its own line) becomes a page break.

Requires python-docx (pip install python-docx).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches, Pt, RGBColor
except ImportError:  # pragma: no cover
    sys.exit("python-docx is required: pip install python-docx")

FONT = "Times New Roman"
INLINE_RE = re.compile(r"(\*\*\*.+?\*\*\*|\*\*.+?\*\*|\*(?!\s).+?\*|`.+?`)")


def strip_template(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            text = text[end + 4:]
    m = re.search(r"^##\s+Form\s*$", text, re.M)
    if m:
        text = text[m.end():]
        text = re.sub(r"^\s*---\s*\n", "", text, count=1)  # rule right after "## Form"
    return text


def add_runs(par, text: str, italic: bool = False) -> None:
    text = text.replace("\\*", "*").replace("\\_", "_")
    for piece in INLINE_RE.split(text):
        if not piece:
            continue
        if piece.startswith("***") and piece.endswith("***"):
            run = par.add_run(piece[3:-3]); run.bold = True; run.italic = True
        elif piece.startswith("**") and piece.endswith("**"):
            run = par.add_run(piece[2:-2]); run.bold = True
        elif piece.startswith("`") and piece.endswith("`"):
            run = par.add_run(piece[1:-1])
        elif piece.startswith("*") and piece.endswith("*") and len(piece) > 2:
            run = par.add_run(piece[1:-1]); run.italic = True
        else:
            run = par.add_run(piece)
        if italic:
            run.italic = True


def shade(par, fill: str = "EDEDED") -> None:
    ppr = par._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    ppr.append(shd)


def add_page_number_footer(doc) -> None:
    for section in doc.sections:
        par = section.footer.paragraphs[0]
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = par.add_run()
        for tag, text in (("begin", None), (None, "PAGE"), ("end", None)):
            if tag:
                el = OxmlElement("w:fldChar"); el.set(qn("w:fldCharType"), tag)
            else:
                el = OxmlElement("w:instrText"); el.set(qn("xml:space"), "preserve"); el.text = text
            run._r.append(el)


def setup(doc) -> None:
    style = doc.styles["Normal"]
    style.font.name = FONT
    style.font.size = Pt(12)
    style.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    style.paragraph_format.space_after = Pt(8)
    style.paragraph_format.space_before = Pt(0)
    for section in doc.sections:
        section.left_margin = section.right_margin = Inches(1)
        section.top_margin = section.bottom_margin = Inches(1)


def add_table(doc, rows: list[str]) -> None:
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    cells = [r for r in cells if not all(re.fullmatch(r":?-{2,}:?", c) for c in r if c)]
    if not cells:
        return
    width = max(len(r) for r in cells)
    table = doc.add_table(rows=len(cells), cols=width)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, row in enumerate(cells):
        for j in range(width):
            par = table.cell(i, j).paragraphs[0]
            par.paragraph_format.space_after = Pt(2)
            add_runs(par, row[j] if j < len(row) else "")
            if i == 0:
                for run in par.runs:
                    run.bold = True
    doc.add_paragraph()


def convert(md: str, keep_notes: bool) -> "Document":
    doc = Document()
    setup(doc)
    lines = md.splitlines()
    i, first_heading = 0, True
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                par = doc.add_paragraph()
                par.paragraph_format.space_after = Pt(0)
                run = par.add_run(lines[i]); run.font.name = "Courier New"; run.font.size = Pt(10)
                i += 1
            i += 1
            continue

        if not stripped:
            i += 1
            continue

        if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", stripped):
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
            i += 1
            continue

        if stripped.startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i]); i += 1
            add_table(doc, block)
            continue

        if stripped.startswith(">"):
            block = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                block.append(lines[i].strip()[1:].strip()); i += 1
            if keep_notes:
                par = doc.add_paragraph()
                add_runs(par, " ".join(block), italic=True)
                shade(par)
                for run in par.runs:
                    run.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
            continue

        m = re.match(r"(#{1,6})\s+(.*)", stripped)
        if m:
            level, text = len(m.group(1)), m.group(2).strip()
            par = doc.add_paragraph()
            par.paragraph_format.keep_with_next = True
            par.paragraph_format.space_before = Pt(12 if level > 1 else 0)
            if level <= 2:
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_runs(par, text)
            for run in par.runs:
                run.bold = True
                if level == 1 and first_heading:
                    run.font.size = Pt(14)
            first_heading = False
            i += 1
            continue

        m = re.match(r"(\s*)([-*+]|\d+[.)]|\([a-zA-Z0-9]+\))\s+(.*)", line)
        if m and (m.group(2) in "-*+" or re.match(r"\d+[.)]", m.group(2))) and not stripped.startswith("**"):
            indent = len(m.group(1).replace("\t", "    ")) // 2
            marker = "•" if m.group(2) in "-*+" else m.group(2)
            par = doc.add_paragraph()
            par.paragraph_format.left_indent = Inches(0.5 + 0.25 * indent)
            par.paragraph_format.first_line_indent = Inches(-0.25)
            par.paragraph_format.space_after = Pt(4)
            add_runs(par, f"{marker}\t{m.group(3)}")
            i += 1
            continue

        # Ordinary paragraph: join soft-wrapped lines until a blank line or block start.
        block = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or re.match(r"(#{1,6}\s|>|\||```|[-*+]\s|\d+[.)]\s|-{3,}$)", nxt):
                break
            if lines[i - 1].endswith("  ") or lines[i - 1].endswith("\\"):
                block.append("\n" + nxt)
            else:
                block.append(" " + nxt)
            i += 1
        text = "".join(block).replace("\\\n", "\n")
        par = doc.add_paragraph()
        is_signature = bool(re.search(r"_{5,}|^By:|^Name:|^Title:", text))
        par.alignment = WD_ALIGN_PARAGRAPH.LEFT if is_signature else WD_ALIGN_PARAGRAPH.JUSTIFY
        if re.match(r"\((?:[a-z]{1,4}|[ivx]+|[A-Z])\)\s", text):
            par.paragraph_format.left_indent = Inches(0.5)
        for k, chunk in enumerate(text.split("\n")):
            if k:
                par.add_run().add_break()
            add_runs(par, chunk)
    add_page_number_footer(doc)
    return doc


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", type=Path)
    ap.add_argument("-o", "--output", type=Path)
    ap.add_argument("--keep-notes", action="store_true", help="keep drafting/verify notes as shaded text")
    args = ap.parse_args()
    md = strip_template(args.input.read_text(encoding="utf-8"))
    out = args.output or args.input.with_suffix(".docx")
    convert(md, args.keep_notes).save(out)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

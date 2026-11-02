#!/usr/bin/env python3
"""Check startupassist drafts and templates.

Finished-draft mode (default) flags anything that must not survive into a
document sent for signature: unfilled {{variables}}, unresolved [[options]],
drafting notes, Verify notes, leftover template scaffolding, broken section
cross-references, and defined-term problems.

  python3 scripts/check_document.py draft.md [more.md ...]

With several files it also prints a fact sheet (entity names, share counts,
prices, dates) per file so numbers can be compared across a document set.

Template mode lints the template library itself:

  python3 scripts/check_document.py --template templates/**/*.md

Exit status is 1 if any error is found, else 0. Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

VAR_RE = re.compile(r"\{\{\s*([A-Za-z0-9_\.]+)\s*\}\}")
OPTION_RE = re.compile(r"\[\[(.{0,80}?)(?::|\]\])", re.S)
NOTE_RE = re.compile(r"^\s*>\s*\*\*(Drafting note|Verify):?\*\*", re.I | re.M)
DEF_RE = re.compile(r"[\"“]\*\*([A-Z][^*\"”]{0,80}?)\*\*[\"”]")
SECTION_HEAD_RE = re.compile(
    r"^(?:\[\[(?:Optional|Alternative[^:]*):\s*)?"
    r"(?:#{1,6}\s+(?:ARTICLE\s+|Section\s+)?|\*\*(?:Section\s+)?)"
    r"(\d+(?:\.\d+)*)[\.\s]",
    re.M,
)
ARTICLE_HEAD_RE = re.compile(r"^#{1,6}\s+ARTICLE\s+([IVXLC]+|\d+)\b", re.M)
SECTION_REF_RE = re.compile(r"\bSections?\s+(\d+(?:\.\d+)*)(?:\(([a-z]{1,3})\))?")
FRONT_KEYS = ["id", "title", "category", "stage", "signers", "authorities",
              "use_when", "do_not_use_when", "related", "sources", "last_verified"]

ENTITY_RE = re.compile(r"\b([A-Z][\w&.,'\- ]{1,60}?,\s+(?:Inc\.|Corp\.|Corporation|L\.P\.|LLC|L\.L\.C\.|Ltd\.))")
SHARES_RE = re.compile(r"\b(\d{1,3}(?:,\d{3})+|\d+)\s+shares\b")
MONEY_RE = re.compile(r"\$\s?\d[\d,]*(?:\.\d+)?(?:\s(?:million|billion))?")
DATE_RE = re.compile(
    r"\b(?:January|February|March|April|May|June|July|August|September|October|"
    r"November|December)\s+\d{1,2},\s+\d{4}\b")


def split_front_matter(text: str) -> tuple[str, str]:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[4:end], text[end + 4:]
    return "", text


def form_part(text: str) -> str:
    """Return the text after '## Form' if present, else the whole body."""
    m = re.search(r"^##\s+Form\s*$", text, re.M)
    return text[m.end():] if m else text


def strip_code(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


class Report:
    def __init__(self, path: Path):
        self.path = path
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def print(self) -> None:
        status = "FAIL" if self.errors else ("WARN" if self.warnings else "OK")
        print(f"\n[{status}] {self.path}")
        for e in self.errors:
            print(f"  error: {e}")
        for w in self.warnings:
            print(f"  warn:  {w}")


def check_cross_references(body: str, rep: Report) -> None:
    defined = set(SECTION_HEAD_RE.findall(body))
    for art in ARTICLE_HEAD_RE.findall(body):
        defined.add(art)
    if not defined:
        return
    missing = Counter()
    for m in SECTION_REF_RE.finditer(body):
        num = m.group(1)
        # "Section 83(b) of the Code", "Section 4.2 of the Restated Certificate":
        # a reference followed by "of <something other than this>" points to
        # another instrument or a statute, not to this document.
        tail = body[m.end():m.end() + 60]
        if re.match(r"(?:\([a-zA-Z0-9]+\))*,?\s+of\s+(?!this\b)", tail):
            continue
        if int(num.split(".")[0]) > 60:  # bare statutory cite, e.g. "Section 141(f)"
            continue
        if num not in defined:
            missing[num] += 1
    for num, count in sorted(missing.items()):
        rep.warn(f"cross-reference to Section {num} ({count}x) but no such section heading found")


def check_defined_terms(body: str, rep: Report) -> None:
    defs = DEF_RE.findall(body)
    counts = Counter(defs)
    for term, n in counts.items():
        if n > 1:
            rep.warn(f'defined term "{term}" is defined {n} times')
    for term in counts:
        uses = len(re.findall(r"\b" + re.escape(term) + r"\b", body))
        if uses <= counts[term]:
            rep.warn(f'defined term "{term}" is never used after its definition')


def check_finished(path: Path) -> Report:
    rep = Report(path)
    text = path.read_text(encoding="utf-8")
    front, body = split_front_matter(text)
    if front:
        rep.error("YAML front matter still present (remove template scaffolding)")
    for heading in ("## About this template", "## Drafting inputs"):
        if heading in body:
            rep.error(f'template section "{heading}" still present')
    scan = strip_code(body)
    for m in VAR_RE.finditer(scan):
        rep.error(f"line {line_of(scan, m.start())}: unfilled variable {{{{{m.group(1)}}}}}")
    for m in re.finditer(r"\[\[", scan):
        snippet = scan[m.start():m.start() + 50].split("\n")[0]
        rep.error(f"line {line_of(scan, m.start())}: unresolved option {snippet}...")
    for m in NOTE_RE.finditer(scan):
        rep.error(f"line {line_of(scan, m.start())}: '{m.group(1)}' note left in document")
    for m in re.finditer(r"\[(?:●|•|___+|\s*\])", scan):
        rep.warn(f"line {line_of(scan, m.start())}: bracketed blank left in document")
    check_cross_references(scan, rep)
    check_defined_terms(scan, rep)
    return rep


def check_template(path: Path) -> Report:
    rep = Report(path)
    text = path.read_text(encoding="utf-8")
    front, body = split_front_matter(text)
    if not front:
        rep.error("missing YAML front matter")
    else:
        for key in FRONT_KEYS:
            if not re.search(rf"^{key}\s*:", front, re.M):
                rep.error(f"front matter missing '{key}'")
        m = re.search(r"^id\s*:\s*(\S+)", front, re.M)
        if m and m.group(1).strip("'\"") != path.stem:
            rep.error(f"front matter id '{m.group(1)}' does not match file name '{path.stem}'")
    for heading in ("## About this template", "## Drafting inputs", "## Form"):
        if not re.search(rf"^{re.escape(heading)}\s*$", body, re.M):
            rep.error(f'missing section "{heading}"')
    form = strip_code(form_part(body))
    inputs_m = re.search(r"^## Drafting inputs\s*$(.*?)^## Form\s*$", body, re.M | re.S)
    documented = set(VAR_RE.findall(inputs_m.group(1))) if inputs_m else set()
    documented |= set(re.findall(r"`([a-z][a-z0-9_]+)`", inputs_m.group(1))) if inputs_m else set()
    used = set(VAR_RE.findall(form))
    undocumented = sorted(v for v in used if v not in documented and v.split(".")[0] not in documented)
    if undocumented:
        rep.warn("variables used in form but not in Drafting inputs: " + ", ".join(undocumented[:25])
                 + (" ..." if len(undocumented) > 25 else ""))
    opens, closes = form.count("[["), form.count("]]")
    if opens != closes:
        rep.error(f"unbalanced option brackets: {opens} '[[' vs {closes} ']]'")
    if re.search(r"(remaining|other) provisions omitted|insert (standard )?boilerplate", form, re.I):
        rep.error("form contains an omission placeholder")
    check_cross_references(form, rep)
    words = len(re.findall(r"\w+", form))
    if words < 300:
        rep.warn(f"form is short ({words} words)")
    return rep


def fact_sheet(paths: list[Path]) -> None:
    print("\nFact sheet (compare across the document set):")
    facts: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for p in paths:
        body = form_part(split_front_matter(p.read_text(encoding="utf-8"))[1])
        for label, rx in (("entities", ENTITY_RE), ("share counts", SHARES_RE),
                          ("amounts", MONEY_RE), ("dates", DATE_RE)):
            for m in rx.finditer(body):
                facts[label][m.group(1) if m.groups() else m.group(0)].add(p.name)
    for label in ("entities", "share counts", "amounts", "dates"):
        if not facts[label]:
            continue
        print(f"\n  {label}:")
        for value, files in sorted(facts[label].items()):
            print(f"    {value.strip():<45} {', '.join(sorted(files))}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--template", action="store_true", help="lint template files instead of finished drafts")
    ap.add_argument("--quiet", action="store_true", help="print only files with errors")
    args = ap.parse_args()

    paths = [p for p in args.files if p.suffix == ".md" and p.is_file()]
    failed = 0
    for p in paths:
        rep = check_template(p) if args.template else check_finished(p)
        failed += bool(rep.errors)
        if not args.quiet or rep.errors:
            rep.print()
    if not args.template and len(paths) > 1:
        fact_sheet(paths)
    print(f"\n{len(paths)} file(s) checked, {failed} with errors.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

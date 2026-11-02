# Drafting Conventions

Every template and reference file in this skill follows these rules. When Claude drafts from a template, the finished document must also satisfy the "Finished document" rules at the end.

## 1. File layout of a template

Each template is one Markdown file with four parts, in this order.

### 1.1 YAML front matter

```yaml
---
id: founder-stock-purchase-agreement        # kebab-case, equals the file name without .md
title: Founder Restricted Stock Purchase Agreement
category: founders                          # the folder name
stage: formation                            # formation | hiring | equity | convertible | priced-round | governance | compliance | commercial
signers: [Company (by an officer), Purchaser, Purchaser's spouse (community property states)]
authorities:                                # controlling law; cite the section, not just the act
  - "8 Del. C. § 152 (consideration for stock)"
  - "26 U.S.C. § 83(b); Treas. Reg. § 1.83-2"
use_when: One sentence.
do_not_use_when: One sentence (and what to use instead).
related: [initial-board-consent, 83b-election-package, technology-assignment-agreement]
sources:                                    # what was consulted and how it was used
  - name: "Cooley GO — Founder Stock Purchase Agreement (reference only; not copied)"
    url: https://www.cooleygo.com/...
last_verified: 2026-11-02
---
```

### 1.2 `## About this template`

Written for Claude as the drafter, at the level of a senior associate's notes to a junior one. Cover, as relevant:

- What the document does and where it sits in the transaction (what must be signed before or after it).
- Statutory and regulatory requirements it must satisfy, with pin cites.
- The key business decisions and the **market position** on each (company-favorable, neutral/market, investor- or employee-favorable), and which this form defaults to.
- State-specific variations (California, New York, Washington, Massachusetts, Illinois and others where they matter).
- Common mistakes and how the form avoids them.
- Filing, notice, and tax deadlines that the signing triggers.

### 1.3 `## Drafting inputs`

A table of every `{{variable}}` in the form: `| Variable | Meaning | Example | Notes |`. Reuse the shared names in [variables.md](variables.md) wherever one fits. New names must be descriptive snake_case.

### 1.4 `## Form`

The document itself, after a `---` rule. Everything below `## Form` is the draft that gets filled in and signed.

## 2. Markup inside the form

| Markup | Meaning | Before signing |
|---|---|---|
| `{{variable_name}}` | Fill-in value | Replace every one |
| `[[Optional: text]]` | Include or delete | Resolve every one |
| `[[Alternative A: text]]` `[[Alternative B: text]]` | Choose exactly one | Resolve every one |
| `> **Drafting note:** text` | Guidance for the drafter | Delete |
| `> **Verify:** text` | A point of law or practice to confirm against current authority before use | Confirm, then delete |

`scripts/check_document.py` flags any of these left in a finished draft. Do not use bare `[ ]` brackets for fill-ins; reserve single brackets for ordinary legal text.

## 3. Drafting style (big-law standard)

- **Structure.** `# TITLE` for the document title. `## ARTICLE 1` / `## 1. Heading` for articles or top-level sections. Subsections are run-in paragraphs: `**1.1 Sale and Issuance.** Text…`, then `(a)`, `(i)`, `(A)`. Keep numbering continuous and every cross-reference correct.
- **Defined terms.** Define once, in bold inside quotes and parentheses: `(the "**Company**")`, or in a Definitions section. Capitalize every later use. Never use a capitalized term you did not define. Never define a term you do not use.
- **Obligation words.** "shall" imposes a duty, "may" grants discretion, "will" states future fact, "must" states a condition. Do not use "and/or"; use "or" (inclusive) or "either … or" (exclusive), with the interpretive clause that "or" is not exclusive.
- **Numbers.** Words and figures for counts and periods ("thirty (30) days"); figures for share counts and dollar amounts, with commas ("1,000,000 shares", "$0.00001 per share").
- **Gender-neutral** throughout. Use the party's defined name rather than pronouns where it reads cleanly.
- **Boilerplate.** Every agreement carries a complete general-provisions article: governing law, forum, jury-trial waiver (where enforceable; note California's limits), notices (with email delivery), entire agreement, amendment and waiver (who must sign), severability, successors and assigns, counterparts and electronic signatures (E-SIGN, 15 U.S.C. § 7001 et seq.; Delaware UETA, 6 Del. C. ch. 12A; for corporate acts, 8 Del. C. § 116), specific performance where relevant, construction/interpretation, further assurances, and expenses.
- **Corporate approvals** (consents, minutes, resolutions) recite the statutory basis (8 Del. C. § 141(f) for board consents; § 228 for stockholder consents) and use `RESOLVED` / `RESOLVED FURTHER` paragraphs with `WHEREAS` recitals. Every consent states a definite effective date. Never "effective when signed by all parties" without a date.
- **Signature blocks.** Entity: `COMPANY NAME` / `By: ________` / `Name:` / `Title:`; individual: signature line plus printed name, address, and email for notices where the agreement needs them.
- **Exhibits and schedules** are referenced by letter or number and included at the end of the form, even if as a stub.
- **No orphan concepts.** If the form gives a right (ROFR, repurchase, acceleration), it states who exercises it, how, by when, at what price, and what happens on failure to exercise.

## 4. Legal accuracy

- **As-of date: November 2026.** State law as it stands now, including the 2022–2026 DGCL amendments, and federal changes such as P.L. 119-21 (2025) to I.R.C. § 1202.
- **Primary sources first:** the Delaware Code (delcode.delaware.gov), the U.S. Code and eCFR, IRS forms and instructions, SEC rules and releases, state statutes on official sites. Secondary sources (law-firm client alerts, Cooley GO, NVCA commentary, YC) support market practice, not black-letter law. Where a rule comes only from secondary sources, say so or confirm with two reputable firms.
- **Pin-cite** every mandatory element in "About this template" and in the front-matter `authorities`.
- **Do not guess.** If a number, deadline, threshold, or fee could not be confirmed, put a `> **Verify:**` note and say what to check.
- **Mark jurisdiction-specific text** (for example California Labor Code § 2870 notices) as optional or alternative text with a note explaining when it applies.

## 5. Sources and copyright

- Use NVCA model documents, law-firm forms (Cooley GO, Orrick, Gunderson, Wilson Sonsini, Fenwick, Goodwin, Latham, etc.), Clerky, Carta, and similar materials **as references for structure, coverage, and market terms only.** Draft original language. Do not copy sentences or distinctive passages verbatim.
- **Series Seed documents are CC0 1.0** (public domain dedication) and may be adapted; cite them in `sources`.
- **Y Combinator SAFE forms** are third-party documents. Link to the official source and explain how to complete them; do not reproduce or modify them unless the license is confirmed to permit it.
- Statutory text and government forms are public and may be quoted.
- Record every source consulted in the template's `sources` list with how it was used.

## 6. Privacy and examples

- No real company, person, firm client, or transaction in any example. Use clearly fictional names (e.g., "Northwind Robotics, Inc."; founders "Alex Rivera" and "Jordan Lee"; investor "Example Ventures Fund I, L.P.").
- No personal data, addresses, or emails of real people.

## 7. Finished document (what Claude delivers)

1. Every `{{…}}`, `[[…]]`, `> **Drafting note:**` and `> **Verify:**` resolved or removed. Run `python3 scripts/check_document.py <file>`.
2. Names, share counts, prices, dates, and defined terms match across every document in the set and the cap table.
3. Front matter, "About this template," and "Drafting inputs" removed; only the form remains.
4. A short cover memo accompanies the set: assumptions made, open items, who signs what, in what order, and every deadline the signing triggers.
5. The memo notes that the documents are drafts for review by a licensed attorney.

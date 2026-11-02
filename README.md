# startupassist

An open-source [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) that turns Claude into an emerging-companies lawyer for **Delaware C corporations**: it knows every document a startup signs from formation through its Series A, drafts complete and internally consistent document sets from institutional-quality templates, reviews documents others send, and tracks the filings and deadlines each signing triggers.

> **Not legal advice.** The templates and guidance are drafts for review by a licensed attorney. Laws change; each template records when it was last verified and flags points to re-check.

## What's inside

| Folder | Contents |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill: role, rules, workflow, stage maps, deadlines, common mistakes |
| [`templates/`](templates) | 56 document templates, each with expert drafting notes, a variables table, and the form |
| [`references/`](references) | Reference guides on Delaware law, equity compensation and tax, securities, SAFEs and notes, employment and IP, priced-round terms, and governance and compliance |
| [`checklists/`](checklists) | Formation, financing closing, due diligence, and annual compliance checklists |
| [`scripts/`](scripts) | Draft checker, Markdown→Word converter, SAFE/note conversion calculator, Delaware franchise tax estimator |

**Templates by stage** (full list in [`references/document-catalog.md`](references/document-catalog.md)):

- **Formation:** certificate of incorporation, action of sole incorporator, bylaws, organizational board consent, director/officer indemnification agreement, stock ledger and § 151(f) notices
- **Founders:** founder restricted stock purchase agreement, technology assignment, 83(b) election package, spousal consent, repurchase notice
- **Equity compensation:** equity incentive plan (ISO/NSO/RSA/RSU, California-compliant), option grant package with early exercise, restricted stock and RSU agreements, plan and grant consents, reserve increases and option amendments
- **Hiring:** offer letter, executive employment agreement, CIIAA with state invention-assignment notices, consulting and advisor agreements, separation agreement and release, confirmatory IP assignment
- **Commercial:** mutual and one-way NDAs
- **SAFEs and notes:** YC SAFE completion guide, SAFE side letter, convertible note purchase agreement and note, financing consent, accredited investor questionnaire
- **Priced rounds:** term sheet, amended and restated certificate of incorporation, stock purchase agreement, disclosure schedule, investors' rights agreement, voting agreement, ROFR and co-sale agreement, management rights letter, board and stockholder financing consents
- **Governance:** resolution library, board and stockholder meeting materials, consents with § 228(e) notice, secretary's certificate, certificate of amendment, § 204 ratification, director agreement
- **Compliance:** Delaware franchise tax and annual report, foreign qualification, LLC-to-C-corp conversion, dissolution

Every template has four parts: YAML front matter (authorities, signers, sources, verification date), **About this template** (statutory requirements, market positions, state variations, pitfalls), **Drafting inputs** (every variable), and the **Form** itself, with `{{variables}}`, `[[Optional]]` and `[[Alternative]]` text, and drafting notes that the checker refuses to let through to a final draft.

## Install

**Claude Code**

```bash
git clone https://github.com/kvngnsn/startupassist ~/.claude/skills/startupassist
```

Restart Claude Code. The skill loads automatically when you ask about a startup document, or invoke it with `/startupassist`.

**Claude apps (claude.ai, desktop):** download this repository as a ZIP and upload it under *Settings → Capabilities → Skills*.

**Claude API / Agent SDK:** upload the folder as a custom skill; see the [Agent Skills docs](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).

## Use

Ask in plain language:

- "Form a Delaware C corp for me and my co-founder: 60/40 split, 4-year vesting, double-trigger acceleration."
- "Draft an offer letter and CIIAA for an engineer in Washington with a 20,000-share option recommendation."
- "We're raising $1.5M on post-money SAFEs at a $15M cap. What do we sign and file?"
- "Here's our Series A term sheet. What's off-market for the company?"
- "Our franchise tax bill says $85,000. What do we actually owe?"
- "We issued shares before the board was formed. How do we fix it?"

The scripts run on Python 3.9+ with the standard library (the Word converter needs `pip install python-docx`):

```bash
python3 scripts/check_document.py drafts/*.md          # unfilled fields, leftover notes, cross-refs, fact sheet
python3 scripts/md_to_docx.py drafts/bylaws.md         # Word output
python3 scripts/conversion_calculator.py --example     # SAFE/note conversion and pro forma cap table
python3 scripts/franchise_tax.py --authorized 10000000 --par 0.00001 --issued 9000000 --gross-assets 500000
```

## How current is it?

Every template records a `last_verified` date (November 2026) and cites the statutes, regulations, and forms it relies on, including recent changes such as the 2025–2026 DGCL amendments (SB 21, SB 95, HB 353), the 2026 FinCEN rule ending beneficial-ownership reporting for U.S. companies, the 2025 changes to I.R.C. § 1202 (QSBS) under P.L. 119-21, Delaware's August 2026 fee schedule, and NVCA's October 2025 model-document updates. Points that move quickly or could not be confirmed from a primary source carry a `> **Verify:**` note inside the template; the skill resolves those before a document is finalized. Run `grep -rn "Verify:" templates` to see them.

## Sources and licensing

The templates are **original drafting**. They were written against primary law (the Delaware General Corporation Law, the Internal Revenue Code and Treasury Regulations, SEC rules, and state statutes) and checked for coverage and market terms against public model forms and guidance, including the [NVCA model legal documents](https://nvca.org/model-legal-documents/), the [Series Seed documents](https://github.com/seriesseed) (CC0), [Y Combinator's SAFE](https://www.ycombinator.com/documents), Cooley GO, and published law-firm guidance. Each template lists what it consulted in its `sources` field. NVCA and law-firm forms were used as references only; no text was copied from them. YC's SAFE forms are not reproduced here: the skill links to the official forms and supplies a completion guide and companion documents.

- Templates, references, checklists, and `SKILL.md`: [CC0 1.0](LICENSE) (public domain dedication). Use them in your own documents without attribution.
- Scripts: [MIT](scripts/LICENSE).

## Contributing

Corrections to the law are the most valuable contribution. Please cite the primary source (statute, regulation, form instructions) in the pull request, update the template's `last_verified` date, and run:

```bash
python3 scripts/check_document.py --template templates/*/*.md
```

Follow [`references/drafting-conventions.md`](references/drafting-conventions.md) for structure and style.

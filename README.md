# StartupAssist — AI startup legal drafting and document templates

An open-source agent skill for **Delaware C-corp startup documents**, from formation through Series A. Draft and review founder equity, SAFEs, convertible notes, hiring agreements and financing documents using **56 templates**, source-linked guidance and consistency checks.

[![Download](https://img.shields.io/github/v/release/kvngnsn/startupassist?label=download)](https://github.com/kvngnsn/startupassist/releases/latest) [![License](https://img.shields.io/badge/license-CC0%20%2B%20MIT-blue)](LICENSE) [![Agent Skills](https://img.shields.io/badge/Agent%20Skills-portable-2d6a4f)](https://agentskills.io/specification)
[![Checks](https://github.com/kvngnsn/startupassist/actions/workflows/check.yml/badge.svg)](https://github.com/kvngnsn/startupassist/actions/workflows/check.yml)

**Start here:** [install](#install) · [example prompts](#use) · [template catalog](references/document-catalog.md) · [download](https://github.com/kvngnsn/startupassist/releases/latest)

For founders, startup lawyers and legal teams working on company formation, equity and venture financing. Portable instructions for Claude Code, Codex and other capable agents; Python helpers run locally. Keep company information and generated drafts outside this repository.

> Templates and generated documents are drafts for attorney review. Each template records its verification date and sources; check current law and transaction facts before use.

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

```sh
git clone https://github.com/kvngnsn/startupassist.git ~/.claude/skills/startupassist
```

**Codex**

```sh
git clone https://github.com/kvngnsn/startupassist.git ~/.agents/skills/startupassist
```

Open a new session and use `/startupassist` in Claude Code or `$startupassist` in Codex. For another host, download the [skill ZIP](https://github.com/kvngnsn/startupassist/releases/latest) or give a capable agent [SKILL.md](SKILL.md). The [Agent Skills format](https://agentskills.io/specification) is portable; host-specific imports and tool access vary.

The full workflow needs file access and current-source retrieval. Optional helpers need Python 3.9+; Word export additionally needs `python-docx`. No particular model, provider key or paid legal database is required by this repository. Instructions are portable; equivalent performance across models has not been established.

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

## Source dates and verification

Templates include `last_verified` dates and primary-source links. Dates are a maintenance record, not a guarantee that every rule remains current. The workflow rechecks material legal rules, changing thresholds/fees and unresolved `Verify:` notes before use. This release's repository and template checks do not constitute a fresh legal audit of every document.

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

## Related open-source skills

| Project | Use it for |
|---|---|
| [no-slop](https://github.com/kvngnsn/no-slop) | Clear AI writing and editing, with facts and meaning preserved. |
| [click-everything](https://github.com/kvngnsn/click-everything) | Exploratory UI testing, reproducible bugs and regression tests. |
| [patentassist](https://github.com/kvngnsn/patentassist) | Invention intake, prior-art research and patent application drafting. |

## Atlas workflow catalog

The optional [Atlas adapter](atlas/README.md) catalogs individual outputs and future shells. It preserves this standalone skill; adapter readiness is tracked separately.

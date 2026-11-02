# Convertible Financing Checklist (SAFE or Convertible Note Round)

Step-by-step checklist for a Delaware C-corporation raising money on Y Combinator post-money SAFEs or convertible promissory notes under Regulation D. Use it as the working closing checklist: copy it into the deal folder, assign an owner and date to each line, and check items off. Cross-references are to the skill's templates and references.

**Last verified:** November 2, 2026. Deadlines and fees change; confirm state items on the filing date.

Legend: **Owner** = Company (Co), Counsel (Cn), Investor (Inv). ☐ = open, ☒ = done.

---

## 1. Before launch: structure and modeling

| ☐ | Item | Owner | Reference |
|---|---|---|---|
| ☐ | Choose the instrument: post-money valuation-cap SAFE (default), discount or uncapped MFN SAFE, convertible note, or priced Series Seed | Co / Cn | [safe-guide](../templates/convertible-financing/safe-guide.md) § 4; [convertible-instruments](../references/convertible-instruments.md) § 12 |
| ☐ | Inventory every existing convertible (SAFEs, notes, warrants), including MFN elections and side letters; confirm pre- versus post-money caps and each instrument's capitalization definition | Cn | convertible-instruments § 14 |
| ☐ | Build the pre-round cap table from the stock ledger and option ledger (common, unvested restricted stock, options and RSUs outstanding, promised grants, unallocated pool) | Co / Cn | |
| ☐ | Model the proposed terms through a hypothetical priced round, including a pool top-up, with `python3 scripts/conversion_calculator.py`; share the output with the founders | Cn | convertible-instruments §§ 6–7 |
| ☐ | Set the cap (state it as post-money for YC SAFEs), discount (state as the discount, and as YC "Discount Rate" = 100 − discount), MFN policy, maximum raise, minimum check, and closing window | Co | safe-guide § 5 |
| ☐ | Set the side-letter policy: threshold check size; aggregate participation budget for the next round; which rights (pro rata, information, MFN, Major Investor) | Co | [safe-side-letter](../templates/convertible-financing/safe-side-letter.md) |
| ☐ | For notes: interest rate (at or above the applicable federal rate), maturity, Qualified Financing threshold, cap basis (Alternative A–D), change-of-control premium, maturity outcome, subordination | Co / Cn | [convertible-promissory-note](../templates/convertible-financing/convertible-promissory-note.md) |
| ☐ | Choose the exemption: Rule 506(b) (no general solicitation) or Rule 506(c) (general solicitation permitted; verify every investor). Review the founders' public statements, demo-day plans (Rule 148 limits), and platform listings | Cn | [securities-law](../references/securities-law.md) §§ 3, 6 |
| ☐ | If any investor may not be accredited: stop and decide whether to exclude them (recommended), use Rule 506(b) with Rule 502(b) disclosure, or another exemption | Cn | securities-law § 5 |
| ☐ | Confirm no finder or other unregistered person will receive transaction-based compensation; if an introducer will be paid, use a registered broker-dealer or a compliant California § 25206.1 finder | Co / Cn | securities-law § 13 |
| ☐ | Foreign investors expected? Determine whether the Company is a TID U.S. business (export classification of its technology; sensitive personal data); plan to withhold board, observer, and technical-information rights from foreign persons absent CFIUS analysis | Cn | securities-law § 16.3 |
| ☐ | Any China (or other country of concern) nexus in the Company's operations or revenue? Check the Outbound Investment Security Program (31 C.F.R. Part 850) and COINS Act status | Cn | securities-law § 16.4 |
| ☐ | If preferred stock is already outstanding: check charter protective provisions and investor agreements for consents, pre-emptive rights, or notice requirements | Cn | |

## 2. Corporate approvals

| ☐ | Item | Owner | Reference |
|---|---|---|---|
| ☐ | Board consent approving the financing, effective **before** any SAFE or note is signed or funded: instrument, approved forms, maximum amount, economic terms, side-letter parameters, § 157 parameters, closing window, authorized officers, filings, reservation approach | Cn | [board-consent-convertible-financing](../templates/convertible-financing/board-consent-convertible-financing.md) |
| ☐ | All directors sign the § 141(f) consent (each consent given no more than 60 days before the effective date) | Co | |
| ☐ | Insider participation? Disclose material facts; approve by majority of disinterested directors (or a committee of two or more disinterested directors if a majority are not disinterested), or by disinterested stockholders, or document fairness; use § 144(b) for controlling stockholders | Cn | board consent § 9; 8 Del. C. § 144 |
| ☐ | Notes: reserve sufficient common for maturity and change-of-control conversions; confirm authorized common is sufficient | Cn | board consent § 8 |
| ☐ | Record that preferred stock cannot be reserved until authorized at the priced round (charter amendment under 8 Del. C. § 242 or certificate of designations under § 151(g)) | Cn | board consent § 8 |
| ☐ | Bad-actor questionnaires from directors, executive officers, officers participating in the offering, 20% holders, and any compensated solicitor | Cn | [investor-questionnaire](../templates/convertible-financing/investor-questionnaire.md) Annex B |

## 3. Documents

| ☐ | Item | Owner | Reference |
|---|---|---|---|
| ☐ | **SAFE:** download the current YC form(s) from https://www.ycombinator.com/documents (or use YC's "Send a SAFE" tool for U.S. companies); record form name and version; do not modify except to complete blanks (and, if needed, add a second signature block) | Cn | safe-guide §§ 2–5 |
| ☐ | **SAFE:** complete blanks: exact legal names, Purchase Amount (matches the wire), date, "Delaware," cap (post-money, full dollars) or Discount Rate (100 − discount), governing law, signature blocks, notice addresses and emails | Cn | safe-guide § 5 |
| ☐ | **Side letters:** YC Pro Rata Side Letter (unmodified) or the skill's side letter, only for qualifying investors; confirm no side letter alters conversion economics; check for overlapping rights | Cn | safe-side-letter |
| ☐ | **Notes:** Note Purchase Agreement, form of Note, Schedule of Purchasers, Disclosure Schedule (capitalization, other convertibles, promised grants, litigation, related parties) | Cn | [convertible-note-purchase-agreement](../templates/convertible-financing/convertible-note-purchase-agreement.md) |
| ☐ | **Notes:** confirm usury position (Delaware governing law; California § 25118 thresholds if California law could apply; avoid New York law for discounted notes) | Cn | convertible-promissory-note About § 4 |
| ☐ | Disclosure package for investors: accurate, dated deck; risk summary; capitalization summary; data room access; opportunity to ask questions | Co / Cn | securities-law § 15 |
| ☐ | SAFE Term Summary prepared for each SAFE; round register started | Cn | safe-guide Form and Schedule 1 |

## 4. Investor onboarding

| ☐ | Item | Owner | Reference |
|---|---|---|---|
| ☐ | Send the investor questionnaire with the documents; require it back before countersignature | Co / Inv | investor-questionnaire |
| ☐ | Review accredited-investor category; follow up on red flags (newly formed entities, inconsistent answers) | Cn | |
| ☐ | **Rule 506(c) only:** collect verification (third-party letter dated within three months; income or net-worth documents; prior verification within five years; or minimum-investment commitment of $200,000 natural persons / $1,000,000 entities with no-third-party-financing representation) | Cn | securities-law § 3.2 |
| ☐ | Bad-actor certification from any investor that will hold 20% or more of voting equity (as converted) | Cn | investor-questionnaire Part E |
| ☐ | Foreign person answers reviewed; CFIUS declaration analysis completed before signing where needed (mandatory declarations are due at least 30 days before completion) | Cn | securities-law § 16.3 |
| ☐ | OFAC screening of each investor and controlling owners (record date and result) | Co / Cn | investor-questionnaire Part G |
| ☐ | ERISA / IRA investors identified; FINRA associated persons identified (investor's own notice obligations under FINRA Rules 3210, 3270, 3280) | Cn | investor-questionnaire Parts H, I |
| ☐ | IRS Form W-9 or W-8BEN / W-8BEN-E collected | Co | |
| ☐ | Record each investor's state or country of residence for blue-sky filings | Cn | |

## 5. Signing, funding, and countersignature

| ☐ | Item | Owner | Reference |
|---|---|---|---|
| ☐ | Investor signs the SAFE (and side letter) or NPA counterpart page | Inv | |
| ☐ | Wire instructions delivered securely; investor confirms by telephone call-back to a known number before wiring (wire-fraud control) | Co / Inv | |
| ☐ | Funds received in the Company account; amount matches Purchase Amount or principal (refund overpayments; resolve shortfalls before countersigning) | Co | YC FAQ |
| ☐ | Company countersigns only after funds arrive; record signature date and funds-received date (both matter for MFN timing) | Co | safe-guide § 5 |
| ☐ | If an escrow or closing agent is used: escrow agreement, release conditions (board consent, minimum amount, signed documents), and release instructions | Co / Cn | |
| ☐ | Notes: Company executes and delivers each Note; note register updated (registered form) | Co / Cn | convertible-promissory-note § 8.3 |
| ☐ | Distribute fully executed copies to each investor | Cn | |
| ☐ | Record the **date of first sale** (first investor irrevocably committed) | Cn | securities-law § 8.1 |

## 6. Securities filings

| ☐ | Item | Deadline | Owner | Reference |
|---|---|---|---|---|
| ☐ | EDGAR access: Form ID submitted (if no CIK); at least two account administrators authorized (one for an individual or single-member filer), each with individual Login.gov credentials and multifactor authentication; filing agent delegated | Start at board approval; allow processing time | Co / Cn | securities-law § 8.4 |
| ☐ | **Form D** filed on EDGAR (no SEC fee) | **15 calendar days after first sale** (next business day if weekend or holiday) | Cn | 17 C.F.R. § 230.503(a)(1) |
| ☐ | Form D Item 9 (type of securities) completed consistently with the instrument; Item 12 (sales compensation) accurate; Item 3 related persons correct | With Form D | Cn | securities-law § 8.3 |
| ☐ | **California** § 25102.1(d) notice ($300) via DFPI online system or NASAA EFD | 15 days after first California sale | Cn | securities-law § 9.2 |
| ☐ | **New York** notice via EFD ($300 if offering ≤ $500,000; $1,200 if > $500,000) | Within 15 days after first New York sale (verify) | Cn | securities-law § 9.2 |
| ☐ | **Texas** notice via EFD (1/10 of 1% of aggregate offering, max $500) | 15 calendar days after first Texas sale | Cn | securities-law § 9.2 |
| ☐ | **Washington** notice via EFD ($300) | 15 days after first Washington sale | Cn | securities-law § 9.2 |
| ☐ | All other investor states: check NASAA EFD requirements and fees for each state; EFD charges a $160 system use fee per initial Form D notice filing | Per state | Cn | securities-law § 9.1 |
| ☐ | Form D amendment for material mistakes or covered changes (e.g., offering amount increase above 10%) | As soon as practicable | Cn | 17 C.F.R. § 230.503(a)(3) |
| ☐ | **Annual Form D amendment** if the offering is still continuing | On or before the first anniversary of the most recent filing | Cn | 17 C.F.R. § 230.503(a)(3)(iii) |
| ☐ | State amendments where required (e.g., Texas requires an amendment with each SEC amendment) | With each SEC amendment | Cn | |
| ☐ | Calendar the end of the closing window; close the offering (cease offering efforts) and note the termination date for integration purposes | Closing window end | Co / Cn | securities-law § 7 |

## 7. Cap table, records, and data room

| ☐ | Item | Owner |
|---|---|---|
| ☐ | Cap table updated: each SAFE or note recorded as a convertible (not as shares), with amount, date, cap and cap type, discount, MFN, side letters | Co |
| ☐ | SAFE Term Summary completed and certified for each SAFE; round register totals tie to the board maximum and the Form D | Cn |
| ☐ | Note register (holder, principal, issue date, transfers) maintained | Co |
| ☐ | Data room folders: board consent; executed SAFEs/NPA/Notes; side letters; questionnaires and verification materials (restricted access); wire confirmations; Form D and state filings with confirmations; bad-actor questionnaires; CFIUS and OFAC memos; conversion models | Cn |
| ☐ | MFN tracking: for each MFN SAFE or MFN side letter, log every later convertible issuance and send MFN Notices promptly; record elections and Replacement SAFEs | Co / Cn |
| ☐ | Pro rata and Major Investor commitments listed for the priced-round lawyers | Cn |
| ☐ | Insurance, banking, and accounting teams told about the new instruments (auditors: ASC 480 classification; 409A provider: convertible instruments outstanding) | Co |

## 8. Tax and accounting

| ☐ | Item | Owner | Reference |
|---|---|---|---|
| ☐ | SAFEs: no Form 83(b) for investors (cash purchase, not compensation); never issue SAFEs for services | Cn | safe-guide § 9 |
| ☐ | SAFEs: advise investors that QSBS (§ 1202) treatment and holding period are uncertain; the YC form states intent to treat the SAFE as stock | Cn | convertible-instruments § 10.1 |
| ☐ | Notes: accountant confirms OID / interest accrual and information reporting (Forms 1099-OID or 1099-INT) and any withholding for foreign holders | Co | convertible-instruments § 10.2 |
| ☐ | Notes: rate at or above the AFR for the issue month and term | Cn | |
| ☐ | Accounting classification (SAFEs typically liabilities under ASC 480; notes under ASC 470 with possible embedded derivatives) confirmed with the Company's accountant | Co | convertible-instruments § 11 |
| ☐ | 409A: tell the valuation provider about the financing; consider whether it is a material event requiring an updated valuation before further option grants | Co | |
| ☐ | Record § 1202 gross-assets data (aggregate gross assets before and after each issuance) to support later QSBS determinations | Co | |

## 9. Preparing for conversion (the priced round)

| ☐ | Item | Owner | Reference |
|---|---|---|---|
| ☐ | Deliver Financing Notices (side letters) and Qualified Financing notices (notes) on time | Co / Cn | safe-side-letter Art. 2; note § 3.8 |
| ☐ | Re-run the conversion model with final term-sheet numbers; confirm whether conversions and the pool increase are in the pre-money | Cn | convertible-instruments § 7 |
| ☐ | Give the priced-round drafter: names and Original Issue Prices (four decimals) of each shadow series (e.g., Series A-1, A-2), share counts, and holders | Cn | convertible-instruments § 8 |
| ☐ | Amended and restated charter authorizes each shadow series with price-based terms keyed to its Original Issue Price; enough common reserved for conversion of preferred | Cn | |
| ☐ | SAFE and note holders sign the stock purchase agreement (or joinder) and investor agreements with limited representations and customary drag-along limits | Cn | YC SAFE § 1(a); note § 3.5(a) |
| ☐ | Pro rata exercises allocated within the round; side letters terminate at the initial closing; Major Investor designations implemented | Cn | safe-side-letter Arts. 2, 5, 6 |
| ☐ | Notes: confirm accrued interest through the actual closing date; cancel Notes; update note register | Cn | |
| ☐ | Conversion shares issued in book entry with legends; Rule 144 holding period tacks to the SAFE or note purchase date | Cn | 17 C.F.R. § 230.144(d)(3)(ii) |
| ☐ | New Form D for the priced round (a separate offering) | Cn | securities-law § 8.3 |

---

**Sources:** 17 C.F.R. §§ 230.144, 230.148, 230.152, 230.501–230.506 (eCFR, current text); SEC Form D guide; SEC EDGAR Next materials; SEC staff no-action letter to Latham & Watkins LLP (Mar. 12, 2025); California DFPI Securities FAQ and fee index (ADM 510, rev. 10/25); Texas State Securities Board Regulation D filing page; Washington DFI Rule 506 FAQ; 13 NYCRR § 10.8; NASAA EFD fee FAQ; 8 Del. C. §§ 141, 144, 151, 152, 157, 242; 31 C.F.R. Parts 800 and 850; Y Combinator SAFE documents page and FAQ. See the Sources sections of [securities-law.md](../references/securities-law.md) and [convertible-instruments.md](../references/convertible-instruments.md) for URLs.

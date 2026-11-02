---
id: priced-round-closing-checklist
title: Priced Preferred Stock Round — Closing Checklist
category: checklists
stage: priced-round
signers: [Not signed; working document maintained by company counsel and shared with lead investor counsel]
authorities:
  - "8 Del. C. §§ 103, 242, 245 (filing and effectiveness of the Restated Certificate)"
  - "8 Del. C. § 141(f) (board consent); § 228 (stockholder consent; § 228(e) notice); § 213(b) (record date)"
  - "8 Del. C. §§ 151(f), 152, 158, 202(a), 224 (uncertificated-share notices; consideration; legends; stock ledger)"
  - "17 C.F.R. § 230.503(a) (Form D within 15 calendar days after first sale); § 230.506(b), (d), (e) (Rule 506; bad actor)"
  - "15 U.S.C. § 18a and 16 C.F.R. Parts 801–803 (HSR; 2026 size-of-transaction threshold $133.9 million, effective Feb. 17, 2026)"
  - "31 C.F.R. Parts 800 and 802 (CFIUS); 31 C.F.R. Part 850 (outbound investment); 28 C.F.R. Part 202 (DOJ data security program)"
  - "26 U.S.C. § 83(b) and Treas. Reg. § 1.83-2 (30-day election); Treas. Reg. § 1.409A-1(b)(5)(iv) (409A valuation)"
  - "26 U.S.C. § 1202 as amended by Pub. L. 119-21 (QSBS gross-asset test at each issuance)"
use_when: Running a seed-priced, Series A or later preferred stock financing for a Delaware corporation from signed term sheet through post-closing filings.
do_not_use_when: The financing is a SAFE or convertible note round (use the convertible-financing checklist), or a public-company financing.
related: [term-sheet, amended-and-restated-certificate-of-incorporation, stock-purchase-agreement, disclosure-schedule, investors-rights-agreement, voting-agreement, rofr-and-co-sale-agreement, management-rights-letter, board-consent-priced-financing, stockholder-consent-priced-financing, due-diligence-request-list, indemnification-agreement]
sources:
  - name: "eCFR 17 C.F.R. § 230.503 (Form D timing) — eCFR API, version 2026-10-01"
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-230/section-230.503
  - name: "Delaware Code, Title 8, ch. 1 — official text"
    url: https://delcode.delaware.gov/title8/c001/index.html
  - name: "Simpson Thacher, 'Revised HSR Act Thresholds and Increased Filing Fees' (Jan. 20, 2026)"
    url: https://www.stblaw.com/about-us/publications/view/2026/01/20/revised-hsr-act-thresholds-and-increased-filing-fees
  - name: "BCLP, 'New York Streamlines and Modernizes Regulation D Filing Procedures' (New York Form D notice via NASAA EFD)"
    url: https://www.bclplaw.com/en-US/events-insights-news/new-york-streamlines-and-modernizes-regulation-d-filing-procedures.html
  - name: "White & Case, COINS Act and outbound investment rule status (FY 2026 NDAA; Treasury NPRM Oct. 22, 2026)"
    url: https://www.whitecase.com/insight-alert/ndaa-fy-2026-and-impending-changes-us-outbound-investment-security-program
  - name: "Law-firm closing checklists published by Cooley GO and others — coverage reference only; no text copied"
    url: https://www.cooleygo.com/
last_verified: 2026-11-02
---

## About this template

**How to use it.** Company counsel owns the checklist; circulate it to the lead investor's counsel at kickoff and update it at least twice a week. Each line has a responsible party ("Co." = Company, "CoC" = Company counsel, "Lead" = lead investor, "LC" = lead investor counsel, "All" = all parties), the signatories, and a status. The phases are in the order things actually have to happen. Three ordering rules matter more than the rest:

1. **Board approval before stockholder approval** of the Restated Certificate (§ 242(b)(1) requires the board resolution first).
2. **Restated Certificate effective before any share issuance.** The new series does not exist until the Delaware Secretary of State has filed the certificate. Order expedited filing (same-day or 24-hour) and receive the filed copy before releasing funds.
3. **Escrowed signatures; simultaneous release.** Every signature page is held in escrow by the receiving counsel and released only when all closing conditions are satisfied and the filing is confirmed.

**Deadlines this checklist tracks.** Form D: 15 calendar days after the first sale (the date investors become irrevocably committed, which counsel usually treats as the Initial Closing). State notice filings: generally 15 days after the first sale in the state. § 228(e) notice: promptly after the stockholder consent. 83(b) elections: 30 days after any restricted stock issuance. Stockholder approval of plan increase: within 12 months of board adoption. D&O insurance and other IRA covenants: per the IRA (often 90 days). Additional Closings: by `{{additional_closing_deadline}}`.

**Regulatory screens to run at kickoff.** (a) *HSR.* Venture preferred stock that votes in director elections is a "voting security" for HSR purposes. If the voting securities an investor will hold after a closing are valued above the size-of-transaction threshold ($133.9 million for 2026, effective February 17, 2026), determine whether a filing is required or an exemption applies (the "solely for the purpose of investment" exemption covers only passive holdings of 10% or less and is unavailable to an investor that designates a director). (b) *CFIUS.* Any foreign investor, and especially one receiving board, observer or information rights in a business working with critical technologies, sensitive personal data or covered infrastructure. (c) *Outbound investment.* U.S. investors' own obligations under 31 C.F.R. Part 850 if the Company has operations or subsidiaries in a country of concern. (d) *DOJ data security program.* Representations in the SPA about covered persons and bulk sensitive data. (e) *Corporate Transparency Act.* Domestic companies no longer file beneficial ownership reports with FinCEN after FinCEN's final rule; no BOI update is needed for the round.

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `{{company_name}}` | Company | Northwind Robotics, Inc. | |
| `{{series_name}}` | New series | Series A | |
| `{{lead_investor_name}}` | Lead investor | Example Ventures Fund I, L.P. | |
| `{{round_size}}` | Maximum new money | $7,500,000 | |
| `{{original_issue_price}}` | Price per share | $1.2345 | |
| `{{initial_closing_date}}` | Target Initial Closing | March 3, 2027 | |
| `{{additional_closing_deadline}}` | Last Additional Closing date | June 1, 2027 | |
| `{{post_closing_pool_percent}}` | Option pool target | 10% | |
| `{{company_counsel_firm}}`, `{{investor_counsel_firm}}` | Counsel | Example Law LLP; Sample & Partners LLP | Fictional |

## Form

---

# {{series_name}} PREFERRED STOCK FINANCING — CLOSING CHECKLIST

**{{company_name}}** | Lead: {{lead_investor_name}} | Round size: up to {{round_size}} at {{original_issue_price}} per share | Target Initial Closing: {{initial_closing_date}} | Company counsel: {{company_counsel_firm}} | Lead counsel: {{investor_counsel_firm}}

**Legend:** Co. = Company; CoC = Company counsel; Lead = lead investor; LC = lead investor counsel; All = all parties. Status: Not started / Drafting / Circulated / Final / Signed (escrow) / Released / Filed / Done.

## Phase 1 — Term Sheet and Kickoff

| # | Item | Responsible | Signatories | Status / notes |
|---|---|---|---|---|
| 1.1 | Signed term sheet (binding provisions only: exclusivity, confidentiality, expenses, governing law) | Co. / Lead | CEO; Lead | Calendar the exclusivity expiration |
| 1.2 | Board approval to sign term sheet with exclusivity (if the board has not already authorized) | CoC | Board | Informal approval is common; document if exclusivity is long or an insider leads |
| 1.3 | Working group list (names, roles, emails, phones) | CoC | — | |
| 1.4 | Timeline to closing, with a filing date for the Restated Certificate | CoC / LC | — | Work backward from funding date |
| 1.5 | Pro forma capitalization table (pre-money fully diluted, pool increase to reach {{post_closing_pool_percent}} post-closing, SAFE/note conversions, new money, post-money) approved by Lead | Co. / CoC | — | The single most important number; reconcile to the ledger before drafting |
| 1.6 | SAFE and note conversion calculations, holder by holder, with each instrument's terms | Co. / CoC | — | Confirm caps, discounts, MFN clauses, interest |
| 1.7 | Identify all existing approval rights and waivers needed: current charter protective provisions, prior IRA pro rata and notice rights, side letters, bylaws ROFR, lender consents, commercial-contract change-of-control or assignment clauses | CoC | — | Build the stockholder vote table (see stockholder-consent template) |
| 1.8 | Regulatory screens: HSR; CFIUS (foreign investors, TID U.S. business status); outbound investment; DOJ data security program; export controls; state securities exemptions for each investor's residence | CoC / LC | — | Record conclusions in a memo to file |
| 1.9 | Investor questionnaires (accredited status, bad-actor status, foreign-person status, ERISA/VCOC needs, tax status) | CoC | Each Purchaser | Collect before final allocations |
| 1.10 | Rule 506(d) bad-actor inquiry of the Company, directors, officers participating in the offering, 20% holders by voting power and any placement agent | CoC | D&O questionnaires | Rule 506(d)(2)(iv) reasonable-care record |

## Phase 2 — Due Diligence

| # | Item | Responsible | Signatories | Status / notes |
|---|---|---|---|---|
| 2.1 | Data room opened and organized by the due-diligence request list categories | Co. / CoC | — | See due-diligence-request-list template |
| 2.2 | Lead's diligence request list received and responses tracked | CoC | — | |
| 2.3 | Corporate records review: charter history, bylaws, all board and stockholder minutes and consents, stock ledger, equity grants, 83(b) elections | CoC | — | Fix defects before the disclosure schedule is final |
| 2.4 | Remediation of defects found: § 204 ratification of defective stock issuances or grants; missing CIIAAs signed; IP assignment confirmations; late 83(b) issues documented | CoC / Co. | Board; stockholders as § 204 requires | § 204 needs board resolutions and, where required, stockholder approval and notice; a § 204 certificate of validation may need to be filed |
| 2.5 | Legal, IP, commercial and financial diligence calls | Co. / Lead | — | |
| 2.6 | Background checks on founders (if Lead requires) | Lead | — | FCRA authorization needed |
| 2.7 | Disclosure Schedule drafted against final SPA representations | CoC / Co. | — | Each exception tied to a specific representation |

## Phase 3 — Transaction Documents

| # | Item | Responsible | Signatories | Status / notes |
|---|---|---|---|---|
| 3.1 | Amended and Restated Certificate of Incorporation | LC (first draft in most deals) / CoC | President or other authorized officer (filing) | Confirm § 245(c) recitals; "adopted under Sections 228, 242 and 245"; pre-clear with the Delaware Division of Corporations if complex |
| 3.2 | {{series_name}} Preferred Stock Purchase Agreement, with Schedule of Purchasers and Exhibits | LC / CoC | Company; each Purchaser | Additional Closing mechanics and deadline |
| 3.3 | Disclosure Schedule | CoC / Co. | Delivered by Company | |
| 3.4 | Investors' Rights Agreement (amended and restated, if prior) | LC / CoC | Company; Investors; Key Holders (if parties) | Major Investor list; prior-agreement amendment threshold met |
| 3.5 | Voting Agreement (amended and restated, if prior) | LC / CoC | Company; Investors; Key Holders; spouses | Board seats match charter and bylaws |
| 3.6 | Right of First Refusal and Co-Sale Agreement | LC / CoC | Company; Investors; Key Holders; spouses | Periods match bylaws ROFR |
| 3.7 | Management Rights Letters (each requesting fund) | LC | Company; fund | |
| 3.8 | Indemnification Agreements (each director; officers if desired) | CoC | Company; each indemnitee | Indemnitor-of-first-resort language matches IRA |
| 3.9 | Legal opinion of Company counsel (if required by the SPA) and opinion backup certificate | CoC | CoC; officer certificate | Many seed and Series A deals now waive the opinion |
| 3.10 | Side letters (if any), each reviewed for MFN and § 122(18) issues | LC / CoC | Company; investor | Remember § 220(a)(1)h: § 122(18) agreements are books and records |
| 3.11 | SAFE/note conversion documents (acknowledgment, joinders, payoff of any cash interest) | CoC | Company; each holder | |
| 3.12 | Founder documents requested by Lead: re-vesting amendments, updated CIIAAs, offer letter updates | CoC / LC | Company; founder; spouse | Re-vesting may require a new 83(b) analysis |
| 3.13 | Plan amendment increasing the pool | CoC | Board; stockholders | |
| 3.14 | Bylaws amendment (board size, director quorum, if needed) | CoC | Board | |
| 3.15 | Pay-off or consent letters for any lender whose loan restricts equity issuance or changes of control | CoC | Lender | |

## Phase 4 — Corporate Approvals

| # | Item | Responsible | Signatories | Status / notes |
|---|---|---|---|---|
| 4.1 | Board consent approving the financing (see board-consent template), with final document forms attached | CoC | All directors | Unanimous; § 144 disclosures; § 122(18) consideration determination |
| 4.2 | Record date confirmed (close of business on board consent date unless board fixed one) | CoC | — | § 213(b) |
| 4.3 | Information package to stockholders whose consent is sought (Restated Certificate; financing summary; conflicts disclosure) | CoC | — | Fiduciary duty of disclosure |
| 4.4 | Stockholder consent (all voting groups, waivers, plan increase) | CoC | Required holders | Track 60-day window from first consent delivered (§ 228(c)) |
| 4.5 | Vote tabulation by class and series with record-date share counts | CoC | Secretary | Keep in minute book |
| 4.6 | Existing investor waivers (pro rata, notices, ROFR) if not in the stockholder consent | CoC | Required holders | |
| 4.7 | Third-party consents (lenders, landlords, key customers) identified in diligence | Co. / CoC | Counterparties | |

## Phase 5 — Pre-Closing Filings and Deliverables

| # | Item | Responsible | Signatories | Status / notes |
|---|---|---|---|---|
| 5.1 | Restated Certificate executed in final form | CoC | Authorized officer | |
| 5.2 | Restated Certificate filed with the Delaware Secretary of State (expedited) on the closing date before funding, or the day before with a specified effective time | CoC | — | Obtain certified copy or filing evidence before release |
| 5.3 | Good standing certificate (Delaware) dated within the period the SPA requires; foreign qualification good standings in the principal-office state | CoC | — | |
| 5.4 | Secretary's certificate (charter, bylaws, board and stockholder resolutions, incumbency) | CoC | Secretary | |
| 5.5 | Compliance (bring-down) certificate | CoC | CEO | Representations true; covenants performed |
| 5.6 | EDGAR access codes obtained or confirmed (Form ID; EDGAR Next individual credentials and account administrators) | CoC / Co. | Officer | Allow lead time; needed for Form D |
| 5.7 | D&O insurance quote bound or binder ready (if a closing condition) | Co. | Broker | Otherwise within the IRA's post-closing period |
| 5.8 | Wire instructions provided on Company letterhead and **verbally confirmed by phone with a known Company officer** | Co. | CFO | Wire-fraud control: never accept changed instructions by email alone |
| 5.9 | Funds flow memorandum (gross proceeds by Purchaser; investor counsel fees deducted or reimbursed; net proceeds) | CoC / Co. | — | |
| 5.10 | Escrow arrangement for signature pages confirmed in writing | CoC / LC | — | |

## Phase 6 — Signatures and Funding (Initial Closing)

| # | Item | Responsible | Signatories | Status / notes |
|---|---|---|---|---|
| 6.1 | Signature pages collected in escrow for every Transaction Agreement from Company, every Purchaser, every Key Holder and spouse | CoC / LC | All | Use a tracker by document and party |
| 6.2 | Confirm all SPA closing conditions satisfied or waived (in writing) | CoC / LC | — | |
| 6.3 | Confirm Restated Certificate effective | CoC | — | Filing evidence circulated |
| 6.4 | Release of signature pages by each counsel on a closing call or by email confirmation | CoC / LC | — | Record the release time |
| 6.5 | Purchasers wire funds; Company confirms receipt in its account | Purchasers / Co. | — | Shares issue only against confirmed funds |
| 6.6 | Issue {{series_name}} Preferred Stock and shadow series (book entry) and deliver § 151(f) notices with legends (§ 202(a)); cancel converted SAFEs and notes | CoC / Co. | Officer | Same day as funding |
| 6.7 | Compiled closing set (PDF) distributed; signature pages released from escrow | CoC | — | |

## Phase 7 — Post-Closing (first 15 days)

| # | Item | Responsible | Deadline | Status / notes |
|---|---|---|---|---|
| 7.1 | Form D filed on EDGAR | CoC | 15 calendar days after the first sale (next business day if a weekend or holiday) | Amend for later closings if the offering size or other required information changes |
| 7.2 | State notice filings and fees (NASAA EFD where available) for each state where a Purchaser resides | CoC | Generally 15 days after the first sale in the state; confirm each state | Includes New York (Form D via EFD since Dec. 2020) |
| 7.3 | § 228(e) notice to non-consenting stockholders | CoC | Promptly | Exhibit A to the stockholder-consent template |
| 7.4 | Post-closing consent of Preferred and Common holders electing designated directors (Voting Agreement) | CoC | At or right after closing | Exhibit B to the stockholder-consent template; § 228(e) notice if not unanimous |
| 7.5 | Stock ledger updated (§ 224), cap table platform updated, converted instruments cancelled, Schedule A/B to IRA, Voting and ROFR updated | CoC / Co. | Within days | Reconcile to the funds flow |
| 7.6 | 83(b) elections for any restricted stock issued or re-vested in connection with the round (founder re-vesting, early-exercised options) | Recipient (CoC to prepare) | 30 days after transfer; mail by certified mail, return receipt, and keep proof | Deadline cannot be extended |
| 7.7 | Board seating: Indemnification Agreements signed; new directors added to D&O policy; board portal access; first board meeting scheduled | Co. / CoC | At closing | |
| 7.8 | Wire receipt confirmations and funds-flow reconciliation; investor counsel fees paid as capped | Co. | Within days | |
| 7.9 | Management rights letters delivered; observer confidentiality agreements signed | Co. / CoC | At closing | |

## Phase 8 — Post-Closing (following months)

| # | Item | Responsible | Deadline | Status / notes |
|---|---|---|---|---|
| 8.1 | New 409A valuation reflecting the round before further option grants | Co. | Before next grant | Treas. Reg. § 1.409A-1(b)(5)(iv)(B)(2)(i) |
| 8.2 | D&O insurance bound at required limits (if not done at closing) | Co. | IRA deadline (e.g., 90 days) | Side A coverage; Series Directors covered |
| 8.3 | Option pool increase stockholder approval confirmed (for ISO status) | CoC | Within 12 months of board adoption | Done in stockholder consent if used |
| 8.4 | Additional Closings: joinders, funds, issuance, ledger, Form D amendment if needed, state filings for new states | CoC | By {{additional_closing_deadline}} | Rerun QSBS gross-asset test before each |
| 8.5 | QSBS record: gross-asset computation immediately after each closing; support file | Co. / accountants | At each closing | § 1202(d)(1)(B) |
| 8.6 | IRA covenant calendar: financial statements, budget, cybersecurity program, required policies, D&O, observer | Co. | Per IRA | Breaches by neglect are common |
| 8.7 | Legends and § 151(f) notices confirmed for all Key Holder and Investor shares | CoC | Within 30 days | § 202(a) enforceability |
| 8.8 | Closing binder (final signed documents, filings, certificates, opinions, consents, vote tabulation, Form D) archived and shared | CoC | Within 60 days | Acquirers and later investors will request it |
| 8.9 | Update 83(b) and equity records for any grants made under the increased pool | CoC | Ongoing | |
| 8.10 | Annual franchise tax planning: authorized-share method vs. assumed-par-value capital method after increase in authorized shares | Co. / accountants | Before March 1 annual report | Large authorized share counts can produce large franchise tax under the default method; file using the assumed-par-value method |

> **Verify:** Before each deal, confirm the current HSR thresholds, each state's notice-filing deadline and fee, and the status of the Treasury COINS Act rulemaking that may replace 31 C.F.R. Part 850. Also confirm the current Delaware franchise tax computation rules and filing deadline for the annual report.

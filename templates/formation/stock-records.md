---
id: stock-records
title: Stock Ledger, Notice of Issuance of Uncertificated Shares, Stock Certificate, and Stock Assignment
category: formation
stage: formation
signers: [Secretary or other officer maintaining the stock ledger (ledger entries); Company by two authorized officers (certificate, if used); an officer (§ 151(f) notice); stockholder (stock assignment)]
authorities:
  - "8 Del. C. § 224 (form of records; stock ledger on electronic or distributed networks)"
  - "8 Del. C. § 219(c) (definition and evidentiary role of the stock ledger)"
  - "8 Del. C. § 151(f) (notice to holders of uncertificated shares)"
  - "8 Del. C. § 158 (certificates signed by any two authorized officers; uncertificated shares by board resolution)"
  - "8 Del. C. § 202(a) (transfer restrictions must be noted conspicuously on the certificate or in the § 151(f) notice)"
  - "8 Del. C. §§ 156, 218(a), 364 (partly paid shares; voting trusts; public benefit corporation legend)"
  - "8 Del. C. § 116(b)(2)–(3) (§ 116's electronic-document rules do not apply to stock-ledger documents or security certificates)"
  - "6 Del. C. Article 8 (investment securities; transfer and registration)"
  - "17 C.F.R. § 230.144 (restricted securities; holding periods referenced in Securities Act legend)"
use_when: Recording every issuance, transfer, repurchase and cancellation of stock, and giving each holder the § 151(f) notice (or a certificate) that makes transfer restrictions enforceable.
do_not_use_when: The Company uses an equity management platform that generates § 151(f)-compliant notices and maintains the ledger; in that case use this file to check the platform's output for the required content and legends rather than duplicating it.
related: [bylaws, initial-board-consent, founder-stock-purchase-agreement, notice-of-repurchase]
sources:
  - name: "Delaware Code, Title 8, §§ 151, 156, 158, 202, 219, 224 (official text)"
    url: https://delcode.delaware.gov/title8/c001/index.html
  - name: "17 C.F.R. § 230.144 (eCFR)"
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-230/subject-group-ECFR4ebd6d5f2e0b9b1/section-230.144
  - name: "Cooley GO — Incorporation Package (Delaware) (coverage reference only; not copied)"
    url: https://cooleygo.com/documents/incorporation-package
last_verified: 2026-11-02
---

## About this template

**What the stock ledger is and why it matters.** The stock ledger is "1 or more records ... in which the names of all of the corporation's stockholders of record, the address and number of shares registered in the name of each such stockholder, and all issuances and transfers of stock of the corporation are recorded" (§ 219(c)). It is "the only evidence" of who may examine the stockholder list or vote at a meeting (§ 219(c)). It may be kept electronically, including on distributed ledgers, if it can produce the stockholder lists required by §§ 219 and 220, records the information required by §§ 156 (partly paid shares), 159 (collateral transfers), 217(a) (pledged shares) and 218 (voting trusts), and records transfers under UCC Article 8 (§ 224). A cap-table spreadsheet is not, by itself, a compliant stock ledger unless it meets these requirements and is maintained as the Company's official record.

**Two ways to evidence shares.**
1. *Uncertificated shares (market default).* The board resolves under § 158 that shares are uncertificated (the initial board consent does so). Within a reasonable time after each issuance or transfer, the Company must give the holder a written or electronic notice containing everything a certificate would have to state under §§ 151, 156, 202(a), 218(a) and 364 (§ 151(f)). Part B is that notice.
2. *Certificated shares.* A certificate signed by any two authorized officers (§ 158), with restrictions noted conspicuously (§ 202(a)). Part C is the form. Paper certificates create lost-certificate, escrow and transfer-mechanics burdens; use them only if a holder or investor requires.

**Legends are not decoration.** Under § 202(a), a transfer restriction — the bylaws' right of first refusal, the founder repurchase option, a market stand-off — is enforceable against a holder or transferee only if noted conspicuously on the certificate or contained in the § 151(f) notice, unless the person has actual knowledge. Omitting the notice is one of the most common formation defects; diligence in the first priced round will ask for copies of every § 151(f) notice.

**Note on § 116.** Section 116 (electronic documents, signatures and delivery; enacted 2019 by 82 Del. Laws c. 45 and amended 2020 by 82 Del. Laws c. 256) expressly does not apply to documents comprising part of the stock ledger or to certificates representing a security (§ 116(b)(2)–(3)). Electronic ledgers and notices are permitted by §§ 224 and 151(f) themselves; but do not assume § 116 validates an informal email as a ledger entry.

**What goes in the ledger for founders.** For each founder issuance: date of issuance (the RSPA closing date, which is also the "transfer" date that starts the 30-day 83(b) clock); board approval date and consent reference; shares; class; price per share; consideration (cash amount; description of assigned technology and board-determined value); vesting and repurchase legend; whether escrow or book-entry hold applies; date the 83(b) copy was received by the Company; § 151(f) notice date. For repurchases: date, shares, price, payment method, and whether the shares were retired or held as treasury shares.

**Common mistakes.**
- Shares shown on a cap table that were never authorized by a board resolution (a void issuance under *STAAR Surgical Co. v. Waggoner*, 588 A.2d 1130 (Del. 1991), and *Nevins v. Bryan*, 885 A.2d 233 (Del. Ch. 2005), absent ratification under § 204 or validation under § 205).
- Issuance entries dated before the bylaws or the board existed.
- No § 151(f) notice, or a notice without the ROFR and repurchase legends.
- Ledger and cap table that do not reconcile; total issued exceeding authorized shares (also void as to the excess absent § 204 ratification).

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `{{company_name}}` | Exact legal name | Northwind Robotics, Inc. | |
| `{{authorized_common_shares}}` | Authorized Common Stock | 10,000,000 | From the charter |
| `{{authorized_preferred_shares}}` | Authorized Preferred Stock | 0 | |
| `{{par_value}}` | Par value | $0.00001 | |
| `{{holder_name}}`, `{{holder_address}}`, `{{holder_email}}` | Registered holder | Alex Rivera | Exact name as it will appear in the ledger |
| `{{issuance_number}}` | Certificate number or book-entry number | CS-1 | Use a prefix by class (CS = common; PA = Series A Preferred) |
| `{{issued_shares}}` | Shares issued | 4,000,000 | |
| `{{issue_date}}` | Date of issuance | January 6, 2027 | RSPA closing date |
| `{{board_approval_date}}` | Date of approving board action | January 6, 2027 | |
| `{{consideration_description}}` | Consideration | $20.00 cash and assignment of Assigned Technology valued at $20.00 | Must match the board consent |
| `{{rspa_date}}` | Date of the restricted stock purchase agreement | January 6, 2027 | |
| `{{notice_date}}` | Date § 151(f) notice is given | January 8, 2027 | "Within a reasonable time"; best practice within a few days |
| `{{officer_one_name}}`, `{{officer_one_title}}`, `{{officer_two_name}}`, `{{officer_two_title}}` | Signing officers | Alex Rivera, CEO; Jordan Lee, Secretary | Certificates need two authorized officers |
| `{{assignee_name}}` | Transferee under the stock assignment | Northwind Robotics, Inc. | For repurchase escrow, replace with a blank line; keep the optional INSTRUCTION |
| `{{price_per_share}}` | Price per share | $0.00001 | |
| `{{board_consent_section}}` | Section of the initial board consent approving the issuance | 14 | |
| `{{company_address}}`, `{{company_notice_email}}` | Secretary contact for the notice | | |
| `{{voting_agreement_date}}` | Date of voting agreement (Legend 5) | | After first priced round |
| `{{partly_paid_total}}`, `{{partly_paid_amount_paid}}` | Partly paid share amounts (Legend 7) | | Rare for startups |
| `{{state_securities_legend}}` | Text of any state-required legend (Legend 8) | | Only if a permit or rule requires |

## Form

---

# PART A — STOCK LEDGER OF {{company_name}}

(maintained under 8 Del. C. §§ 219(c) and 224)

**A-1. Capitalization Summary** (update after each entry)

| Class / Series | Par Value | Authorized | Issued | Treasury | Outstanding | Reserved for Plan | Reserved for Convertible Securities |
|---|---|---|---|---|---|---|---|
| Common Stock | {{par_value}} | {{authorized_common_shares}} | | | | | |
| Preferred Stock (if any) | {{par_value}} | {{authorized_preferred_shares}} | | | | | |

**A-2. Register of Issuances**

| Entry No. | Certificate / Book-Entry No. | Holder (exact name) | Holder Address and Email | Class / Series | Shares Issued | Issue Date | Price per Share | Consideration (type and amount) | Board Approval (date; consent reference) | Agreement (type and date) | Restrictions / Legend Codes | § 151(f) Notice Date | 83(b) Copy Received (date) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | {{issuance_number}} | {{holder_name}} | {{holder_address}}; {{holder_email}} | Common | {{issued_shares}} | {{issue_date}} | {{price_per_share}} | {{consideration_description}} | {{board_approval_date}}; Initial Board Consent, Section {{board_consent_section}} | Founder RSPA, {{rspa_date}} | 1, 2, 3, 4 | {{notice_date}} | |

**A-3. Register of Transfers, Repurchases and Cancellations**

| Entry No. | Date | From (holder; certificate / book-entry no.) | To (transferee; new certificate / book-entry no.) | Class / Series | Shares | Nature (transfer; repurchase; forfeiture; cancellation; conversion) | Consideration | Authority (board consent; ROFR waiver; repurchase notice) | Treasury or Retired | Notice Given to New Holder (date) |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

**A-4. Holder Balances** (one row per holder per class; reconcile to A-1)

| Holder | Class / Series | Total Issued to Holder | Transferred Out | Repurchased / Cancelled | Current Balance | Vested (if subject to repurchase) | Unvested |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**A-5. Legend Codes**

| Code | Legend |
|---|---|
| 1 | Securities Act / state securities law restriction (Part B, Legend 1) |
| 2 | Bylaws right of first refusal, Section 7.6 (Part B, Legend 2) |
| 3 | Vesting, repurchase option and escrow or book-entry hold under stock purchase agreement (Part B, Legend 3) |
| 4 | Market stand-off (Part B, Legend 4) |
| 5 | Voting agreement or voting trust (Part B, Legend 5) |
| 6 | Public benefit corporation (Part B, Legend 6) |
| 7 | Partly paid shares (Part B, Legend 7) |
| 8 | Additional state securities law legend (Part B, Legend 8) |

**A-6. Pledges and Collateral Transfers** (§§ 159, 217(a))

| Date | Holder (pledgor) | Pledgee | Shares | Instrument | Voting rights retained by pledgor? | Release Date |
|---|---|---|---|---|---|---|
| | | | | | | |

**A-7. Certification of Ledger Custodian**

The undersigned certifies that the foregoing records constitute the stock ledger of {{company_name}} as of ________________, maintained in accordance with Sections 219 and 224 of the Delaware General Corporation Law.

______________________________
Name:
Title: Secretary

---

# PART B — NOTICE OF ISSUANCE OF UNCERTIFICATED SHARES

**{{company_name}}**

**(a Delaware corporation)**

**NOTICE OF ISSUANCE OF UNCERTIFICATED SHARES**

**Given under Section 151(f) of the Delaware General Corporation Law**

Date of this notice: {{notice_date}}

To: {{holder_name}} ("**Holder**")
Address: {{holder_address}}
Email: {{holder_email}}

You are the registered owner of uncertificated shares of capital stock of {{company_name}}, a Delaware corporation (the "**Company**"), as follows:

| Book-entry number | {{issuance_number}} |
|---|---|
| Class and series | Common Stock |
| Number of shares | {{issued_shares}} |
| Par value per share | {{par_value}} |
| Date of issuance or transfer | {{issue_date}} |
| Registered owner | {{holder_name}} |

**Statement of rights.** [[Alternative A: The Company is authorized to issue only one class of stock.]][[Alternative B: The Company is authorized to issue more than one class of stock (or more than one series of a class). The Company will furnish without charge to each stockholder who so requests the powers, designations, preferences and relative, participating, optional or other special rights of each class of stock or series thereof and the qualifications, limitations or restrictions of such preferences or rights. Requests may be directed to the Secretary of the Company at the address below.]]

**Restrictions and legends.** The shares described above are subject to the following restrictions, which are stated here as required by Sections 151(f) and 202(a) of the Delaware General Corporation Law and are binding on you and on any transferee:

**Legend 1 — Securities laws.** THE SHARES HAVE NOT BEEN REGISTERED UNDER THE SECURITIES ACT OF 1933, AS AMENDED (THE "ACT"), OR QUALIFIED OR REGISTERED UNDER THE SECURITIES LAWS OF ANY STATE, AND HAVE BEEN ACQUIRED FOR INVESTMENT AND NOT WITH A VIEW TO, OR IN CONNECTION WITH, THE SALE OR DISTRIBUTION THEREOF. THEY MAY NOT BE SOLD, OFFERED FOR SALE, PLEDGED, HYPOTHECATED OR OTHERWISE TRANSFERRED IN THE ABSENCE OF AN EFFECTIVE REGISTRATION STATEMENT UNDER THE ACT AND QUALIFICATION OR REGISTRATION UNDER APPLICABLE STATE SECURITIES LAWS, OR AN OPINION OF COUNSEL SATISFACTORY TO THE COMPANY THAT SUCH REGISTRATION AND QUALIFICATION ARE NOT REQUIRED.

**Legend 2 — Right of first refusal.** THE SHARES ARE SUBJECT TO A RIGHT OF FIRST REFUSAL IN FAVOR OF THE COMPANY OR ITS ASSIGNEES SET FORTH IN SECTION 7.6 OF THE BYLAWS OF THE COMPANY[[Optional: , AND TO A REQUIREMENT OF PRIOR APPROVAL OF THE BOARD OF DIRECTORS FOR ANY TRANSFER SET FORTH IN SECTION 7.6(m) OF THE BYLAWS]], A COPY OF WHICH MAY BE OBTAINED WITHOUT CHARGE FROM THE SECRETARY OF THE COMPANY. ANY TRANSFER IN VIOLATION OF THOSE PROVISIONS IS VOID.

[[Optional: **Legend 3 — Vesting and repurchase option.** THE SHARES ARE SUBJECT TO VESTING, TO AN OPTION OF THE COMPANY TO REPURCHASE UNVESTED SHARES, TO ESCROW OR BOOK-ENTRY CUSTODY ARRANGEMENTS PENDING VESTING, AND TO RESTRICTIONS ON TRANSFER, ALL AS SET FORTH IN A RESTRICTED STOCK PURCHASE AGREEMENT DATED {{rspa_date}} BETWEEN THE COMPANY AND THE ORIGINAL HOLDER, A COPY OF WHICH IS ON FILE WITH THE SECRETARY OF THE COMPANY. THOSE RESTRICTIONS ARE BINDING ON TRANSFEREES OF THE SHARES.]]

[[Optional: **Legend 4 — Market stand-off.** THE SHARES ARE SUBJECT TO A MARKET STAND-OFF (LOCK-UP) RESTRICTION ON TRANSFER FOR A PERIOD OF UP TO ONE HUNDRED EIGHTY (180) DAYS AFTER THE EFFECTIVE DATE OF THE COMPANY'S FIRST REGISTRATION STATEMENT UNDER THE ACT, AS SET FORTH IN AN AGREEMENT BETWEEN THE COMPANY AND THE ORIGINAL HOLDER, A COPY OF WHICH IS ON FILE WITH THE SECRETARY OF THE COMPANY. THOSE RESTRICTIONS ARE BINDING ON TRANSFEREES OF THE SHARES.]]

[[Optional: **Legend 5 — Voting agreement.** THE SHARES ARE SUBJECT TO A VOTING AGREEMENT, INCLUDING AN IRREVOCABLE PROXY, DATED {{voting_agreement_date}}, A COPY OF WHICH IS ON FILE WITH THE SECRETARY OF THE COMPANY. BY ACCEPTING ANY INTEREST IN THE SHARES, THE TRANSFEREE AGREES TO BE BOUND BY THAT AGREEMENT.]]

[[Optional: **Legend 6 — Public benefit corporation.** THE COMPANY IS A PUBLIC BENEFIT CORPORATION FORMED PURSUANT TO SUBCHAPTER XV OF THE DELAWARE GENERAL CORPORATION LAW.]]

[[Optional: **Legend 7 — Partly paid shares.** THESE SHARES ARE PARTLY PAID. THE TOTAL CONSIDERATION TO BE PAID FOR THEM IS {{partly_paid_total}} AND THE AMOUNT PAID AS OF THE DATE OF THIS NOTICE IS {{partly_paid_amount_paid}}.]]

[[Optional: **Legend 8 — Additional state securities law legend.** {{state_securities_legend}}]]

**Equal rights.** Except as otherwise expressly provided by law, the rights and obligations of holders of uncertificated shares and of holders of certificates representing shares of the same class and series are identical.

**Your responsibilities.** Keep this notice with your records. It is not a negotiable instrument and is not a certificate. Transfers may be registered only on the stock ledger of the Company in compliance with the restrictions above. Please notify the Secretary of any change of address or email address.

**{{company_name}}**

By: ______________________________
Name: {{officer_one_name}}
Title: {{officer_one_title}}

Secretary contact: {{company_address}}; {{company_notice_email}}

> **Drafting note:** Choose the legends that actually apply to the shares. For a founder issuance under the founder RSPA, Legends 1, 2, 3 and 4 always apply; Legend 5 applies once a voting agreement exists (it is usually added by a re-issued notice after the first priced round); if shares are instead deposited in a voting trust under § 218(a), the voting trust certificate or notice must state that fact, so adapt Legend 5; Legend 6 applies only to a PBC (§ 364 requires it to be stated "conspicuously"). Use Legend 8 only if a state securities qualification permit or condition requires a specific legend. Keep the capital letters or bold type: § 202(a) requires the restriction to be "noted conspicuously."

> **Verify:** If shares are issued under a California qualification permit or other state order (not typical for founders, who rely on § 25102(f)), confirm whether the permit or 10 Cal. Code Regs. § 260.141.11 requires a specific legend and delivery of a copy of the rule to the holder, and insert it as Legend 8.

---

# PART C — FORM OF STOCK CERTIFICATE (OPTIONAL)

> **Drafting note:** Use only if the Board has resolved that some shares are certificated. Two authorized officers sign (§ 158); signatures may be facsimile. Put the legends on the face, or on the face refer conspicuously to legends on the reverse. Number certificates sequentially by class (CS-1, CS-2 ...).

**Face of certificate**

Certificate No. {{issuance_number}}  {{issued_shares}} Shares

**{{company_name}}**

INCORPORATED UNDER THE LAWS OF THE STATE OF DELAWARE

[[Optional: A PUBLIC BENEFIT CORPORATION FORMED PURSUANT TO SUBCHAPTER XV OF THE DELAWARE GENERAL CORPORATION LAW]]

COMMON STOCK, PAR VALUE {{par_value}} PER SHARE

THIS CERTIFIES THAT **{{holder_name}}** is the registered holder of **{{issued_shares}}** fully paid and nonassessable shares of Common Stock of {{company_name}} (the "**Company**"), transferable only on the stock ledger of the Company by the holder in person or by duly authorized attorney upon surrender of this certificate properly endorsed or accompanied by a duly executed stock assignment, and subject to the restrictions on transfer described in the legends on this certificate. This certificate is not valid until countersigned by the transfer agent and registered by the registrar, if any.

**THE SHARES REPRESENTED BY THIS CERTIFICATE ARE SUBJECT TO RESTRICTIONS ON TRANSFER, A RIGHT OF FIRST REFUSAL AND [[Optional: A REPURCHASE OPTION]], AS SET FORTH IN THE LEGENDS ON THE REVERSE OF THIS CERTIFICATE.**

IN WITNESS WHEREOF, the Company has caused this certificate to be signed by its duly authorized officers on {{issue_date}}.

______________________________   ______________________________
{{officer_one_name}}, {{officer_one_title}}   {{officer_two_name}}, {{officer_two_title}}

**Reverse of certificate**

[[Alternative A: The Company is authorized to issue only one class of stock.]][[Alternative B: The Company will furnish without charge to each stockholder who so requests the powers, designations, preferences and relative, participating, optional or other special rights of each class of stock or series thereof and the qualifications, limitations or restrictions of such preferences or rights.]]

> **Drafting note:** Reproduce here, verbatim, each applicable legend from Part B (Legends 1 through 8).

**Assignment.** For value received, the undersigned sells, assigns and transfers to ______________________________ ________ shares of the capital stock represented by this certificate, and irrevocably constitutes and appoints ______________________________ as attorney-in-fact to transfer those shares on the books of the Company, with full power of substitution.

Dated: ________________  Signature: ______________________________

NOTICE: THE SIGNATURE TO THIS ASSIGNMENT MUST CORRESPOND WITH THE NAME AS WRITTEN UPON THE FACE OF THE CERTIFICATE IN EVERY PARTICULAR, WITHOUT ALTERATION OR ENLARGEMENT OR ANY CHANGE WHATEVER.

---

# PART D — STOCK ASSIGNMENT SEPARATE FROM CERTIFICATE

> **Drafting note:** This stand-alone stock power transfers shares on the books without endorsing a certificate, and works for uncertificated shares. For a founder's escrow under the RSPA, the founder signs it at closing with the assignee, share number and date left blank; the escrow agent completes it only when the Company exercises its repurchase option. The RSPA's Exhibit A is a version of this form tailored to that use. Do not reference the RSPA in the body of the assignment; that would put the repurchase terms in the transferee's chain of title unnecessarily.

**STOCK ASSIGNMENT SEPARATE FROM CERTIFICATE**

FOR VALUE RECEIVED, the undersigned sells, assigns and transfers unto {{assignee_name}} ______________ (________) shares of the Common Stock of {{company_name}}, a Delaware corporation (the "**Company**"), standing in the undersigned's name on the books of the Company [[Alternative A: represented by Certificate No. {{issuance_number}}]][[Alternative B: in uncertificated form under book-entry number {{issuance_number}}]], and irrevocably constitutes and appoints ______________________________ as attorney-in-fact to transfer those shares on the books of the Company, with full power of substitution in the premises.

Dated: ________________

______________________________
{{holder_name}}

[[Optional: **Spouse.** The undersigned spouse of the stockholder consents to this assignment and agrees that any community property or other marital interest in the shares is bound by it.

______________________________
Name of spouse:]]

[[Optional: **INSTRUCTION:** Do not fill in any blank other than the signature line(s). The purpose of this assignment is to enable the Company or its escrow agent to exercise a repurchase option or right of first refusal without requiring an additional signature from the stockholder.]]

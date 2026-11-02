---
id: secretarys-certificate
title: Secretary's Certificate (Charter, Bylaws, Resolutions, Incumbency) and Officer's Bring-Down Compliance Certificate
category: governance
stage: governance
signers: [Secretary or Assistant Secretary (certificate); a second officer (certifying the Secretary's incumbency and signature); Chief Executive Officer or other officer named in the transaction agreement (compliance certificate)]
authorities:
  - "8 Del. C. § 104 (definition of 'certificate of incorporation', including all amendments and other filed instruments)"
  - "8 Del. C. § 142(a) (officers; one officer records proceedings)"
  - "8 Del. C. § 103(c) (filing; Secretary of State certification)"
  - "8 Del. C. § 502(f) (no certificate of good standing while franchise tax is unpaid or the annual report is missing)"
  - "8 Del. C. § 391(a)(10)–(11) and Delaware Division of Corporations Fee Schedule (certified copies; good standing certificates)"
  - "8 Del. C. § 141(f), § 228 (consents certified as in full force)"
use_when: A financing, loan, bank account opening, acquisition, or commercial counterparty requires certified copies of the charter, bylaws, and authorizing resolutions and evidence of who may sign (incumbency), or the company must certify at closing that its representations remain true and conditions are satisfied (bring-down).
do_not_use_when: The counterparty supplies its own mandatory form (most banks do; complete it, using this template as a checklist), or the request is for a certificate of good standing (order it from the Delaware Division of Corporations; it is a state certificate, not an officer's certificate).
related: [board-consent-resolution-library, stockholder-consent-and-notice, board-consent-priced-financing, board-consent-convertible-financing, stock-purchase-agreement, bylaws, certificate-of-incorporation]
sources:
  - name: "Delaware Code, Title 8, §§ 103, 104, 142, 391, 502 (official text, read November 2, 2026)"
    url: https://delcode.delaware.gov/title8/c001/index.html
  - name: "Delaware Division of Corporations Fee Schedule, revised August 1, 2026 (good standing short form $50; long form $175; certified copies $50 plus $2 per page)"
    url: https://corpfiles.delaware.gov/Fee_Schedule/AugustFee2026.pdf
  - name: "NVCA Model Stock Purchase Agreement — closing conditions requiring secretary's and compliance certificates (reference only; not copied)"
    url: https://nvca.org/model-legal-documents/
last_verified: 2026-11-02
---

## About this template

**What it does.** Part 1 is a Secretary's Certificate that certifies, as of a closing, (1) the certificate of incorporation, (2) the bylaws, (3) the authorizing board and stockholder resolutions, and (4) the incumbency and specimen signatures of the officers signing the transaction documents. A second officer certifies the Secretary's own incumbency and signature, because no one can reliably certify their own authority. Part 2 is a short-form incumbency certificate for banks and counterparties. Part 3 is an Officer's Compliance (Bring-Down) Certificate certifying that representations remain true, covenants have been performed, and closing conditions are satisfied.

**Where it sits in a transaction.** A priced-round stock purchase agreement conditions each investor's obligation to close on delivery of a secretary's certificate and a compliance certificate (see templates/priced-financing/stock-purchase-agreement.md and the closing checklist). Venture lenders, acquirers, and banks require the same. Both certificates are signed at closing and dated the closing date, after the authorizing resolutions are effective and the restated charter (if any) has been filed.

**Statutory and practical points.**
- **"Certificate of incorporation" means all of it.** Under § 104, the term includes the original certificate and every amendment, certificate of designations, merger or conversion certificate, and certificate of correction or validation. Certify the full, current charter; a long-form good standing certificate ($175) lists every filed instrument and is the best way to confirm nothing is missing. A certified copy from the Division costs $50 per document plus $2 per page (fee schedule revised August 1, 2026).
- **Good standing.** The Division will not issue a good standing certificate if any franchise tax is unpaid or an annual report is missing (§ 502(f)). Order a short-form certificate ($50) dated within a few days of closing (investors and lenders typically require a date within five business days; some accept 30 days). For a company qualified elsewhere, the counterparty may also require good standing in the home state (California, New York, etc.).
- **Resolutions "in full force and effect."** Certify only resolutions actually adopted, in the exact form adopted, and confirm none has been amended or rescinded. If resolutions were adopted at a meeting, attach an extract of the minutes; if by consent, attach the consent with all signatures, or a statement that it was duly executed by all directors (§ 141(f)) or by the requisite stockholders with § 228(e) notice given.
- **Incumbency.** Each officer who signs a transaction document is listed with title and a specimen signature. Electronic specimen signatures are acceptable to most counterparties; banks sometimes require wet ink.
- **Capacity.** Officers sign "solely in [their] capacity as an officer and not individually." That limits contractual exposure; it does not protect against liability for knowingly false statements. The Secretary must actually check each statement against the minute book and the stock ledger.
- **Bring-down standard.** The compliance certificate repeats the purchase agreement's closing condition exactly: typically, representations "true and correct in all material respects" (except those qualified by materiality, which must be true in all respects) as of the closing as though made then, covenants performed in all material respects, and any specific conditions (no material adverse effect, required consents obtained). Do not paraphrase the condition; copy its standard from the agreement and cite the section.

**Common mistakes this form prevents.**
- Certifying a charter that omits a certificate of amendment or certificate of designations.
- Certifying resolutions that were never effective (a consent missing a director's signature).
- The Secretary certifying their own incumbency; the form adds a second officer.
- A compliance certificate signed before the restated charter is filed or before every condition is satisfied.
- A good standing certificate that predates a missed March 1 franchise tax deadline.

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `company_name` | Exact legal name | Northwind Robotics, Inc. | Shared |
| `secretary_name` | Secretary signing the certificate | Jordan Lee | Shared |
| `certifying_officer_name`, `certifying_officer_title` | Second officer certifying the Secretary | Alex Rivera; Chief Executive Officer | |
| `ceo_name`, `cfo_name`, `president_name` | Officers listed in incumbency | | Shared |
| `signatory_name`, `signatory_title` | Officer signing the compliance certificate | Alex Rivera; Chief Executive Officer | Shared |
| `closing_date` | Date of closing and of the certificates | July 1, 2027 | Shared |
| `transaction_agreement_title` | Agreement requiring the certificate | Series A Preferred Stock Purchase Agreement | |
| `transaction_agreement_date` | Date of that agreement | June 24, 2027 | |
| `counterparty_name` | Investors, lender, or other recipient | the Purchasers (as defined in the Purchase Agreement) | |
| `good_standing_date` | Date of the Delaware good standing certificate | June 29, 2027 | |
| `charter_certification_date` | Date of the Delaware certified copy of the charter | June 29, 2027 | |
| `board_resolution_date` | Date of the board resolutions | June 20, 2027 | |
| `stockholder_consent_date` | Date of the stockholder consent | June 22, 2027 | |
| `bring_down_section` | Section of the agreement stating the representation condition | Section 4.1 | |
| `covenant_section` | Section stating the performance condition | Section 4.2 | |
| `additional_conditions` | Other conditions certified | the Restated Certificate was filed and is in effect | |

## Form

---

# PART 1. SECRETARY'S CERTIFICATE OF {{company_name}}

**{{closing_date}}**

The undersigned, {{secretary_name}}, hereby certifies, solely in the undersigned's capacity as the duly elected and acting Secretary of {{company_name}}, a Delaware corporation (the "**Company**"), and not individually, to {{counterparty_name}} in connection with the {{transaction_agreement_title}} dated {{transaction_agreement_date}} (the "**Agreement**"), that:

1. **Certificate of Incorporation.** Attached hereto as Exhibit A is a true, correct, and complete copy of the Certificate of Incorporation of the Company, including all amendments thereto and all other instruments constituting the "certificate of incorporation" of the Company within the meaning of Section 104 of the General Corporation Law of the State of Delaware (the "**DGCL**"), as certified by the Secretary of State of the State of Delaware on {{charter_certification_date}}. Such Certificate of Incorporation is in full force and effect on the date hereof. No amendment or other document relating to or affecting the Certificate of Incorporation has been filed with the Secretary of State of the State of Delaware since {{charter_certification_date}}, no action has been taken by the Company, its Board of Directors (the "**Board**"), or its stockholders in contemplation of any such amendment or filing [[Optional: other than the filing contemplated by the Agreement]], and no proceeding for the dissolution, liquidation, merger, or conversion of the Company is pending or contemplated.

2. **Bylaws.** Attached hereto as Exhibit B is a true, correct, and complete copy of the Bylaws of the Company as in full force and effect on the date hereof and at all times since {{board_resolution_date}}. No amendment to the Bylaws is pending or contemplated.

3. **Board Resolutions.** Attached hereto as Exhibit C is a true, correct, and complete copy of resolutions duly adopted by the Board [[Alternative A: by unanimous written consent effective {{board_resolution_date}}, executed by every director then in office in accordance with Section 141(f) of the DGCL]] [[Alternative B: at a meeting duly called and held on {{board_resolution_date}}, at which a quorum was present and acting throughout]]. Such resolutions have not been amended, modified, or rescinded, are in full force and effect on the date hereof, and are the only resolutions of the Board or any committee thereof relating to the Agreement and the transactions contemplated thereby.

4. **Stockholder Approval.** [[Alternative A: Attached hereto as Exhibit D is a true, correct, and complete copy of resolutions duly adopted by the stockholders of the Company by written consent effective {{stockholder_consent_date}}, executed by the holders of outstanding stock having not less than the minimum number of votes necessary to take such action (including each required separate class or series vote) in accordance with Section 228 of the DGCL and the Certificate of Incorporation. Prompt notice of the action has been given, or will be given, to each stockholder entitled thereto under Section 228(e) of the DGCL. Such resolutions have not been amended, modified, or rescinded and are in full force and effect on the date hereof.]] [[Alternative B: No approval of the stockholders of the Company is required for the Company's execution, delivery, and performance of the Agreement.]]

5. **Good Standing.** Attached hereto as Exhibit E is a certificate of the Secretary of State of the State of Delaware dated {{good_standing_date}} stating that the Company is duly incorporated, validly existing, and in good standing under the laws of the State of Delaware. Since that date, the Company has not received any notice of, and the undersigned has no knowledge of, any change in such status.

6. **Incumbency.** Each person named below is a duly elected or appointed, qualified, and acting officer of the Company holding the office set forth opposite such person's name, has held such office at all times since the date the Agreement was signed, and the signature set forth opposite such person's name is such person's genuine signature (or electronic signature adopted with intent to sign). Each such officer is authorized to execute and deliver, on behalf of the Company, the Agreement and each other document to be delivered by the Company under it.

| Name | Office | Specimen Signature |
|---|---|---|
| {{ceo_name}} | Chief Executive Officer | ______________________________ |
| {{president_name}} | President | ______________________________ |
| {{cfo_name}} | Chief Financial Officer | ______________________________ |
| {{secretary_name}} | Secretary | ______________________________ |

IN WITNESS WHEREOF, the undersigned has executed this Secretary's Certificate as of {{closing_date}}.

______________________________
Name: {{secretary_name}}
Title: Secretary

**CERTIFICATION OF SECRETARY'S INCUMBENCY**

The undersigned, {{certifying_officer_name}}, solely in the undersigned's capacity as {{certifying_officer_title}} of the Company and not individually, hereby certifies that {{secretary_name}} is the duly elected or appointed, qualified, and acting Secretary of the Company, and that the signature set forth above is the genuine signature of such person.

______________________________
Name: {{certifying_officer_name}}
Title: {{certifying_officer_title}}

Date: {{closing_date}}

**Exhibits:** A — Certificate of Incorporation (certified by the Delaware Secretary of State); B — Bylaws; C — Board resolutions; D — Stockholder resolutions (or statement that none are required); E — Delaware good standing certificate.

> **Drafting note:** If the Secretary is the only officer (common at very early stages, where one founder holds every office), have a director other than the Secretary sign the incumbency certification, stating the director's capacity. Attach the exhibits in the exact form certified; do not re-type them.

---

# PART 2. SHORT-FORM INCUMBENCY CERTIFICATE (BANKS AND COUNTERPARTIES)

**{{company_name}} — Certificate of Incumbency**

The undersigned, solely in the undersigned's capacity as Secretary of {{company_name}}, a Delaware corporation (the "**Company**"), and not individually, certifies that each person named below is a duly elected or appointed and acting officer of the Company holding the office set forth opposite such person's name, that the signature opposite each name is such person's genuine signature, and that each such person is authorized, under resolutions of the Board of Directors of the Company adopted on {{board_resolution_date}} and in full force and effect, to act on behalf of the Company in the matters described in those resolutions.

| Name | Office | Specimen Signature |
|---|---|---|
| {{ceo_name}} | Chief Executive Officer | ______________________________ |
| {{cfo_name}} | Chief Financial Officer | ______________________________ |

______________________________
Name: {{secretary_name}}
Title: Secretary
Date: {{closing_date}}

---

# PART 3. OFFICER'S COMPLIANCE (BRING-DOWN) CERTIFICATE

**{{company_name}} — Compliance Certificate**

**{{closing_date}}**

The undersigned, {{signatory_name}}, hereby certifies, solely in the undersigned's capacity as {{signatory_title}} of {{company_name}}, a Delaware corporation (the "**Company**"), and not individually, pursuant to the {{transaction_agreement_title}} dated {{transaction_agreement_date}} (the "**Agreement**"), that:

1. **Representations and Warranties.** The representations and warranties of the Company contained in the Agreement (as qualified by the disclosure schedule delivered under the Agreement) are true and correct in all respects as of the date hereof, as though made on and as of the date hereof (except to the extent any such representation or warranty speaks as of an earlier date, in which case it is true and correct as of such earlier date), to the extent and in the manner required by {{bring_down_section}} of the Agreement.

2. **Covenants.** The Company has performed and complied with all covenants, agreements, obligations, and conditions contained in the Agreement that are required to be performed or complied with by the Company on or before the date hereof, to the extent and in the manner required by {{covenant_section}} of the Agreement.

3. **Other Conditions.** {{additional_conditions}}.

4. **Defined Terms.** Capitalized terms used but not defined in this Compliance Certificate have the meanings given to them in the Agreement.

IN WITNESS WHEREOF, the undersigned has executed this Compliance Certificate as of {{closing_date}}.

______________________________
Name: {{signatory_name}}
Title: {{signatory_title}}

> **Drafting note:** Replace items 1 and 2 with the exact materiality standards in the Agreement's closing-condition sections if the Agreement states them differently (for example, "true and correct in all material respects, except for representations qualified by materiality, which shall be true and correct in all respects"). Before signing, the officer should confirm with counsel and the CFO that nothing has occurred since signing that makes a representation untrue (new litigation, a key employee departure, a cap table change). If something has, update the disclosure schedule as the Agreement permits, or obtain a waiver from the counterparty; never sign a knowingly false certificate.

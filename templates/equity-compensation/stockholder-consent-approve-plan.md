---
id: stockholder-consent-approve-plan
title: Stockholder Written Consent Approving Equity Incentive Plan
category: equity-compensation
stage: equity
signers: [Stockholders holding at least the minimum voting power required (majority of outstanding voting power, plus any separate class or series vote required by the charter or investor agreements)]
authorities:
  - "8 Del. C. § 228(a), (c), (d), (e) (stockholder action by written consent; 60-day delivery window; delivery methods; prompt notice)"
  - "8 Del. C. § 213(b) (record date for consents), § 216 (default vote), § 116 (electronic signatures)"
  - "26 U.S.C. § 422(b)(1); Treas. Reg. §§ 1.422-2(b)(2)–(4), 1.422-3"
  - "Cal. Code Regs. tit. 10, §§ 260.140.41(g), 260.140.42(e)"
use_when: Stockholders are approving a newly adopted equity incentive plan (or a replacement plan) within 12 months of Board adoption.
do_not_use_when: Approving only a share-reserve increase or a repricing (use plan-share-increase-and-option-amendment), or approving 280G payments (use a separate 280G stockholder disclosure and consent).
related: [equity-incentive-plan, board-consent-adopt-plan, board-consent-equity-grants, plan-share-increase-and-option-amendment]
sources:
  - name: "8 Del. C. § 228 (Delaware Code Online, subch. VII)"
    url: https://delcode.delaware.gov/title8/c001/sc07/index.html
  - name: "Treas. Reg. § 1.422-3 (eCFR), method of stockholder approval"
    url: https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.422-3
  - name: "Cal. Code Regs. tit. 10, § 260.140.41 (Cornell LII)"
    url: https://www.law.cornell.edu/regulations/california/10-CCR-260.140.41
  - name: "Law-firm stockholder consent forms (Cooley GO, Clerky), structure only; no text copied"
    url: https://www.cooleygo.com/
last_verified: 2026-11-02
---

## About this template

**What it does.** Stockholders approve the Plan by written consent under 8 Del. C. § 228, and the Company then sends prompt notice to non-consenting stockholders under § 228(e).

**Why the approval is needed (state it correctly).** The consent recites the actual legal reasons:

1. **ISO qualification.** I.R.C. § 422(b)(1) requires that ISOs be granted under a plan approved by stockholders within 12 months before or after Board adoption. Treas. Reg. § 1.422-2(b)(3)–(4) requires that the stockholders approve the maximum aggregate number of shares issuable as ISOs and the class of employees eligible. The approval must follow the method and vote that state law, the charter, and the bylaws require (Treas. Reg. § 1.422-3); a § 228 written consent qualifies.
2. **California exemption.** 10 CCR §§ 260.140.41(g) and 260.140.42(e) require approval by "a majority of the outstanding securities entitled to vote" (not merely a majority of votes cast) by the later of 12 months before or after adoption or before or within 12 months after the first California grant. California securities issued before approval are not counted toward the approval and must be rescinded if approval fails.
3. **Charter and investor agreements.** Many venture charters and voting agreements require a separate Preferred vote for any new plan or reserve increase.

**Rule 701 does not require stockholder approval.** Do not describe this consent as being "for purposes of Rule 701." That error is common in simple startup forms and is a diligence flag.

**Vote required.** Unless the charter provides otherwise, a § 228 consent must be signed by holders of outstanding stock having at least the minimum number of votes that would be necessary at a meeting at which all shares entitled to vote were present and voted (§ 228(a)). For plan approval, that is generally a majority of the outstanding voting power (Common and Preferred voting together on an as-converted basis), plus any separate class or series vote required by the charter's protective provisions. Check the charter: a charter may prohibit action by written consent (§ 228(a) "unless otherwise provided in the certificate of incorporation").

**Mechanics.**

- **Record date.** If the Board has not fixed a record date for the consent, the record date is the first date on which a signed consent is delivered to the Company (8 Del. C. § 213(b)).
- **60-day window.** Consents from enough holders must be delivered within 60 days after the first consent is delivered (§ 228(c)). A signer may make the consent effective at a future time up to 60 days later.
- **Delivery.** To the principal place of business, to the officer with custody of the minute book, to the registered office by hand or certified mail, or electronically to an information processing system the Company designates (§ 228(d)(1)). A consent signed electronically under § 116 and delivered under clauses (i)–(iii) must be reproduced and delivered in paper form (§ 228(d)(2)).
- **Prompt notice.** If the action is taken by less than unanimous consent, give prompt notice to the stockholders as of the record date who did not consent and who would have been entitled to notice of a meeting (§ 228(e)). Exhibit B is a form. Send it within days, not weeks.
- **Effective date.** This consent states a definite effective date. The consent is effective on that date only if consents from enough holders have been delivered by then; if they arrive later (but within the 60-day window), the action is effective when the last required consent is delivered, and the ISO 12-month window is measured from Board adoption regardless.

**Common mistakes.** Collecting consents from fewer than a majority of outstanding voting power; forgetting a separate Preferred class vote; counting California restricted shares issued before approval; letting the 12-month ISO window lapse; failing to give § 228(e) notice; approving "the Plan" without stating the share numbers or eligible class.

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `{{company_name}}` | Company legal name | Northwind Robotics, Inc. | Shared |
| `{{plan_name}}` | Plan title | 2027 Equity Incentive Plan | Shared |
| `{{board_adoption_date}}` | Date of Board adoption | February 1, 2027 | Shared |
| `{{stockholder_approval_date}}` | Effective date of this consent | February 3, 2027 | Shared; within 12 months of adoption |
| `{{plan_reserve_shares}}` | Share Reserve | 1,500,000 | Shared |
| `{{iso_limit_shares}}` | ISO limit | 1,500,000 | Must match the Plan |
| `{{stockholder_name_1}}`, `{{stockholder_shares_1}}`, `{{stockholder_class_1}}` (and `_2`, `_3`, … for each additional signer) | Each consenting holder, shares, and class | Alex Rivera; 4,000,000; Common | One row per signer |
| `{{stockholder_name_2}}`, `{{stockholder_shares_2}}`, `{{stockholder_class_2}}`, `{{stockholder_name_3}}` | Additional signers | Jordan Lee; 4,000,000; Common | Add or delete rows |
| `{{stockholder_name_n}}` | Entity stockholder signing through an officer | Example Ventures Fund I, L.P. | Optional entity signature block |
| `{{record_date}}` | Record date for the consent | February 3, 2027 | § 213(b) |
| `{{secretary_name}}` | Secretary sending notice | Jordan Lee | Shared |
| `{{company_address}}` | Company principal place of business | | Shared |

---

## Form

# ACTION BY WRITTEN CONSENT OF THE STOCKHOLDERS OF {{company_name}}

**Approval of {{plan_name}}**

**Effective Date: {{stockholder_approval_date}}**

The undersigned stockholders of {{company_name}}, a Delaware corporation (the "**Company**"), holding shares of the Company's outstanding capital stock having not less than the minimum number of votes that would be necessary to authorize or take the following actions at a meeting at which all shares entitled to vote on them were present and voted [[Optional: , including the holders of at least the percentage of the outstanding shares of Preferred Stock required by Section ___ of the Company's Certificate of Incorporation, voting as a separate class]], acting under Section 228 of the Delaware General Corporation Law (the "**DGCL**") and the Company's Certificate of Incorporation and Bylaws, consent to the adoption of the following resolutions, effective as of the Effective Date stated above, without a meeting, without prior notice, and without a vote.

## 1. APPROVAL OF THE PLAN

**WHEREAS**, on {{board_adoption_date}}, the Board of Directors of the Company (the "**Board**") adopted the {{plan_name}} in the form attached as **Exhibit A** (the "**Plan**"), subject to stockholder approval, and recommended that the stockholders approve it;

**WHEREAS**, the Plan provides that (a) the maximum aggregate number of shares of the Company's Common Stock that may be issued under the Plan is {{plan_reserve_shares}} shares, subject to adjustment for changes in capitalization as provided in the Plan; (b) the maximum aggregate number of shares that may be issued on the exercise of incentive stock options is {{iso_limit_shares}} shares, subject to the same adjustment; and (c) all employees of the Company and of any present or future parent or subsidiary corporation of the Company (as defined in Sections 424(e) and (f) of the Internal Revenue Code of 1986, as amended (the "**Code**")) are eligible to receive incentive stock options, and employees, directors, and consultants of the Company and its affiliates are eligible to receive other awards;

**WHEREAS**, stockholder approval of the Plan is required (a) under Section 422(b)(1) of the Code, so that options granted under the Plan may qualify as incentive stock options, which requires approval by the stockholders within twelve (12) months before or after the date the Board adopted the Plan, by the method and degree of approval described in Treasury Regulations Section 1.422-3; (b) under Sections 260.140.41(g) and 260.140.42(e) of Title 10 of the California Code of Regulations, for awards to residents of California in reliance on Section 25102(o) of the California Corporations Code, which require approval by a majority of the outstanding securities entitled to vote; [[Optional: and (c) under Section ___ of the Company's Certificate of Incorporation [and Section ___ of the Voting Agreement dated ___]]]; and

**WHEREAS**, the stockholders acknowledge that Rule 701 under the Securities Act of 1933, as amended, does not itself require stockholder approval of the Plan.

**NOW, THEREFORE, BE IT RESOLVED**, that the Plan, in the form attached as Exhibit A, is approved in all respects, including (a) the reservation of {{plan_reserve_shares}} shares of Common Stock for issuance under the Plan, (b) the maximum of {{iso_limit_shares}} shares of Common Stock that may be issued on the exercise of incentive stock options, and (c) the designation of the employees eligible to receive incentive stock options, in each case as set out in the Plan;

**RESOLVED FURTHER**, that this approval constitutes the stockholder approval of the Plan for purposes of Section 422(b)(1) of the Code and Treasury Regulations Sections 1.422-2(b)(2) and 1.422-3, and for purposes of Sections 260.140.41(g) and 260.140.42(e) of Title 10 of the California Code of Regulations [[Optional: , and the approval of the holders of Preferred Stock required by Section ___ of the Certificate of Incorporation]];

**RESOLVED FURTHER**, that all awards granted under the Plan before the Effective Date, to the extent consistent with the Plan, are ratified and confirmed, and options granted before the Effective Date that were designated as incentive stock options will continue to be treated as incentive stock options to the extent they otherwise qualify; and

**RESOLVED FURTHER**, that the officers of the Company are each authorized and directed to take all actions and to execute and deliver all documents that they determine necessary or advisable to carry out the purposes of these resolutions, including giving the notice required by Section 228(e) of the DGCL.

> **Drafting note:** Do not count, toward the majority needed for California purposes, shares that were issued under the Plan to California residents before this approval (10 CCR §§ 260.140.41(g), 260.140.42(e)). If any such shares exist, prepare a separate tally excluding them. Shares issued under the Plan to non-California holders, and founder shares issued outside the Plan, may be counted.

## 2. GENERAL

**2.1 Effectiveness.** This consent is effective as of the Effective Date, provided that by that date the Company has received consents signed by holders of a sufficient number of shares to take the actions described in it. If consents from a sufficient number of holders are delivered after the Effective Date, this consent will be effective on the date the last consent needed to take the action is delivered, provided that it is delivered within sixty (60) days after the first date on which a consent is delivered to the Company, as required by Section 228(c) of the DGCL.

**2.2 Record Date.** The record date for determining the stockholders entitled to consent to the actions in this consent is {{record_date}}, [[Alternative A: the date fixed by the Board under Section 213(b) of the DGCL]] [[Alternative B: the first date on which a signed consent was delivered to the Company, as provided in Section 213(b) of the DGCL]].

**2.3 Revocability.** Any consent may be revoked by the signing stockholder by written notice delivered to the Company before the time the consents of holders of the minimum number of shares required have been delivered.

**2.4 Counterparts; Electronic Signature and Delivery.** This consent may be executed in counterparts, each of which is an original and all of which together are one instrument. Each stockholder may sign by electronic signature and deliver this consent by electronic transmission to the information processing system designated by the Company for that purpose, in accordance with Sections 116 and 228(d) of the DGCL. A copy, facsimile, or other reliable reproduction of this consent may be used in place of the original for any purpose for which the original could be used.

**2.5 Filing.** This consent will be filed with the minutes of the proceedings of the stockholders of the Company.

| Stockholder | Class / Series | Number of Shares | Signature | Date signed |
|---|---|---|---|---|
| {{stockholder_name_1}} | {{stockholder_class_1}} | {{stockholder_shares_1}} | ______________________ | __________ |
| {{stockholder_name_2}} | {{stockholder_class_2}} | {{stockholder_shares_2}} | ______________________ | __________ |
| [[Optional: {{stockholder_name_3}}]] | | | ______________________ | __________ |

*For an entity stockholder:*

{{stockholder_name_n}}
By: ______________________________
Name:
Title:

> **Drafting note:** Attach a vote tally (as a working paper, not part of the consent) showing total outstanding voting power on the record date, the voting power of each signer, and any separate class vote. For Preferred voting on an as-converted basis, use the conversion rate in effect on the record date.

**Exhibit A:** {{plan_name}}

---

## EXHIBIT B — NOTICE OF ACTION BY WRITTEN CONSENT OF STOCKHOLDERS (8 Del. C. § 228(e))

{{company_name}}
{{company_address}}

Date: ____________________

To the Stockholders of {{company_name}} who did not sign the written consent described below:

Under Section 228(e) of the Delaware General Corporation Law, you are notified that on {{stockholder_approval_date}}, the stockholders of {{company_name}}, a Delaware corporation (the "**Company**"), holding the requisite number of shares of the Company's outstanding capital stock, acted by written consent without a meeting to approve the Company's {{plan_name}} (the "**Plan**"), including the reservation of {{plan_reserve_shares}} shares of Common Stock for issuance under the Plan, the maximum of {{iso_limit_shares}} shares that may be issued under incentive stock options, and the class of employees eligible for incentive stock options. The record date for determining the stockholders entitled to consent was {{record_date}}.

No action is required of you. A copy of the Plan is available on request from the Company's Secretary at the address above [[Optional: or is enclosed with this notice]].

Sincerely,

______________________________
{{secretary_name}}, Secretary

> **Drafting note:** Send the notice by a method permitted by 8 Del. C. § 232 (including electronic transmission to a stockholder who has not objected under § 232). Keep a record of the date and method of delivery with the minute book. § 228(e) does not require the notice to include the Plan, but making it available avoids questions from minority holders.

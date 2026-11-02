---
id: one-way-nda
title: Nondisclosure Agreement (Company as Discloser)
category: commercial
stage: commercial
signers: [Company (by an officer), Recipient (an individual, or an entity by an authorized signatory)]
authorities:
  - "18 U.S.C. §§ 1836–1839 (Defend Trade Secrets Act); 18 U.S.C. § 1839(3) (reasonable measures)"
  - "18 U.S.C. § 1833(b) (whistleblower immunity notice; § 1833(b)(4) extends 'employee' to contractors and consultants)"
  - "6 Del. C. §§ 2001–2009 (Delaware Uniform Trade Secrets Act)"
  - "17 C.F.R. § 240.21F-17(a) (SEC whistleblower communications)"
  - "42 U.S.C. §§ 19401–19404 (Speak Out Act)"
  - "29 U.S.C. § 157 (NLRA § 7) (applies once the Recipient is a non-supervisory employee)"
  - "Cal. Gov. Code § 12964.5 (agreements related to employment may not restrict disclosure of information about unlawful acts in the workplace); Cal. Lab. Code § 232.5 (disclosure of working conditions); Cal. Bus. & Prof. Code § 16600"
  - "15 C.F.R. § 734.13(b) (deemed exports)"
  - "15 U.S.C. § 7001 et seq. (E-SIGN); 6 Del. C. ch. 12A (Delaware UETA)"
use_when: Only the Company will disclose confidential information — to a job candidate (late-stage interviews, take-home technical exercises, executive recruiting), a prospective vendor or service provider, or a prospective channel, integration, or distribution partner.
do_not_use_when: Both sides will disclose (use mutual-nda); the recipient will actually perform work or create deliverables (use consulting-agreement, which includes IP assignment, or an offer letter plus ciiaa-employee); the recipient is an investor (most will not sign).
related: [mutual-nda, ciiaa-employee, offer-letter, consulting-agreement]
sources:
  - name: "18 U.S.C. § 1833 (Cornell LII) — immunity notice language tracked"
    url: https://www.law.cornell.edu/uscode/text/18/1833
  - name: "California Government Code § 12964.5 (leginfo) — required carve-out for employment-related agreements"
    url: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=12964.5
  - name: "Cooley GO — NDA forms (reference only; not copied)"
    url: https://www.cooleygo.com/documents/
  - name: "Clerky — NDA (reference for coverage only; not copied)"
    url: https://www.clerky.com/
last_verified: 2026-11-02
---

## About this template

**What it does.** A one-way (unilateral) NDA protects the Company's information when the Company is the only party disclosing. It is shorter and more protective than the mutual form because the Recipient takes on obligations without receiving reciprocal ones. Three recurring uses:

1. **Candidates.** Late-stage candidates (especially executives and senior engineers) often need to see the roadmap, financials, or architecture. A candidate NDA lets the Company share that before the offer and CIIAA are signed. It is *not* a substitute for the CIIAA: it contains no invention assignment, so a candidate should never be asked to do substantive work under it. If a candidate will do a paid work trial or a take-home exercise the Company may use, sign a short consulting agreement with an IP assignment instead, and pay at least minimum wage for the time (an unpaid "work trial" of productive work by a prospective employee can create FLSA and state wage-and-hour exposure).
2. **Vendors and service providers** who need access to Company systems or data to scope or perform a project, before the master services agreement (which will carry its own confidentiality and data-protection terms) is signed.
3. **Prospective partners** that will receive product, pricing, or integration details while the Company receives little or nothing in return.

**Statutory overlay.**
- *Trade secrets* require "reasonable measures" to keep the information secret (18 U.S.C. § 1839(3)(A); 6 Del. C. § 2001(4)). A signed NDA plus access controls is the standard evidence.
- *DTSA notice.* Required in an agreement "with an employee that governs the use of a trade secret or other confidential information" (18 U.S.C. § 1833(b)(3)(A)); "employee" includes an individual contractor or consultant (§ 1833(b)(4)). A candidate is not yet an employee, but candidates frequently become employees, and the notice is required if the agreement later governs an employee's use of trade secrets, so the form includes it whenever the Recipient is an individual. Omission forfeits exemplary damages and attorney fees against that individual (§ 1833(b)(3)(C)).
- *Protected activity.* Section 5.1 preserves communications with government agencies (SEC Rule 21F-17(a) applies to "any person"), testimony, and disclosures protected by the Speak Out Act (42 U.S.C. §§ 19401–19404). Once a candidate is hired, NLRA § 7 protects non-supervisory employees' discussion of wages and working conditions; the CIIAA, not this NDA, governs at that point.
- *California candidates.* An agreement "related to an employee's employment" entered into as a condition of employment may not deny the right to disclose information about unlawful acts in the workplace, and a provision restricting disclosure of workplace conditions must include the sentence required by Cal. Gov. Code § 12964.5(a)(1)(B)(ii). A candidate NDA is close enough to that line that the form includes the California sentence as an optional clause for California-based candidates. California also prohibits employers from restraining employee disclosure of their own working conditions (Lab. Code § 232.5) and voids non-competes and employee non-solicits (Bus. & Prof. Code § 16600); this form contains neither.

**Market positions and defaults.**

| Issue | Company-favorable | Market | Recipient-favorable | This form |
|---|---|---|---|---|
| Definition | Everything disclosed, marked or not | Marked or reasonably understood to be confidential | Marked only | Market |
| Term | Perpetual | 3–5 years after disclosure ends, trade secrets for as long as protected | 1–2 years | 5 years (variable) plus trade-secret tail |
| Residuals | None | None | Residuals clause | None (do not accept a residuals clause in a one-way NDA) |
| Feedback | Assignment | Perpetual royalty-free license | Silent | License |
| Equitable relief | No bond, irreparable harm stipulated | Entitled to seek equitable relief without proving damages | Silent | Market |

**Candidate-specific points.**
- **Third-party information.** Section 6 prohibits the candidate from bringing or disclosing a current or former employer's confidential information. This protects the Company against trade-secret contamination claims, which are a common source of litigation when engineers move between competitors.
- **No offer of employment.** Section 8.2 makes clear that the NDA is not an offer, a promise of employment, or a contract for a definite term.
- **Do not include** non-competes, non-solicits, or assignment of ideas the candidate already has. Those belong (if anywhere) in the CIIAA.

**Common mistakes the form avoids.** Using an NDA as a substitute for an IP assignment; omitting the DTSA notice for individuals; no return-or-destroy mechanics; a fixed term that lets trade secrets lapse; omitting the third-party information covenant for candidates; and failing to restrict pasting Confidential Information into public generative-AI tools (Section 3.6).

**Deadlines triggered by signing.** None by statute. Calendar the end of the Disclosure Period and any return-or-destroy request.

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `company_name` | Company's exact legal name | Northwind Robotics, Inc. | |
| `company_address` | Company's principal place of business | 100 Example Street, Suite 200, Austin, Texas 78701 | |
| `company_notice_email` | Company's legal notice email | legal@northwind.example | |
| `signatory_name`, `signatory_title` | Company officer signing | Alex Rivera, Chief Executive Officer | |
| `recipient_name` | Recipient's exact legal name | Morgan Okafor, or Harbor Data Services LLC | |
| `recipient_description` | Entity type and jurisdiction, or "an individual" | a Colorado limited liability company | |
| `recipient_address`, `recipient_email` | Recipient's notice address and email | | |
| `recipient_signatory_name`, `recipient_signatory_title` | For an entity Recipient | | Delete for individuals |
| `effective_date` | Effective date | December 1, 2027 | |
| `disclosure_start_date` | First date covered disclosures were made | December 1, 2027 | May precede the Effective Date if disclosures already began |
| `purpose_description` | The Purpose | evaluating the Recipient's potential employment with the Company as Head of Platform Engineering | Draft narrowly |
| `disclosure_period_months` | Disclosure window | 12 | |
| `confidentiality_years` | Survival after Disclosure Period | 5 | |
| `governing_law_state` | Governing law | Delaware; for an individual California resident, California | See Cal. Lab. Code § 925 once employed |
| `forum` | Exclusive forum | the state and federal courts located in the State of Delaware | For an individual, prefer the county where the individual resides |

## Form

---

# NONDISCLOSURE AGREEMENT

This Nondisclosure Agreement (this "**Agreement**") is entered into as of {{effective_date}} (the "**Effective Date**") by and between {{company_name}}, a Delaware corporation (the "**Company**"), and {{recipient_name}}, {{recipient_description}} (the "**Recipient**").

The Company is willing to disclose certain of its non-public information to the Recipient solely for the purpose of {{purpose_description}} (the "**Purpose**"), on the condition that the Recipient agrees to the terms of this Agreement. In consideration of the Company's disclosure of Confidential Information and the mutual covenants in this Agreement, the receipt and sufficiency of which are acknowledged, the Company and the Recipient agree as follows:

## 1. Definitions

**1.1 "Affiliate"** means any entity that directly or indirectly controls, is controlled by, or is under common control with the Company, where "control" means ownership of more than fifty percent (50%) of the voting interests of the entity or the power to direct its management and policies.

**1.2 "Confidential Information"** means all non-public information, in any form or medium (whether oral, written, electronic, visual, or by demonstration or inspection), that is disclosed or made available by or on behalf of the Company or its Affiliates to the Recipient or any Permitted Recipient during the Disclosure Period, whether before or after the Effective Date, and that is marked or identified as confidential or that a reasonable person would understand to be confidential given the nature of the information and the circumstances of disclosure, including: source code, object code, algorithms, models, model weights, data sets, inventions, designs, specifications, know-how, and research and development; product plans and roadmaps; pricing, costs, and financial information and projections; capitalization, fundraising, and investor information; customer, supplier, and partner identities and terms; personnel and compensation information of persons other than the Recipient; security practices, credentials, and system architecture; business plans and strategies; the existence and content of discussions concerning the Purpose; and all notes, analyses, compilations, and other materials prepared by or for the Recipient to the extent they contain or reflect any of the foregoing ("**Derivatives**").

**1.3 "Disclosure Period"** means the period beginning on {{disclosure_start_date}} and ending on the earlier of (a) the date that is {{disclosure_period_months}} months after the Effective Date and (b) the date the Company notifies the Recipient in writing that the Disclosure Period has ended.

**1.4 "Law"** means any applicable statute, regulation, rule, ordinance, order, judgment, decree, or subpoena.

**1.5 "Permitted Recipients"** means, if the Recipient is an entity, those of the Recipient's directors, officers, employees, and legal counsel who have a need to know Confidential Information for the Purpose. If the Recipient is an individual, there are no Permitted Recipients other than the Recipient's own legal counsel and, solely as to the terms of any proposed compensation, the Recipient's spouse or domestic partner and tax and financial advisors.

**1.6 "Trade Secret"** means Confidential Information that constitutes a trade secret under 18 U.S.C. § 1839(3) or the trade secret law of any applicable jurisdiction.

## 2. Exclusions

**2.1 Excluded Information.** Confidential Information does not include information that the Recipient can demonstrate by competent written evidence (a) is or becomes generally available to the public other than through a breach of this Agreement by the Recipient or any Permitted Recipient; (b) was known to the Recipient, without an obligation of confidentiality, before its disclosure by or on behalf of the Company; (c) is received by the Recipient on a non-confidential basis from a third party that, to the Recipient's knowledge after reasonable inquiry, is not prohibited from disclosing it; or (d) is independently developed by the Recipient without use of or reference to the Confidential Information.

**2.2 Combinations; Burden.** Confidential Information is not within an exclusion merely because individual features of it, or more general information embracing it, are within an exclusion. The Recipient bears the burden of proving that an exclusion applies.

## 3. Obligations of the Recipient

**3.1 Use Restriction.** The Recipient shall use Confidential Information solely for the Purpose and for no other purpose, including, without limitation, to compete with the Company, to develop, train, or improve any product, service, or machine-learning model, to solicit the Company's customers, suppliers, or employees, or to file or prosecute any patent application.

**3.2 Nondisclosure.** The Recipient shall not disclose Confidential Information to any person other than Permitted Recipients, except as permitted by Article 4 or Article 5 or with the Company's prior written consent.

**3.3 Permitted Recipients.** The Recipient shall inform each Permitted Recipient of the confidential nature of the Confidential Information before disclosure, shall ensure that each Permitted Recipient (other than legal counsel bound by professional duties of confidentiality) is bound by written confidentiality and restricted-use obligations at least as protective as those in this Agreement, and is responsible for any act or omission of a Permitted Recipient that would breach this Agreement if committed by the Recipient.

**3.4 Standard of Care; Security.** The Recipient shall protect Confidential Information with at least the degree of care it uses to protect its own confidential information of similar importance, and in no event less than reasonable care. The Recipient shall comply with any reasonable security instructions the Company provides in writing, including restrictions on downloading, printing, or copying information made available through a data room or the Company's systems, and shall not attempt to access any Company system, account, or data beyond the access the Company expressly grants.

**3.5 No Reverse Engineering; Copies.** The Recipient shall not decompile, disassemble, reverse engineer, or analyze the composition of any software, hardware, prototype, or other item provided by the Company, or attempt to do so. The Recipient shall not copy Confidential Information except as reasonably necessary for the Purpose, and every copy shall retain all proprietary legends.

**3.6 Third-Party Tools.** The Recipient shall not upload, paste, or otherwise input any Confidential Information into any generative artificial-intelligence tool, translation service, or other third-party application or service, unless (a) the Company has approved the tool in writing, or (b) the tool is provided or administered by the Recipient's organization under terms that prohibit the provider from retaining the input beyond the session, using it to train or improve any model, or disclosing it to any other person.

**3.7 Notice of Unauthorized Use or Disclosure.** The Recipient shall notify the Company in writing promptly (and in any event within three (3) business days) after becoming aware of any actual or reasonably suspected unauthorized access to, or use or disclosure of, Confidential Information, and shall cooperate with the Company to regain possession of it and prevent further unauthorized access, use, or disclosure.

## 4. Compelled Disclosure

**4.1 Notice and Cooperation.** If the Recipient or any Permitted Recipient is required by Law to disclose any Confidential Information, the Recipient shall, to the extent legally permitted, give the Company prompt written notice so that the Company may seek, at its expense, a protective order or other remedy, and shall reasonably cooperate with those efforts.

**4.2 Limited Disclosure.** If no protective order or other remedy is obtained, the Recipient may disclose only the portion of the Confidential Information that its legal counsel advises is legally required to be disclosed and shall use reasonable efforts to obtain confidential treatment for it. Information so disclosed remains Confidential Information for all other purposes.

## 5. Protected Disclosures; Defend Trade Secrets Act Notice

**5.1 Protected Disclosures.** Nothing in this Agreement prohibits or restricts the Recipient from (a) reporting a possible violation of Law to, filing a charge or complaint with, communicating with, or participating in an investigation or proceeding conducted by any federal, state, or local governmental agency or commission, including the Securities and Exchange Commission, the Equal Employment Opportunity Commission, the National Labor Relations Board, the Occupational Safety and Health Administration, or the Department of Justice, in each case without notice to or consent from the Company; (b) receiving an award for information provided to any governmental agency; (c) testifying truthfully in any legal proceeding; or (d) disclosing information concerning sexual assault, sexual harassment, discrimination, retaliation, wage-and-hour violations, or other conduct that the Recipient reasonably believes is unlawful, to the extent such a disclosure is protected by Law.

**5.2 Defend Trade Secrets Act Notice.** [[Optional: Under 18 U.S.C. § 1833(b), an individual shall not be held criminally or civilly liable under any federal or state trade secret law for the disclosure of a trade secret that (a) is made (i) in confidence to a federal, state, or local government official, either directly or indirectly, or to an attorney, and (ii) solely for the purpose of reporting or investigating a suspected violation of law; or (b) is made in a complaint or other document filed in a lawsuit or other proceeding, if such filing is made under seal. An individual who files a lawsuit for retaliation by an employer for reporting a suspected violation of law may disclose the trade secret to the individual's attorney and use the trade secret information in the court proceeding, if the individual files any document containing the trade secret under seal and does not disclose the trade secret, except pursuant to court order.]]

> **Drafting note:** Keep Section 5.2 whenever the Recipient is an individual (candidates, individual consultants, sole proprietors). It may be deleted for an entity Recipient.

**5.3 California.** [[Optional: Nothing in this Agreement prevents the Recipient from discussing or disclosing information about unlawful acts in the workplace, such as harassment or discrimination or any other conduct that the Recipient has reason to believe is unlawful.]]

> **Drafting note:** Include Section 5.3 for a candidate who resides or will work in California. It tracks the sentence that Cal. Gov. Code § 12964.5(a)(1)(B)(ii) requires, in substantial form, in nondisparagement or other provisions restricting disclosure of workplace conditions in agreements entered into as a condition of employment (unchanged since SB 331, effective January 1, 2022).

## 6. Third-Party Information

**6.1 No Disclosure of Others' Confidential Information.** [[Optional: The Recipient shall not disclose to the Company, bring onto the Company's premises or systems, or use in any discussion with the Company, any confidential or proprietary information or trade secret of any current or former employer, client, or other person to whom the Recipient owes a duty of confidentiality. The Company does not wish to receive any such information, and the Recipient shall decline any request that would require disclosing it.]]

> **Drafting note:** Include Section 6.1 for every candidate and for any vendor or partner that works for the Company's competitors. If the Company later learns that a candidate disclosed a third party's confidential information, isolate and document it, and do not use it.

## 7. Ownership; No License; Feedback

**7.1 Ownership; No License.** All Confidential Information remains the property of the Company or its licensors. Nothing in this Agreement grants the Recipient any license, ownership interest, or other right in or to any Confidential Information or under any patent, copyright, trademark, trade secret, or other intellectual property right of the Company, whether by implication, estoppel, or otherwise, except the limited right to use Confidential Information for the Purpose in accordance with this Agreement.

**7.2 Feedback.** If the Recipient provides the Company with any suggestion, comment, or idea concerning the Company's products, services, or business ("**Feedback**"), the Recipient grants the Company a perpetual, irrevocable, worldwide, royalty-free, fully paid-up, non-exclusive license, with the right to sublicense through multiple tiers, to use, reproduce, modify, and otherwise exploit the Feedback for any purpose, without attribution or compensation. The Recipient is not required to provide Feedback.

## 8. No Warranty; No Obligation

**8.1 As Is.** All Confidential Information is provided "AS IS," without any representation or warranty, express or implied, as to its accuracy, completeness, non-infringement, merchantability, or fitness for a particular purpose.

**8.2 No Obligation; No Offer.** This Agreement does not obligate the Company to disclose any particular information or to enter into any further agreement or transaction, and either party may end discussions concerning the Purpose at any time. This Agreement is not an offer of employment, engagement, or purchase, and does not create any employment, agency, partnership, or joint-venture relationship. Any employment or engagement of the Recipient by the Company will be governed solely by a separate written agreement signed by an authorized officer of the Company.

## 9. Return and Destruction

**9.1 Return or Destruction.** Within ten (10) days after the Company's written request at any time, and in any event within thirty (30) days after the end of the Disclosure Period, the Recipient shall return to the Company or destroy (and permanently erase from all devices, accounts, and systems in its or any Permitted Recipient's possession or control) all Confidential Information and Derivatives and, on request, certify in writing (email sufficing) that it has done so.

**9.2 Permitted Retention.** [[Optional: If the Recipient is an entity, it may retain Confidential Information in automatic electronic archival or backup systems in the ordinary course, so long as no attempt is made to access it other than for backup restoration, legal, or compliance purposes, and its legal department may retain one copy solely to demonstrate compliance with this Agreement. All retained Confidential Information remains subject to this Agreement for as long as it is retained.]]

## 10. Term; Duration of Obligations

**10.1 Duration.** The Recipient's obligations under this Agreement with respect to Confidential Information continue until the date that is {{confidentiality_years}} years after the end of the Disclosure Period, except that those obligations continue, with respect to any Trade Secret, for as long as it remains a trade secret under applicable Law, and with respect to Confidential Information retained under Section 9.2, for as long as it is retained.

**10.2 Effect of Later Agreements.** If the Recipient becomes an employee, consultant, or contractor of the Company, or enters into a definitive agreement with the Company containing confidentiality obligations, that later agreement governs Confidential Information disclosed after its effective date, and this Agreement continues to govern Confidential Information disclosed before that date, in each case except as the later agreement expressly provides otherwise.

**10.3 Survival.** Articles 5, 7, 8, 9, 11, and 13 and this Article 10 survive any expiration or termination of this Agreement.

## 11. Remedies

**11.1 Equitable Relief.** The Recipient acknowledges that unauthorized use or disclosure of Confidential Information may cause the Company irreparable harm for which monetary damages would be an inadequate remedy. Accordingly, in addition to any other remedy available at law or in equity, the Company is entitled to seek specific performance and injunctive or other equitable relief to prevent or restrain any actual or threatened breach of this Agreement, without proof of actual damages and, to the extent permitted by Law, without posting a bond or other security.

**11.2 Remedies Cumulative.** The Company's rights and remedies under this Agreement are cumulative and are in addition to its rights and remedies under the Defend Trade Secrets Act, any state trade secret law, and other applicable Law.

## 12. Export Control

**12.1 Compliance.** The Recipient shall comply with all applicable export control and economic sanctions Laws in connection with Confidential Information and shall not export, re-export, release, or transfer any Confidential Information (including by a release to a foreign person within the United States) except in compliance with those Laws. The Company shall notify the Recipient in writing before disclosing any Confidential Information that is subject to the International Traffic in Arms Regulations or classified under the Export Administration Regulations other than as EAR99.

## 13. General Provisions

**13.1 Governing Law.** This Agreement, and all claims arising out of or relating to it, are governed by the laws of the State of {{governing_law_state}}, without giving effect to any choice-of-law or conflict-of-law rule that would cause the application of the laws of any other jurisdiction.

**13.2 Forum.** Each party irrevocably submits to the exclusive jurisdiction of {{forum}} for any action arising out of or relating to this Agreement and waives any objection to venue there, except that the Company may seek injunctive or other equitable relief under Article 11 in any court of competent jurisdiction.

**13.3 Waiver of Jury Trial.** TO THE FULLEST EXTENT PERMITTED BY LAW, EACH PARTY KNOWINGLY, VOLUNTARILY, AND INTENTIONALLY WAIVES ANY RIGHT TO A TRIAL BY JURY IN ANY ACTION ARISING OUT OF OR RELATING TO THIS AGREEMENT. If this waiver is unenforceable in the forum in which an action is brought, this Section 13.3 does not apply to that action.

**13.4 Notices.** All notices under this Agreement shall be in writing and are deemed given (a) when delivered personally; (b) one (1) business day after deposit with a nationally recognized overnight courier, charges prepaid; or (c) when sent by email, if sent before 5:00 p.m. in the recipient's time zone on a business day, and otherwise on the next business day, provided that no automated notice of delivery failure is received. Notices to the Company shall be sent to {{company_address}}, Attention: {{signatory_name}}, Email: {{company_notice_email}}; notices to the Recipient shall be sent to {{recipient_address}}, Email: {{recipient_email}}; or, in each case, to any other address a party designates by notice.

**13.5 Entire Agreement.** This Agreement is the entire agreement between the parties concerning its subject matter and supersedes all prior and contemporaneous agreements and understandings concerning that subject matter, subject to Section 10.2. No click-through or data-room terms modify this Agreement.

**13.6 Amendment; Waiver.** This Agreement may be amended only by a written instrument signed by both parties, and a provision may be waived only by a written instrument signed by the party against whom the waiver is to be enforced. No failure or delay in exercising any right operates as a waiver of it.

**13.7 Severability.** If any provision of this Agreement is held invalid, illegal, or unenforceable, it shall be enforced to the maximum extent permissible and reformed to the minimum extent necessary to make it enforceable, and the remaining provisions remain in full force and effect.

**13.8 Assignment; Successors.** The Recipient may not assign or delegate this Agreement or any right or obligation under it without the Company's prior written consent, and any attempted assignment without consent is void. The Company may assign this Agreement without consent to any Affiliate or to any successor to all or substantially all of its business or assets, whether by merger, sale of stock, sale of assets, or otherwise. This Agreement binds and benefits the parties and their permitted successors and assigns, and the Company's Affiliates are intended third-party beneficiaries with respect to their Confidential Information.

**13.9 Counterparts; Electronic Signatures.** This Agreement may be executed in counterparts (including by PDF or by an electronic signature service complying with the ESIGN Act, 15 U.S.C. § 7001 et seq., or the Delaware Uniform Electronic Transactions Act, 6 Del. C. ch. 12A), each of which is deemed an original and all of which together constitute one instrument.

**13.10 Interpretation.** Headings are for convenience only. "Including" means "including without limitation." "Or" is not exclusive. "Days" means calendar days unless business days are specified. References to a statute or regulation include any successor provision. No presumption arises against either party by virtue of authorship.

**13.11 Expenses.** Each party bears its own costs and expenses in connection with this Agreement and the Purpose, except as the Company otherwise agrees in writing (for example, reimbursement of a candidate's pre-approved interview travel).

IN WITNESS WHEREOF, the parties have executed this Nondisclosure Agreement as of the Effective Date.

**{{company_name}}**

By: ______________________________
Name: {{signatory_name}}
Title: {{signatory_title}}

**RECIPIENT**

[[Alternative A: **{{recipient_name}}**

By: ______________________________
Name: {{recipient_signatory_name}}
Title: {{recipient_signatory_title}}]]

[[Alternative B: ______________________________
{{recipient_name}}
Address: {{recipient_address}}
Email: {{recipient_email}}]]

> **Drafting note:** Use Alternative A for an entity Recipient and Alternative B for an individual.

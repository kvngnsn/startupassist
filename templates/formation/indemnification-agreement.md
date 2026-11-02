---
id: indemnification-agreement
title: Director and Officer Indemnification Agreement
category: formation
stage: formation
signers: [Company (by an officer other than the indemnitee where practicable), Indemnitee]
authorities:
  - "8 Del. C. § 145(a)–(k) (indemnification, advancement, non-exclusivity, insurance, Court of Chancery jurisdiction)"
  - "8 Del. C. § 102(b)(7) and 10 Del. C. § 3114(b) (exculpation; meaning of 'officer')"
  - "8 Del. C. § 144 (approval of the agreement as a transaction with directors and officers)"
  - "Securities Act of 1933 § 16(b)-type exclusions: 15 U.S.C. § 78p(b); Sarbanes-Oxley Act § 304, 15 U.S.C. § 7243; Exchange Act § 10D and Rule 10D-1, 17 C.F.R. § 240.10D-1"
  - "17 C.F.R. § 229.510 (Regulation S-K Item 510; SEC position on indemnification for Securities Act liabilities)"
use_when: Giving each director and officer (and any investor-designated director) contractual indemnification and advancement rights, at formation or when a person joins the board or becomes an officer.
do_not_use_when: Indemnifying a non-officer employee, consultant or agent in the ordinary course (use a narrower, permissive indemnity approved by the board), or for a public company without updating the SEC-related provisions with securities counsel.
related: [bylaws, certificate-of-incorporation, initial-board-consent]
sources:
  - name: "Delaware Code, Title 8, § 145 (official text)"
    url: https://delcode.delaware.gov/title8/c001/sc04/index.html
  - name: "NVCA Model Indemnification Agreement (coverage and market-term reference only; not copied)"
    url: https://nvca.org/model-legal-documents/
  - name: "Cooley GO — Incorporation Package (Delaware) (notes that indemnification agreements accompany bylaws; reference only)"
    url: https://cooleygo.com/documents/incorporation-package
  - name: "17 C.F.R. § 229.510 (eCFR)"
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-229/subpart-229.500/section-229.510
last_verified: 2026-11-02
---

## About this template

**What it does.** Gives a director or officer (the "Indemnitee") a direct contract with the Company for indemnification and advancement of expenses to the fullest extent Delaware law permits, with procedures that make the rights quick and hard to resist: prompt advancement against an unsecured undertaking, a presumption of entitlement, a short decision clock, a right to sue in the Court of Chancery at the Company's expense, D&O insurance covenants, and protection against later amendment of the charter or bylaws.

**Why a contract on top of the bylaws.** Bylaw rights can be amended prospectively and are sometimes drafted narrowly. Section 145(f) makes indemnification and advancement non-exclusive, so a contract can add procedural protections; and the Court of Chancery has exclusive jurisdiction to hear and summarily determine advancement claims under any bylaw or agreement (§ 145(k)). A contract also binds successors expressly and handles investor-fund coordination.

**Statutory limits the form respects.**
- Indemnification for **third-party** proceedings (§ 145(a)) covers expenses, judgments, fines and settlements, if the person acted in good faith and reasonably believed the conduct was in or not opposed to the Company's best interests (and, for criminal matters, had no reasonable cause to believe it unlawful).
- Indemnification in **derivative** proceedings (§ 145(b)) covers only expenses, and none for matters on which the person is adjudged liable to the Company unless a court orders it. Indemnifying derivative judgments or settlements payments is not permitted; the form excludes them except as a court may allow.
- Indemnification of a director or officer who is **successful on the merits or otherwise** is mandatory (§ 145(c)). For acts after December 31, 2020, "officer" in § 145(c) means a § 3114(b) officer.
- **Determinations** (§ 145(d)) for a current director or officer are made by disinterested directors, a committee of them, independent counsel, or stockholders. This form shifts to independent counsel after a Change in Control so a hostile new board does not decide.
- **Advancement** (§ 145(e)) requires an undertaking to repay if the person is ultimately found not entitled.

**Key business points and market positions.**

| Issue | Company-favorable | Market (NVCA-style) | Indemnitee-favorable | This form |
|---|---|---|---|---|
| Scope | "to the extent permitted" and permissive | Mandatory to fullest extent permitted | Same, plus no exclusions | Market |
| Advancement timing | 60–90 days, with ability-to-pay test | 30 days, unsecured, interest-free undertaking | 10–20 days | 30 days; optional 20 |
| Burden on entitlement | On indemnitee | Presumption in indemnitee's favor; Company bears burden | Clear-and-convincing burden on Company | Market with clear-and-convincing |
| Determination after change in control | Board | Independent Counsel selected by indemnitee | Same | Market |
| Fees to enforce | Only if wholly successful | If successful in whole or part | Always | Market |
| D&O insurance | No covenant | Maintain while commercially reasonable, no less favorable than other directors | Specified minimum limits and six-year tail on change in control | Market, with optional tail |
| Fund indemnitor | Silent | Company is indemnitor of first resort | Same | Included (Section 13) |

**Fund indemnitor provisions.** Venture investors indemnify partners who serve as portfolio-company directors. Without contract language, a fund that pays first can claim contribution against the portfolio company and vice versa (*Levy v. HLI Operating Co.*, 924 A.2d 210 (Del. Ch. 2007)). Section 13 makes the Company primary, waives the Company's contribution claims against the fund, and subrogates the fund to the director's rights against the Company. Investors will insist on this; it is market and should not be negotiated away at formation.

**Approval and conflicts.** The board approves the form and authorizes execution with each director and officer (see the initial board consent). Because every director is interested in his or her own agreement, approval should be by the full board after disclosure of the common interest, and the agreements should be uniform; § 144(a) safe-harbor approval by disinterested directors is not available when all directors are interested, so the standard is fairness, which a uniform, market-standard form readily satisfies. A stockholder ratification at the first annual consent is a belt-and-suspenders option.

**Coordination.** Defined terms track Article VI of the bylaws: "Proceeding," "Expenses," "Fund Indemnitors." Keep the agreement no less favorable than the bylaws; Section 14(a) gives the indemnitee the benefit of any more favorable bylaw or charter provision.

**Public-company note.** If the Company later registers securities, the SEC's position (Regulation S-K Item 510) is that indemnification for Securities Act liabilities is against public policy; registration statements include the required undertaking. Optional Section 19.13 acknowledges this.

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `{{company_name}}` | Exact legal name | Northwind Robotics, Inc. | |
| `{{effective_date}}` | Effective date of the agreement | January 6, 2027 | Rights relate back to the start of service (Section 17) |
| `{{indemnitee_name}}` | Director or officer | Jordan Lee | One agreement per person |
| `{{indemnitee_address}}`, `{{indemnitee_email}}` | Notice details | | |
| `{{indemnitee_capacity}}` | Director, officer, or both | director and Chief Technology Officer | |
| `{{signatory_name}}`, `{{signatory_title}}` | Officer signing for the Company | Alex Rivera, Chief Executive Officer | Use a different person from the indemnitee where possible |
| `{{company_notice_email}}` | Company notice email | legal@northwind.example | |
| `{{company_address}}` | Company notice address | 100 Example Street, Suite 200, Austin, Texas 78701 | |
| `{{fund_indemnitor_names}}` | Investor entities that indemnify the director | Example Ventures Fund I, L.P. and its affiliated funds and management company | Only for investor-designated directors |
| `{{advancement_days}}` | Days to advance after request | 30 | 20 if indemnitee-favorable |
| `{{d_and_o_tail_years}}` | Tail coverage on change in control | 6 | Optional |

## Form

---

# INDEMNIFICATION AGREEMENT

This Indemnification Agreement (this "**Agreement**") is entered into as of {{effective_date}} (the "**Effective Date**") between {{company_name}}, a Delaware corporation (the "**Company**"), and {{indemnitee_name}} ("**Indemnitee**").

## RECITALS

A. Highly competent persons have become more reluctant to serve as directors or officers of corporations unless they are protected by comprehensive liability insurance and indemnification, because of the increased risk of claims and actions against them arising out of their service, which bear no reasonable relationship to the compensation of directors and officers.

B. The Board of Directors of the Company (the "**Board**") has determined that the Company's ability to attract and retain qualified persons is in the best interests of the Company and its stockholders, and that it is reasonable, prudent and necessary for the Company to obligate itself contractually to indemnify, and to advance expenses on behalf of, those persons to the fullest extent permitted by applicable law, so that they will serve or continue to serve free from undue concern that they will not be so protected.

C. Section 145 of the General Corporation Law of the State of Delaware (the "**DGCL**") and the Company's Certificate of Incorporation and Bylaws permit, and the Bylaws require, indemnification of the Company's directors and officers, and expressly provide that those rights are not exclusive and that the Company may enter into contracts with its directors and officers with respect to indemnification and advancement.

D. Indemnitee does not regard the protection available under the Certificate of Incorporation, the Bylaws and insurance as adequate in the present circumstances, and is willing to serve as {{indemnitee_capacity}} of the Company on the condition that Indemnitee be indemnified as provided in this Agreement.

[[Optional: E. Indemnitee may have certain rights to indemnification, advancement of expenses or insurance provided by {{fund_indemnitor_names}}, which Indemnitee and those persons intend to be secondary to the primary obligation of the Company to indemnify Indemnitee as provided in this Agreement.]]

NOW, THEREFORE, in consideration of Indemnitee's agreement to serve or continue to serve the Company, and intending to be legally bound, the parties agree as follows:

## 1. SERVICES TO THE COMPANY

Indemnitee agrees to serve as a director or officer of the Company, or both, for so long as Indemnitee is duly elected or appointed or until Indemnitee resigns. This Agreement does not create any obligation of the Company to continue Indemnitee's service, does not constitute an employment agreement, and does not limit any right of the Company, its stockholders, or Indemnitee to terminate Indemnitee's service, subject to any separate agreement. This Agreement continues in force after Indemnitee ceases to serve, as provided in Section 17.

## 2. DEFINITIONS

For purposes of this Agreement:

(a) "**Change in Control**" means the occurrence after the Effective Date of any of the following: (i) any "person" (as used in Sections 13(d) and 14(d) of the Securities Exchange Act of 1934, as amended (the "**Exchange Act**")), other than a trustee or other fiduciary holding securities under an employee benefit plan of the Company or a corporation owned, directly or indirectly, by the stockholders of the Company in substantially the same proportions as their ownership of stock of the Company, becomes the beneficial owner, directly or indirectly, of securities of the Company representing more than fifty percent (50%) of the total voting power of the Company's then-outstanding voting securities, other than through the Company's issuance of securities in a bona fide equity financing transaction; (ii) during any period of two (2) consecutive years, individuals who at the beginning of the period constitute the Board, together with any new director whose election by the Board or nomination for election by the stockholders was approved by a vote of at least a majority of the directors then still in office who either were directors at the beginning of the period or whose election or nomination was previously so approved, cease for any reason to constitute at least a majority of the Board; (iii) the consummation of a merger or consolidation of the Company with any other entity, other than a merger or consolidation that would result in the voting securities of the Company outstanding immediately before it continuing to represent (either by remaining outstanding or by being converted into voting securities of the surviving entity) more than fifty percent (50%) of the combined voting power of the voting securities of the surviving entity or its parent outstanding immediately after it; or (iv) the sale or disposition by the Company of all or substantially all of its assets, or the approval by the stockholders of a complete liquidation of the Company.

(b) "**Corporate Status**" describes the status of a person who is or was a director, officer, employee, agent or fiduciary of the Company or of any other Enterprise that the person is or was serving at the request of the Company.

(c) "**Disinterested Director**" means a director of the Company who is not and was not a party to the Proceeding in respect of which Indemnitee seeks indemnification.

(d) "**Enterprise**" means the Company and any other corporation, partnership, limited liability company, joint venture, trust, employee benefit plan, nonprofit entity or other enterprise of which Indemnitee is or was serving at the request of the Company as a director, officer, manager, partner, trustee, employee, agent or fiduciary.

(e) "**Expenses**" means all reasonable attorneys' fees, retainers, court costs, transcript costs, fees of experts and witnesses, travel expenses, duplicating costs, printing and binding costs, telephone and electronic communication charges, postage, delivery service fees, costs of electronic discovery and data hosting, and all other disbursements or expenses of the types customarily incurred in connection with prosecuting, defending, preparing to prosecute or defend, investigating, being or preparing to be a witness in, or otherwise participating in, a Proceeding. Expenses also include (i) Expenses incurred in connection with any appeal resulting from any Proceeding, including the premium, security for, and other costs relating to any cost bond, supersedeas bond, or other appeal bond or its equivalent, and (ii) for purposes of Section 15(d) only, Expenses incurred by Indemnitee in any action to enforce this Agreement or to obtain insurance recoveries. Expenses do not include amounts paid in settlement by Indemnitee or the amount of judgments or fines against Indemnitee.

(f) "**Fund Indemnitors**" has the meaning given in Section 13(a).

(g) "**Independent Counsel**" means a law firm, or a member of a law firm, that is experienced in matters of Delaware corporation law and neither presently is, nor in the past five (5) years has been, retained to represent (i) the Company, Indemnitee, or any Fund Indemnitor in any matter material to any of them (other than as Independent Counsel under this Agreement or similar indemnification agreements), or (ii) any other party to the Proceeding giving rise to a claim for indemnification. "Independent Counsel" does not include any person who, under the applicable standards of professional conduct then prevailing, would have a conflict of interest in representing either the Company or Indemnitee in an action to determine Indemnitee's rights under this Agreement.

(h) "**Proceeding**" means any threatened, pending or completed action, suit, claim, counterclaim, cross-claim, arbitration, mediation, alternative dispute resolution mechanism, investigation, inquiry, administrative hearing, or other proceeding, whether brought by or in the right of the Company or otherwise, and whether civil, criminal, administrative, regulatory, legislative or investigative (formal or informal), in which Indemnitee was, is, or will be involved as a party, witness or otherwise by reason of Indemnitee's Corporate Status or by reason of any action taken (or failure to act) by Indemnitee or of any action (or failure to act) on Indemnitee's part while acting in any Corporate Status, in each case whether or not Indemnitee is serving in that capacity at the time any liability or Expense is incurred. "Proceeding" includes any proceeding initiated by Indemnitee to enforce Indemnitee's rights under this Agreement, but otherwise excludes any proceeding initiated by Indemnitee except as provided in Section 8(c).

(i) References to "**fines**" include any excise tax assessed on Indemnitee with respect to an employee benefit plan; references to "**serving at the request of the Company**" include any service as a director, officer, employee, agent or fiduciary of the Company that imposes duties on, or involves services by, Indemnitee with respect to an employee benefit plan, its participants or beneficiaries; and a person who acted in good faith and in a manner the person reasonably believed to be in the interest of the participants and beneficiaries of an employee benefit plan is deemed to have acted in a manner "not opposed to the best interests of the Company."

## 3. INDEMNITY IN THIRD-PARTY PROCEEDINGS

The Company shall indemnify Indemnitee, to the fullest extent permitted by applicable law, if Indemnitee was, is, or is threatened to be made a party to or a participant in any Proceeding, other than a Proceeding by or in the right of the Company to procure a judgment in its favor. Under this Section 3, Indemnitee shall be indemnified against all Expenses, judgments, fines, penalties and amounts paid in settlement (with the Company's consent where required by Section 10(d)) actually and reasonably incurred by Indemnitee or on Indemnitee's behalf in connection with the Proceeding or any claim, issue or matter in it, if Indemnitee acted in good faith and in a manner Indemnitee reasonably believed to be in or not opposed to the best interests of the Company and, in the case of a criminal Proceeding, had no reasonable cause to believe that Indemnitee's conduct was unlawful.

## 4. INDEMNITY IN PROCEEDINGS BY OR IN THE RIGHT OF THE COMPANY

The Company shall indemnify Indemnitee, to the fullest extent permitted by applicable law, if Indemnitee was, is, or is threatened to be made a party to or a participant in any Proceeding by or in the right of the Company to procure a judgment in its favor. Under this Section 4, Indemnitee shall be indemnified against all Expenses actually and reasonably incurred by Indemnitee or on Indemnitee's behalf in connection with the Proceeding or any claim, issue or matter in it, if Indemnitee acted in good faith and in a manner Indemnitee reasonably believed to be in or not opposed to the best interests of the Company. No indemnification for Expenses shall be made under this Section 4 in respect of any claim, issue or matter as to which Indemnitee has been finally adjudged by a court to be liable to the Company, unless and only to the extent that the Court of Chancery of the State of Delaware or the court in which the Proceeding was brought determines on application that, despite the adjudication of liability but in view of all the circumstances, Indemnitee is fairly and reasonably entitled to indemnification for the Expenses that court deems proper.

## 5. INDEMNIFICATION FOR EXPENSES OF A PARTY WHO IS WHOLLY OR PARTLY SUCCESSFUL

(a) Notwithstanding any other provision of this Agreement except Section 8, to the extent that Indemnitee is a party to or a participant in any Proceeding and is successful, on the merits or otherwise, in defense of the Proceeding or any claim, issue or matter in it, in whole or in part, the Company shall indemnify Indemnitee against all Expenses actually and reasonably incurred by Indemnitee or on Indemnitee's behalf in connection with it.

(b) If Indemnitee is not wholly successful in the Proceeding but is successful, on the merits or otherwise, as to one or more but fewer than all claims, issues or matters in it, the Company shall indemnify Indemnitee against all Expenses actually and reasonably incurred by Indemnitee or on Indemnitee's behalf in connection with each successfully resolved claim, issue or matter, and the Company shall have the burden of proving any allocation of Expenses between successful and unsuccessful claims, issues or matters.

(c) For purposes of this Section 5, the termination of any claim, issue or matter in a Proceeding by dismissal, with or without prejudice, is deemed a successful result as to that claim, issue or matter.

## 6. INDEMNIFICATION FOR EXPENSES OF A WITNESS

Notwithstanding any other provision of this Agreement, to the extent that Indemnitee is, by reason of Indemnitee's Corporate Status, a witness or otherwise asked to participate in any Proceeding to which Indemnitee is not a party, the Company shall indemnify Indemnitee against all Expenses actually and reasonably incurred by Indemnitee or on Indemnitee's behalf in connection with it.

## 7. ADDITIONAL INDEMNIFICATION

(a) Notwithstanding any limitation in Sections 3, 4 or 5, the Company shall indemnify Indemnitee, to the fullest extent permitted by applicable law, if Indemnitee is a party to or threatened to be made a party to any Proceeding (including a Proceeding by or in the right of the Company to procure a judgment in its favor) against all Expenses, judgments, fines, penalties and amounts paid in settlement actually and reasonably incurred by Indemnitee in connection with the Proceeding; provided that no indemnity shall be made under this Section 7(a) for judgments or amounts paid in settlement in a Proceeding by or in the right of the Company, or on account of Indemnitee's conduct that constitutes a breach of Indemnitee's duty of loyalty to the Company or its stockholders or an act or omission not in good faith or that involves intentional misconduct or a knowing violation of law, in each case to the extent indemnification for those amounts is not permitted by the DGCL.

(b) For purposes of Section 7(a), the meaning of "to the fullest extent permitted by applicable law" includes (i) to the fullest extent permitted by the provision of the DGCL that authorizes or contemplates additional indemnification by agreement, or the corresponding provision of any amendment to or replacement of the DGCL, and (ii) to the fullest extent authorized or permitted by any amendment to or replacement of the DGCL adopted after the Effective Date that increases the extent to which a corporation may indemnify its directors and officers.

## 8. EXCLUSIONS

Notwithstanding any provision in this Agreement, the Company is not obligated under this Agreement to make any indemnity payment in connection with any claim made against Indemnitee:

(a) for which payment has actually been received by or on behalf of Indemnitee under any insurance policy or other indemnity or advancement provision, except for any excess beyond the amount received (and subject to Section 13 as to the Fund Indemnitors);

(b) (i) for an accounting or disgorgement of profits from the purchase and sale (or sale and purchase) by Indemnitee of securities of the Company within the meaning of Section 16(b) of the Exchange Act or similar provisions of state statutory or common law; or (ii) for any reimbursement of the Company by Indemnitee of any bonus or other incentive-based or equity-based compensation, or of any profits realized by Indemnitee from the sale of securities of the Company, as required under Section 304 of the Sarbanes-Oxley Act of 2002, Section 10D of the Exchange Act and the rules thereunder (including Rule 10D-1 and any related listing standard), or any clawback policy adopted by the Company to comply with them;

(c) in connection with any Proceeding (or any part of any Proceeding) initiated by Indemnitee, including any Proceeding (or part) initiated by Indemnitee against the Company or its directors, officers, employees or other indemnitees, unless (i) the Board authorized the Proceeding (or that part) before its initiation, (ii) the Company provides the indemnification, in its sole discretion, under the powers vested in it under applicable law, (iii) the Proceeding is one to establish or enforce a right to indemnification or advancement under this Agreement or any other agreement, insurance policy, or the Certificate of Incorporation or Bylaws, or (iv) otherwise required by applicable law; or

(d) if a court of competent jurisdiction finally determines, in a decision from which there is no further right to appeal, that indemnification is prohibited by applicable law.

> **Drafting note:** Keep the exclusions narrow. Investor counsel will push back on exclusions that go beyond what the law prohibits (for example, a "fraud" exclusion triggered by allegation rather than final adjudication). The Rule 10D-1 clawback exclusion matters only after an IPO but is now standard and protects the Company from indemnifying a compensation recovery that the exchange rules forbid it to indemnify.

## 9. ADVANCES OF EXPENSES; DEFENSE OF CLAIM

(a) *Advancement.* Notwithstanding any provision of this Agreement to the contrary (other than Section 8(c)), and to the fullest extent permitted by applicable law, the Company shall advance the Expenses incurred by Indemnitee or on Indemnitee's behalf in connection with any Proceeding (or any part of any Proceeding) not initiated by Indemnitee (other than a Proceeding to enforce rights under this Agreement), before the final disposition of the Proceeding, within {{advancement_days}} days after the Company's receipt of a written statement or statements requesting advances, from time to time. Advances shall include Expenses incurred in pursuing an action to enforce this right of advancement, including Expenses incurred preparing and forwarding statements to the Company to support the advances claimed. Advances are unsecured and interest-free and shall be made without regard to Indemnitee's ability to repay them and without regard to Indemnitee's ultimate entitlement to indemnification under any other provision of this Agreement.

(b) *Statements.* Each statement shall reasonably evidence the Expenses incurred by Indemnitee, which may be in the form of invoices from counsel; Indemnitee may redact or omit any information that would waive any privilege or work-product protection. The Company shall not be required to advance any amount unless and until the statement is delivered.

(c) *Undertaking.* Indemnitee undertakes to repay the advances if, and to the extent that, it is ultimately determined by a court of competent jurisdiction in a final judgment, from which there is no further right to appeal, that Indemnitee is not entitled to be indemnified by the Company. This Section 9(c) is the only undertaking required, and it shall be accepted without reference to Indemnitee's financial ability to repay. Indemnitee shall sign and deliver any further form of undertaking the DGCL may require at the time of the request, if consistent with this Section 9(c).

(d) *Partial advancement.* If the Company disputes a portion of the amounts requested for advancement, it shall nevertheless advance the undisputed portion within the period stated in Section 9(a).

## 10. PROCEDURES FOR NOTIFICATION AND DEFENSE OF CLAIM

(a) *Notice.* Indemnitee shall notify the Company in writing of any matter with respect to which Indemnitee intends to seek indemnification or advancement as soon as reasonably practicable after Indemnitee receives notice of it. The failure of Indemnitee to notify the Company, or any delay in notifying it, does not relieve the Company of any obligation it may have to Indemnitee under this Agreement or otherwise, except to the extent the Company is actually and materially prejudiced by the failure or delay. If, at the time of receipt of the notice, the Company has directors' and officers' liability insurance in effect, the Company shall give prompt notice of the Proceeding to its insurers in accordance with the policies and shall thereafter take all necessary or desirable action to cause the insurers to pay all amounts payable on behalf of Indemnitee in accordance with the policies.

(b) *Defense by the Company.* With respect to any Proceeding of which the Company is so notified, the Company may, at its option and expense, assume the defense of the Proceeding, with counsel reasonably satisfactory to Indemnitee, upon delivery to Indemnitee of written notice of its election to do so. After that notice, the Company is not liable to Indemnitee for any later legal or other Expenses incurred by Indemnitee in connection with the defense, other than as provided below. Indemnitee has the right to employ separate counsel in the Proceeding at Indemnitee's expense, but the reasonable Expenses of that counsel shall be Expenses subject to indemnification and advancement under this Agreement if (i) the employment of separate counsel has been authorized by the Company; (ii) counsel for the Company or Indemnitee reasonably concludes that there is or may be a conflict of interest between the Company and Indemnitee in the conduct of the defense, or that Indemnitee has defenses not available to the Company; (iii) the Company has not in fact employed counsel to assume the defense within thirty (30) days after its notice of election; or (iv) the Proceeding is brought by or in the right of the Company.

(c) *Joint representation.* If two or more persons who may be entitled to indemnification from the Company, including Indemnitee, are parties to a Proceeding, the Company may require Indemnitee to engage the same legal counsel as the other parties, except where clause (ii) of Section 10(b) applies.

(d) *Settlement.* The Company is not liable to indemnify Indemnitee under this Agreement for any amounts paid in settlement of any Proceeding effected without the Company's prior written consent, which shall not be unreasonably withheld, conditioned or delayed. The Company shall not, without Indemnitee's prior written consent, which shall not be unreasonably withheld, conditioned or delayed, settle any Proceeding (or part) in any manner that would (i) impose any fine, penalty, or limitation on Indemnitee; (ii) include an admission of fault or wrongdoing by Indemnitee; or (iii) fail to include a full and unconditional release of Indemnitee from all liability on any claims that are the subject of the Proceeding.

(e) *Cooperation.* Indemnitee shall give the Company the information and cooperation it may reasonably require and that is within Indemnitee's power, at the Company's expense.

## 11. PROCEDURE UPON APPLICATION FOR INDEMNIFICATION

(a) *Request.* To obtain indemnification, Indemnitee shall submit to the Company a written request, including documentation and information reasonably available to Indemnitee and reasonably necessary to determine whether and to what extent Indemnitee is entitled to indemnification, following the final disposition of the Proceeding. The Secretary of the Company shall, promptly upon receipt of the request, advise the Board in writing that Indemnitee has requested indemnification.

(b) *Determination.* Any determination required by applicable law with respect to Indemnitee's entitlement to indemnification shall be made: (i) if a Change in Control has occurred, by Independent Counsel in a written opinion to the Board, a copy of which shall be delivered to Indemnitee, unless Indemnitee requests that the determination be made by the Board under clause (ii); or (ii) if a Change in Control has not occurred, (A) by a majority vote of the Disinterested Directors, even though less than a quorum of the Board; (B) by a committee of Disinterested Directors designated by a majority vote of the Disinterested Directors, even though less than a quorum of the Board; (C) if there are no Disinterested Directors, or if the Disinterested Directors so direct, by Independent Counsel in a written opinion to the Board, a copy of which shall be delivered to Indemnitee; or (D) if Indemnitee so requests and the Board so directs, by the stockholders of the Company. If it is determined that Indemnitee is entitled to indemnification, payment shall be made within ten (10) days after the determination.

(c) *Independent Counsel selection.* If the determination is to be made by Independent Counsel under Section 11(b)(i), Indemnitee shall select the Independent Counsel; otherwise the Board shall select it. The selecting party shall give written notice to the other party advising it of the identity of the Independent Counsel selected. Within ten (10) days after the notice, the other party may deliver a written objection to the selection, which may be asserted only on the ground that the Independent Counsel so selected does not meet the requirements of "Independent Counsel" in Section 2(g), and shall set forth with particularity the factual basis of the assertion. Absent a proper and timely objection, the person selected shall act as Independent Counsel. If no Independent Counsel has been selected or approved within twenty (20) days after the Company's receipt of the request for indemnification, either party may petition the Court of Chancery of the State of Delaware to resolve any objection or to appoint as Independent Counsel a person selected by the court. The Company shall pay all reasonable fees and expenses of Independent Counsel and fully indemnify that counsel against all liabilities arising from its engagement.

(d) *Cooperation; costs.* Indemnitee shall cooperate with the person making the determination, including by providing on reasonable request any documentation or information that is not privileged and is reasonably available to Indemnitee and reasonably necessary to the determination. Any costs or expenses (including attorneys' fees and disbursements) Indemnitee incurs in so cooperating shall be borne by the Company, irrespective of the determination.

(e) *Timing.* If the person empowered to make the determination has not made it within sixty (60) days after the Company's receipt of the request (or, if Independent Counsel is to make it, within thirty (30) days after its selection becomes final), the requisite determination of entitlement is deemed made and Indemnitee is entitled to indemnification, absent (i) a misstatement by Indemnitee of a material fact, or an omission of a material fact necessary to make Indemnitee's statement not materially misleading, in connection with the request, or (ii) a prohibition of indemnification under applicable law.

## 12. PRESUMPTIONS AND EFFECT OF CERTAIN PROCEEDINGS

(a) *Presumption of entitlement.* In making a determination of whether Indemnitee is entitled to indemnification, the person making the determination shall presume that Indemnitee is entitled to indemnification under this Agreement if Indemnitee has submitted a request in accordance with Section 11(a), and the Company has the burden of proof to overcome that presumption by clear and convincing evidence.

(b) *Effect of other Proceedings.* The termination of any Proceeding or any claim, issue or matter in it, by judgment, order, settlement or conviction, or upon a plea of *nolo contendere* or its equivalent, does not of itself adversely affect Indemnitee's right to indemnification or create a presumption that Indemnitee did not act in good faith and in a manner Indemnitee reasonably believed to be in or not opposed to the best interests of the Company or, with respect to any criminal Proceeding, that Indemnitee had reasonable cause to believe that Indemnitee's conduct was unlawful.

(c) *Reliance as safe harbor.* For purposes of any determination of good faith, Indemnitee is deemed to have acted in good faith if Indemnitee's action is based on the records or books of account of the Enterprise, including financial statements; on information supplied to Indemnitee by the officers of the Enterprise in the course of their duties; on the advice of legal counsel for the Enterprise or the Board or any committee of it; or on information or records given, or reports made, to the Enterprise or the Board or any committee by an independent certified public accountant, an appraiser, or another expert selected with reasonable care by the Enterprise, the Board, or a committee. The provisions of this Section 12(c) are not exclusive and do not limit in any way the other circumstances in which Indemnitee may be deemed or found to have met the applicable standard of conduct.

(d) *No imputation.* The knowledge, actions, or failure to act of any other director, officer, trustee, partner, manager, managing member, fiduciary, agent or employee of the Enterprise shall not be imputed to Indemnitee for purposes of determining Indemnitee's right to indemnification under this Agreement.

## 13. SECONDARY INDEMNITORS; COMPANY AS INDEMNITOR OF FIRST RESORT

> **Drafting note:** Include Section 13 for every director designated by or affiliated with an investor fund, and keep it (harmlessly) in the uniform form for everyone else. If no fund indemnitor exists for a given Indemnitee, the provision simply has no application. The bylaws (Section 6.10) contain matching language; keep them consistent.

(a) The Company acknowledges that Indemnitee has or may from time to time obtain rights to indemnification, advancement of expenses or insurance provided by one or more persons with whom or which Indemnitee may be associated, including [[Optional: {{fund_indemnitor_names}} and]] any investment fund, management company, general partner, or other affiliate of any stockholder of the Company that has designated or nominated Indemnitee to serve on the Board (collectively, the "**Fund Indemnitors**").

(b) The Company (i) is the indemnitor of first resort with respect to Indemnitee — that is, its obligations to Indemnitee are primary, and any obligation of the Fund Indemnitors to advance expenses or to provide indemnification for the same Expenses or liabilities incurred by Indemnitee is secondary; (ii) shall be required to advance the full amount of Expenses incurred by Indemnitee and shall be liable for the full amount of all Expenses, judgments, penalties, fines and amounts paid in settlement to the extent legally permitted and required by this Agreement, the Certificate of Incorporation and the Bylaws (or any other agreement between the Company and Indemnitee), without regard to any rights Indemnitee may have against the Fund Indemnitors; and (iii) irrevocably waives, relinquishes and releases the Fund Indemnitors from any and all claims against them for contribution, subrogation or any other recovery of any kind in respect of any amount paid by the Company.

(c) No advancement or payment by the Fund Indemnitors on behalf of Indemnitee with respect to any claim for which Indemnitee has sought indemnification from the Company affects the foregoing. The Fund Indemnitors have a right of contribution or are subrogated to the extent of that advancement or payment to all of the rights of recovery of Indemnitee against the Company, and the Company shall reimburse the Fund Indemnitors on demand.

(d) The Fund Indemnitors are express third-party beneficiaries of this Section 13, entitled to enforce it as though each were a party to this Agreement. No amendment of this Section 13 that adversely affects the Fund Indemnitors is effective against them without their written consent.

(e) Section 8(a) and Section 14(c) shall not be construed to reduce the Company's obligations by reason of any right of Indemnitee against, or payment by, a Fund Indemnitor.

## 14. NON-EXCLUSIVITY; INSURANCE; SUBROGATION

(a) *Non-exclusivity; more favorable terms.* The rights of indemnification and advancement provided by this Agreement are not exclusive of any other rights to which Indemnitee may at any time be entitled under applicable law, the Certificate of Incorporation, the Bylaws, any agreement, a vote of stockholders or a resolution of directors, or otherwise. No amendment, alteration or repeal of this Agreement or of any provision of it limits or restricts any right of Indemnitee under this Agreement with respect to any action taken or omitted by Indemnitee in Indemnitee's Corporate Status before the amendment, alteration or repeal. To the extent that a change in Delaware law (whether by statute or judicial decision) permits greater indemnification or advancement than would be afforded under the Certificate of Incorporation, the Bylaws or this Agreement, it is the intent of the parties that Indemnitee enjoy by this Agreement the greater benefits so afforded. To the extent the Certificate of Incorporation or Bylaws at any time provide rights more favorable to Indemnitee than this Agreement, Indemnitee is entitled to those more favorable rights. No right or remedy in this Agreement is exclusive of any other right or remedy, and every right and remedy is cumulative.

(b) *D&O insurance.* For as long as the Company maintains directors' and officers' liability insurance, Indemnitee shall be covered by the policy or policies in accordance with their terms to the maximum extent of the coverage available for any director or officer of the Company under the policy or policies. [[Optional: The Company shall use commercially reasonable efforts to obtain and maintain directors' and officers' liability insurance with reputable insurers, with coverage and limits the Board determines in good faith to be reasonable. If the Company determines in good faith that insurance is not reasonably available, the premium costs are disproportionate to the coverage provided, or the coverage is so limited by exclusions that it provides an insufficient benefit, the Company may decline to obtain or maintain it and shall promptly notify Indemnitee.]] [[Optional: Upon a Change in Control, the Company shall obtain, or cause the acquirer or successor to obtain, a "tail" policy of directors' and officers' liability insurance with a term of not less than {{d_and_o_tail_years}} years after the Change in Control, covering Indemnitee on terms no less favorable in coverage and amount than the policy in effect immediately before the Change in Control.]]

(c) *Subrogation.* In the event of any payment under this Agreement, the Company is subrogated to the extent of the payment to all of Indemnitee's rights of recovery (other than against the Fund Indemnitors), and Indemnitee shall sign all papers required and take all action necessary to secure those rights, including signing any documents necessary to enable the Company to bring suit to enforce them.

(d) *No duplication.* Except as provided in Section 13, the Company is not liable under this Agreement to make any payment of amounts otherwise indemnifiable (or for which advancement is provided) to the extent Indemnitee has otherwise actually received payment under any insurance policy, contract, agreement or otherwise.

(e) *Service for other Enterprises.* The Company's obligation to indemnify or advance Expenses to Indemnitee for Indemnitee's service at the Company's request with any other Enterprise is reduced by any amount Indemnitee has actually received as indemnification or advancement from that Enterprise.

## 15. REMEDIES OF INDEMNITEE

(a) *Right to sue.* If (i) a determination is made under Section 11 that Indemnitee is not entitled to indemnification; (ii) advancement is not timely made under Section 9; (iii) no determination of entitlement is made within the periods in Section 11(e); (iv) payment of indemnification is not made within ten (10) days after a determination (or deemed determination) of entitlement; or (v) payment under Section 5 or 6 is not made within ten (10) days after the Company receives a written request for it, then Indemnitee is entitled to an adjudication by the Court of Chancery of the State of Delaware of Indemnitee's entitlement to that indemnification or advancement. The Company shall not oppose Indemnitee's right to seek any such adjudication. [[Optional: Alternatively, Indemnitee may elect an award in arbitration conducted by a single arbitrator under the Commercial Arbitration Rules of the American Arbitration Association, seated in Wilmington, Delaware.]]

(b) *De novo; burden.* If a determination has been made under Section 11 that Indemnitee is not entitled to indemnification, any judicial proceeding commenced under this Section 15 shall be conducted in all respects as a de novo trial on the merits, and Indemnitee shall not be prejudiced by reason of that adverse determination. In any such proceeding the Company has the burden of proving that Indemnitee is not entitled to indemnification or advancement.

(c) *Binding favorable determination.* If a determination has been made under Section 11 that Indemnitee is entitled to indemnification, the Company is bound by that determination in any judicial proceeding commenced under this Section 15, absent (i) a misstatement by Indemnitee of a material fact, or an omission of a material fact necessary to make Indemnitee's statement not materially misleading, in connection with the request for indemnification, or (ii) a prohibition of indemnification under applicable law.

(d) *Expenses of enforcement.* The Company shall indemnify Indemnitee against all Expenses actually and reasonably incurred by Indemnitee in any action for indemnification or advancement from the Company under this Agreement, or under any directors' and officers' liability insurance policies maintained by the Company, if Indemnitee ultimately is determined to be entitled to that indemnification, advancement or insurance recovery, in whole or in part, and shall advance those Expenses within {{advancement_days}} days after request, subject to the undertaking in Section 9(c).

(e) *No challenge to validity.* The Company is precluded from asserting in any judicial proceeding commenced under this Section 15 that the procedures and presumptions of this Agreement are not valid, binding and enforceable, and shall stipulate in that proceeding that the Company is bound by all the provisions of this Agreement.

## 16. CONTRIBUTION

(a) To the fullest extent permissible under applicable law, if the indemnification provided for in this Agreement is unavailable to Indemnitee for any reason, the Company, in lieu of indemnifying Indemnitee, shall contribute to the amounts incurred by Indemnitee, whether for judgments, fines, penalties, excise taxes, amounts paid or to be paid in settlement, or Expenses, in connection with any claim relating to an indemnifiable event under this Agreement, in the proportion the Company deems fair and reasonable in light of all of the circumstances of the Proceeding, in order to reflect (i) the relative benefits received by the Company and Indemnitee as a result of the events or transactions giving rise to the Proceeding, and (ii) the relative fault of the Company (and its directors, officers, employees and agents) and Indemnitee in connection with those events or transactions.

(b) The Company shall fully indemnify and hold Indemnitee harmless from any claims of contribution that may be brought by officers, directors or employees of the Company (other than Indemnitee) who may be jointly liable with Indemnitee, to the extent Indemnitee would be entitled to indemnification for the underlying liability under this Agreement.

## 17. DURATION OF AGREEMENT

This Agreement is effective as of the Effective Date and applies to acts or omissions of Indemnitee occurring before, on or after the Effective Date, if Indemnitee was serving in a Corporate Status at the time of the act or omission. This Agreement continues until, and terminates upon, the later of (a) ten (10) years after the date that Indemnitee has ceased to serve as a director or officer of the Company or as a director, officer, manager, partner, trustee, employee, agent or fiduciary of any other Enterprise at the Company's request, and (b) one (1) year after the final termination of any Proceeding then pending in respect of which Indemnitee is granted rights of indemnification or advancement under this Agreement and of any proceeding commenced by Indemnitee under Section 15 relating to it.

## 18. ENFORCEMENT AND BINDING EFFECT

(a) *Inducement.* The Company has entered into this Agreement and assumed the obligations imposed on it to induce Indemnitee to serve or continue to serve the Company, and acknowledges that Indemnitee is relying on this Agreement in serving.

(b) *Successors.* This Agreement is binding on and enforceable by the parties and their respective successors (including any direct or indirect successor by purchase, merger, consolidation or otherwise to all or substantially all of the business or assets of the Company), assigns, spouses, heirs, executors and personal and legal representatives. The Company shall require and cause any such successor, by written agreement in form and substance satisfactory to Indemnitee, expressly to assume and agree to perform this Agreement in the same manner and to the same extent that the Company would be required to perform if no succession had taken place.

(c) *Specific performance.* The Company and Indemnitee agree that Indemnitee may suffer irreparable harm from a breach of this Agreement by the Company, that monetary damages may be inadequate, and that Indemnitee may enforce this Agreement by seeking injunctive relief or specific performance, without any requirement to post a bond or other security (which the Company waives) and without proof of actual damages. The Company acknowledges that the Court of Chancery has exclusive jurisdiction under Section 145(k) of the DGCL to hear and determine actions for advancement and indemnification and may summarily determine the Company's obligation to advance Expenses.

## 19. GENERAL PROVISIONS

**19.1 Governing Law.** This Agreement and all claims arising out of or relating to it are governed by the laws of the State of Delaware, without regard to conflict-of-laws principles that would require the application of the laws of another jurisdiction.

**19.2 Forum; Consent to Jurisdiction.** Except with respect to any arbitration elected by Indemnitee under Section 15(a), the Company and Indemnitee irrevocably and unconditionally (a) agree that any action or proceeding arising out of or in connection with this Agreement shall be brought only in the Court of Chancery of the State of Delaware, and not in any other state or federal court in the United States or any court in any other country; (b) consent to submit to the exclusive jurisdiction of the Court of Chancery for purposes of any such action or proceeding; (c) appoint, to the extent that party is not otherwise subject to service of process in the State of Delaware, the Company's registered agent in Delaware as its agent in Delaware for acceptance of legal process in connection with any such action or proceeding, with the same legal force and validity as if served upon that party personally within the State of Delaware; (d) waive any objection to the laying of venue of any such action or proceeding in the Court of Chancery; and (e) waive, and agree not to plead or make, any claim that any such action or proceeding brought in the Court of Chancery has been brought in an improper or inconvenient forum.

**19.3 Waiver of Jury Trial.** EACH PARTY KNOWINGLY, VOLUNTARILY AND INTENTIONALLY WAIVES, TO THE FULLEST EXTENT PERMITTED BY LAW, ANY RIGHT TO A TRIAL BY JURY IN ANY ACTION OR PROCEEDING ARISING OUT OF OR RELATING TO THIS AGREEMENT. (Actions in the Court of Chancery are tried without a jury; this waiver applies to any action that is nonetheless heard in another court.)

**19.4 Notices.** All notices and other communications under this Agreement shall be in writing and are deemed duly given (a) when delivered by hand, with written confirmation of receipt; (b) one (1) business day after deposit with a nationally recognized overnight courier, charges prepaid, for next-business-day delivery; (c) three (3) business days after mailing by certified or registered mail, return receipt requested, postage prepaid; or (d) when sent by electronic mail, if sent before 5:00 p.m. in the recipient's time zone on a business day and no notice of delivery failure is received (and otherwise on the next business day), in each case to the address or email address below (or another address a party designates by notice):

If to the Company: {{company_name}}, {{company_address}}, Attention: Chief Executive Officer; email: {{company_notice_email}}.

If to Indemnitee: {{indemnitee_address}}; email: {{indemnitee_email}}.

**19.5 Entire Agreement.** This Agreement constitutes the entire agreement between the parties with respect to its subject matter and supersedes all prior agreements and understandings, oral or written, between the parties with respect to that subject matter; provided that this Agreement is a supplement to and in furtherance of the Certificate of Incorporation, the Bylaws, and applicable law, and does not diminish or abrogate any rights of Indemnitee under them.

**19.6 Amendment and Waiver.** No supplement, modification, termination or amendment of this Agreement is binding unless in writing and signed by both parties (and, as to Section 13, subject to Section 13(d)). No waiver of any provision of this Agreement is a waiver of any other provision, whether or not similar, and no waiver is a continuing waiver. No failure or delay in exercising any right operates as a waiver of it.

**19.7 Severability.** If any provision of this Agreement is held invalid, illegal or unenforceable for any reason, (a) the validity, legality and enforceability of the remaining provisions (including each portion of any section containing the invalid provision that is not itself invalid, illegal or unenforceable) are not affected or impaired; and (b) to the fullest extent possible, the provisions of this Agreement shall be construed so as to give effect to the intent manifested by the invalid, illegal or unenforceable provision.

**19.8 Assignment.** Indemnitee may not assign this Agreement except by will or the laws of descent and distribution. The Company may not assign this Agreement except to a successor that assumes it under Section 18(b).

**19.9 Counterparts; Electronic Signatures.** This Agreement may be executed in counterparts, each of which is an original and all of which together are one instrument. Signatures delivered by electronic transmission (including PDF and any electronic signature complying with the U.S. federal Electronic Signatures in Global and National Commerce Act, 15 U.S.C. § 7001 et seq., or the Delaware Uniform Electronic Transactions Act, 6 Del. C. ch. 12A) are effective as originals.

**19.10 Construction.** Headings are for convenience only and do not affect interpretation. "Including" means "including without limitation"; "or" is not exclusive; words in the singular include the plural and vice versa; references to sections are to sections of this Agreement; and references to a statute or rule include any successor provision. This Agreement shall be construed as having been drafted jointly, and no presumption or burden of proof arises favoring or disfavoring either party by virtue of authorship.

**19.11 Further Assurances.** Each party shall sign and deliver any further instruments and take any further action reasonably requested by the other party to carry out the intent of this Agreement.

**19.12 Expenses.** Except as otherwise provided in this Agreement, each party bears its own costs in negotiating and entering into this Agreement.

[[Optional: **19.13 Securities Act Undertaking.** Indemnitee acknowledges that the Securities and Exchange Commission has taken the position that indemnification of directors and officers for liabilities under the Securities Act of 1933 is against public policy and therefore unenforceable, and that the Company may be required to undertake, in a registration statement filed under that Act, to submit the question of indemnification to a court in certain circumstances before making any indemnification payment for such liabilities. Indemnitee agrees that this Agreement is subject to any such undertaking.]]

**19.14 Approval.** The Company represents that the Board has approved this Agreement and authorized its execution and delivery.

*[Signature page follows.]*

---

IN WITNESS WHEREOF, the parties have executed this Indemnification Agreement as of the Effective Date.

**{{company_name}}**

By: ______________________________
Name: {{signatory_name}}
Title: {{signatory_title}}

**INDEMNITEE**

______________________________
{{indemnitee_name}}

Address: {{indemnitee_address}}
Email: {{indemnitee_email}}

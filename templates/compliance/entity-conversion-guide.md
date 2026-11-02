---
id: entity-conversion-guide
title: Converting an LLC to a Delaware Corporation — Guide, Plan of Conversion, Member Consent, and Certificate of Conversion
category: compliance
stage: compliance
signers: [LLC members or managers as the LLC agreement and 6 Del. C. § 18-216 require (plan of conversion); authorized person of the LLC (certificate of conversion); incorporator or authorized person (certificate of incorporation); recipients of restricted stock (restricted stock agreements)]
authorities:
  - "8 Del. C. § 265 (conversion of other entities to a Delaware corporation; certificate of conversion and certificate of incorporation filed together; existence relates back; plan of conversion; corporate actions deemed approved under § 265(l))"
  - "6 Del. C. § 18-216 (approval of conversion of a Delaware LLC; default approval by members owning more than 50% of profits interests)"
  - "6 Del. C. § 18-1107 (LLC annual tax of $400; full year's tax due before a filing that ends LLC existence)"
  - "8 Del. C. § 391(a)(26) and Division of Corporations Fee Schedule revised August 1, 2026 (conversion of other entity to corporation $184 plus certificate of incorporation fee)"
  - "26 U.S.C. §§ 351, 357, 358, 362, 368(a)(1)(F), 721, 732 (tax treatment of incorporation)"
  - "Rev. Rul. 2004-59, 2004-24 I.R.B. 1050 (formless state-law conversion of partnership to corporation treated as assets-over contribution and liquidating distribution)"
  - "Treas. Reg. § 301.7701-3(g)(1)(i) (elective change from partnership to association)"
  - "26 U.S.C. § 1202(c), (d), (i) as amended by P.L. 119-21 (QSBS: original issuance; $75 million gross assets test for stock issued after July 4, 2025; holding period from exchange; basis not less than fair market value of property exchanged)"
  - "26 U.S.C. § 83 and Treas. Reg. § 1.83-2 (restricted stock; 83(b) elections); Rev. Proc. 93-27 and Rev. Proc. 2001-43 (profits interests)"
use_when: An operating LLC (Delaware or another state) needs to become a Delaware C corporation, typically before a venture financing, a stock option program, or a QSBS-motivated restructuring.
do_not_use_when: The business has not yet formed an entity (form a Delaware corporation directly; see templates/formation/), the LLC is taxed as an S corporation or C corporation and only a state-law change is wanted (the same statutory steps apply, but the tax analysis is an F reorganization; involve tax counsel), or the converting entity is a foreign (non-U.S.) entity (use domestication under § 388).
related: [certificate-of-incorporation, bylaws, initial-board-consent, founder-stock-purchase-agreement, 83b-election-package, equity-incentive-plan, foreign-qualification-guide, delaware-franchise-tax-and-annual-report]
sources:
  - name: "Delaware Code, Title 8, § 265 (official text, read November 2, 2026)"
    url: https://delcode.delaware.gov/title8/c001/sc09/index.html
  - name: "Delaware Code, Title 6, §§ 18-216 and 18-1107 (official text, read November 2, 2026)"
    url: https://delcode.delaware.gov/title6/c018/sc02/index.html
  - name: "Delaware Division of Corporations Fee Schedule, revised August 1, 2026"
    url: https://corpfiles.delaware.gov/Fee_Schedule/AugustFee2026.pdf
  - name: "Rev. Rul. 2004-59, 2004-24 I.R.B. 1050"
    url: https://www.irs.gov/pub/irs-irbs/irb04-24.pdf
  - name: "Treas. Reg. § 301.7701-3 (eCFR)"
    url: https://www.ecfr.gov/current/title-26/section-301.7701-3
  - name: "26 U.S.C. § 1202 (uscode.house.gov, current through P.L. 119-136)"
    url: https://uscode.house.gov/us/usc/t26/s1202/
  - name: "Cooley GO, Gunderson, and Orrick commentary on LLC-to-C-corporation conversions (structure reference only; no text copied)"
    url: https://www.cooleygo.com/
last_verified: 2026-11-02
---

## About this template

**What it does.** This file explains how to convert a limited liability company into a Delaware corporation, the tax consequences, and the equity mechanics (vesting, profits interests, options, the cap table), and provides a plan of conversion, a member consent approving it, and a certificate of conversion. The converted corporation's certificate of incorporation and bylaws come from templates/formation/certificate-of-incorporation.md and templates/formation/bylaws.md.

**Why startups convert.** Venture investors buy preferred stock of C corporations; stock options and ISOs require a corporation; partnership tax (K-1s, phantom income, state filings for every member) is unworkable for funds with tax-exempt and foreign limited partners; and only C corporation stock can be qualified small business stock under I.R.C. § 1202. Convert before the financing term sheet is signed, because the conversion is a closing condition with its own timeline (two to six weeks is typical).

**Methods compared.**

| Method | How | Pros | Cons |
|---|---|---|---|
| Statutory conversion (recommended for a Delaware LLC) | Approve under 6 Del. C. § 18-216; file a certificate of conversion and a certificate of incorporation simultaneously under 8 Del. C. § 265 | Same legal entity; contracts, permits, property, and liabilities stay with it (§ 265(f)); no assignment for Delaware law purposes; one filing | Tax treated as an assets-over incorporation under Rev. Rul. 2004-59 for a partnership; foreign-state registrations must be updated |
| Conversion of a non-Delaware LLC | Convert out under the home state's LLC act and into Delaware under § 265 (or first convert or domesticate to a Delaware LLC) | Same as above | Two states' statutes and filings; confirm the home state permits outbound conversion to a foreign corporation |
| Merger | Merge the LLC into a newly formed Delaware corporation (8 Del. C. § 264; 6 Del. C. § 18-209) | Useful when the LLC agreement's merger approval is easier, or for combining entities | Contracts may treat a merger as an assignment; more paperwork |
| Contribution ("interests over") | Members contribute their LLC interests to a new corporation for stock; the LLC becomes a subsidiary | No state-law conversion; can keep the LLC for licenses | Two entities to maintain; the LLC later merges up or is disregarded |
| Check-the-box only | LLC elects corporate tax status on Form 8832 | Simple | Still an LLC under state law; investors will not buy; no ISOs |

**Delaware mechanics (statutory conversion of a Delaware LLC).**
1. **Approval (6 Del. C. § 18-216(b)).** If the LLC agreement specifies how to authorize a conversion, follow it. If it is silent on conversion but specifies how to approve a merger or consolidation, use that. If it is silent on both and does not prohibit conversion, approval requires members owning more than 50% of the then-current percentage or other interest in the profits of the LLC (LLCs formed on or before July 31, 2015 keep the rule in effect on that date unless the agreement provides otherwise). Check the LLC agreement for consent rights of particular classes, preemptive or tag rights, and drag provisions.
2. **Plan of conversion (8 Del. C. § 265(k)).** Optional but recommended. It may state the terms and conditions; attach the certificate of incorporation; state how interests convert into stock, rights, or other securities (or are cancelled) (§ 265(j)); and list corporate actions the converted corporation will take. Any corporate action set out in an approved plan that is within the corporation's powers "shall be deemed authorized, adopted and approved" by the corporation, its board, and its stockholders without further action (§ 265(l)), so the plan can adopt the bylaws, fix the board size, elect directors, appoint officers, and approve forms of restricted stock agreements.
3. **Filings (§ 265(b)–(c), (i)).** File simultaneously (and with the same future effective time, if any) a certificate of conversion and a certificate of incorporation. The certificate of conversion states (1) the date and jurisdiction of the LLC's original formation (and its jurisdiction immediately before conversion if changed); (2) the LLC's name and entity type immediately before filing; (3) the corporation's name as set forth in its certificate of incorporation; and (4) if a plan of conversion was adopted, that all its provisions were approved before effectiveness under all applicable law. It is signed by a person authorized to sign for the LLC.
4. **Fees and taxes.** Division fee for a conversion of another entity to a corporation: $184, plus the certificate of incorporation fee (from $109 for a one-page certificate; varies with authorized stock), plus page fees and expedite fees (fee schedule revised August 1, 2026). The LLC's full annual tax for the calendar year of conversion ($400) must be paid before the filing (6 Del. C. § 18-1107(c)), along with any unpaid prior-year taxes.
5. **Effect.** The corporation is the same entity as the LLC for all purposes of Delaware law; its existence is deemed to have commenced when the LLC was formed (§ 265(d)); all property, rights, debts, and liabilities remain vested in it and are not deemed transferred (§ 265(f)); the LLC is not required to wind up (§ 265(g)). Prior obligations and personal liabilities are not affected (§ 265(e)).

**Tax treatment (summary; always involve tax counsel).**
- **Multi-member LLC taxed as a partnership.** A formless state-law conversion is treated as if the partnership contributed all its assets and liabilities to the corporation for stock and then distributed the stock to its partners in liquidation (Rev. Rul. 2004-59; the same "assets-over" form applies to an elective change under Treas. Reg. § 301.7701-3(g)(1)(i)). The contribution is generally tax-free under I.R.C. § 351, but gain is recognized to the extent liabilities assumed exceed the aggregate basis of the assets (§ 357(c), with the § 357(c)(3) exclusion for liabilities that would give rise to a deduction, such as cash-basis payables). The corporation takes a carryover basis in the assets (§ 362); each partner's basis in the distributed stock generally equals the partner's outside basis in the partnership (§ 732(b)). The partnership files a final Form 1065 and K-1s for the short year ending on the conversion date.
- **Single-member LLC (disregarded).** Treated as the owner contributing the LLC's assets to the new corporation for stock, generally tax-free under § 351, subject to § 357(c).
- **LLC already taxed as a corporation.** A conversion of an LLC that elected C corporation (or S corporation) status is generally a reorganization under § 368(a)(1)(F); the S election may terminate if the converted corporation issues preferred stock or admits ineligible holders.
- **EIN.** IRS guidance generally requires a new EIN when a partnership incorporates; an entity already taxed as a corporation that changes only its state-law form generally keeps its EIN.

> **Verify:** Confirm on IRS.gov ("Do you need a new EIN?") whether the converted corporation needs a new EIN on the client's facts, and update payroll, state tax, and bank records accordingly.

**QSBS (I.R.C. § 1202) after P.L. 119-21.** For stock issued after July 4, 2025, the exclusion is 50% after three years, 75% after four years, and 100% after five years; the per-issuer cap is $15,000,000 (indexed after 2026) or, if greater, ten times the taxpayer's aggregate adjusted basis in the issuer's stock disposed of in the year; and the issuer's aggregate gross assets may not exceed $75,000,000 (indexed after 2026) at any time before and immediately after issuance. On a conversion:
- Stock received in exchange for property (including partnership assets in the assets-over form) is treated as acquired on the date of the exchange, and its basis for § 1202 purposes "shall in no event be less than the fair market value of the property exchanged" (§ 1202(i)(1)). The holding period starts at conversion, and pre-conversion appreciation is not eligible; only post-conversion gain can be excluded. The fair-market-value basis also increases the "10 times basis" alternative cap, which can make the cap far larger than $15,000,000 for a valuable LLC.
- For the $75,000,000 gross assets test, contributed property is counted at its fair market value when contributed (§ 1202(d)(2)(B)). A highly valued LLC may fail the test at conversion; value the business before converting.
- Profits-interest holders who receive stock also get a new holding period from conversion.
- An LLC that had elected corporate tax status raises separate questions about whether its earlier interests were "stock" for § 1202; obtain a specific opinion.
- Several states (notably California) do not conform to § 1202.

> **Verify:** Confirm the § 1202 analysis for an LLC that was taxed as a corporation before its state-law conversion, and the state conformity position for the members' states of residence, with tax counsel.

**Equity mechanics.**
- **Allocation of shares.** The plan of conversion must say exactly how many shares each member receives. For a partnership with a distribution waterfall (capital-first, then profits), allocate shares by a hypothetical liquidation at fair market value on the conversion date, so each member receives stock equal in value to what the member would receive if the LLC sold its assets for that value and liquidated. Profits interests below their hurdle (threshold value) may receive nothing. Record the valuation and the waterfall computation as an exhibit.
- **Preferred units.** If the LLC had preferred units, either convert them into a series of Preferred Stock with corresponding economic terms (requiring a more complex charter) or negotiate a conversion to Common Stock. Investors in the next round usually prefer a clean Common-only cap table.
- **Vesting carries over.** Shares received for unvested units should be restricted stock subject to the same vesting schedule, acceleration, and repurchase terms, documented in a restricted stock agreement signed at conversion. Founders often take the opportunity to adopt investor-standard vesting.
- **83(b) elections.** For shares received in exchange for unvested interests, file an 83(b) election within 30 days after the conversion unless tax counsel concludes it is unnecessary; practitioners commonly file protective elections because the treatment of an exchange of unvested profits interests for unvested stock is not settled.
- **Options and phantom units.** LLC unit options convert into options for Common Stock under a new equity plan, preserving the spread and ratio to stay within the § 409A substitution rules (Treas. Reg. § 1.409A-1(b)(5)(v)(D)); they cannot become ISOs retroactively, and new ISOs require a stockholder-approved plan (I.R.C. § 422(b)(1)). Phantom units or unit appreciation rights are often deferred compensation under § 409A; convert them only with tax advice.
- **New 409A valuation.** Obtain a valuation of the corporation's Common Stock before any option grant after conversion; the LLC's unit valuation does not carry over.
- **Securities law.** The exchange of LLC interests for stock should be treated as an offering. Because the converted corporation is the same entity under Delaware law, counsel commonly rely on § 3(a)(9) of the Securities Act (exchange with existing security holders, no commission paid) or, alternatively, § 4(a)(2) and Regulation D; restricted stock to service providers may rely on Rule 701. Check state blue-sky exemptions.

**After conversion (operational checklist).** Update foreign qualifications (many states require the converted corporation to qualify as a corporation and the LLC registration to be withdrawn or amended); notify banks, payroll, insurers, landlord, customers, and vendors; review contracts for change-of-form or assignment clauses and licenses or permits issued to the LLC; file final LLC tax returns and any state LLC fee returns (California LLCs owe the LLC tax and fee for the final year); register the corporation with state tax agencies; begin Delaware annual reports and franchise tax (due March 1 following the year of conversion); and update the stock ledger and issue § 151(f) notices.

**Common mistakes.**
- Converting without reading the LLC agreement's approval and consent rights.
- Filing the certificate of conversion and certificate of incorporation at different times or with different effective times (§ 265(b) requires simultaneous filing).
- No valuation or waterfall support for the share allocation, inviting member disputes and tax exposure.
- Forgetting 83(b) elections for restricted stock received in exchange for unvested units.
- Granting options right after conversion without a new 409A valuation or a stockholder-approved plan.
- Assuming QSBS holding periods include LLC years.

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `llc_name` | Exact name of the LLC | Northwind Robotics LLC | |
| `llc_formation_state`, `llc_formation_date` | Where and when the LLC was formed | Delaware; March 2, 2025 | § 265(c)(1) |
| `llc_agreement_title` | LLC operating agreement | Amended and Restated Limited Liability Company Agreement dated June 1, 2025 | |
| `company_name` | Name of the converted corporation | Northwind Robotics, Inc. | Shared |
| `effective_date`, `effective_time_of_day` | Effective time of the conversion | January 4, 2027; 12:01 a.m. Eastern Time | Shared |
| `authorized_common_shares`, `par_value` | Charter capitalization | 10,000,000; $0.00001 | Shared |
| `conversion_valuation`, `valuation_date` | Fair market value used for the waterfall | $6,000,000; December 31, 2026 | |
| `member_names` | Members and their units | Alex Rivera (Class A Units); Jordan Lee (Class B Units) | |
| `total_shares_issued_in_conversion` | Shares issued to all members | 8,000,000 | |
| `initial_directors`, `board_size` | Board of the corporation | Alex Rivera; Jordan Lee; 2 | Shared |
| `ceo_name`, `secretary_name`, `cfo_name` | Officers | | Shared |
| `fiscal_year_end` | Fiscal year end | December 31 | Shared |
| `plan_name` | New equity plan | 2027 Equity Incentive Plan | Shared |
| `plan_reserve_shares` | Shares reserved | 1,500,000 | Shared |
| `registered_agent_name`, `registered_agent_address` | Delaware registered agent | | Shared |
| `authorized_person_name`, `authorized_person_title` | Person signing the certificate of conversion | Alex Rivera; Manager | |
| `approval_threshold_description` | LLC approval required | Members holding a majority of the Class A Units, as required by Section 9.2 of the LLC Agreement | |

## Form

---

# PART 1. PLAN OF CONVERSION

# PLAN OF CONVERSION OF {{llc_name}} (a {{llc_formation_state}} limited liability company) INTO {{company_name}} (a Delaware corporation)

This Plan of Conversion (this "**Plan**") is adopted by {{llc_name}}, a {{llc_formation_state}} limited liability company (the "**LLC**"), pursuant to § 18-216 of the Delaware Limited Liability Company Act (the "**LLC Act**") [[Optional: and the applicable provisions of the laws of the State of {{llc_formation_state}}]], Section 265 of the General Corporation Law of the State of Delaware (the "**DGCL**"), and the {{llc_agreement_title}} (the "**LLC Agreement**").

## 1. Conversion

**1.1 Conversion.** At the Effective Time (as defined in Section 1.2), the LLC shall convert into a Delaware corporation named {{company_name}} (the "**Corporation**") in accordance with § 18-216 of the LLC Act and Section 265 of the DGCL (the "**Conversion**"). The Corporation shall be deemed the same entity as the LLC for all purposes of the laws of the State of Delaware, and the existence of the Corporation shall be deemed to have commenced on {{llc_formation_date}}, the date the LLC commenced its existence.

**1.2 Effective Time.** The LLC shall file with the Secretary of State of the State of Delaware, simultaneously, a certificate of conversion in the form of Exhibit A (the "**Certificate of Conversion**") and a certificate of incorporation in the form of Exhibit B (the "**Certificate of Incorporation**"), each providing that it shall become effective at {{effective_time_of_day}} on {{effective_date}} (the "**Effective Time**").

**1.3 Effect.** At the Effective Time, all of the rights, privileges, and powers of the LLC, and all property, real, personal, and mixed, all debts due to the LLC, and all other things and causes of action belonging to the LLC, shall remain vested in the Corporation, and all debts, liabilities, and duties of the LLC shall remain attached to the Corporation, as provided in Section 265(f) of the DGCL. The LLC shall not be required to wind up its affairs or pay its liabilities and distribute its assets, and the Conversion shall not constitute a dissolution of the LLC.

## 2. Conversion of Interests

**2.1 Conversion of Units.** At the Effective Time, by virtue of the Conversion and without any action by any member, all limited liability company interests in the LLC (the "**Units**") outstanding immediately before the Effective Time shall be converted into an aggregate of {{total_shares_issued_in_conversion}} shares of Common Stock, par value {{par_value}} per share, of the Corporation (the "**Common Stock**"), allocated among the holders of Units as set forth in Schedule 1. The allocation in Schedule 1 has been determined by applying the distribution provisions of the LLC Agreement to a hypothetical sale of all of the LLC's assets for {{conversion_valuation}}, the fair market value of the LLC as of {{valuation_date}}, followed by a liquidation of the LLC, and each member's shares have an aggregate value equal to the amount such member would have received in that hypothetical liquidation.

**2.2 No Fractional Shares.** No fractional shares of Common Stock shall be issued. Any fractional share to which a member would otherwise be entitled shall be rounded [[Alternative A: down to the nearest whole share, and no consideration shall be paid for the fraction]] [[Alternative B: to the nearest whole share (with one-half rounded up)]].

**2.3 Unvested Units.** Each Unit that is unvested or subject to forfeiture or repurchase immediately before the Effective Time (an "**Unvested Unit**") shall be converted into shares of Common Stock that are subject to the same vesting schedule (including the same vesting commencement date and any acceleration provisions) and to forfeiture or repurchase on the same terms, adjusted to reflect the conversion. As a condition to receiving such shares, each holder of Unvested Units shall execute a restricted stock agreement with the Corporation in the form of Exhibit C. The Corporation shall deliver to each such holder a form of election under Section 83(b) of the Internal Revenue Code of 1986, as amended (the "**Code**"), which the holder may file within thirty (30) days after the Effective Time, and each holder is advised to consult the holder's own tax advisor.

**2.4 Options and Other Rights.** [[Alternative A: No options, warrants, phantom units, or other rights to acquire Units are outstanding.]] [[Alternative B: Each option to acquire Units outstanding immediately before the Effective Time shall be converted into an option to purchase shares of Common Stock under the {{plan_name}}, with the number of shares and exercise price adjusted in a manner that preserves the aggregate spread and the ratio of exercise price to fair market value, so as to comply with Treasury Regulation § 1.409A-1(b)(5)(v)(D), and otherwise on substantially the same terms.]]

**2.5 Uncertificated Shares; Stock Ledger.** The shares of Common Stock issued in the Conversion shall be uncertificated. Promptly after the Effective Time, the Corporation shall record such shares in its stock ledger and deliver to each holder the notice required by Section 151(f) of the DGCL, including the legends required by the restricted stock agreements, the Bylaws, and applicable securities laws.

## 3. Governance of the Corporation

**3.1 Certificate of Incorporation and Bylaws.** At the Effective Time, the Certificate of Incorporation shall be the certificate of incorporation of the Corporation, and the bylaws in the form of Exhibit D (the "**Bylaws**") shall be the bylaws of the Corporation.

**3.2 Corporate Actions Deemed Approved.** Pursuant to Section 265(l) of the DGCL, upon approval of this Plan in accordance with Section 4.1, each of the following corporate actions of the Corporation, effective at the Effective Time, shall be deemed authorized, adopted, and approved by the Corporation and its board of directors and stockholders without further action:

(a) the adoption of the Bylaws;

(b) the fixing of the number of directors at {{board_size}} and the election of {{initial_directors}} as the directors of the Corporation, each to serve until such director's successor is duly elected and qualified or until such director's earlier death, resignation, or removal;

(c) the appointment of {{ceo_name}} as Chief Executive Officer, {{secretary_name}} as Secretary, and {{cfo_name}} as Chief Financial Officer;

(d) the issuance of the shares of Common Stock described in Article 2, for the consideration consisting of the Units, which the Corporation determines has a value not less than the par value of such shares, and the approval of the restricted stock agreement in the form of Exhibit C;

(e) the adoption of {{fiscal_year_end}} as the end of the Corporation's fiscal year;

(f) the continuation of the LLC's bank accounts, contracts, and qualifications in the name of the Corporation and the authorization of the officers to amend such qualifications and registrations, register the Corporation with tax authorities, and obtain any new employer identification number required;

(g) [[Optional: the adoption of the {{plan_name}} reserving {{plan_reserve_shares}} shares of Common Stock, subject to approval of such plan by the stockholders of the Corporation within twelve (12) months for purposes of Section 422 of the Code, which approval shall be sought after the Effective Time]]; and

(h) the authorization of the officers to take all actions necessary or advisable to carry out this Plan.

> **Drafting note:** § 265(l) deems these actions approved, which avoids a separate initial board consent; many practitioners still have the new board sign a short ratifying consent after the Effective Time (templates/formation/initial-board-consent.md) for a clean minute book. Seek a separate post-conversion stockholder approval of the equity plan for ISO purposes even if the plan is listed here.

> **Verify:** Confirm with tax counsel whether approval of the equity plan through the plan of conversion (by the members who become stockholders) satisfies Treas. Reg. § 1.422-3; the conservative approach is a separate stockholder consent after the Effective Time.

## 4. Approval; Amendment; Abandonment

**4.1 Approval.** This Plan, the Conversion, the Certificate of Conversion, and the Certificate of Incorporation shall be approved by {{approval_threshold_description}}, in accordance with § 18-216(b) of the LLC Act and the LLC Agreement, and by any other approval required under the LLC Agreement or applicable law, before the Effective Time.

**4.2 Amendment and Abandonment.** At any time before the Effective Time, the [[Alternative A: manager or managers]] [[Alternative B: members holding the approval required by Section 4.1]] may amend this Plan or abandon the Conversion, provided that no amendment that adversely changes the number of shares a member receives shall be made without that member's consent. If the Certificate of Conversion has been filed with a future Effective Time, abandonment or amendment shall be effected by filing a certificate of termination or amendment under Section 103(d) of the DGCL before the Effective Time.

## 5. Tax Treatment

The members intend that, for United States federal income tax purposes, the Conversion be treated in the manner described in Revenue Ruling 2004-59 (or, for an LLC disregarded as an entity separate from its owner, as a contribution of the LLC's assets to the Corporation in exchange for stock in a transaction described in Section 351 of the Code). No member is relying on the LLC, the Corporation, or any other member for tax advice, and each member shall bear the member's own taxes.

## 6. General

**6.1 Governing Law.** This Plan is governed by the laws of the State of Delaware [[Optional: , except that the authorization of the Conversion by the LLC is also governed by the laws of the State of {{llc_formation_state}}]].

**6.2 Counterparts; Electronic Signatures.** Consents approving this Plan may be executed in counterparts and delivered electronically, and each has the effect of an original under the Delaware Uniform Electronic Transactions Act (6 Del. C. ch. 12A) and the Electronic Signatures in Global and National Commerce Act (15 U.S.C. § 7001 et seq.).

**6.3 Further Assurances.** The LLC, the Corporation, and each member shall execute such further documents as are reasonably necessary to carry out this Plan.

**Schedule 1 — Allocation of Common Stock**

| Member | Units held (class) | Vested Units | Unvested Units | Shares of Common Stock (vested) | Shares of Common Stock (unvested) |
|---|---|---|---|---|---|
| {{member_names}} | | | | | |
| **Total** | | | | | **{{total_shares_issued_in_conversion}} (all shares)** |

**Exhibits:** A — Certificate of Conversion; B — Certificate of Incorporation (from templates/formation/certificate-of-incorporation.md); C — Restricted Stock Agreement; D — Bylaws (from templates/formation/bylaws.md); E — Valuation and waterfall computation.

---

# PART 2. WRITTEN CONSENT OF MEMBERS APPROVING CONVERSION

**{{llc_name}} — Action by Written Consent of the [[Alternative A: Members]] [[Alternative B: Manager(s) and Members]]**

The undersigned, constituting {{approval_threshold_description}} of {{llc_name}}, a {{llc_formation_state}} limited liability company (the "**LLC**"), acting by written consent pursuant to the LLC Agreement and § 18-302(d) of the Delaware Limited Liability Company Act, hereby adopt the following resolutions:

RESOLVED, that the Plan of Conversion attached hereto as Annex 1 (the "**Plan**"), the conversion of the LLC into {{company_name}}, a Delaware corporation, on the terms of the Plan (the "**Conversion**"), the Certificate of Conversion, the Certificate of Incorporation, and each corporate action of the Corporation described in Section 3.2 of the Plan, are hereby approved in all respects in accordance with § 18-216 of the Delaware Limited Liability Company Act and Section 265 of the General Corporation Law of the State of Delaware.

RESOLVED FURTHER, that {{authorized_person_name}}, as {{authorized_person_title}} of the LLC, is hereby authorized to execute and file the Certificate of Conversion and the Certificate of Incorporation with the Secretary of State of the State of Delaware, to pay all fees and taxes due (including the LLC's annual tax for the current calendar year), and to take all other actions necessary to effect the Conversion.

RESOLVED FURTHER, that each undersigned member waives any notice, preemptive right, right of first refusal, tag-along right, or other right under the LLC Agreement that would otherwise apply to the Conversion or the issuance of shares under the Plan.

This consent may be executed in counterparts and delivered electronically and is effective as of {{effective_date}}, provided that it has been signed by members holding the approval required above.

| Member | Units held | Signature | Date |
|---|---|---|---|
| {{member_names}} | | ______________________________ | |

> **Drafting note:** Replace the § 18-302(d) reference with the LLC agreement's consent provision if it differs, and for a non-Delaware LLC cite the home state's LLC act. Obtain unanimous member consent where practical; it eliminates appraisal-type or fiduciary claims and simplifies waivers.

---

# PART 3. CERTIFICATE OF CONVERSION

# STATE OF DELAWARE CERTIFICATE OF CONVERSION FROM A LIMITED LIABILITY COMPANY TO A CORPORATION PURSUANT TO SECTION 265 OF THE DELAWARE GENERAL CORPORATION LAW

1. The jurisdiction where the limited liability company first formed is {{llc_formation_state}}.
2. The jurisdiction immediately prior to filing this Certificate is {{llc_formation_state}}.
3. The date the limited liability company first formed is {{llc_formation_date}}.
4. The name of the limited liability company immediately prior to filing this Certificate is {{llc_name}}.
5. The name of the corporation as set forth in the Certificate of Incorporation is {{company_name}}.
6. A plan of conversion was adopted in accordance with Section 265(k) of the General Corporation Law of the State of Delaware, and all provisions of the plan of conversion were approved prior to the effectiveness of this Certificate in accordance with all law applicable to the limited liability company, including any approval required under such law for the authorization of the types of corporate action specified in the plan of conversion.
7. [[Alternative A: This Certificate of Conversion shall be effective upon filing.]] [[Alternative B: This Certificate of Conversion shall be effective at {{effective_time_of_day}} on {{effective_date}}, which is the same effective time as that of the Certificate of Incorporation filed herewith.]]

IN WITNESS WHEREOF, the undersigned, being duly authorized to sign on behalf of the converting limited liability company, has executed this Certificate on ____________.

{{llc_name}}

By: ______________________________
Name: {{authorized_person_name}}
Title: {{authorized_person_title}}

> **Drafting note:** The Division publishes its own form of certificate of conversion; using it reduces rejection risk, and this form tracks its required content (§ 265(c)). File it together with the certificate of incorporation (§ 265(b)). For a non-Delaware LLC, item 2 is the LLC's jurisdiction immediately before conversion, and the home state's outbound conversion filing must also be made.

---

# PART 4. CONVERSION TIMELINE CHECKLIST

| Week | Step | Owner |
|---|---|---|
| 1 | Review LLC agreement approvals, consents, and transfer rights; collect cap table and capital accounts | Counsel |
| 1–2 | Tax analysis (assets-over consequences, § 357(c), § 1202 gross-assets test, state taxes); obtain valuation for the waterfall | Tax counsel; valuation firm |
| 2 | Draft plan of conversion, certificate of conversion, certificate of incorporation, bylaws, restricted stock agreements, member consent | Counsel |
| 3 | Member approval; pay LLC annual tax; order Delaware good standing | Company |
| 3 | File certificate of conversion and certificate of incorporation together | Registered agent |
| 3–4 | Restricted stock agreements signed; 83(b) elections mailed within 30 days after the Effective Time | Holders; counsel |
| 4 | Post-conversion board consent ratifying actions; stockholder approval of the equity plan; new 409A valuation before grants | Board; stockholders |
| 4–6 | New EIN if required; update payroll, banks, foreign qualifications, insurance, contracts; final LLC tax returns | Company; CPA |

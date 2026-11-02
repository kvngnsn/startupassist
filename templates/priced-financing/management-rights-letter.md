---
id: management-rights-letter
title: Management Rights Letter (VCOC Management Rights)
category: priced-financing
stage: priced-round
signers: [Company (by an officer), the investing fund (countersignature)]
authorities:
  - "29 C.F.R. § 2510.3-101(d) (venture capital operating company; 'management rights' defined in § 2510.3-101(d)(3)(ii))"
  - "29 C.F.R. § 2510.3-101(f) and ERISA § 3(42), 29 U.S.C. § 1002(42) (25% 'significant participation' test for benefit plan investors)"
  - "29 C.F.R. § 2510.3-101(j) (examples (5)–(6): VCOC need only actually exercise management rights in one portfolio company per year)"
  - "31 C.F.R. § 800.211(b) (CFIUS: board observer and information rights as covered-investment triggers for foreign persons)"
  - "8 Del. C. § 122(18) (Company undertakings to stockholders)"
use_when: An investing fund that relies on the venture capital operating company (VCOC) exception to the ERISA plan-asset rules asks for contractual management rights directly from the Company, typically when it will not hold a board seat or wants rights independent of its board designee.
do_not_use_when: The investor is not a fund with benefit plan investors (individuals, corporate strategics, most family offices), or the investor's counsel confirms the fund qualifies for another exception (for example, benefit plan investors hold less than 25% of each class of its equity) and does not want a letter.
related: [investors-rights-agreement, voting-agreement, stock-purchase-agreement, board-consent-priced-financing, priced-round-closing-checklist]
sources:
  - name: "eCFR 29 C.F.R. § 2510.3-101 (plan assets regulation), version current to October 2026 — quoted"
    url: https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XXV/subchapter-B/part-2510/section-2510.3-101
  - name: "eCFR 31 C.F.R. § 800.211 (CFIUS covered investment)"
    url: https://www.ecfr.gov/current/title-31/subtitle-B/chapter-VIII/part-800/subpart-B/section-800.211
  - name: "NVCA Model Management Rights Letter (July 2020) — listed for awareness of market practice; not reviewed for drafting and no text copied"
    url: https://nvca.org/model-legal-documents/
last_verified: 2026-11-02
---

## About this template

**Why funds ask for this letter.** Under ERISA's plan-asset regulation, if "benefit plan investors" (ERISA plans, IRAs and Keogh plans, and entities holding their assets) own 25% or more of the value of any class of a fund's equity, the fund's underlying assets are treated as "plan assets" unless an exception applies (29 C.F.R. § 2510.3-101(a)(2), (f); ERISA § 3(42)). Plan-asset status would make the fund manager an ERISA fiduciary and expose the fund's investments to ERISA's prohibited-transaction rules — something no venture fund will accept. The main exception for venture funds is the **venture capital operating company** ("VCOC") exception. A fund is a VCOC if, on its initial valuation date and at least once during each annual valuation period (a pre-set window of no more than ninety (90) days), at least 50% of its assets (other than short-term investments pending long-term commitment or distribution), valued at cost, are "venture capital investments," and it actually exercises management rights in the ordinary course of business with respect to at least one portfolio company during the year (§ 2510.3-101(d)(1), (d)(5)).

**What counts as "management rights."** The regulation defines them as "contractual rights directly between the investor and an operating company to substantially participate in, or substantially influence the conduct of, the management of the operating company" (§ 2510.3-101(d)(3)(ii)). Three features matter for drafting:

1. *Contractual and direct.* The rights must run from the Company to the fund itself — not to an affiliated fund, and not merely through charter class-voting rights. That is why each fund signs its own letter even if it is a party to the Investors' Rights Agreement.
2. *Substantial.* Information rights alone are not enough. Practice treats a right to consult with and advise management on significant matters, a right to inspect, and either a board seat or a board observer right as the core package. A contractual right to designate a director (in the Voting Agreement) is generally treated as a management right too; the letter is belt-and-suspenders for funds with a seat and essential for funds without one.
3. *Actually exercised.* The fund must actually exercise management rights with at least one portfolio company in each annual valuation period (the regulation's examples confirm it need not do so with every portfolio company, § 2510.3-101(j)(5)). The letter does not satisfy that requirement by itself; the fund's own compliance program does.

**Company perspective.** The letter costs the Company little because its rights overlap the IRA. The Company's concerns are (a) confidentiality — Section 4 incorporates protection at least as strong as the IRA; (b) a board observer right for a fund that has no seat — Section 3 gives the Company the same exclusions it has in the IRA (privilege, conflicts, competitive harm, CFIUS); and (c) termination — the letter ends at the IPO or a sale, like the IRA's information rights.

**CFIUS.** For a foreign-person fund investing in a "TID U.S. business," board observer rights, access to material nonpublic technical information, or involvement in substantive decision-making each make the investment a "covered investment" (31 C.F.R. § 800.211(b)). If the fund (or a controlling general partner) is a foreign person, delete the observer right or condition it on the CFIUS covenant in the IRA. Most U.S.-managed funds are not foreign persons even if they have foreign limited partners, but confirm with the fund.

**Market practice.** Funds with ERISA money ask for this letter as a matter of course; companies routinely grant it. Negotiation is limited to the observer right (usually given only when the fund has no board designee) and the scope of any consultation right (keep it to "reasonable" frequency at mutually convenient times). The NVCA's model has not been updated since July 2020, reflecting how stable the form is.

**Mechanics.** Sign at the Initial Closing on Company letterhead; the fund countersigns. List it in the Purchase Agreement's definition of Transaction Agreements and in the closing checklist. The letter is a § 122(18) undertaking of the Company to a stockholder; the board consent's § 122(18) recital covers it.

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `{{company_name}}` | Exact legal name | Northwind Robotics, Inc. | |
| `{{company_address}}` | Principal office | 100 Example Street, Suite 200, Austin, Texas 78701 | Letterhead |
| `{{effective_date}}` | Date of the letter | March 3, 2027 | Initial Closing date |
| `{{investor_name}}` | Fund receiving the rights | Example Ventures Fund I, L.P. | The specific fund entity, not the management company |
| `{{investor_address}}` | Fund notice address | | |
| `{{series_name}}` | Series purchased | Series A | |
| `{{investor_signatory_name}}`, `{{investor_signatory_title}}` | Fund signatory | Sam Example, Managing Member of the General Partner | |
| `{{signatory_name}}`, `{{signatory_title}}` | Company signatory | Alex Rivera, Chief Executive Officer | |

## Form

---

**{{company_name}}**
{{company_address}}

{{effective_date}}

{{investor_name}}
{{investor_address}}

**Re: Management Rights**

Ladies and Gentlemen:

This letter is delivered in connection with the purchase by {{investor_name}} (the "**Investor**") of shares of {{series_name}} Preferred Stock of {{company_name}} (the "**Company**") under the {{series_name}} Preferred Stock Purchase Agreement dated {{effective_date}} (the "**Purchase Agreement**"). Capitalized terms used but not defined in this letter have the meanings given in the Purchase Agreement or, if not defined there, in the Investors' Rights Agreement of the same date among the Company and the investors party to it (the "**Investors' Rights Agreement**").

The Investor has told the Company that it intends to qualify, or that one or more of its affiliated funds intends to qualify, as a "venture capital operating company" under 29 C.F.R. § 2510.3-101(d), and that to do so it needs management rights directly from the Company. Effective as of the Initial Closing, and for so long as the Investor (together with its affiliated funds) continues to hold shares of the Company's capital stock (or securities convertible into it), the Company therefore agrees with the Investor as follows.

**1. Consultation.** The Investor may consult with and advise the Company's management on significant business matters, including management's proposed annual operating plans. Management shall meet with the Investor's representatives on the Investor's reasonable request, at mutually agreeable times and no more often than quarterly (plus any additional meetings management agrees to), to discuss those matters. The Company is not required to follow the Investor's advice, and the final decision on any matter remains with the Company's Board and management.

**2. Information and Inspection.** The Investor may (a) receive the financial statements, budgets and other information the Company provides to Major Investors under the Investors' Rights Agreement, whether or not the Investor is then a Major Investor; and (b) on reasonable advance notice and during normal business hours, inspect the Company's facilities, books and records and discuss the Company's business with its officers, in a way that does not unreasonably disrupt operations. The Company may withhold information on the same grounds on which it may withhold information from a Major Investor under the Investors' Rights Agreement.

**3. Board Observer.** [[Alternative A: If the Investor is not represented on the Company's Board of Directors (the "**Board**") by a director it designated, the Company shall invite one representative of the Investor, reasonably acceptable to the Board, to attend Board meetings as a non-voting observer and shall give that representative the notices, minutes, consents and other materials it gives directors, at the same time and in the same way.]] [[Alternative B: If the Investor is not represented on the Board by a director it designated, and the Investor is not then entitled to an observer under the Investors' Rights Agreement, the Company shall give due consideration to the Investor's advice on significant matters raised by the Investor's representative in the consultations described in Section 1.]] The observer has no vote, is not counted toward a quorum, owes no fiduciary duty in that capacity, and is not paid, but the Company shall reimburse reasonable travel costs on the same basis as for non-employee directors. The Company may exclude the observer from any meeting or portion of a meeting, and may withhold any material, if the Board reasonably determines that attendance or disclosure would (a) put at risk the attorney-client privilege or reveal trade secrets or highly sensitive proprietary information; (b) present a conflict of interest, including a matter involving the Investor, its affiliates or its portfolio companies; (c) cause competitive harm to the Company; (d) give a foreign person a right described in 31 C.F.R. § 800.211(b), unless the Board has approved it under the Investors' Rights Agreement; or (e) violate law.

**4. Confidentiality.** The Investor shall keep confidential, and use only to monitor and manage its investment in the Company, all information it receives under this letter, on terms at least as protective of the Company as Section 3.7 of the Investors' Rights Agreement (which applies to this letter as though set out here), and shall cause any observer to agree in writing to the same obligations. The Investor acknowledges that information it receives may be material nonpublic information under federal securities laws.

**5. Nature of Rights; No Transfer.** The rights in this letter are in addition to, and do not limit, any rights the Investor has under the Investors' Rights Agreement, the Voting Agreement, the Restated Certificate or applicable law. They are personal to the Investor and may be assigned only to an affiliated fund that is a stockholder of the Company and agrees in writing to Section 4. This letter is an undertaking of the Company to a stockholder under Section 122(18) of the Delaware General Corporation Law, made for the consideration provided under the Purchase Agreement, and it does not obligate any director to act in a way inconsistent with that director's fiduciary duties.

**6. Termination.** The rights in Sections 1 through 3 end at the earliest of (a) the closing of the Company's IPO (as defined in the Investors' Rights Agreement); (b) the date the Company first becomes subject to the periodic reporting requirements of Section 13(a) or 15(d) of the Securities Exchange Act of 1934; (c) the closing of a Deemed Liquidation Event; and (d) the date the Investor and its affiliated funds no longer hold any of the Company's capital stock. Section 4 survives termination.

**7. General.** This letter is governed by Delaware law, without regard to choice-of-law rules that would apply another jurisdiction's law, and any dispute under it shall be resolved in the forum specified in the Investors' Rights Agreement. It may be amended or waived only in a writing signed by the Company and the Investor. It may be signed in counterparts and electronically (including under 15 U.S.C. § 7001 et seq., 6 Del. C. ch. 12A and 8 Del. C. § 116).

> **Drafting note:** Do not water the consultation right down to "the Company will consider in good faith any recommendations." The regulation requires rights to "substantially participate in, or substantially influence the conduct of, the management" of the company; a right to meet with management on request and an observer seat (or a designated director) is the conventional package that funds' ERISA counsel accept. Equally, do not let the letter become a backdoor approval right — Section 1 says expressly that decisions stay with the Board and management.

Very truly yours,

**{{company_name}}**

By: ______________________________
Name: {{signatory_name}}
Title: {{signatory_title}}

AGREED AND ACKNOWLEDGED:

**{{investor_name}}**

By: ______________________________
Name: {{investor_signatory_name}}
Title: {{investor_signatory_title}}

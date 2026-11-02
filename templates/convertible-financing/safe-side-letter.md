---
id: safe-side-letter
title: SAFE Investor Side Letter (Pro Rata, MFN, Information Rights, Major Investor Designation)
category: convertible-financing
stage: convertible
signers: [Company (by an officer), Investor]
authorities:
  - "8 Del. C. § 141(f) (board approval of side letters as part of the SAFE financing)"
  - "8 Del. C. § 122 (corporate power to make contracts); 8 Del. C. § 157 (rights to acquire stock)"
  - "17 C.F.R. §§ 230.501(a), 230.502(b), 230.506 (Regulation D; accredited investors; non-accredited disclosure)"
  - "31 C.F.R. §§ 800.211, 800.401 (CFIUS covered investments; mandatory declarations)"
  - "6 Del. C. § 2708 (enforceability of Delaware choice of law in contracts of $100,000 or more)"
use_when: A SAFE investor has negotiated rights beyond the official YC SAFE (participation in the next priced round, most-favored-nation protection, information rights, or Major Investor status) and the company wants those rights in a separate agreement that leaves the YC SAFE unmodified.
do_not_use_when: The parties want only YC's standard pro rata right (use YC's Pro Rata Side Letter as published, unmodified), the instrument is a convertible note (put these rights in the note purchase agreement), or the rights are intended to change conversion economics (that requires a different SAFE, not a side letter).
related: [safe-guide, board-consent-convertible-financing, investor-questionnaire, convertible-note-purchase-agreement]
sources:
  - name: "Y Combinator — Pro Rata Side Letter v1.0 and MFN SAFE v1.3 (structure and scope reviewed; not copied)"
    url: https://www.ycombinator.com/documents
  - name: "Y Combinator — Post-Money SAFE User Guide (pro rata allocation guidance; paraphrased)"
    url: https://www.ycombinator.com/documents
  - name: "Series Seed documents (CC0 1.0) — information-right and participation-right structure (reference)"
    url: https://www.seriesseed.com
  - name: "31 C.F.R. Part 800 (CFIUS) — eCFR"
    url: https://www.ecfr.gov/current/title-31/subtitle-B/chapter-VIII/part-800
last_verified: 2026-11-02
---

# SAFE Investor Side Letter

## About this template

### 1. What this document does and where it sits

This is an original side letter between the company and one SAFE holder. It grants contract rights that sit **alongside** the Y Combinator post-money SAFE and expressly does **not** amend it. The YC SAFE contains the parties' agreement that neither has modified the form except to fill in blanks; keeping extra rights in a side letter preserves that statement, keeps the SAFE identical to every other SAFE in the round, and keeps majority-in-interest amendments workable.

Sign it at the same time as the SAFE, after the board has approved the SAFE financing and authorized side letters within stated parameters (see [board-consent-convertible-financing](board-consent-convertible-financing.md)). Record it in the investor's SAFE Term Summary ([safe-guide](safe-guide.md)).

The letter offers four modules. Include only the ones the company actually agreed to:

| Module | What it gives | Market position | Default in this form |
|---|---|---|---|
| Article 2: Participation Right | Right to buy part of the next priced round | Common for checks above a threshold; YC offers its own standard pro rata letter | Ownership-based allocation in the first Equity Financing only, with a proportional lead cutback |
| Article 3: Most-Favored-Nation | If the company later issues convertible securities (or side-letter rights) on better terms, the investor may take them | Common for early, large, or lead SAFE checks; less common for small checks | Exchange for a new, unmodified YC SAFE on the better terms; one-time or continuing (alternatives) |
| Article 4: Information Rights | Annual (and optionally quarterly) financials; budget | Common for institutional investors; often limited to "Major" SAFE holders | Annual within 120 days; quarterly optional; confidentiality and competitor carve-outs |
| Article 5: Major Investor Designation | Treated as a "Major Investor" in the priced round's investors' rights agreement | Investor-favorable; leads may resist | Commercially reasonable efforts (company-favorable) or firm covenant (alternative) |

### 2. Key business decisions

- **Participation formula.** Alternative A (ownership-based) gives the investor the percentage of the new round equal to its as-converted ownership of Company Capitalization; this mirrors the economic logic of YC's letter without copying it. Alternative B caps participation at a fixed dollar amount (simpler for the lead to budget). The form defaults to A with an optional dollar cap.
- **Duration.** Default: the first Equity Financing only (the round in which the SAFE converts). Later rounds are governed by the investors' rights agreement signed in that round.
- **Lead cutback.** A lead investor will often require a fixed allocation. The default allows the company to reduce participation only if all holders of participation rights in the same round are cut back proportionately. Delete the cutback for an investor-favorable letter.
- **MFN scope.** Default covers economic terms of later convertible securities issued to raise capital, and side-letter rights granted to later SAFE holders investing the same or a smaller amount. Exclusions follow market practice (equity plan, lenders, strategic deals, the Equity Financing itself). Choose between a single election (YC-style) and a continuing MFN until the Equity Financing.
- **How MFN economics are delivered.** Because this letter must not modify the SAFE, the default delivers better economic terms by **exchanging** the investor's SAFE for a new, unmodified YC SAFE completed with the same Purchase Amount and the better terms (a "Replacement SAFE"). The Replacement SAFE is a new instrument dated when signed; see the Drafting note after Section 3.3 on dating and on other holders' MFN rights. Record it as an exchange and confirm the securities exemption (Securities Act § 3(a)(9) covers an exchange with an existing holder where no commission is paid for soliciting it).
- **Choice of law threshold.** 6 Del. C. § 2708 makes a written Delaware choice of law conclusively enforceable for contracts involving $100,000 or more where the parties submit to Delaware jurisdiction and service; smaller SAFEs fall back on ordinary conflicts rules, under which a Delaware corporation's choice of Delaware law is still generally respected.
- **Information rights and foreign investors.** For a foreign person in a TID U.S. business, access to "material nonpublic technical information" can make an otherwise passive investment a CFIUS "covered investment" (31 C.F.R. § 800.211). Section 4.4 excludes technical information for foreign persons.

### 3. Statutory and regulatory points

- **Securities law.** Exercise of the participation right is a purchase in the priced round; the investor must be accredited (or the company must be able to satisfy Rule 502(b) disclosure) and the company may exclude an investor whose participation would require registration or disclosure the company is not otherwise providing (§ 2.6).
- **Corporate law.** A side letter is an ordinary contract (8 Del. C. § 122). Rights to acquire stock should be approved by the board (8 Del. C. § 157); the board consent template authorizes side letters within parameters. If the investor is a director or officer, follow 8 Del. C. § 144 (see the board consent template).
- **California jury waivers.** Pre-dispute jury waivers are unenforceable under California law (*Grafton Partners L.P. v. Superior Court*, 36 Cal. 4th 944 (2005)); the forum clause selects Delaware, and the jury waiver is drafted to apply to the extent permitted.

### 4. Common mistakes this form avoids

1. Side letters that change the SAFE's cap, discount, or conversion mechanics (breaks the "unmodified" statement and invites MFN claims by other holders). This form delivers MFN economics only through a new, unmodified SAFE.
2. Participation rights with no notice period, no exercise deadline, and no consequence for silence (delays the Series A). Article 2 sets all three.
3. Perpetual information rights that survive conversion and duplicate the investors' rights agreement. Section 6.1 ends them at conversion.
4. MFN rights the company forgets to honor. Section 3.2 requires a written MFN Notice; the SAFE Term Summary logs it.
5. Overlapping rights (the same investor holding YC's Pro Rata Side Letter and this letter). Section 2.8 prevents double counting.

### 5. Deadlines the letter creates

| Event | Deadline (default) |
|---|---|
| Company sends Financing Notice | At least {{financing_notice_days}} days before the expected initial closing of the Equity Financing |
| Investor exercises participation right | Within {{exercise_period_days}} days after receiving the Financing Notice |
| Company sends MFN Notice | Within {{mfn_notice_days}} days after issuing a Subsequent Convertible Security or granting More Favorable Side Letter Rights |
| Investor makes MFN election | Within {{mfn_election_days}} days after receiving the MFN Notice |
| Annual financial statements | Within {{annual_info_days}} days after fiscal year end |
| Quarterly financial statements (optional) | Within {{quarterly_info_days}} days after quarter end |

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `{{company_name}}` | Exact legal name | Northwind Robotics, Inc. | Shared |
| `{{company_address}}`, `{{company_notice_email}}` | Company notice address and email | 100 Example Street, Suite 200, Austin, Texas 78701; legal@northwind.example | Shared |
| `{{investor_name}}`, `{{investor_entity_type}}` | Investor and entity type | Example Ventures Fund I, L.P., a Delaware limited partnership | Shared |
| `{{investor_address}}`, `{{investor_email}}` | Investor notice details | | Shared |
| `{{effective_date}}` | Date of this letter (same as the SAFE) | March 3, 2027 | Shared |
| `{{safe_date}}` | Date of the SAFE | March 3, 2027 | |
| `{{purchase_amount}}` | SAFE Purchase Amount | $500,000 | Shared |
| `{{safe_form_description}}` | YC form used | Post-Money SAFE (Valuation Cap only), version 1.2 | |
| `{{participation_dollar_cap}}` | Maximum dollars purchasable under Article 2 | $500,000 | Alternative B or optional cap |
| `{{financing_notice_days}}` | Minimum notice before the Equity Financing closes | 10 | Days |
| `{{exercise_period_days}}` | Exercise period after Financing Notice | 10 | Days |
| `{{mfn_notice_days}}` | Days to send MFN Notice | 10 | |
| `{{mfn_election_days}}` | Days for investor to elect | 10 | |
| `{{mfn_side_letter_amount_test}}` | Size test for side-letter MFN | equal to or less than the Purchase Amount | |
| `{{annual_info_days}}` | Annual statement delivery period | 120 | |
| `{{quarterly_info_days}}` | Quarterly statement delivery period | 45 | Optional |
| `{{major_investor_threshold}}` | Conversion-share or dollar threshold for Major Investor designation | $500,000 of Purchase Amount | Shared |
| `{{governing_law_state}}` | Governing law | Delaware | Shared |
| `{{forum}}` | Exclusive forum | Court of Chancery of the State of Delaware | Shared |
| `{{signatory_name}}`, `{{signatory_title}}` | Company officer signing | Alex Rivera, Chief Executive Officer | Shared |
| `{{investor_signatory_name}}`, `{{investor_signatory_title}}` | Investor signatory | | For entity investors |


## Form

---

# {{company_name}}

## SIDE LETTER AGREEMENT

This Side Letter Agreement (this "**Agreement**") is entered into as of {{effective_date}} (the "**Effective Date**") by and between {{company_name}}, a Delaware corporation (the "**Company**"), and {{investor_name}}, {{investor_entity_type}} (the "**Investor**").

### RECITALS

A. On {{safe_date}}, the Company issued to the Investor a Simple Agreement for Future Equity in the form published by Y Combinator as the {{safe_form_description}}, in exchange for a Purchase Amount of {{purchase_amount}} (as it may be exchanged under Article 3, the "**SAFE**").

B. As an inducement to the Investor's investment, the Company has agreed to grant the Investor the rights set forth in this Agreement, which are in addition to, and not an amendment of, the SAFE.

NOW, THEREFORE, in consideration of the mutual promises in this Agreement and the Investor's purchase of the SAFE, the Company and the Investor agree as follows.

## ARTICLE 1. DEFINITIONS AND RELATIONSHIP TO THE SAFE

**1.1 Defined Terms.** Capitalized terms used but not defined in this Agreement have the meanings given to them in the SAFE, including "Capital Stock," "Change of Control," "Company Capitalization," "Converting Securities," "Dissolution Event," "Equity Financing," "Liquidity Event," "Purchase Amount," "Safe," "Safe Preferred Stock," and "Standard Preferred Stock." In addition:

(a) "**Affiliate**" means, with respect to a person, any other person that directly or indirectly controls, is controlled by, or is under common control with that person, including any investment fund now or later existing that is managed or advised by the same general partner, managing member, or management company as that person.

(b) "**Business Day**" means any day other than a Saturday, Sunday, or a day on which banks in New York, New York are authorized or required to close.

(c) "**Competitor**" means any person that the Company's board of directors determines in good faith is engaged, directly or through a controlled affiliate, in a business that competes with the Company's business; provided that no investment fund or other financial investor shall be a Competitor solely because it holds a minority, passive investment in a competing business, unless that investor (or its Affiliate) has a representative on the board of directors of, or an information right in, that competing business and does not maintain customary information barriers.

(d) "**Conversion Shares**" means the shares of Capital Stock issued, or issuable, to the Investor on conversion of the SAFE in the Equity Financing.

(e) "**Foreign Person**" has the meaning given in 31 C.F.R. § 800.224.

(f) "**More Favorable Side Letter Rights**" has the meaning given in Section 3.1(b).

(g) "**New Securities**" means the shares of Standard Preferred Stock (and any other equity securities sold for cash to new-money investors on the same terms) offered in the Equity Financing, excluding shares of Safe Preferred Stock or other securities issued on conversion of Converting Securities.

(h) "**Subsequent Convertible Securities**" means Safes, convertible promissory notes, and other securities convertible into or exercisable for Capital Stock that the Company issues for cash after the Effective Date and before the termination of the MFN Right under Section 6.1, with the principal purpose of raising capital, but excluding Excluded Securities.

(i) "**Excluded Securities**" means: (i) options, restricted stock, restricted stock units, and other awards issued under an equity incentive plan or compensatory arrangement approved by the Company's board of directors; (ii) warrants or convertible securities issued to banks, equipment lessors, or other lenders in a bona fide debt financing or equipment lease; (iii) convertible securities issued to suppliers, service providers, or strategic partners in connection with commercial, licensing, collaboration, research, or similar transactions approved by the Company's board of directors and not principally for capital raising; (iv) securities issued in an acquisition of another business approved by the Company's board of directors; (v) securities issued in the Equity Financing; and (vi) securities issued on conversion or exercise of any of the foregoing or of Converting Securities outstanding on the Effective Date.

**1.2 Relationship to the SAFE.** This Agreement does not amend, modify, supplement, or waive any provision of the SAFE, and the SAFE remains in the form published by Y Combinator, completed only as to its blanks and bracketed terms. The conversion of the SAFE, the amounts payable under the SAFE in a Liquidity Event or Dissolution Event, and the priority of those amounts are governed exclusively by the SAFE. This Agreement governs only the rights expressly granted in it. If any provision of this Agreement could be read to change the SAFE, the parties intend that provision to operate solely as a separate contractual covenant of the Company, and it shall be so construed.

**1.3 Interpretation.** In this Agreement: (a) "including" means "including without limitation"; (b) "or" is not exclusive; (c) references to Articles and Sections are to this Agreement; (d) headings are for convenience only; (e) "days" means calendar days unless Business Days are specified, and a period ending on a day that is not a Business Day ends on the next Business Day; and (f) no provision shall be construed against a party because that party drafted it.

## ARTICLE 2. PARTICIPATION RIGHT IN THE EQUITY FINANCING

**2.1 Grant.** Subject to this Article 2, the Investor shall have the right (the "**Participation Right**") to purchase, at the initial closing of the first Equity Financing after the Effective Date and on the same terms and at the same price per share as the new-money investors, up to the Investor's Participation Amount of the New Securities.

**2.2 Participation Amount.** The "**Participation Amount**" is:

[[Alternative A: the number of New Securities (rounded down to the nearest whole share) equal to the total number of New Securities offered in the Equity Financing multiplied by a fraction, the numerator of which is the number of Conversion Shares and the denominator of which is the Company Capitalization used to calculate the conversion of the SAFE (or, if the SAFE converts into Standard Preferred Stock, the fully diluted capitalization of the Company immediately before the initial closing, calculated in the same manner as Company Capitalization).]]

[[Alternative B: the number of New Securities (rounded down to the nearest whole share) that can be purchased at the price per share paid by new-money investors for an aggregate purchase price of {{participation_dollar_cap}}.]]

[[Optional: Notwithstanding the foregoing, the Participation Amount shall not exceed the number of New Securities that can be purchased at the price per share paid by new-money investors for an aggregate purchase price of {{participation_dollar_cap}}.]]

> **Drafting note:** Alternative A tracks the investor's as-converted ownership and grows with the round; Alternative B gives the lead and the company a fixed number to budget. Before granting either, run the participation budget in references/convertible-instruments.md § 9.2 against all side letters in the round.

**2.3 Financing Notice.** The Company shall deliver to the Investor a written notice (the "**Financing Notice**") at least {{financing_notice_days}} days before the anticipated initial closing of the Equity Financing, stating: (a) the anticipated closing date; (b) the series, price per share, and aggregate amount of New Securities to be offered; (c) the identity of the lead investor, if any; (d) the Company's good-faith calculation of the Investor's Participation Amount, with reasonable supporting detail; and (e) the principal terms of the Equity Financing, together with the term sheet if one has been signed. The Company may deliver the Financing Notice before definitive documents are final, and it shall promptly notify the Investor of any material change to the information in the Financing Notice. If a material change reduces the price or improves the terms for investors, the exercise period in Section 2.4 shall be extended, if necessary, so that it ends no earlier than five (5) Business Days after the Investor receives notice of the change.

**2.4 Exercise.** The Investor may exercise the Participation Right, in whole or in part, by written notice to the Company within {{exercise_period_days}} days after receipt of the Financing Notice (the "**Exercise Period**"), stating the number of New Securities (or the dollar amount) the Investor elects to purchase. An exercise is irrevocable unless the terms of the Equity Financing change materially and adversely to the Investor after the exercise, in which case the Investor may withdraw within five (5) Business Days after notice of the change.

**2.5 Failure to Exercise.** If the Investor does not exercise the Participation Right within the Exercise Period, or exercises it as to fewer than all of the New Securities included in its Participation Amount, the Participation Right lapses as to the unexercised portion, and the Company may sell the New Securities to other investors in the Equity Financing.

**2.6 Conditions to Purchase.** The Investor's purchase of New Securities is conditioned on: (a) the Investor's execution and delivery of the definitive documents for the Equity Financing on the same terms as the new-money investors (with no greater obligations); (b) the Investor's being an "accredited investor" under Rule 501(a) of Regulation D at the time of purchase and delivering the representations and information reasonably requested by the Company to establish an exemption from registration; (c) payment of the purchase price at the initial closing; and (d) the absence of any requirement, as a result of the Investor's participation, for the Company to register or qualify the New Securities, to deliver disclosure under Rule 502(b) of Regulation D that it is not otherwise delivering, or to submit a declaration or notice to the Committee on Foreign Investment in the United States, unless the Company agrees in writing to do so.

**2.7 Lead Investor Cutback.** [[Alternative A: If the lead investor in the Equity Financing requires, as a condition to its investment, that the aggregate New Securities available to holders of participation rights be reduced, the Company may reduce the Investor's Participation Amount, provided that the reduction is applied to the Investor and to every other holder of a participation right granted in connection with the Company's Safe financings in proportion to their respective participation amounts, and the Company delivers to the Investor written evidence of the lead investor's requirement.]] [[Alternative B: The Company shall not reduce the Investor's Participation Amount for any reason without the Investor's prior written consent.]]

**2.8 No Duplication.** The Participation Right is in lieu of, and not in addition to, any pro rata or participation right in the Equity Financing granted to the Investor under any other agreement relating to the SAFE (including any pro rata side letter published by Y Combinator), and the Investor shall not purchase New Securities under more than one such right in respect of the same SAFE.

**2.9 Assignment of Participation Right.** The Investor may assign the Participation Right, in whole or in part, to one or more of its Affiliates that are accredited investors and are not Competitors, by written notice to the Company before the end of the Exercise Period.

## ARTICLE 3. MOST-FAVORED-NATION RIGHT

**3.1 Scope.** If, before the termination of this Article 3 under Section 6.1, the Company:

(a) issues any Subsequent Convertible Securities whose economic terms are more favorable to the holder than those of the SAFE (including a lower valuation cap, a valuation cap measured on a basis more favorable to the holder, a greater discount, interest, or a liquidation entitlement greater than the purchase amount); or

(b) grants to any holder of Subsequent Convertible Securities [[Optional: or of any Safe issued after the Effective Date]] whose investment is {{mfn_side_letter_amount_test}} any participation, information, inspection, observer, or Major Investor right, by side letter or otherwise, that is more favorable than, or not included among, the rights granted to the Investor in this Agreement ("**More Favorable Side Letter Rights**"),

then the Investor shall have the rights in this Article 3 (the "**MFN Right**").

**3.2 MFN Notice.** Within {{mfn_notice_days}} days after issuing Subsequent Convertible Securities or granting More Favorable Side Letter Rights described in Section 3.1, the Company shall deliver to the Investor a written notice (an "**MFN Notice**") describing the terms, together with copies of the instruments and any side letters, and shall provide any additional information about them that the Investor reasonably requests.

**3.3 Election.** Within {{mfn_election_days}} days after receiving an MFN Notice, the Investor may elect by written notice to the Company to receive:

(a) **as to economic terms under Section 3.1(a):** the exchange of the SAFE for a new Simple Agreement for Future Equity on the form published by Y Combinator that the Subsequent Convertible Securities use (or, if the Subsequent Convertible Securities are not Safes, the Y Combinator form that most closely reproduces their economic terms), completed only as to its blanks and bracketed terms with the Investor's Purchase Amount and the more favorable terms (a "**Replacement SAFE**"). On the Company's and the Investor's execution of the Replacement SAFE, the SAFE shall be cancelled and shall terminate, and the Replacement SAFE shall be the "SAFE" for all purposes of this Agreement. No additional consideration shall be payable by either party for the exchange; and

(b) **as to More Favorable Side Letter Rights under Section 3.1(b):** the grant of those rights to the Investor, effective on the date of the election, by an amendment to this Agreement that the Company shall promptly execute.

> **Drafting note:** A Replacement SAFE is a new instrument, dated when signed. Under the YC MFN form and FAQ, the date of a SAFE matters for MFN purposes; if the Investor's SAFE is itself referenced by other holders' MFN rights, consider whether the exchange triggers notices to them. Record the exchange in the SAFE Term Summary. The exchange of one Company security for another with an existing holder, with no commission paid, is ordinarily exempt under Securities Act § 3(a)(9). If the Subsequent Convertible Securities are notes, do not convert the Investor into a noteholder by side letter; instead offer the closest YC SAFE form, or have counsel paper a separate exchange.

**3.4 Number of Elections.** [[Alternative A: The MFN Right may be exercised only once. After the Investor makes an election under Section 3.3, or the election period for an MFN Notice expires without an election, the MFN Right terminates, unless the Replacement SAFE or the More Favorable Side Letter Rights themselves include a most-favored-nation right.]] [[Alternative B: The MFN Right may be exercised each time the Company delivers an MFN Notice, until the MFN Right terminates under Section 6.1. An election not made within the election period for a particular MFN Notice is waived only as to the instruments described in that notice.]]

**3.5 No Cherry-Picking.** An election under Section 3.3(a) applies to all economic terms of the Subsequent Convertible Securities taken together, including any terms less favorable to the holder; the Investor may not select individual terms. An election under Section 3.3(b) may be made right by right.

## ARTICLE 4. INFORMATION RIGHTS

**4.1 Annual Financial Statements.** The Company shall deliver to the Investor, within {{annual_info_days}} days after the end of each fiscal year, a balance sheet as of the end of that year and statements of income and cash flows for that year, prepared in accordance with U.S. generally accepted accounting principles (except that they need not be audited and may omit footnotes and year-end adjustments) [[Optional: , audited by an independent accounting firm if the Company has obtained audited statements for that year]].

**4.2 Quarterly Financial Statements.** [[Optional: The Company shall deliver to the Investor, within {{quarterly_info_days}} days after the end of each of the first three fiscal quarters of each fiscal year, an unaudited balance sheet as of the end of that quarter and unaudited statements of income and cash flows for that quarter, prepared on a basis consistent with the annual statements.]]

**4.3 Budget.** [[Optional: The Company shall deliver to the Investor, within thirty (30) days after its approval by the Company's board of directors and in any event before the end of the first quarter of each fiscal year, the Company's operating budget for that fiscal year.]]

**4.4 Limitations.** The Company is not required to deliver any information that: (a) the Company's board of directors determines in good faith is a trade secret or confidential technical information, or whose disclosure would adversely affect the attorney-client privilege; (b) is to be delivered to an Investor that the Company's board of directors determines in good faith is, or is controlled by or controls, a Competitor; or (c) if the Investor is a Foreign Person, constitutes material nonpublic technical information within the meaning of 31 C.F.R. § 800.232, it being the parties' intent that this Agreement not afford a Foreign Person any right described in 31 C.F.R. § 800.211(b).

**4.5 Confidentiality.** The Investor shall keep confidential, and shall not use for any purpose other than monitoring its investment in the Company, any confidential information it receives under this Agreement, except information that (a) is or becomes public other than through the Investor's breach, (b) was known to the Investor without confidentiality obligations before the Company disclosed it, or (c) is independently developed or lawfully received from a third party without confidentiality obligations. The Investor may disclose confidential information (i) to its Affiliates, partners, members, managers, employees, attorneys, accountants, and other advisers who need to know it for monitoring the investment and who are bound by confidentiality obligations, (ii) to existing or prospective limited partners in the ordinary course, limited to customary summary performance information, (iii) to a prospective permitted transferee of the SAFE that agrees in writing to be bound by this Section 4.5, or (iv) as required by law, regulation, or legal process, after giving the Company prompt notice (if legally permitted) and reasonable cooperation in seeking a protective order. The Investor acknowledges that it is aware that the securities laws restrict persons who possess material nonpublic information about an issuer from trading in that issuer's securities.

## ARTICLE 5. MAJOR INVESTOR DESIGNATION

**5.1 Designation.** [[Alternative A: In connection with the Equity Financing, the Company shall use commercially reasonable efforts to cause the investors' rights agreement (or comparable agreement) entered into in the Equity Financing to treat the Investor as a "Major Investor" (or the equivalent term used to define investors entitled to information, inspection, and participation rights) for so long as the Investor and its Affiliates hold Conversion Shares (together with any New Securities purchased under Article 2) that would satisfy the minimum holding requirement applicable to the new-money investors, or, if lower, Conversion Shares issued on conversion of a Purchase Amount of at least {{major_investor_threshold}}.]] [[Alternative B: The Company shall not consummate the initial closing of the Equity Financing unless the investors' rights agreement (or comparable agreement) entered into in the Equity Financing treats the Investor as a "Major Investor" (or the equivalent term) for so long as the Investor and its Affiliates hold at least the Conversion Shares issued to the Investor on conversion of a Purchase Amount of at least {{major_investor_threshold}}, and the Investor shall be entitled to become a party to that agreement on the same terms as the other investors.]]

**5.2 Joinder.** The Investor shall execute and deliver the investors' rights agreement and the other agreements entered into by the new-money investors in the Equity Financing, with the variations permitted by the SAFE, as a condition to receiving the rights described in Section 5.1.

## ARTICLE 6. TERM AND TERMINATION

**6.1 Termination.** This Agreement and each right in it shall terminate automatically, without further action of either party, on the earliest of:

(a) the initial closing of the first Equity Financing after the Effective Date, except that (i) the Company's obligation to sell, and the Investor's right to purchase, New Securities that the Investor has validly elected to purchase under Article 2 shall be performed at that closing, (ii) Article 5 shall be performed at that closing, and (iii) Section 4.5 shall survive as to information received before termination for two (2) years;

(b) immediately before the consummation of a Liquidity Event;

(c) immediately before the consummation of a Dissolution Event;

(d) the termination of the SAFE (or any Replacement SAFE) for any reason other than conversion in the Equity Financing;

(e) a transfer of the SAFE by the Investor to any person other than an Affiliate of the Investor, as to the transferred SAFE; and

(f) the written agreement of the Company and the Investor.

**6.2 Effect of Termination.** Termination shall not relieve either party of liability for a breach occurring before termination.

## ARTICLE 7. REPRESENTATIONS

**7.1 Mutual Representations.** Each party represents to the other that: (a) it has full power and authority to enter into and perform this Agreement; (b) this Agreement has been duly authorized, executed, and delivered by it and is a valid and binding obligation enforceable against it in accordance with its terms, subject to bankruptcy, insolvency, and similar laws affecting creditors' rights generally and to general principles of equity; and (c) its execution and performance of this Agreement do not violate its organizational documents or any agreement binding on it.

**7.2 Company Approval.** The Company represents that the Company's board of directors has approved this Agreement.

## ARTICLE 8. GENERAL PROVISIONS

**8.1 Governing Law.** This Agreement and all claims arising out of or relating to it are governed by the laws of the State of {{governing_law_state}}, without regard to conflict-of-laws principles that would require the application of the laws of another jurisdiction.

**8.2 Forum.** Each party irrevocably submits to the exclusive jurisdiction of the {{forum}} (or, if that court lacks subject-matter jurisdiction, the Superior Court of the State of Delaware or the United States District Court for the District of Delaware) for any action arising out of or relating to this Agreement, and waives any objection to venue in those courts.

**8.3 Waiver of Jury Trial.** TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, EACH PARTY WAIVES ITS RIGHT TO A JURY TRIAL IN ANY ACTION ARISING OUT OF OR RELATING TO THIS AGREEMENT.

**8.4 Notices.** All notices under this Agreement shall be in writing and are deemed given (a) when delivered personally, (b) one (1) Business Day after deposit with a nationally recognized overnight courier, (c) when sent by email, if sent before 5:00 p.m. in the recipient's time zone on a Business Day (and otherwise on the next Business Day), provided that no automated notice of delivery failure is received, or (d) three (3) Business Days after mailing by certified or registered mail, return receipt requested, postage prepaid, in each case to the addresses below or another address a party designates by notice:

If to the Company: {{company_name}}, {{company_address}}; email: {{company_notice_email}}; Attention: {{signatory_title}}.

If to the Investor: {{investor_address}}; email: {{investor_email}}.

**8.5 Entire Agreement.** This Agreement and the SAFE constitute the entire agreement between the parties about their subject matter and supersede all prior and contemporaneous understandings, term sheets, and communications about it.

**8.6 Amendment and Waiver.** This Agreement may be amended, and any provision waived, only by a written instrument signed by the Company and the Investor. [[Optional: Notwithstanding the preceding sentence, Articles 2 and 4 may be amended or waived by the Company and the holders of a majority of the aggregate Purchase Amount of all Safes whose holders are party to side letters with the Company in substantially this form, provided that the amendment or waiver applies to all such holders in the same manner and the Company promptly notifies every holder that did not consent.]] No failure or delay in exercising any right operates as a waiver of it.

**8.7 Severability.** If any provision of this Agreement is held invalid or unenforceable, that provision shall be enforced to the maximum extent permitted and the remaining provisions shall remain in full force.

**8.8 Successors and Assigns.** This Agreement binds and benefits the parties and their respective successors and permitted assigns. The Investor may assign this Agreement only together with the SAFE and only to a person to whom the SAFE is transferred in compliance with the SAFE's transfer provisions; an assignment to anyone other than an Affiliate of the Investor terminates this Agreement under Section 6.1(e). The Company may not assign this Agreement except to a successor in a reincorporation or similar transaction that is not a Liquidity Event.

**8.9 No Third-Party Beneficiaries.** Nothing in this Agreement confers any right or remedy on any person other than the parties and their permitted successors and assigns.

**8.10 Specific Performance.** The Company acknowledges that the Investor would be irreparably harmed by a breach of Articles 2, 3, or 4 and that damages would be an inadequate remedy. The Investor shall be entitled to specific performance and injunctive relief, without posting a bond, in addition to any other remedy.

**8.11 Counterparts; Electronic Signatures.** This Agreement may be executed in counterparts, each of which is an original and all of which constitute one instrument. Signatures delivered by email in portable document format, or by an electronic signature service complying with the U.S. federal ESIGN Act of 2000 (15 U.S.C. § 7001 et seq.) or the Delaware Uniform Electronic Transactions Act (6 Del. C. ch. 12A), are effective as originals.

**8.12 Further Assurances.** Each party shall execute and deliver further documents and take further actions reasonably requested by the other to carry out this Agreement.

**8.13 Expenses.** Each party shall bear its own expenses in connection with this Agreement.

**8.14 Independent Counsel.** Each party acknowledges that it has had the opportunity to consult counsel of its choice about this Agreement.

*(Signature page follows.)*

---

IN WITNESS WHEREOF, the parties have executed this Side Letter Agreement as of the Effective Date.

**COMPANY:**

{{company_name}}

By: ______________________________
Name: {{signatory_name}}
Title: {{signatory_title}}

**INVESTOR:**

[[Alternative A: {{investor_name}}

By: ______________________________
Name: {{investor_signatory_name}}
Title: {{investor_signatory_title}}]]

[[Alternative B: ______________________________
{{investor_name}}]]

Address: {{investor_address}}
Email: {{investor_email}}

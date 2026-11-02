---
id: rofr-and-co-sale-agreement
title: Right of First Refusal and Co-Sale Agreement
category: priced-financing
stage: priced-round
signers: [Company (by an officer), each Investor, each Key Holder, each Key Holder's spouse (consent)]
authorities:
  - "8 Del. C. § 202(a)–(c) (transfer restrictions: prior-opportunity rights under § 202(c)(1), consent rights under § 202(c)(3), prohibited transferees under § 202(c)(5); legend or § 151(f) notice)"
  - "8 Del. C. § 151(f) (notice for uncertificated shares)"
  - "8 Del. C. § 122(18) (Company covenants in stockholder contracts)"
  - "8 Del. C. § 160 (corporation's power to purchase its own shares; capital impairment limit)"
  - "Securities Act of 1933 §§ 4(a)(1), 4(a)(7); 17 C.F.R. § 230.144 (resale exemptions for private secondary transfers)"
  - "Exchange Act § 14(e) and Regulation 14E, 17 C.F.R. §§ 240.14e-1 et seq. (tender offers, if a liquidity program is a tender offer)"
  - "26 U.S.C. §§ 83 and 409A (compensatory character of premium secondary sales; effect on fair market value)"
use_when: Closing a priced preferred round in which founders and other significant common holders ("Key Holders") give the Company a first right, and the investors a secondary right, to buy shares the Key Holders propose to transfer, plus a right for investors to sell alongside them.
do_not_use_when: The company relies only on the bylaws right of first refusal (common at seed), or the transfer is by an investor (investors' transfers are restricted, if at all, by the IRA and charter, not this agreement).
related: [term-sheet, amended-and-restated-certificate-of-incorporation, stock-purchase-agreement, investors-rights-agreement, voting-agreement, bylaws, board-consent-priced-financing, spousal-consent]
sources:
  - name: "Delaware Code, Title 8, ch. 1, subch. VI (§ 202) and subch. V (§§ 151, 160) — official text"
    url: https://delcode.delaware.gov/title8/c001/sc06/index.html
  - name: "eCFR 17 C.F.R. § 230.144 (Rule 144) — eCFR API, version 2026-10-01"
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-230/section-230.144
  - name: "NVCA Model Right of First Refusal and Co-Sale Agreement (updated April 2026; posted June 2026) — structure and market-term reference only; no text copied"
    url: https://nvca.org/model-legal-documents/
  - name: "Bylaws template in this skill, Section 7.6 right of first refusal — coordination of notice and exercise periods"
    url: ../formation/bylaws.md
  - name: "Series Seed documents (CC0 1.0) — consulted for structure of the founder transfer restrictions"
    url: https://github.com/seriesseed/equity
  - name: "Cooley GO, Gunderson Dettmer, Wilson Sonsini, Goodwin, Fenwick public commentary on secondary sales and ROFR/co-sale — market positions only; no text copied"
    url: https://www.cooleygo.com/
last_verified: 2026-11-02
---

## About this template

**What it does.** Each Key Holder (founders, and sometimes early employees and angels holding common stock) agrees that before transferring shares it will (1) offer them first to the Company (the **First Refusal Right**), (2) then to the Investors for any shares the Company does not take (the **Secondary Purchase Right**), and (3) if neither buys all of them, let the Investors sell a pro rata portion of their own shares to the same buyer on the same terms (the **Co-Sale Right**). It also binds Key Holders to an IPO lock-up (useful if they are not parties to the IRA) and carries the § 202 legend. It is a "Transaction Agreement" signed at the Initial Closing.

**Why investors want it.** The investors priced the round on the founders' continued ownership and commitment. A ROFR lets the Company (and investors) keep the cap table clean and block transfers to competitors, and a co-sale right ensures investors share in any premium liquidity founders arrange.

**Statutory frame.**

- *§ 202(c).* Delaware expressly permits restrictions that obligate a holder to offer the corporation or other holders "a prior opportunity, to be exercised within a reasonable time, to acquire the restricted securities" (§ 202(c)(1)), that require consent to a transfer or approval of a transferee (§ 202(c)(3)), and that prohibit transfers to designated persons or classes "if such designation is not manifestly unreasonable" (§ 202(c)(5)). Keep the exercise periods reasonable (aggregate exercise windows of 30–60 days are market).
- *§ 202(a)–(b).* A restriction is enforceable against transferees only if "noted conspicuously" on the certificate or included in the § 151(f) notice for uncertificated shares; otherwise it binds only persons with actual knowledge. A restriction binds shares issued before its adoption only if the holder is a party to the agreement or voted for it. Article 4 handles the legend.
- *§ 160.* The Company may buy its own shares only if doing so would not impair capital; most startups satisfy this easily, but confirm at exercise.
- *§ 122(18).* The Company's covenants (for example, to refuse to register non-compliant transfers) are within § 122(18); keep them consistent with the Restated Certificate and Bylaws.

**Coordination with the bylaws right of first refusal.** The bylaws template in this skill contains a Company right of first refusal on all transfers of common stock (Section 7.6 of the Bylaws) that terminates on an IPO and, by its Section 7.6(i), is designed to run concurrently with this Agreement under a single notice. This form follows that approach: one Transfer Notice satisfies both; the Company's exercise period here and under the Bylaws must be identical (use the same `{{rofr_notice_days}}` value); an exercise or waiver by the Company counts under both; and the Investors' Secondary Purchase Right and Co-Sale Right under this Agreement apply after the Company's period ends, regardless of what happens under the Bylaws (Section 3.4). If the Company's bylaws lack a ROFR, employees' and other non-Key Holders' transfers are restricted only by their equity award agreements; check them.

**Key business decisions (defaults in bold).**

| Issue | Company/founder-favorable | Market (default) | Investor-favorable |
|---|---|---|---|
| Who is a Key Holder | Founders only, and only while employed | **Founders and holders of 1%+ of fully diluted common, including after departure** | All common holders |
| Company exercise window | 15 days | **`{{rofr_notice_days}}` days (30 typical)** | 45 days |
| Investor secondary window | 10 days | **`{{investor_rofr_days}}` days (10–15) after the Secondary Notice, plus over-allotment** | 20 days |
| Co-sale | Not applicable if Company/Investors buy any shares | **Applies to any Offered Shares not purchased under the first refusal and secondary rights** | Applies to the whole transfer |
| De minimis exemption | Up to 10% of holdings per year | **None, or a small optional basket** | None |
| Estate-planning and family transfers | Exempt with joinder | **Exempt with joinder, transferee bound** | Exempt with joinder |
| Forfeiture if not all shares bought | No | **Optional** (if the Company and Investors do not buy all, the Key Holder may sell all to the buyer, subject to co-sale) | — |
| Prohibited transferees | None | **Competitors; Sanctioned Parties** | Plus Foreign Persons (CFIUS) |

**Secondary-sale practice points (Claude should raise these with the client).**

1. *Securities law.* Every Key Holder transfer must have its own exemption from registration. Private resales typically rely on § 4(a)(7) (accredited purchasers, specified information, no general solicitation) or the "§ 4(a)(1½)" analysis; Rule 144 is available for non-affiliates after a one-year holding period for a non-reporting issuer (Rule 144(d)(1)(ii)). Section 3.1's exemptions require a transferee joinder and compliance with law.
2. *Tender offer rules.* A Company-sponsored or investor-led liquidity program offered broadly to employees can be a "tender offer," triggering Regulation 14E (minimum 20 business days open, among other requirements) even for a private company. Section 3.5 lets the Board approve a structured program outside the ROFR mechanics.
3. *Tax.* If a Key Holder who is a service provider sells at a price above fair market value to the Company or to an investor, the IRS may treat the premium as compensation (wages subject to withholding) under § 83. Secondary sales at prices above the most recent 409A value can also be evidence of a higher fair market value for future option grants; tell the valuation firm.
4. *Information.* Buyers will ask for financial information. Any disclosure by the Company must be under an NDA and is subject to Rule 10b-5 anti-fraud liability; the Company should not "sponsor" information it has not vetted.

**Common mistakes this form avoids.** Bylaws and agreement ROFR periods that conflict; a ROFR at the "same price" with no method to value non-cash consideration (Section 2.1(g)); no anti-circumvention clause for Key Holders that hold through entities (Section 2.4); allowing founders to escape by transferring to a trust without a joinder; failing to obtain spousal consent; omitting the § 202 legend from uncertificated-share notices.

**Deadlines.** None imposed on signing. Each Transfer Notice starts the clock: Company `{{rofr_notice_days}}` days; Secondary Offer Notice within five (5) days after that; Investors `{{investor_rofr_days}}` days; over-allotment `{{undersubscription_days}}` days; closing within `{{rofr_closing_days}}` days after the last exercise; free transfer within `{{rofr_free_transfer_days}}` days.

## Drafting inputs

| Variable | Meaning | Example | Notes |
|---|---|---|---|
| `{{company_name}}` | Exact legal name | Northwind Robotics, Inc. | |
| `{{company_address}}`, `{{company_notice_email}}` | Notice details | | |
| `{{effective_date}}` | Date of this Agreement | March 3, 2027 | Initial Closing date |
| `{{series_name}}` | New series | Series A | |
| `{{shadow_series_name}}` | Shadow series, if any | Series A-1 | Optional |
| `{{par_value}}` | Par value | $0.00001 | |
| `{{prior_agreement_title}}`, `{{prior_agreement_date}}` | Prior ROFR agreement being amended and restated | | Delete if none |
| `{{requisite_preferred_percent}}` | Requisite Preferred Holders threshold if higher than a majority (Alternative B) | sixty percent (60%) | Must match the Restated Certificate |
| `{{rofr_notice_days}}` | Company exercise period | thirty (30) | **Same value as the Bylaws Section 7.6 period** |
| `{{investor_rofr_days}}` | Investor secondary refusal period | ten (10) | |
| `{{undersubscription_days}}` | Over-allotment period | five (5) | |
| `{{co_sale_days}}` | Investor co-sale election period | fifteen (15) | Runs from the deadline for the Secondary Offer Notice |
| `{{rofr_closing_days}}` | Days to close a ROFR purchase | thirty (30) | Same as Bylaws if possible |
| `{{rofr_free_transfer_days}}` | Days the Key Holder has to complete a permitted transfer to the Prospective Transferee | ninety (90) | Bylaws default 60–90 |
| `{{de_minimis_transfer_shares}}` | Optional annual de minimis exemption | 50,000 shares | Optional |
| `{{lockup_days}}` | IPO lock-up | one hundred eighty (180) | Must match the IRA |
| `{{signatory_name}}`, `{{signatory_title}}` | Company signer | | |
| `{{investor_name}}`, `{{investor_address}}`, `{{investor_email}}`, `{{investor_signatory_name}}`, `{{investor_signatory_title}}` | Investor details | | Repeat |
| `{{key_holder_name}}`, `{{key_holder_address}}`, `{{key_holder_email}}` | Key Holder details | Alex Rivera | Repeat |
| `{{key_holder_spouse_name}}` | Spouse signing Exhibit A | | |
| `{{company_counsel_notice}}`, `{{investor_counsel_notice}}` | Copy-to counsel | | |
| `{{forum}}` | Exclusive forum | Court of Chancery of the State of Delaware | |

## Form

---

# {{company_name}}

# [[Optional: AMENDED AND RESTATED]] RIGHT OF FIRST REFUSAL AND CO-SALE AGREEMENT

This [[Optional: Amended and Restated]] Right of First Refusal and Co-Sale Agreement (this "**Agreement**") is dated {{effective_date}} and is among {{company_name}}, a Delaware corporation (the "**Company**"); the Investors identified on Schedule A; and the Key Holders identified on Schedule B.

## BACKGROUND

A. Schedule B shows, for each Key Holder, the shares of Capital Stock and the options to acquire Common Stock that the Key Holder beneficially owns on the date of this Agreement.

B. On the date of this Agreement the Company is issuing {{series_name}} Preferred Stock to the Purchasers (as defined in the Purchase Agreement) under the {{series_name}} Preferred Stock Purchase Agreement of the same date (as amended, the "**Purchase Agreement**"). The Purchasers have made the Key Holders' and the Company's entry into this Agreement a condition of their investment. The Board has determined that the investment is adequate consideration for the Company's undertakings in this Agreement for purposes of Section 122(18) of the DGCL.

[[Optional: C. Some of the parties are bound by the {{prior_agreement_title}} dated {{prior_agreement_date}} (the "**Prior Agreement**"). The parties to the Prior Agreement who sign this Agreement hold enough shares to amend it, and they intend this Agreement to replace it in full.]]

The parties therefore agree as follows.

## ARTICLE 1 — DEFINITIONS AND INTERPRETATION

**1.1 Defined Terms.** Capitalized terms have these meanings:

"**Affiliate**" of a Person means another Person that controls, is controlled by or is under common control with it, directly or indirectly. For an investment fund, Affiliates include its general partner, managing member and investment adviser and any other fund managed or advised by the same adviser or an affiliate of that adviser.

"**Board**" means the Company's board of directors.

"**Business Day**" means a day other than a Saturday, a Sunday or a day on which banks in New York, New York or Wilmington, Delaware may close by law.

"**Bylaws ROFR**" means the Company's right of first refusal in Section 7.6 of its Bylaws, as in effect from time to time.

"**Capital Stock**" means the Company's Common Stock and Preferred Stock, including (a) Common Stock issued or issuable on conversion of Preferred Stock and (b) Common Stock issued or issuable on the exercise or conversion of options, warrants or other convertible securities, in each case whether held now or acquired later. In counting a holder's Capital Stock, each share of Preferred Stock counts as the number of shares of Common Stock into which it is then convertible.

"**Change of Control**" means any sale or series of related sales by stockholders in which one Person, or a group of Persons acting together, acquires shares carrying more than fifty percent (50%) of the Company's outstanding voting power.

"**Co-Sale Participant**" has the meaning given in Section 2.2(a).

"**Co-Sale Right**" means each Investor's right under Section 2.2 to sell its own Capital Stock to a Proposed Transferee alongside a Key Holder.

"**Common Stock**" means the Company's common stock, par value {{par_value}} per share.

"**Company Election Notice**" means the Company's written notice under Section 2.1(c) stating how many Offered Shares it will buy.

"**Competitor**" and "**Sanctioned Party**" have the meanings given in the Investors' Rights Agreement.

"**Deemed Liquidation Event**" has the meaning given in the Restated Certificate.

"**DGCL**" means the General Corporation Law of the State of Delaware.

"**Entity Transfer**" has the meaning given in Section 2.4.

"**First Refusal Right**" means the Company's right under Section 2.1 to buy Offered Shares.

"**Immediate Family Member**" of an individual means the individual's spouse or domestic partner, and any child, stepchild, grandchild, parent, stepparent, grandparent, sibling or in-law of the individual, including adoptive relationships.

"**Investor Election Notice**" means an Investor's written notice under Section 2.1(d) stating how many Offered Shares it will buy.

"**Investors**" means the Persons listed on Schedule A and every Person who later becomes an Investor under Section 6.10 or 6.12.

"**Investors' Rights Agreement**" and "**Voting Agreement**" mean the agreements with those titles dated as of the date of this Agreement and delivered under the Purchase Agreement, each as amended.

"**IPO**" means the closing of the Company's first firm-commitment underwritten public offering of Common Stock registered under the Securities Act [[Optional: , or, if earlier, the first listing of the Common Stock on a national securities exchange through an effective resale registration statement or the closing of a business combination with a publicly traded special purpose acquisition company]].

"**Key Holder Shares**" means all Capital Stock that a Key Holder holds now or acquires later, including shares acquired by option or warrant exercise or through a stock split, dividend, recapitalization or similar event, but excluding Preferred Stock and Common Stock issued on conversion of Preferred Stock.

"**Key Holders**" means the Persons listed on Schedule B and every Person who later becomes a Key Holder under Section 3.1, 6.10 or 6.13.

"**Offered Shares**" means the Key Holder Shares covered by a Transfer Notice.

"**Over-Allotment Notice**" has the meaning given in Section 2.1(e).

"**Person**" means an individual or any corporation, partnership, limited liability company, trust, association or other entity.

"**Preferred Stock**" means every series of preferred stock designated in the Restated Certificate, including the {{series_name}} Preferred Stock [[Optional: and the {{shadow_series_name}} Preferred Stock]].

"**Proposed Transfer**" means any sale, gift, assignment, pledge, hypothecation, grant of a security interest, encumbrance or other disposition of Key Holder Shares or of any interest in them, whether voluntary or involuntary, by operation of law or otherwise, and includes an Entity Transfer.

"**Proposed Transferee**" means the Person to whom a Key Holder proposes to make a Proposed Transfer.

"**Requisite Preferred Holders**" means the holders of at least [[Alternative A: a majority]] [[Alternative B: {{requisite_preferred_percent}}]] of the outstanding shares of Preferred Stock, with all series acting together as a single class and each share counted on an as-converted basis [[Optional: , disregarding shares held by any Sanctioned Party]].

"**Restated Certificate**" means the Company's Amended and Restated Certificate of Incorporation, as amended or restated.

"**Secondary Offer Notice**" has the meaning given in Section 2.1(d).

"**Secondary Purchase Right**" means each Investor's right under Section 2.1(d) to buy Offered Shares that the Company does not buy.

"**Securities Act**" means the Securities Act of 1933, as amended, and the SEC's rules under it.

"**{{series_name}} Preferred Stock**" means the Company's {{series_name}} Preferred Stock, par value {{par_value}} per share.

"**Transfer Notice**" means the notice a Key Holder must give under Section 2.1(b), substantially in the form of Exhibit B.

**1.2 Interpretation.** "Including" means "including without limitation," and "or" is not exclusive. Article, Section, Schedule and Exhibit references are to this Agreement. A reference to a law or rule includes its successor, as amended. Share numbers adjust under Section 6.2. When a period ends on a day that is not a Business Day, it ends on the next Business Day instead.

## ARTICLE 2 — FIRST REFUSAL, SECONDARY PURCHASE AND CO-SALE

**2.1 Company First Refusal Right and Investor Secondary Purchase Right.**

(a) *Grant.* Except for transfers exempted by Article 3, each Key Holder irrevocably grants the Company the right to buy any or all Offered Shares in each Proposed Transfer, at the price and on the other terms offered by the Proposed Transferee.

(b) *Transfer Notice.* A Key Holder that wishes to make a Proposed Transfer shall deliver a Transfer Notice to the Company and to every Investor at least forty-five (45) days before the intended closing. The Transfer Notice must state: (i) the number and class of Offered Shares; (ii) the form of the transaction; (iii) the identity and address of the Proposed Transferee and, for an entity, of the individuals or entities that control it; (iv) the price per share and every other element of consideration; (v) the remaining material terms, including the intended closing date; and (vi) that the Key Holder has told the Proposed Transferee about this Agreement and Section 3.3, and that the Proposed Transferee has agreed to sign the joinder in Exhibit C if it acquires any Offered Shares. Copies of any written offer, term sheet, letter of intent or draft purchase agreement must accompany it. One Transfer Notice also serves as notice under the Bylaws ROFR, and the periods under both run at the same time.

(c) *Company Election.* The Company may exercise its First Refusal Right by delivering a Company Election Notice to the Key Holder and every Investor within {{rofr_notice_days}} days after it receives the Transfer Notice.

(d) *Secondary Purchase Right.* If the Company does not elect to buy all Offered Shares, then within five (5) days after its election period ends the Company shall notify the Key Holder and every Investor of the number of Offered Shares that remain available (the "**Secondary Offer Notice**"). Each Investor then has the right, exercisable by delivering an Investor Election Notice to the Key Holder and the Company within {{investor_rofr_days}} days after the last day on which the Secondary Offer Notice could timely be given (the "**Investor Election Period**"), to buy up to its pro rata share of the remaining Offered Shares. An Investor's pro rata share is the fraction whose numerator is the Capital Stock it holds and whose denominator is the Capital Stock held by all Investors.

(e) *Over-Allotment.* If, after the Company and the Investors have made their elections, some Offered Shares are still unclaimed, the Company shall, within five (5) days after the Investor Election Period ends, notify each Investor that elected to buy its full pro rata share (each, a "**Fully Electing Investor**"). Each Fully Electing Investor may then elect, by written notice to the Key Holder and the Company within {{undersubscription_days}} days after that notice (an "**Over-Allotment Notice**"), to buy any number of the unclaimed Offered Shares. If the Fully Electing Investors together ask for more than are available, the available shares are divided among them in proportion to the number of Offered Shares each elected to buy under Section 2.1(d), or as they otherwise agree. The Company shall promptly tell the Key Holder and the Fully Electing Investors the result.

[[Optional: (f) *All-or-Nothing.* If the Company and the Investors together elect to buy fewer than all of the Offered Shares, every election under this Section 2.1 lapses, and the Key Holder may sell all (and not part) of the Offered Shares to the Proposed Transferee, subject to Section 2.2 and Section 3.3, at a price and on terms no more favorable to the Proposed Transferee than those in the Transfer Notice. That sale must close within {{rofr_free_transfer_days}} days after the Company received the Transfer Notice; otherwise the Offered Shares again become subject to this Article 2. Any later Proposed Transfer is also subject to this Article 2.]]

(g) *Non-Cash Consideration.* If any part of the Proposed Transferee's consideration is property, services or anything other than cash, the Board shall determine its fair market value in good faith and state it in the Company Election Notice (or, if the Company makes no election, in the Secondary Offer Notice). The Company and each electing Investor may pay that value in cash instead of delivering the same non-cash consideration. If the Key Holder believes in good faith that the Board's figure is wrong, the Key Holder may object by notice within five (5) days after receiving it. The Key Holder and the Company shall then jointly engage an independent valuation firm, whose determination binds everyone and whose fees the Company and the Key Holder shall split equally. Every period in this Section 2.1 is suspended until the firm reports. Within five (5) days after the report, the Company and any electing Investor may withdraw its election.

(h) *Closing of Purchases.* Purchases under this Section 2.1 close, and the purchase price shall be paid to the Key Holder, on the later of the closing date stated in the Transfer Notice and the date {{rofr_closing_days}} days after the Company received the Transfer Notice. If the Proposed Transferee had been offered deferred or installment payment terms, each buyer may pay on those terms or in cash at closing, but no buyer must give any guarantee or credit support the Proposed Transferee would have given. At closing, the Key Holder shall deliver the Offered Shares free of liens other than those created by this Agreement, the Voting Agreement or securities laws, together with any stock power or other transfer instrument the Company reasonably asks for.

> **Drafting note:** The Company's right mirrors the Bylaws ROFR so one notice works for both. A company typically exercises only when it wants to retire shares or route them to a preferred buyer; check § 160 (no repurchase that impairs capital), cash needs, and whether the repurchase price will be treated as evidence of fair market value for later option grants. The investor right sits second, which is why it is called "secondary."

**2.2 Co-Sale Right.**

(a) *Election.* If any Offered Shares are not bought under Section 2.1 and the Key Holder intends to sell them to the Proposed Transferee, each Investor may sell part of its own Capital Stock in that transaction. An Investor that wants to do so (a "**Co-Sale Participant**") shall notify the Key Holder within {{co_sale_days}} days after the last day on which the Secondary Offer Notice could timely be given. Delivering that notice is a binding exercise of the Co-Sale Right.

(b) *Number of Shares.* Each Co-Sale Participant may sell up to the number of its shares of Capital Stock equal to A × (B ÷ C), where:

- A = the number of Offered Shares remaining after the purchases under Section 2.1;
- B = the Capital Stock held by that Co-Sale Participant immediately before the sale (counting Offered Shares it has elected to buy); and
- C = the Capital Stock held by all Co-Sale Participants immediately before the sale (counting Offered Shares they have elected to buy), plus the Offered Shares held by the selling Key Holder.

The number of Offered Shares the Key Holder may sell falls by the number of shares the Co-Sale Participants sell.

(c) *Sale Documents.* The Key Holder and the Co-Sale Participants shall sell under a single written agreement with the Proposed Transferee on customary terms. A Co-Sale Participant need only give representations about its own title, authority, enforceability, absence of conflicts and securities-law status, and its liability under that agreement may not exceed the proceeds it receives except for its own fraud. Signing that agreement is a condition to any sale under this Section 2.2.

(d) *Division of Proceeds.*

(i) Except as provided in clause (ii), the total proceeds shall be divided among the Key Holder and the Co-Sale Participants according to the number of shares each sells. If a Co-Sale Participant sells Preferred Stock, its price per share is the price for Common Stock multiplied by the number of shares of Common Stock into which each share of that Preferred Stock is then convertible.

(ii) If the sale is a Change of Control, the sale agreement shall divide the proceeds as the liquidation provisions of the Restated Certificate would divide them if the sale were a Deemed Liquidation Event and the shares being sold were the only shares outstanding.

(e) *Buyer Refusal.* If the Proposed Transferee will not buy shares from a Co-Sale Participant, or will not negotiate in good faith a sale agreement reasonably acceptable to the Co-Sale Participants, the Key Holder may not sell any Offered Shares to the Proposed Transferee unless, at the same time, the Key Holder itself buys from each Co-Sale Participant the shares it was entitled to sell, at the price and on the terms in the Transfer Notice (as adjusted by Section 2.2(d)(i)). The Co-Sale Participants shall deliver those shares, with proper transfer instruments, against payment. If the Proposed Transferee objects to buying shares of a particular class, the Key Holder need not buy those shares, and the affected Co-Sale Participants may withdraw their elections instead.

(f) *Time Limit.* A Key Holder that has not completed a sale to the Proposed Transferee within {{rofr_free_transfer_days}} days after the Company received the Transfer Notice must start the Article 2 process again before selling. An Investor's decision to use or not use its rights in one transaction does not affect its rights in any later transaction.

> **Drafting note:** *Denominator.* Clause (b) counts only participating Investors plus the seller, so the founder and the Investors who choose to sell share the buyer's demand in proportion to their holdings. A founder-favorable variant counts all Investors' holdings, which shrinks each Investor's allocation. *Preferred.* An Investor that sells Preferred outside a Change of Control gets only the as-converted price, giving up its liquidation preference; clause (d)(ii) protects it when the sale shifts control. *Founder sales in a financing.* When a new lead buys founder shares in a round, obtain written waivers of this Article from the Investors (the board and stockholder consent templates include them) and consider the § 83 and § 409A consequences of any premium.

**2.3 Consequences of Non-Compliance.**

(a) *No Effect; Equitable Relief.* A Proposed Transfer that does not comply with this Agreement is void from the start; the Company shall not record it, and neither the Company nor its transfer agent shall treat the transferee as a stockholder. Because money damages could not adequately remedy a breach, each non-breaching party may seek injunctions, specific performance, rescission and any other remedy available at law or in equity.

(b) *Refusal to Deliver.* If a Key Holder must sell Offered Shares to the Company or an Investor under Section 2.1 but does not deliver them, the buyer may tender the purchase price to the Key Holder (in addition to any other remedy). On that tender, the Company may cancel the Key Holder's certificate or book entry for those shares and issue them to the buyer, and the Key Holder's only remaining right is to receive the tendered price.

(c) *Sale in Breach of the Co-Sale Right.* If a Key Holder sells Offered Shares without honoring the Co-Sale Right, each Investor that was denied the chance to participate may require the Key Holder to buy from it the number and type of shares that Investor could have sold under Section 2.2, at the price and on the terms set by Section 2.2(d). The Investor must give notice of its election within ninety (90) days after the later of receiving notice of the sale and otherwise learning of it, and the Key Holder shall pay in cash at the closing of that purchase against delivery of the shares.

**2.4 Transfers of Interests in Entity Key Holders.** A Key Holder that is an entity or trust shall not permit, and shall cause its equity holders not to make, any transfer or issuance of an equity or voting interest in that Key Holder, or any change of trustee or beneficiary of a trust Key Holder, if as a result the individual who controlled the Key Holder when it signed this Agreement would no longer control it or any Person other than that individual and that individual's Immediate Family Members would acquire a beneficial interest in Key Holder Shares (an "**Entity Transfer**"). An Entity Transfer is permitted only if it is treated as a Proposed Transfer of the Key Holder Shares held by that Key Holder and complies with this Article 2. The Key Holder shall notify the Company promptly of any Entity Transfer.

[[Optional: **2.5 Foreign Person Investors.** No Investor that is a "Foreign Person" (as defined in the Investors' Rights Agreement) may buy shares under Section 2.1 or sell under Section 2.2 in a way that would give it a "DPA Triggering Right" (as so defined) or require a filing under the DPA (as so defined) unless the Board approves as required by the Investors' Rights Agreement.]]


## ARTICLE 3 — EXEMPT TRANSFERS; PROHIBITED TRANSFEREES; COORDINATION

**3.1 Exempt Transfers.** Sections 2.1 and 2.2 do not apply to the following transfers:

(a) by a Key Holder that is an entity, (i) to its own equity holders as a distribution on their interests, or (ii) to an Affiliate controlled by the same individual who controls the Key Holder;

(b) to the Company in a repurchase at no more than the Key Holder's original cost, under a vesting or repurchase arrangement approved by a majority of the Board;

(c) by a Key Holder who is an individual, without consideration and for bona fide estate-planning purposes, (i) by gift to an Immediate Family Member or to a trust, family limited partnership or similar vehicle for the benefit of the Key Holder or Immediate Family Members, or (ii) on death, by will or intestacy, to the Key Holder's estate, heirs or legatees;

(d) a pledge that creates only a security interest, if the Board has approved it in advance and the pledgee agrees in writing to be bound by this Agreement as if it were the pledging Key Holder;

[[Optional: (e) transfers by a Key Holder of not more than {{de_minimis_transfer_shares}} Key Holder Shares in total in any twelve (12)-month period, to transferees that are neither Competitors nor Sanctioned Parties; and]]

(f) any transfer that the Board (including [[Alternative A: at least one Series Director (as defined in the Restated Certificate)]] [[Alternative B: a majority of the Series Directors (as defined in the Restated Certificate)]]) and the Requisite Preferred Holders approve in writing in advance.

For any transfer under clause (a), (c), (d) or (e), the Key Holder must notify the Investors in writing before the transfer, and the transferee must sign the joinder in Exhibit C (and, if married, deliver a Consent of Spouse) before the transfer is recorded. Shares so transferred remain Key Holder Shares, and the transferee is a Key Holder for all purposes of this Agreement.

**3.2 Exempt Offerings.** Article 2 does not apply to (a) any sale of Capital Stock to the Company under an agreement the Board has approved; (b) any sale of Key Holder Shares to the public in the IPO under an effective registration statement; or (c) any sale of all or substantially all of the Company's outstanding Capital Stock in a Deemed Liquidation Event, including a sale compelled by the drag-along provisions of the Voting Agreement.

**3.3 Prohibited Transferees.** Unless the Board approves in writing in advance, no Key Holder may transfer any Key Holder Shares to (a) a Competitor; (b) a Sanctioned Party; or (c) any Person who, after the transfer, would beneficially own twenty percent (20%) or more of the Company's outstanding voting equity securities (measured by voting power) and is, or has a controlling Affiliate that is, subject to a Disqualification Event (as defined in the Voting Agreement).

> **Drafting note:** § 202(c)(5) allows a restriction that bars transfers to "designated persons or classes of persons or groups of persons" so long as the designation "is not manifestly unreasonable," and § 202(d) conclusively presumes some purposes (such as preserving tax attributes) to be reasonable. Competitors and sanctioned parties are easy cases. A blanket bar on transfers to foreign persons can seriously limit liquidity; prefer the targeted CFIUS covenant in the Investors' Rights Agreement unless the Company is a TID U.S. business.

**3.4 Coordination with the Bylaws ROFR.** The Company's First Refusal Right under this Agreement and the Bylaws ROFR are meant to work as one right over Key Holder Shares. Specifically:

(a) one Transfer Notice under Section 2.1(b) satisfies the notice requirement of both;

(b) whatever the Company does under one — full exercise, partial exercise or no exercise — counts as the same action under the other, on the same terms;

(c) as among the parties to this Agreement, and to the extent the Bylaws permit, this Agreement's periods, pricing rules and closing procedures govern any conflict with the Bylaws ROFR for Key Holder Shares;

(d) the Company's waiver of the Bylaws ROFR does not waive the Investors' Secondary Purchase Right or Co-Sale Right, which may be waived only under Section 6.9; and

(e) an exemption under Section 3.1 or 3.2 does not by itself exempt a transfer from the Bylaws ROFR; the Bylaws, or a Board waiver, govern that question.

> **Drafting note:** Use the same `{{rofr_notice_days}}`, `{{rofr_closing_days}}` and `{{rofr_free_transfer_days}}` values as the Bylaws. If the Company's bylaws are not this skill's form, read the actual bylaw provision and adapt Section 3.4, including any Board-consent requirement layered on top. A bylaw restriction binds shares issued before its adoption only if the holder signed an agreement or voted for it (§ 202(b)); this Agreement binds the Key Holders contractually regardless.

[[Optional: **3.5 Liquidity Programs.** The Board (including at least one Series Director) and the Requisite Preferred Holders may approve a structured program in which the Company, one or more Investors or a third party offers to buy Capital Stock from Key Holders and other stockholders on uniform terms (a "**Liquidity Program**"). Sales in a Liquidity Program are not subject to Sections 2.1 and 2.2 if (a) every Major Investor (as defined in the Investors' Rights Agreement) is offered the chance to take part as a buyer [[Optional: or seller]] on the approved terms, and (b) the program complies with securities laws, including Regulation 14E under the Securities Exchange Act of 1934 where the program is a tender offer.]]

## ARTICLE 4 — LEGEND AND TRANSFER RECORDS

**4.1 Legend.** The Company shall place the following legend on every certificate representing Key Holder Shares (including shares held by a transferee under Section 3.1), and, for uncertificated shares, shall include it in the notice required by Section 151(f) of the DGCL:

> "TRANSFERS OF THESE SHARES, INCLUDING ANY SALE, PLEDGE OR OTHER DISPOSITION, ARE RESTRICTED BY, AND IN SOME CASES PROHIBITED UNDER, A RIGHT OF FIRST REFUSAL AND CO-SALE AGREEMENT AMONG THE HOLDER, THE CORPORATION AND OTHER STOCKHOLDERS, AND ARE ALSO SUBJECT TO A RIGHT OF FIRST REFUSAL IN THE CORPORATION'S BYLAWS. THE SECRETARY OF THE CORPORATION WILL PROVIDE COPIES ON WRITTEN REQUEST."

**4.2 Records and Instructions.** Each Key Holder authorizes the Company to instruct its transfer agent, or the administrator of its electronic stock ledger, to block any transfer of legended shares that does not comply with this Agreement, and the Company shall give that instruction promptly. The Company shall not record any transfer that does not comply with this Agreement and may decline to treat a purported transferee as a holder for any purpose. On termination of this Agreement, the Company shall remove the legend at the holder's request.

## ARTICLE 5 — IPO LOCK-UP

**5.1 Lock-Up Undertaking.** Unless the managing underwriter consents in writing, no Key Holder shall, from the date of the final IPO prospectus until the date the Company and the managing underwriter set (not more than {{lockup_days}} days later):

(a) sell, offer, contract to sell, lend, pledge or grant any option, right or warrant over, or otherwise dispose of, directly or indirectly, any Capital Stock or any security convertible into, or exercisable or exchangeable for, Capital Stock, whether owned on that date or acquired later; or

(b) enter into a swap, hedge or other arrangement that transfers any of the economic consequences of owning those securities, however settled.

This Section 5.1 does not restrict (i) sales to the underwriters in the IPO; (ii) Capital Stock bought in the IPO or in the public market afterward; or (iii) transfers described in Section 3.1(c) if the transferee agrees to this Section 5.1. It binds a Key Holder only if every officer and director is bound by the same restriction. If the Company or the underwriters release any holder early in their discretion, the release shall extend proportionately to the Key Holders and the Investors bound by similar restrictions, as provided in the Investors' Rights Agreement. The IPO underwriters may enforce this Article 5 as third-party beneficiaries. Each Key Holder shall sign any lock-up agreement the underwriters reasonably request that is consistent with this Article 5.

**5.2 Enforcement.** The Company may place stop-transfer instructions on each Key Holder's Capital Stock (and that of its transferees) for the lock-up period.

**5.3 Survival.** Except to the extent an underwriting agreement for the IPO supersedes it, this Article 5 survives termination of this Agreement under Section 6.1(a).

> **Drafting note:** If the Key Holders also sign the Investors' Rights Agreement and its market stand-off, delete this Article or conform it so the two cannot be read inconsistently. Founder stock purchase agreements and equity plans usually contain their own stand-off; the stricter provision governs.

## ARTICLE 6 — GENERAL PROVISIONS

**6.1 Term.** This Agreement ends automatically at the earliest of (a) immediately before the closing of the IPO; (b) the closing of a Deemed Liquidation Event; and (c) termination under Section 6.9. Article 5 survives as stated in Section 5.3, and Section 2.3 survives as to any breach before termination.

**6.2 Adjustments.** Every share number in this Agreement adjusts proportionately for any stock split, stock dividend, combination, recapitalization or similar event after the date of this Agreement, and any securities a Key Holder receives in such an event become Key Holder Shares.

**6.3 Key Holder Representation.** Each Key Holder represents that it is the sole legal and beneficial owner of the Key Holder Shares shown for it on Schedule B, free of liens other than those under this Agreement, the Voting Agreement and applicable securities laws, and that no other Person has any interest in them other than, if applicable, a spouse's community or marital-property interest.

**6.4 Governing Law.** Delaware law governs this Agreement and every claim arising out of or relating to it, whether in contract, tort or under statute, without giving effect to any choice-of-law rule that would apply another jurisdiction's law.

**6.5 Forum; Jury Waiver.** Every action arising out of or relating to this Agreement must be brought exclusively in the {{forum}} (or, only if that court lacks subject-matter jurisdiction, in the Superior Court of the State of Delaware, Complex Commercial Litigation Division, or, if that court also lacks jurisdiction, in the United States District Court for the District of Delaware), together with any court hearing an appeal from them. Each party submits to the personal jurisdiction of those courts for that purpose, waives any objection based on venue or inconvenient forum, and agrees that service of process may be made by notice under Section 6.6 in addition to any other lawful method. EACH PARTY, HAVING CONSULTED COUNSEL, KNOWINGLY AND VOLUNTARILY GIVES UP ANY RIGHT TO A JURY TRIAL IN ANY PROCEEDING ARISING OUT OF OR RELATING TO THIS AGREEMENT, THE OTHER TRANSACTION AGREEMENTS (AS DEFINED IN THE PURCHASE AGREEMENT) OR THE COMPANY'S SECURITIES, WHETHER THE CLAIM SOUNDS IN CONTRACT, TORT, FIDUCIARY DUTY OR STATUTE, AND ACKNOWLEDGES THAT THE OTHER PARTIES RELIED ON THIS WAIVER. [[Optional: If a California state court will not enforce this jury waiver, the dispute shall be heard by a referee under California Code of Civil Procedure § 638.]]

**6.6 Notices.** Notices under this Agreement must be in writing. A notice is effective at the earliest of: actual receipt; hand delivery; transmission by email (if sent during the recipient's business hours, or otherwise on the recipient's next Business Day, in each case unless the sender receives an automated delivery-failure message); five (5) days after mailing by certified or registered mail, return receipt requested; or one (1) Business Day after deposit with a national overnight courier for next-day delivery. Notices go to the addresses and email addresses on Schedule A or Schedule B or, for the Company, to its principal office, attention Chief Executive Officer, at {{company_notice_email}}, in each case as updated by notice. Copies (which are not themselves notice) go to {{company_counsel_notice}} for notices to the Company and to {{investor_counsel_notice}} for notices to the Investors. Each Investor and Key Holder consents under Section 232 of the DGCL to receive stockholder notices by email at its listed address; if an email notice bounces, that consent is suspended until the holder gives a working address, and the notice shall be given by another permitted method.

**6.7 Entire Agreement.** This Agreement (with its Schedules and Exhibits), the Bylaws ROFR, the Restated Certificate and the other Transaction Agreements (as defined in the Purchase Agreement) are the parties' entire agreement on this subject and replace all earlier understandings about it. [[Optional: When this Agreement takes effect, it amends, restates and replaces the Prior Agreement in full.]]

**6.8 No Waiver by Delay.** A party's delay or failure in exercising a right or remedy does not waive it or acquiesce in any breach, and waiving one breach does not waive another. Remedies under this Agreement are cumulative with those available at law or in equity.

**6.9 Amendment, Waiver and Termination.**

(a) This Agreement may be amended, terminated or waived (generally or for a particular case, prospectively or retroactively) only in a writing signed by (i) the Company; (ii) the Key Holders holding a majority of the Key Holder Shares then held by Key Holders who are then providing services to the Company as officers, employees or consultants; and (iii) the Requisite Preferred Holders.

(b) Despite Section 6.9(a): (i) no amendment, termination or waiver may affect an Investor or Key Holder without its written consent unless it applies to all Investors or all Key Holders, as applicable, in the same way, and any change that adversely affects one holder disproportionately compared with other holders of the same class or series requires that holder's consent; (ii) the Company may update Schedule A or Schedule B under Sections 6.12 and 6.13 without anyone else's consent; (iii) a waiver of Article 2 for a specific Proposed Transfer may be given by the Company and the Requisite Preferred Holders alone, provided that a waiver of the Secondary Purchase Right or Co-Sale Right binds an Investor that did not sign it only if no Investor (or its Affiliate) that signed it buys or sells shares in that transfer; and (iv) any party may waive its own rights without anyone else's consent.

(c) The Company shall promptly notify any party that did not consent of any amendment, termination or waiver. An amendment, termination or waiver made under this Section 6.9 binds every party and its successors and assigns. A waiver in one instance is not a continuing waiver. A required writing may be signed electronically.

**6.10 Assignment.** An Investor may assign its rights under this Agreement only together with a transfer of its Capital Stock that complies with this Agreement and the Investors' Rights Agreement, and only to (a) an Affiliate of that Investor, or (b) a transferee that, after the transfer, would be a Major Investor (as defined in the Investors' Rights Agreement), in each case if the assignee signs the joinder in Exhibit C as an Investor and is not a Competitor or Sanctioned Party. Key Holders may not assign their rights except to a permitted transferee under Section 3.1 that becomes a Key Holder. This Agreement binds and benefits the parties' permitted successors and assigns. Nobody else has rights under it.

**6.11 Severability.** If a court holds any provision invalid or unenforceable, the rest of this Agreement remains in force, and the provision shall be reformed to the minimum extent needed to make it enforceable.

**6.12 Additional Investors.** A Person who buys {{series_name}} Preferred Stock under the Purchase Agreement after the date of this Agreement may become an Investor by signing a counterpart signature page or the joinder in Exhibit C, without any other party's consent, and the Company shall update Schedule A.

**6.13 Additional Key Holders.** As a condition of issuing Common Stock (or options or other rights for Common Stock) to any Person who would, after the issuance, hold [[Optional: one percent (1%)]] or more of the Company's outstanding Capital Stock on a fully diluted basis, the Company shall have that Person sign the joinder in Exhibit C as a Key Holder (and, if married, deliver a Consent of Spouse), unless the Board and the Requisite Preferred Holders waive the requirement. The Company shall update Schedule B.

**6.14 Spousal Consent.** Each married Key Holder (or Key Holder in a registered domestic partnership) shall cause the Key Holder's spouse or partner to sign a consent in the form of Exhibit A (a "**Consent of Spouse**") on the date of this Agreement or, for a later marriage or partnership, within thirty (30) days after it. A spouse or partner who signs a Consent of Spouse does not thereby acquire any rights under this Agreement.

**6.15 Counterparts and Electronic Signatures.** This Agreement may be signed in counterparts, which together form one instrument. Signatures delivered by PDF or by an electronic signature process that complies with the federal ESIGN Act (15 U.S.C. § 7001 et seq.), the Delaware Uniform Electronic Transactions Act (6 Del. C. ch. 12A) or Section 116 of the DGCL are binding as originals.

**6.16 Specific Performance.** The parties agree that a breach of this Agreement would cause irreparable harm that money could not adequately remedy. Each party may therefore obtain specific performance, injunctions and other equitable relief to prevent or cure a breach, without proving actual damages or posting a bond, in addition to its other remedies.

**6.17 Aggregation.** Shares held by an Investor and its Affiliates are combined to determine rights under this Agreement, and those Affiliates may allocate those rights among themselves as they choose.

**6.18 Costs.** [[Alternative A: Each party bears its own costs in any dispute under this Agreement.]] [[Alternative B: In any action to enforce this Agreement, the prevailing party may recover its reasonable attorneys' fees and costs from the losing party.]]

**6.19 Section 122(18); Directors.** The Company's undertakings in this Agreement are made under Section 122(18) of the DGCL for the consideration recited in Background paragraph B. The Restated Certificate prevails over any conflicting provision of this Agreement. Nothing in this Agreement requires a director or officer, acting in that capacity, to breach a fiduciary duty, and no director or officer is personally liable under this Agreement for acts in that capacity.

**6.20 Headings; Effectiveness.** Headings are for convenience only. This Agreement takes effect at the Initial Closing (as defined in the Purchase Agreement) and is void if the Purchase Agreement terminates before then.

*[Signature pages follow]*

---

The parties have signed this [[Optional: Amended and Restated]] Right of First Refusal and Co-Sale Agreement as of the date first written above.

**COMPANY:**

{{company_name}}

By: ______________________________
Name: {{signatory_name}}
Title: {{signatory_title}}

Address: {{company_address}}
Email: {{company_notice_email}}

---

**INVESTORS:**

{{investor_name}}

By: ______________________________
Name: {{investor_signatory_name}}
Title: {{investor_signatory_title}}

---

**KEY HOLDERS:**

______________________________
{{key_holder_name}}

---

## SCHEDULE A — INVESTORS

| Investor | Address | Email for notices | Capital Stock held (as converted) |
|---|---|---|---|
| {{investor_name}} | {{investor_address}} | {{investor_email}} | |

## SCHEDULE B — KEY HOLDERS

| Key Holder | Address | Email for notices | Key Holder Shares and options |
|---|---|---|---|
| {{key_holder_name}} | {{key_holder_address}} | {{key_holder_email}} | |

---

## EXHIBIT A — CONSENT OF SPOUSE

I, {{key_holder_spouse_name}}, am the spouse or registered domestic partner of {{key_holder_name}}. I have read the [[Optional: Amended and Restated]] Right of First Refusal and Co-Sale Agreement dated {{effective_date}} among {{company_name}} and certain of its stockholders (the "**Agreement**"). I understand that the Agreement limits how my spouse or partner may sell or otherwise transfer shares of {{company_name}}, gives the company and certain investors rights to buy those shares first or to sell alongside my spouse or partner, and requires a lock-up at the company's initial public offering.

I agree that any interest I have in those shares, including any community-property or marital-property interest, is bound by the Agreement to the same extent as my spouse's or partner's interest. I understand that I may consult independent counsel about this consent, and I have either done so or chosen, after reading the Agreement carefully, not to do so.

Date: ____________________

______________________________
{{key_holder_spouse_name}}

---

## EXHIBIT B — FORM OF TRANSFER NOTICE

To: {{company_name}} (Attention: Chief Executive Officer) and each Investor listed on Schedule A to the Right of First Refusal and Co-Sale Agreement dated {{effective_date}} (the "**Agreement**")

The undersigned Key Holder gives notice under Section 2.1(b) of the Agreement and Section 7.6 of the Company's Bylaws of the following Proposed Transfer:

| Item | Detail |
|---|---|
| Offered Shares (number and class) | |
| Form of transaction (sale, gift, pledge, other) | |
| Proposed Transferee (name and address) | |
| Controlling persons of the Proposed Transferee (if an entity) | |
| Price per share and all other consideration | |
| Other material terms (payment timing, conditions, representations) | |
| Intended closing date (at least 45 days after this notice) | |
| Securities-law exemption relied on for the transfer | |

The Key Holder confirms that it has told the Proposed Transferee about the Agreement, the Bylaws ROFR and Section 3.3 of the Agreement, and that the Proposed Transferee has agreed to sign the joinder in Exhibit C if it acquires any Offered Shares. Copies of all written offers and draft transaction documents are attached.

Key Holder: ______________________________ Date: ____________________

---

## EXHIBIT C — JOINDER

The undersigned is acquiring Capital Stock of {{company_name}} (or an option or other right to acquire it) and, as a condition of that acquisition, joins the [[Optional: Amended and Restated]] Right of First Refusal and Co-Sale Agreement dated {{effective_date}} (the "**Agreement**") as (check one):

☐ an "Investor" (as an additional purchaser under Section 6.12 or an assignee under Section 6.10); or

☐ a "Key Holder" (as a permitted transferee under Section 3.1, an assignee under Section 6.10 or a new holder under Section 6.13).

The undersigned agrees that all Capital Stock it holds now or later acquires is bound by the Agreement and that it is a party to the Agreement in that capacity as if it had signed it originally, including the lock-up in Article 5. Notices to the undersigned should be sent to the address and email below.

Signature: ______________________________
Name: ____________________
Address: ____________________
Email: ____________________
Date: ____________________

Acknowledged: {{company_name}}

By: ______________________________
Name:
Title:

# Venture Financing Terms: Priced Seed and Series A Rounds

Expert reference for Claude when negotiating, drafting, modeling or reviewing a priced preferred stock round of a Delaware C-corporation. It explains each term, its mechanics and math, the market position with dated data, the law that constrains it, and how the term appears in this skill's templates: [term-sheet](../templates/priced-financing/term-sheet.md), [amended-and-restated-certificate-of-incorporation](../templates/priced-financing/amended-and-restated-certificate-of-incorporation.md) (the "Restated Certificate"), [stock-purchase-agreement](../templates/priced-financing/stock-purchase-agreement.md), [investors-rights-agreement](../templates/priced-financing/investors-rights-agreement.md), [voting-agreement](../templates/priced-financing/voting-agreement.md), [rofr-and-co-sale-agreement](../templates/priced-financing/rofr-and-co-sale-agreement.md) and [management-rights-letter](../templates/priced-financing/management-rights-letter.md). Read with [convertible-instruments.md](convertible-instruments.md) (SAFE and note conversion math) and [securities-law.md](securities-law.md) (exemptions and filings).

**Last verified:** November 2, 2026. Market figures carry their source and period; refresh them before quoting to a client. Every number in the worked examples can be reproduced with `python3 scripts/conversion_calculator.py` (pricing) or by hand from the formulas given.

**Shared defined terms.** All documents in the set use: "{{series_name}} Preferred Stock," "Preferred Stock," "Common Stock," "Original Issue Price," "Conversion Price," "Requisite Preferred Holders," "Deemed Liquidation Event," "Qualified Public Offering," "Exempted Securities," "Purchasers," "Investors," "Key Holders," "Major Investor," "Transaction Agreements," "Series Directors," "Common Directors," "Independent Directors" and "Restated Certificate." Do not introduce synonyms ("Preferred Directors," "Major Purchasers," "Founders" as a defined class) in one document of the set.

---

## 1. Where each term lives

A priced round splits rights between the charter and contracts. The split matters because charter rights bind every present and future holder and can be changed only by charter amendment (8 Del. C. § 242), while contract rights bind only signatories and are amended under the contract.

| Must be in the Restated Certificate | Usually in a contract |
|---|---|
| Authorized shares; each series and its Original Issue Price (8 Del. C. § 102(a)(4), § 151(a)) | Purchase, closing conditions, representations (Stock Purchase Agreement) |
| Dividend preference, liquidation preference, Deemed Liquidation Events | Registration rights, information rights, pro rata right, covenants (Investors' Rights Agreement) |
| Conversion, anti-dilution, mandatory conversion | Who designates each director; drag-along (Voting Agreement) |
| Class or series election of directors (§ 141(d)) | ROFR and co-sale on Key Holder shares (ROFR and Co-Sale Agreement) |
| Protective provisions (class and series votes) | Management rights (letter) |
| Redemption, pay-to-play | Side letter rights |

Section 151(a) lets a charter make the terms of a series depend on "facts ascertainable outside" the charter, which is how a charter can refer to the Original Issue Price or to a Requisite Preferred Holder election without restating them. Since August 1, 2024, 8 Del. C. § 122(18) also lets the corporation itself contract with stockholders to restrict corporate action or require specified approvals, so covenants that once worried practitioners after *West Palm Beach Firefighters' Pension Fund v. Moelis & Co.*, 311 A.3d 809 (Del. Ch. 2024), may sit in the investor agreements — but a § 122(18) covenant is unenforceable against the corporation to the extent it conflicts with the charter or could not lawfully be placed in it. See Section 9.4.

---

## 2. Price per share

### 2.1 The formula

The round is priced from a negotiated **pre-money valuation** and a negotiated **share count**:

- **Original Issue Price (P)** = Pre-money valuation ÷ Pre-money fully diluted shares (S).
- **New-money shares** = Investment ÷ P, rounded down per investor.
- **Post-money valuation** = Pre-money valuation + New money. If converting SAFEs and notes are counted in S, their money is *not* added; the "post-money" is pre-money plus new cash only.

S is a defined term in the term sheet ("Fully Diluted Capitalization"). The negotiable components:

| Component | Usually in S? | Effect if included |
|---|---|---|
| Outstanding Common Stock (including unvested restricted stock) | Always | — |
| Outstanding Preferred Stock, as converted | Always | — |
| Outstanding options, RSUs, warrants, vested or not | Always | — |
| Unallocated pool existing before the round | Always | — |
| **Pool increase** to reach the post-closing target | Market: yes | Lowers P; dilution falls only on existing holders |
| **SAFE and note conversion shares** | Market: yes | Lowers P; new investors are insulated from SAFE dilution |
| Promised but ungranted options | Yes, through the pool target | Investors insist the target counts only truly available shares |

### 2.2 The circularity

When the pool target is a percentage of *post*-closing shares and the pool increase is in the pre-money, P depends on the pool increase, which depends on post-closing shares, which depend on P. Discount-based SAFE and note conversions also depend on P, and post-money SAFE prices depend on the total of all converting shares. The system is solved by iteration (the calculator) or, for simple cases, in closed form, as below.

### 2.3 Worked example: Northwind Robotics, Inc. Series A

**Facts.** Pre-round: 8,000,000 shares of Common Stock held by the founders; 1,000,000 options outstanding; 500,000 shares available in the pool (so pre-round fully diluted shares *F* = 9,500,000). Converting securities: post-money SAFEs with an aggregate purchase amount of $1,500,000 and a $12,000,000 post-money valuation cap. Series A: $24,000,000 pre-money; $6,000,000 new money ($5,000,000 from Example Ventures Fund I, L.P., the lead; $1,000,000 from other Purchasers); available pool after closing equal to 10% of post-closing fully diluted shares; pool increase and conversion shares both in the pre-money. These are the inputs behind the Restated Certificate template's illustrative figures.

**Step 1 — SAFE price.** A post-money SAFE converts at the cap divided by "Company Capitalization," which includes all converting securities but excludes the pool increase made in the round. Because the SAFE money is 12.5% of its cap ($1,500,000 ÷ $12,000,000), the SAFE holders will own 12.5% of Company Capitalization:

- CC = F ÷ (1 − 0.125) = 9,500,000 ÷ 0.875 = 10,857,142.86
- SAFE price = $12,000,000 ÷ 10,857,142.86 = $1.10526 → **$1.1053** (four decimals, half-up)
- SAFE conversion shares = $1,500,000 ÷ $1.1053 = 1,357,097.6 → **1,357,097** (rounded down)

**Step 2 — pool increase (ΔP).** Post-closing shares T = S × (post-money ÷ pre-money) = 1.25 S, and S = CC + ΔP. The pool condition is 500,000 + ΔP = 10% × 1.25 × (CC + ΔP), so ΔP = (0.125 × CC − 500,000) ÷ 0.875 = (1,357,142.86 − 500,000) ÷ 0.875 = 979,591.84 → **979,592** (rounded up so the pool is not below target).

**Step 3 — price.** S = 10,857,142.86 + 979,591.84 = 11,836,734.69; P = $24,000,000 ÷ 11,836,734.69 = $2.027586 → **$2.0276**.

**Step 4 — new-money shares.** $5,000,000 ÷ $2.0276 = **2,465,969**; $1,000,000 ÷ $2.0276 = **493,193** (each rounded down; 2,959,162 in total).

| Holder | Class or series | Shares | Fully diluted % |
|---|---|---|---|
| Founders | Common Stock | 8,000,000 | 54.0692% |
| Options outstanding | Common Stock (underlying) | 1,000,000 | 6.7587% |
| Pool available before the round | Common Stock (reserved) | 500,000 | 3.3793% |
| Pool increase | Common Stock (reserved) | 979,592 | 6.6207% |
| SAFE holders | Series A-1 Preferred Stock ($1.1053) | 1,357,097 | 9.1721% |
| Example Ventures Fund I, L.P. | Series A Preferred Stock ($2.0276) | 2,465,969 | 16.6666% |
| Other Purchasers | Series A Preferred Stock ($2.0276) | 493,193 | 3.3333% |
| **Total** | | **14,795,851** | 100% |

Available pool after closing: 1,479,592 shares, exactly 10.0000%. Liquidation preferences at 1x: Series A $5,999,997; Series A-1 $1,499,999. To reproduce, save the following as `northwind.json` and run `python3 scripts/conversion_calculator.py northwind.json` (the calculator's built-in Example 6 uses two SAFEs with different caps and so gives different figures):

```json
{
  "company_name": "Northwind Robotics, Inc.",
  "series_name": "Series A",
  "pre_round": {"common_outstanding": 8000000, "options_outstanding": 1000000, "unallocated_pool": 500000},
  "safes": [{"name": "SAFE holders", "type": "post_money", "purchase_amount": 1500000, "valuation_cap": 12000000}],
  "new_round": {
    "pre_money_valuation": 24000000,
    "new_money": 6000000,
    "investors": [{"name": "Example Ventures Fund I, L.P.", "amount": 5000000}, {"name": "Other Purchasers", "amount": 1000000}],
    "post_closing_pool_percent": 10,
    "pool_target_basis": "available",
    "pool_increase_in_pre_money": true,
    "converting_securities_in_pre_money": true
  }
}
```

**Step 5 — what the founders actually paid.** At $2.0276, the pre-round holders' 9,500,000 shares are worth $19,262,200, not $24,000,000. The rest of the headline pre-money pays for the pool increase (979,592 × $2.0276 = $1,986,221) and the SAFE conversion shares (1,357,097 × $2.0276 = $2,751,650). The "effective pre-money" for existing holders is about $19.3 million.

### 2.4 Variants (same inputs)

| Variant | Original Issue Price | Pool increase | New investors' FD % | Founders' FD % |
|---|---|---|---|---|
| Base case: pool increase in the pre-money | $2.0276 | 979,592 | 19.9999% | 54.0692% |
| Pool increase outside the pre-money ("post-money pool") | $2.2105 | 952,381 | 18.6888% | 55.0820% |
| No pool increase (available pool falls to 3.68%) | $2.2105 | 0 | 20.0003% | 58.9474% |

Putting the pool increase outside the pre-money moves about one percentage point of the company from the new investors to the founders here, and raises the price by 9%. Investors resist it because a pool they did not pay for dilutes them; founders resist a large pool in the pre-money because it is paid for by them and may never be granted.

### 2.5 The option pool shuffle — how to negotiate it

1. Ask for the investor's pool target in writing and the basis ("available" versus "available plus outstanding").
2. Build a hiring plan to the next financing (typically 18–24 months) with grant sizes by role. The pool should cover the plan plus a cushion, not a round number.
3. Count promised but ungranted grants as already used; investors will insist and it avoids a later top-up dispute.
4. Trade pool size for price: a smaller pool at a lower headline price can leave the founders better off than a larger pool at a higher one. Show both on one page.
5. If the investor insists on a large pool in the pre-money, ask that any unused increase be cancelled at the next round or that the next round's pool be priced in that round's pre-money.

### 2.6 Converting SAFEs and notes — effects on price

- **Post-money SAFEs** fix their own ownership (purchase amount ÷ post-money cap, measured against Company Capitalization, which excludes the round's pool increase). If the term sheet puts their shares in the pre-money, the founders bear all of the SAFE dilution and the new investors none. That is market.
- **Pre-money SAFEs** compute their price on a denominator that (in the YC pre-money form) includes the round's pool increase, so the SAFE holders share the pool dilution; their ownership is not fixed and grows with every additional SAFE.
- **Convertible notes** convert principal plus accrued interest (unless the note pays interest in cash) at the lower of the cap price and the discounted round price; each note defines its own cap denominator. Interest accrues to the actual conversion date, so remodel if the closing slips.
- **Discount-only instruments** convert at (1 − discount) × P; because P depends on the conversion shares, they make the system circular even without a cap.
- **Shadow series.** Each distinct conversion price becomes its own series (Series A-1, A-2) whose Original Issue Price equals that price. The shadow series gets a liquidation preference equal to the cash invested, its own initial Conversion Price (so it converts one-for-one) and anti-dilution protection measured from its own lower price. Without a shadow series, the Northwind SAFE holders would hold 1,357,097 shares of Series A with a $2,751,650 preference for $1,500,000 invested — about 1.83x. The post-money SAFE requires a shadow series ("Safe Preferred Stock"); some notes and older SAFEs do not, in which case the overhang is a business point, not a drafting fix. See [convertible-instruments.md § 8](convertible-instruments.md).
- **Paperwork.** Converting holders sign the Stock Purchase Agreement (or a joinder) and the investor agreements with limited representations, the charter authorizes each shadow series, and the capitalization representation lists every converting instrument.

### 2.7 Rounding convention

State in the Stock Purchase Agreement that the Original Issue Price and each conversion price are rounded to four decimal places, that shares issued to each holder are rounded down to a whole share (with cash for fractions, or no cash where the instrument says so), and that the pool increase is rounded up. These are the calculator's defaults. Use the same rounded figures in every document; a penny difference between the charter and the purchase agreement is a common closing-week error.

---

## 3. Liquidation preference

### 3.1 The variants

| Variant | What the Preferred receives | Restated Certificate (Section 4.1(b) / 4.2) |
|---|---|---|
| **1x non-participating** (market) | The greater of 1x its Original Issue Price (plus declared but unpaid dividends) and its as-converted share | Alternative A / Alternative A |
| **Full participation** | 1x, then a pro rata share of everything left as if converted | Alternative B / Alternative B |
| **Capped participation** | 1x, then pro rata participation until total receipts reach a cap (often 2x–3x), or its as-converted share if greater | Alternative B / Alternative C |
| **Multiple above 1x** | 1.5x–3x before Common | Any of the above with `liquidation_multiple` above one |

**Seniority** is a separate axis. *Pari passu* (all series share pro rata by preference amount when proceeds are short) is market at seed and Series A. *Standard seniority* or *stacking* (latest series first) appears in later and down rounds; Wilson Sonsini reports senior preferences in 16% of its Series B-and-later financings in 1H 2026. A shadow series ranks with the series it shadows.

**The "greater of" clause.** In a non-participating structure, the Restated Certificate gives each series the better of its preference or its as-converted amount automatically, so holders need not deliver conversion notices before a sale. With several series, each series' choice affects the others; the waterfall must find the outcome in which no series would do better by switching (in practice, test every combination of "convert" and "take preference" and keep the stable one).

### 3.2 Worked waterfall (Northwind post-closing capitalization)

Assumptions: the 1,000,000 outstanding options are fully vested and exercised for a nominal price (so 9,000,000 shares of Common Stock participate); the unallocated pool is ignored; no dividends were declared; no transaction expenses, escrow or debt. As-converted total: 13,316,259 shares. Preferences: Series A $5,999,997 (2,959,162 shares × $2.0276); Series A-1 $1,499,999 (1,357,097 × $1.1053); together about $7.5 million. Amounts rounded to the nearest dollar.

**1x non-participating (market).**

| Exit proceeds | Series A | Series A-1 | Common | Who converts |
|---|---|---|---|---|
| $5,000,000 | $4,000,000 | $1,000,000 | $0 | Neither (pro rata 80/20 by preference) |
| $15,000,000 | $5,999,997 | $1,499,999 | $7,500,004 | Neither |
| $20,000,000 | $5,999,997 | $1,834,429 | $12,165,574 | Series A-1 only |
| $30,000,000 | $6,666,652 | $3,057,383 | $20,275,965 | Both |
| $60,000,000 | $13,333,303 | $6,114,767 | $40,551,930 | Both |
| $150,000,000 | $33,333,258 | $15,286,917 | $101,379,824 | Both |

Breakpoints: Series A-1 converts once proceeds exceed about $17.45 million ($5,999,997 + $1.1053 × 10,357,097 shares of Common Stock and Series A-1). Series A converts once proceeds exceed about $27.0 million ($2.0276 × 13,316,259). So, above the $7.5 million of preferences and below about $17.45 million, every additional dollar goes to Common; between the two breakpoints Common shares each additional dollar with the Series A-1; above about $27.0 million all shares participate equally.

**Full participation (investor-favorable).**

| Exit proceeds | Series A | Series A-1 | Common |
|---|---|---|---|
| $5,000,000 | $4,000,000 | $1,000,000 | $0 |
| $15,000,000 | $7,666,661 | $2,264,346 | $5,068,994 |
| $20,000,000 | $8,777,769 | $2,773,909 | $8,448,321 |
| $30,000,000 | $10,999,986 | $3,793,037 | $15,206,976 |
| $60,000,000 | $17,666,638 | $6,850,421 | $35,482,941 |
| $150,000,000 | $37,666,593 | $16,022,571 | $96,310,836 |

**Capped participation at 3x.** Identical to full participation through $30 million. At $60 million the Series A receives $17,999,971, just under its cap of $17,999,991 (3 × $5,999,997), while the Series A-1 does better converting ($5,503,291 versus $4,499,998 at its own cap); Common receives $36,496,739. Any larger exit pins the Series A at its cap until converting becomes better. Above about $81.0 million (3 × $2.0276 × 13,316,259), the Series A converts and the result matches the non-participating table ($150 million row).

**Lessons for the client.** At a $15 million exit, full participation moves about $2.4 million from Common to Preferred compared with the market term; at $150 million it still moves about $5.1 million. A participation cap protects founders only at large exits. A 1x non-participating preference matters mainly in modest exits and acqui-hires, where it decides whether Common receives anything at all — the scenario in which directors face *Trados* risk (Section 23).

### 3.3 Deemed Liquidation Events, escrows and earnouts

- A **Deemed Liquidation Event** treats a merger in which pre-closing stockholders lose majority voting control, and a sale or exclusive license of all or substantially all assets, as a liquidation, so the preference applies to sale proceeds. A sale by stockholders of a majority of the voting stock is often added, but the charter cannot by itself make selling stockholders share their consideration according to the waterfall; the Voting Agreement's drag-along and allocation covenant do that work.
- **Asset sales without dissolution.** Because the Company, not the stockholders, receives asset-sale proceeds, the Restated Certificate requires the Company to redeem the Preferred Stock from available proceeds if it does not dissolve within a set period (90 days in the template) and the Requisite Preferred Holders ask. The redemption is subject to § 160 and § 173.
- **Escrows and earnouts.** The merger agreement must allocate escrowed, held-back and contingent consideration as if it were paid at closing and then reallocate on release; otherwise a release could be distributed as a separate, smaller liquidation and Common could be shortchanged or overpaid.
- **Waiver.** The Requisite Preferred Holders may waive Deemed Liquidation Event treatment, for example where the buyer issues its own preferred stock with a rolled-over preference.
- **Carve-outs.** Management carve-out plans (a percentage of sale proceeds set aside for employees ahead of the preference) are approved by the Board and usually require Preferred consent because they reduce the preference. They raise the *Trados* issue of whose interests the Board is serving.

---

## 4. Dividends

| Variant | Mechanics | Market |
|---|---|---|
| None / as-converted participation (Series Seed approach) | No stated dividend; Preferred shares in any Common dividend as if converted | Wilson Sonsini 1H 2026: no dividend provision in 64% of financings |
| Non-cumulative, "when and if declared" | Rate (often 6%–8%) of the Original Issue Price, paid before Common only if declared; undeclared amounts lapse | Wilson Sonsini 1H 2026: 34% |
| Cumulative accruing | Accrues daily, unpaid amounts added to the liquidation preference and redemption price | Wilson Sonsini 1H 2026: 1%; Cooley Q2 2026: accruing dividends in 3% of deals |

Dividends may be paid only out of surplus or current or preceding-year net profits (8 Del. C. § 170(a)), and directors who willfully or negligently approve an unlawful dividend are jointly and severally liable (§ 174). Cumulative dividends at 8% on a 1x preference make a five-year-old preference about 1.4x; treat an accruing dividend as a disguised increase in the multiple. Compounding dividends are rarer still.

---

## 5. Conversion

### 5.1 Optional conversion

Each share converts into Common Stock at Original Issue Price ÷ Conversion Price, initially one-for-one. The Conversion Price adjusts for splits, stock dividends and combinations, and under the anti-dilution formula (Section 6). Holders convert voluntarily mainly to vote as Common or, in a participating structure, never; in a non-participating structure the "greater of" clause makes conversion before a sale unnecessary.

### 5.2 Mandatory conversion

All Preferred Stock converts automatically (a) on a **Qualified Public Offering** — a firm-commitment underwritten IPO meeting a minimum price per share and minimum gross proceeds, with an exchange listing — and (b) on the vote of the Requisite Preferred Holders.

| QPO threshold | Company-favorable | Market | Investor-favorable |
|---|---|---|---|
| Price floor | None | 1x–2x the latest Original Issue Price | 3x or more, creating an IPO veto for the latest series |
| Minimum gross proceeds | None, or a modest figure | $50 million–$100 million at Series A and later | High, plus a market-capitalization test |
| Other routes | Direct listing and de-SPAC also count | Direct listing included | IPO only |

Each new lead asks for its own floor; revisit the definition in every round, because one series with a high floor can block an IPO that every other holder wants. The optional "anti-cram-down" clause in the Restated Certificate stops the Requisite Preferred Holders from forcing conversion of the newest series in a sale or financing that disadvantages it; it is reasonable for a small new series and unnecessary for a lead that controls the Requisite Preferred Holder vote.

---

## 6. Anti-dilution

### 6.1 Formulas

When the Company issues Additional Shares (anything other than Exempted Securities) below a series' Conversion Price, that Conversion Price drops.

**Weighted average:** CP2 = CP1 × (A + B) ÷ (A + C), where:

- CP1 and CP2 are the Conversion Prices before and after the dilutive issuance;
- A is the number of shares deemed outstanding before the issuance;
- B is the number of shares the consideration received would have bought at CP1 (aggregate consideration ÷ CP1);
- C is the number of Additional Shares actually issued.

The variants differ only in **A**:

| Variant | What A counts | Effect |
|---|---|---|
| Narrow-based | Only outstanding Preferred Stock (or only outstanding Common Stock, depending on the form) | Larger adjustment; investor-favorable; essentially extinct in U.S. venture deals |
| **Broad-based** (market; Restated Certificate default) | All outstanding Common Stock plus all shares issuable on conversion or exercise of outstanding Preferred Stock, options and other convertible securities | Moderate adjustment |
| Broader-based | Broad-based plus the unallocated pool | Slightly smaller adjustment; company-favorable, often refused |

**Full ratchet:** CP2 = the price of the new issuance, regardless of size. One share sold at a low price reprices the whole series.

### 6.2 Worked example: a Series B down round

Northwind later sells 4,000,000 shares of Series B Preferred Stock at $1.50 ($6,000,000). Before the issuance: 8,000,000 Common; 1,000,000 options; 2,959,162 Series A; 1,357,097 Series A-1; 1,479,592 available in the pool.

For the Series A (CP1 = $2.0276): B = $6,000,000 ÷ $2.0276 = 2,959,163.5; C = 4,000,000.

| Method | A | CP2 (to four decimals) | Series A converts into | Extra Common shares | Founders' FD % after Series B | Series A FD % after |
|---|---|---|---|---|---|---|
| No adjustment (for comparison) | — | $2.0276 | 2,959,162 | 0 | 42.56% | 15.74% |
| Broad-based weighted average | 13,316,259 | $1.9057 | 3,148,447 | 189,285 | 42.14% | 16.58% |
| Broader-based (pool in A) | 14,795,851 | $1.9153 | 3,132,666 | 173,504 | 42.17% | 16.51% |
| Narrow-based (Preferred only) | 4,316,259 | $1.7738 | 3,382,566 | 423,404 | 41.62% | 17.60% |
| Full ratchet | — | $1.5000 | 3,999,997 | 1,040,835 | 40.33% | 20.16% |

(Shares converted = 2,959,162 × $2.0276 ÷ CP2, rounded down. Fully diluted figures include the 4,000,000 Series B shares and the pool.)

The Series A-1, with a Conversion Price of $1.1053, gets **no** adjustment because $1.50 is above its Conversion Price. This is the intended result of the shadow series: SAFE holders are protected against a round priced below what they paid, not below what the Series A paid.

### 6.3 Practice points

- **Exempted Securities** (option grants, conversion shares, splits, equipment-lease and bank warrants, acquisitions, strategic deals, IPO shares, Additional Closing shares, and anything the Requisite Preferred Holders bless) do not trigger adjustment. The Investors' Rights Agreement's pro rata right should exclude the same list by cross-reference to the Restated Certificate.
- **Waiver in a down round.** The Requisite Preferred Holders (and any series with its own vote on the point) can waive an adjustment; a down round often packages a waiver, a pay-to-play and a recapitalization. Each element may require a § 242(b)(2) class or series vote if it adversely changes a series' rights.
- **Market.** Wilson Sonsini reports broad-based weighted average in 98% of its 1H 2026 financings, full ratchet in 1% and narrow-based in 0%.
- **Full ratchet, if conceded,** should be limited in time (for example, the first 12 months) or to a defined bridge, and should exclude Exempted Securities.

---

## 7. Protective provisions and series votes

### 7.1 Three layers of stockholder approval

1. **Statutory general vote.** A charter amendment needs a majority of the outstanding stock entitled to vote (8 Del. C. § 242(b)(1)).
2. **Statutory class and series votes.** A class votes separately on an amendment that would increase or decrease its authorized shares, change its par value, or alter or change its powers, preferences or special rights so as to affect it adversely; a series votes separately when an amendment affects it adversely but not the whole class (§ 242(b)(2)). The charter may opt out of the class vote on changes in authorized shares (but not on adverse changes in rights). After the 2026 amendments (effective August 1, 2026), an opt-out of the § 242(b)(2) class vote does not by itself opt out of § 242(d) — the provision that lets listed companies change authorized shares or effect reverse splits by a majority of votes cast — unless the charter expressly says so or requires a greater vote for authorized-share changes; see *Salama v. Simon*, 328 A.3d 356 (Del. Ch. 2024), *aff'd*, 342 A.3d 373 (Del. 2025). For a private venture company the point matters mainly when drafting the opt-out language and before an IPO.
3. **Charter protective provisions.** Votes the Restated Certificate adds (Requisite Preferred Holders; optional series votes). They are enforced as written but construed narrowly.

### 7.2 Drafting rules

- **Cover mergers.** A protective provision that reaches changes "by amendment, merger, consolidation or otherwise" applies to a merger that changes the charter; one that speaks only of amendments may not (*Elliott Associates, L.P. v. Avatex Corp.*, 715 A.2d 843 (Del. 1998); *Benchmark Capital Partners IV, L.P. v. Vague*, 2002 WL 1732423 (Del. Ch. July 15, 2002), *aff'd*, 822 A.2d 396 (Del. 2003), where a structure through a subsidiary merger avoided a series vote).
- **Cover subsidiaries.** Extend vetoes to actions taken through subsidiaries (issuing subsidiary equity, selling subsidiary assets).
- **Sunset.** Protective provisions usually fall away when the Preferred Stock outstanding falls below a floor (often 20%–25% of the shares originally issued).
- **Threshold design.** "Requisite Preferred Holders" at a majority is the Series Seed and market default. Set a higher percentage only to give an identified investor a veto, and test it against the cap table at each future round.
- **Series votes.** A broad series veto lets the newest series block matters the rest of the Preferred favor. Company counsel's usual concession is a series vote only on changes that affect the series "adversely and differently" from other Preferred — largely duplicating § 242(b)(2) — plus sometimes a series vote on its own mandatory conversion.

### 7.3 Market lists

| Seed (Series Seed-style) | Series A (market) | Investor-favorable additions |
|---|---|---|
| Adverse charter changes; change in authorized shares; senior or parity stock; redemptions and dividends; board size; liquidation or Deemed Liquidation Event | Seed list plus debt above a basket, subsidiary equity or asset transfers, bylaw amendments | Pool increases, change of business, token issuances, budget approval, hiring or firing of executives, series-specific vetoes |

Director-level approval rights (the "Series Director must approve" list) can live in the charter or in a § 122(18) covenant; NVCA's October 24, 2024 model documents moved them from the IRA into the charter, and the October 2025 charter keeps them there (Section 3.3.9).

---

## 8. Board composition by stage

| Stage | Common market | Variants | Notes |
|---|---|---|---|
| Pre-seed / SAFE | Founders only | — | SAFEs carry no board rights |
| Seed (priced) | 2 Common, 1 Series (3 seats) | 2–0 with an observer; 1–1–1 | Many seed investors take an observer rather than a seat |
| Series A | 2 Common, 2 Series, 1 Independent (5 seats); or 2 Common, 1 Series (3 seats) | 3–2 Common majority | The Independent is often unfilled for a year |
| Series B and later | Series seats grow; Common seats often shrink to the CEO | Independent seats added before an IPO | Track § 144(e) control consequences |

Mechanics and law:

- Class-elected seats are created in the charter (§ 141(d)); the Voting Agreement decides who designates each seat. Keep the seat counts identical in the charter, the Voting Agreement and the Bylaws (§ 141(b)).
- A director elected by a class or series can be removed without cause only by that class or series (§ 141(k)), and class-elected vacancies may be filled by the remaining directors elected by that class unless the charter or bylaws say otherwise (§ 223(a)(2)).
- **Control.** Under § 144(e) as amended in 2025, a person with a contractual right to elect a majority of the board is a "controlling stockholder," and two or more holders who act together under an agreement can form a "control group." A Voting Agreement giving two investors who vote together three of five seats may do this. That status changes the safe-harbor process for later transactions with them (Section 22).
- **Observers** are not directors, owe no fiduciary duties, and should sign confidentiality undertakings; the board may exclude them to protect privilege and to manage conflicts.
- **Foreign investors.** A board seat, observer right or right to nominate a director given to a foreign person can make a non-controlling investment in a TID U.S. business a CFIUS "covered investment" (31 C.F.R. § 800.211(b)(2)) (Section 20).

---

## 9. Drag-along

### 9.1 What it does

The drag-along in the Voting Agreement obliges the parties to vote for, not object to, and (for a stock sale) sell their shares in a Sale of the Company approved by specified constituencies, backed by an irrevocable proxy (8 Del. C. § 212(e)). It is a contract among stockholders (§ 218(c)) and a transfer restriction (§ 202(c)(4)) that binds transferees only if noted on the certificate or the uncertificated-shares notice (§ 202(a)).

### 9.2 Who triggers it

| Position | Trigger |
|---|---|
| Founder-favorable | Board + Requisite Preferred Holders + a majority of Common held by Key Holders then providing services |
| Market | Board + Requisite Preferred Holders (Common approval optional) |
| Investor-favorable | Requisite Preferred Holders alone |

A merger always needs Board approval (§ 251(b)), so a Board trigger adds no risk for mergers. For a stock sale among stockholders, making the Board a trigger can import fiduciary review into what would otherwise be a stockholder decision; the Voting Agreement template keeps the Board trigger bracketed for stock sales.

### 9.3 The protective conditions dragged holders expect

1. Representations limited to the holder's own title, authority, capacity, enforceability and no conflicts.
2. Several (not joint) liability, pro rata to consideration received, capped at the consideration received, except for the holder's own fraud.
3. Indemnity for Company representations satisfied first from escrow, borne pro rata.
4. Same form and amount of consideration per share within each class or series, allocated by the charter waterfall (including escrows and earnouts).
5. No non-compete or non-solicit except in an employment capacity on terms similar persons accept; releases limited to claims as a stockholder.
6. Cash in lieu of securities for non-accredited holders.
7. An optional price floor (a minimum amount per share of Common or a minimum multiple for the Preferred).

### 9.4 Limits: appraisal waivers, fiduciary claims, § 122(18)

- **Appraisal.** *Manti Holdings, LLC v. Authentix Acquisition Co.*, 261 A.3d 1199 (Del. 2021), enforced an advance waiver of § 262 appraisal rights in a stockholders agreement signed by sophisticated, counseled holders with bargaining power who received consideration. The waiver must be express, and the drag-along must actually be invoked according to its terms; the Court of Chancery declined to bar appraisal where the majority completed a merger without exercising the drag-along (*Halpin v. Riverstone National, Inc.*, 2015 WL 854724 (Del. Ch. Feb. 26, 2015)). Do not rely on an appraisal waiver against unrepresented employee holders who sign a short joinder.
- **Fiduciary claims.** Sophisticated venture investors who had promised not to sue over fiduciary claims arising from a drag-along sale were told in *New Enterprise Associates 14, L.P. v. Rich*, 295 A.3d 520 (Del. Ch. 2023), that the promise was facially valid and reasonable, subject to limits (it cannot bar claims for intentional wrongdoing, and its proponent must show enforcement is reasonable); because the complaint pleaded intentional, bad-faith conduct, the motion to dismiss was denied. A drag-along does not displace directors' duties in approving the sale itself.
- **§ 122(18) and Moelis.** The Court of Chancery's 2024 *Moelis* decision held that several board-approval rights in a stockholders agreement violated § 141(a). The legislature responded with § 122(18) (84 Del. Laws c. 309, effective August 1, 2024), which authorizes the corporation to contract with current or prospective stockholders to restrict its own actions, require approvals and make covenants, subject to the charter and to what the charter could lawfully contain. On January 20, 2026, the Delaware Supreme Court reversed *Moelis*, holding the challenged provisions at most voidable and the challenge barred by laches, without deciding facial validity. Drag-along voting covenants among stockholders were never in doubt; Company covenants in the Voting Agreement (to seat designees, to enforce the agreement) rely on § 122(18).
- **§ 220.** After the 2025 amendments, any § 122(18) agreement is part of the "books and records" a stockholder with a proper purpose may inspect (§ 220(a)(1)). Assume the Voting Agreement and Investors' Rights Agreement will be seen by every stockholder.

---

## 10. Registration rights

Registration rights let investors force or join an SEC registration of the Common Stock they receive on conversion ("Registrable Securities"). They are seldom used — an IPO is a company decision and underwriters control allocations — but they set the IPO lock-up and are expensive to renegotiate later, so they are papered from Series A.

| Right | Company-favorable | Market | Investor-favorable |
|---|---|---|---|
| S-1 demand: start | 5 years after closing | Earlier of 5 years after closing or 180 days after the IPO | 3 years after closing |
| S-1 demand: initiators and size | Majority; $20M+ | Majority (or a percentage that includes the lead); $20M anticipated aggregate offering price (NVCA's default since its October 2024 update, up from $15M) | 20%–30%; $10M |
| Number of S-1 demands | 1 | 2 | 3+ |
| S-3 demands | 1 per year; $5M | 2 per 12 months; $3M | Unlimited |
| Piggyback cutback | IPO: to zero; later: to zero | IPO: to zero; later: holders keep at least 25% | 30%+ floor |
| Expenses | Selling counsel not paid | One selling counsel, capped | Uncapped |
| Lock-up | 180 days; all later offerings | 180 days for the IPO; releases shared pro rata | IPO only |
| Termination | Earlier of Deemed Liquidation Event and 3 years after IPO; Rule 144 availability | Same, with 3–5 years | 5+ years |

The lock-up must remain consistent with FINRA Rule 2241, which no longer requires research quiet periods around lock-up expirations (so the old 16-day extension is obsolete).

---

## 11. Information and inspection rights

- **Who gets them.** Major Investors (a dollar threshold, often $250,000–$1,000,000 at Series A, set so the lead and serious co-investors qualify). Include SAFE holders' original purchase amounts in the threshold count if they hold side-letter information rights; otherwise obtain waivers.
- **What.** Annual financial statements (audited only if the Board or the Requisite Preferred Holders require it — early-stage audits are expensive), quarterly statements, an annual budget, and sometimes monthly statements and a capitalization report. Inspection rights at reasonable times.
- **Limits.** Exclude competitors; exclude trade secrets and privileged material; condition on confidentiality. NVCA's October 2024 update clarified that the Company need not create information that does not exist.
- **Statutory floor.** Every stockholder keeps § 220 inspection rights for a proper purpose. The 2025 amendments to § 220 (85 Del. Laws c. 6) define "books and records" more narrowly and add conditions, but they also make every § 122(18) agreement inspectable. Contractual waivers of § 220 rights must be clear and are most defensible against counseled institutional investors.
- **Termination.** On the IPO (when public reporting takes over) or a Deemed Liquidation Event.

---

## 12. Pro rata (preemptive) rights

- **Formula.** Each Major Investor may buy (its fully diluted shares) ÷ (total fully diluted shares) of each issuance of New Securities, measured either against total fully diluted capitalization (market) or against shares held by all Major Investors (investor-favorable: it entitles Major Investors to the whole round between them). Over-allotment lets participating Major Investors take up shares others decline.
- **Exclusions.** The same Exempted Securities list as the anti-dilution provision.
- **SAFE side letters.** The YC Pro Rata Side Letter grants SAFE holders a participation right in the round in which the SAFE converts. Reconcile it in the term sheet: either the SAFE holder is a Major Investor going forward or its side-letter right is satisfied and terminated at closing.
- **Super pro rata** (a right to buy more than one's share) is a lead-investor ask; cap it by amount and by round.
- **Waiver.** The Requisite Preferred Holders can waive for all, but a waiver that lets some Major Investors participate while excluding others should require the excluded holders' consent.
- **Termination.** IPO or Deemed Liquidation Event.

---

## 13. Redemption

Investor-elected redemption ("put") rights after five to seven years are uncommon (Cooley Q2 2026: 5.4% of deals; Wilson Sonsini 1H 2026: 5%) and weak in practice. Section 160(a)(1) bars a redemption when capital is impaired or would become impaired, and directors who approve an unlawful redemption face liability under § 174. In *Frederick Hsu Living Trust v. ODN Holding Corp.*, C.A. No. 12108-VCL (Del. Ch. Apr. 14, 2017, corrected Apr. 25, 2017), the court held that directors owe their duties to the residual claimants and need not sacrifice the enterprise to fund a redemption, while allowing claims that the board had favored the redeeming holder to proceed. Charters that include redemption usually add a remedy for failure (a higher dividend rate, a board seat, a right to force a sale); each remedy is investor-favorable and should be resisted at Series A. The Deemed Liquidation Event redemption after an asset sale (Section 3.3) is different and is market.

---

## 14. Pay-to-play

A pay-to-play converts (or reclassifies into a lesser shadow series) the Preferred Stock of any holder that does not buy its pro rata share of a designated later financing. It is a down-round and recapitalization tool: Cooley reports pay-to-play in 8.4% of its Q2 2026 deals; Wilson Sonsini reports it in 11% of Series B-and-later financings in 1H 2026. Implementation:

- **Charter-based** (the Restated Certificate's optional special mandatory conversion) or **deal-based** (the new round's charter amendment converts non-participants). Either requires the votes for a charter amendment, often including § 242(b)(2) series votes.
- **Fiduciary exposure.** When insiders lead the financing and the conversion falls on outsiders, the board's approval is an interested transaction (Section 22). Offer every holder its full pro rata share, give adequate notice and time, and have the price tested independently.
- **Accredited status.** Holders that cannot invest (non-accredited angels, funds past their investment period) are penalized; consider carve-outs for small holders.

---

## 15. Founder vesting

- **Standard.** Four-year vesting with a one-year cliff, starting from the founder's start date, with a Company repurchase right over unvested shares at the lower of cost and fair market value. Most founders already have it under their restricted stock purchase agreements (see the founders templates).
- **Re-vesting at a financing.** Investors sometimes ask founders whose shares are largely vested to re-vest a portion. Market practice is to give credit for time served (for example, 25% vested at closing and the rest monthly over 36 months), to avoid a new cliff, and to accelerate on a termination without cause.
- **Acceleration.** Single-trigger (on a change of control alone) is rare and buyer-unfriendly. Double-trigger (change of control plus termination without cause or resignation for good reason within 12 months) of 25%–100% is common for founders and senior executives.
- **Tax.** Imposing new vesting on shares the same founder already owns is generally not a new transfer under 26 U.S.C. § 83 (Rev. Rul. 2007-49, Situation 1), so no new 83(b) election is required, though many practitioners file a protective election. If shares are exchanged (for example, in a reorganization), a new transfer may occur and a timely 83(b) election (within 30 days) becomes critical.
- **QSBS.** Re-vesting does not by itself restart the § 1202 holding period for stock already issued. Repurchases of unvested shares at cost on termination fall within the § 1202 redemption rules only to the extent the regulations do not exempt them; check Treas. Reg. § 1.1202-2.

---

## 16. Side letters

Side letters give individual investors rights outside the Transaction Agreements: pro rata rights below the Major Investor threshold, information rights, MFN protection, regulatory accommodations (Bank Holding Company Act, ERISA "VCOC" management rights, sovereign or tax-exempt investor needs), or confidentiality carve-outs. Rules:

1. Disclose every side letter in the disclosure schedule and give the lead a copy.
2. An MFN in a side letter can spread terms to all investors with the same instrument; read the MFN's scope before granting anything.
3. A side letter with the corporation is likely a § 122(18) agreement and a § 220 book and record (Section 9.4); do not expect confidentiality from other stockholders.
4. A side letter cannot override the charter; charter-level economics (preference, conversion) must be in the Restated Certificate.
5. Terminate SAFE-era side letters at the priced round unless they are expressly preserved.

---

## 17. Series Seed, NVCA and YC-standard documents compared

| Feature | Series Seed (v3.2; CC0) | NVCA model documents (charter, SPA, IRA, Voting, ROFR updated Oct. 2025) | YC-standard seed (post-money SAFE + pro rata side letter) |
|---|---|---|---|
| Instrument | Priced Series Seed Preferred Stock | Priced preferred, any series | Contract right to future preferred; no stock until a priced round |
| Documents | Term sheet, investment agreement, restated charter (three documents) | Term sheet, charter, SPA, IRA, Voting Agreement, ROFR/co-sale, management rights letter, indemnification agreement | SAFE, side letter |
| Liquidation preference | 1x non-participating; mergers treated as liquidations | Alternatives from 1x non-participating to participating with cap | Purchase amount (or as-converted amount) on a liquidity event; on par with preferred |
| Dividends | As-converted only | Alternatives (as-converted, non-cumulative, cumulative) | None |
| Anti-dilution | None beyond splits in v3.2 (later rounds add it) | Broad-based weighted average default; full ratchet alternative | None (price fixed by cap) |
| Protective provisions | Short list, majority of Preferred | Long list, Requisite Preferred Holders, optional series votes and director-approval matters | None |
| Board | Specified seats by class | Detailed board-designation mechanics | None |
| Investor rights | Major Purchaser information and pro rata; "future rights" clause gives Series Seed the next round's rights | Full registration, information, pro rata and covenant package | Pro rata right in the conversion round via side letter |
| Drag-along / ROFR | Light or none | Full drag-along with protections; ROFR and co-sale on Key Holders | None |
| Counsel fees | Flat fee (the v3.2 term sheet suggests $10,000) | Capped by negotiation | None |
| Best for | Small priced seed rounds that want cheap documents | Series A and later; institutional seed | Pre-seed and seed; fastest, cheapest |

Observations:

- **Y Combinator's standard deal** is $500,000 on two SAFEs signed together: $125,000 on a post-money SAFE for 7% of the company, and $375,000 on an uncapped MFN SAFE (ycombinator.com/deal, consulted Nov. 2, 2026). YC publishes SAFEs and a pro rata side letter but no priced-round documents; its earlier "Series AA" seed documents are no longer offered. Use the YC forms unmodified (see the SAFE guide).
- **Series Seed** documents are dedicated to the public domain (CC0) and may be adapted; this skill uses them for structure and for the light-form protective-provision list. The GitHub repository's latest release notes are for version 3.2.
- **NVCA.** NVCA's October 2, 2025 update revised the charter, SPA, IRA, Voting Agreement and ROFR/co-sale models (milestone tranches in the SPA, two-way national-security and data-security representations, QSBS changes reflecting Pub. L. 119-21, governance-policy and outbound-investment covenants, and other changes summarized by Foley and Nixon Peabody). This reference did not confirm whether the NVCA term sheet itself was revised in 2025.

> **Verify:** Before describing "the current NVCA term sheet," confirm its latest revision date on nvca.org/model-legal-documents.

---

## 18. Market data (dated)

| Data point | Value | Source and period |
|---|---|---|
| Deals and capital | 166 financings; $85.7 billion invested | Cooley, Q2 2026 Venture Financing Report (Aug. 17, 2026), Cooley deals in Q2 2026 |
| Up / flat / down rounds | 83.6% / 4.3% / 12.1% | Same |
| 1x liquidation preference | 95.8% of deals | Same |
| Non-participating Preferred Stock | 96.4% | Same |
| Accruing dividends | 3% | Same |
| Redemption rights | 5.4% | Same |
| Pay-to-play | 8.4% | Same |
| Median pre-money, Series B | $185.2 million (up from $152.5 million in Q1 2026) | Same (Cooley gives direction only for seed and Series A) |
| Median pre-money, seed | $23.0 million (down from $35.0 million in Q1 2026) | Wilson Sonsini, The Entrepreneurs Report: Q2 2026, Wilson Sonsini deals in Q2 2026 |
| Median pre-money, Series A | $80.0 million | Same |
| Median pre-money, Series B | $290.5 million | Same (Wilson Sonsini and Cooley data sets differ; never mix them in one comparison) |
| Median seed raise | $6.7 million (down from $7.8 million in Q1 2026) | Same |
| Broad-based weighted average anti-dilution | 98% of financings (full ratchet 1%; narrow-based 0%) | Wilson Sonsini, Q2 2026 report, deal-terms appendix, 1H 2026 |
| Non-participating | 97% (capped participation 1%; uncapped 2%) | Same |
| Dividends | None 64%; non-cumulative 34%; cumulative 1% | Same |
| Redemption | 5% | Same |
| Senior liquidation preference (Series B and later) | 16% | Same |
| Pay-to-play (Series B and later) | 11% | Same |
| Post-seed convertible notes | Median qualified-financing threshold $10 million; median cap $55 million | Same, 1H 2026 |
| Qualitative | Participating and greater-than-1x preferences "remained rare"; median seed and Series A pre-money valuations reached record highs in 2025; 61% of venture dollars went to AI companies in Q1 2026 | Fenwick, Venture Beacon Q1 2026 (June 29, 2026) |

How to use it: quote the source and period every time; use the medians for context, not as a target (AI rounds skew 2025–2026 medians upward); and compare like with like (Cooley and Wilson Sonsini measure different deal populations). Carta's State of Private Markets reports, which draw on a much larger cap-table data set, were not retrievable for this update; secondary sources conflict on Carta's 2026 medians.

> **Verify:** Before quoting Carta valuation, round-size or dilution medians, obtain the current Carta State of Private Markets report directly. Gunderson Dettmer, Goodwin and Orrick also publish periodic venture reports; none was used for figures here.

---

## 19. Approvals and closing mechanics

### 19.1 Board consent (8 Del. C. § 141(f))

The Board, usually by unanimous written consent, should: (a) adopt the Restated Certificate, declare it advisable and submit it to the stockholders (§ 242(b)(1); § 245(b) for a restatement that also amends); (b) approve the Stock Purchase Agreement and other Transaction Agreements and the sale and issuance of the shares, including at Additional Closings and on conversion of SAFEs and notes; (c) reserve Common Stock for conversion; (d) approve the pool increase and recommend it to the stockholders (and, for incentive stock options, obtain stockholder approval within 12 months under 26 U.S.C. § 422(b)(1)); (e) determine the consideration for any § 122(18) covenants; (f) approve the indemnification agreements, D&O insurance and the Form D and state filings; (g) if any director is interested, record the disinterested-director approval required for the § 144 safe harbor (Section 22). A director may make a consent effective at a future time no more than 60 days after giving it (§ 141(f)); state a definite effective date.

### 19.2 Stockholder consent (8 Del. C. §§ 228, 242, 245)

- **Votes.** Majority of outstanding voting power (§ 242(b)(1)); each class or series entitled to a § 242(b)(2) vote (in a first priced round, the Common Stock votes as a class on the increase in authorized shares unless the charter already opted out); any charter-based votes of existing Preferred Stock (Requisite Preferred Holders and any series votes); and any contractual consents.
- **Written consent.** Valid if signed by holders of at least the minimum votes needed at a meeting, unless the charter prohibits action by written consent (§ 228(a)); consents must be delivered within 60 days of the earliest dated consent (§ 228(c)). The record date is the first date a signed consent is delivered, unless the Board fixes one (§ 213(b)).
- **Notice.** Prompt notice to stockholders who did not consent and would have been entitled to notice of a meeting (§ 228(e)). Send it with or shortly after closing; include enough information that holders understand the financing, especially where employees or angels hold Common Stock.
- **Information statement.** Where non-consenting holders are numerous or the financing affects them adversely, consider a short information statement to reduce disclosure-claim risk.

### 19.3 Waivers and contractual consents

Collect waivers of: existing pro rata or preemptive rights (for the new shares and the SAFE conversion shares); MFN rights in SAFEs and side letters; existing ROFR and co-sale rights if a founder secondary occurs; consent rights in existing investor agreements (and confirm that the signers satisfy each prior agreement's amendment provision); and any bank-loan covenants restricting new equity or charter changes.

### 19.4 Filing and closing order

1. Board consent effective.
2. Stockholder consents delivered and effective.
3. Restated Certificate signed by an authorized officer and filed with the Delaware Division of Corporations; effective on filing or at a specified time no later than the 90th day after filing (§ 103(d)). The shares do not exist until it is effective; never wire funds or issue shares before the filing is confirmed.
4. Signature pages released from escrow; funds received; shares issued and recorded in the stock ledger, with § 151(f) notices for uncertificated shares (including the § 202(a) legend for transfer restrictions).
5. Post-closing: § 228(e) notice; Form D within 15 calendar days after the first sale (17 C.F.R. § 230.503(a)(1); the date of first sale is when the first investor is irrevocably committed); state notice filings by each purchaser's state of residence (California § 25102.1(d) notice within 15 days, others through NASAA's EFD); updated cap table and 409A review (a priced round is a material event for valuation purposes); Delaware franchise tax recalculation because authorized shares increased.
6. Additional Closings follow the same steps without a new charter filing if the authorized shares suffice; amend the Form D if required by Rule 503(a)(3).

**Antitrust.** Venture preferred stock that votes for directors is a voting security for Hart-Scott-Rodino purposes. A single investor's acquisition rarely approaches the 2026 size-of-transaction threshold of $133.9 million (effective Feb. 17, 2026), and acquisitions of 10% or less solely for investment are exempt, but check large late-stage rounds.

> **Verify:** The HSR thresholds are adjusted every January; confirm the current figure and the investment-only exemption's applicability (for example, where the investor takes a board seat) before relying on it.

---

## 20. Foreign investors: CFIUS and outbound investment

### 20.1 CFIUS (50 U.S.C. § 4565; 31 C.F.R. Part 800)

- **Jurisdiction.** CFIUS can review (a) any transaction giving a foreign person control of a U.S. business, and (b) a non-controlling "covered investment" in a **TID U.S. business** — one that produces, designs, tests, manufactures, fabricates or develops critical technologies, performs specified functions for covered critical infrastructure, or maintains or collects sensitive personal data of U.S. citizens (31 C.F.R. § 800.248). A minority venture investment becomes a covered investment only if it gives the foreign person (1) access to material nonpublic technical information, (2) membership or observer rights on the board, or the right to nominate a director, or (3) involvement, other than through voting shares, in substantive decisionmaking about sensitive personal data, critical technologies or covered infrastructure (§ 800.211(b)).
- **"Foreign person"** includes any foreign national, government or entity, and any entity controlled by one (§ 800.224). A U.S.-managed venture fund with foreign limited partners is usually not a foreign person; a fund whose general partner is foreign usually is. The fund exception in § 800.307 lets passive foreign limited partners invest through a U.S.-controlled fund without making the fund's investment covered, subject to conditions.
- **Mandatory declarations.** Required for (a) covered transactions in which a foreign government has a "substantial interest" in the acquirer, and (b) covered transactions in a TID U.S. business that deals in critical technologies for which a U.S. export authorization would be required for the foreign investor (§ 800.401(b), (c)), subject to exceptions (including certain investment funds managed by U.S. general partners, § 800.401(d)). File at least 30 days before completion (§ 800.401(g)).
- **Drafting.** (1) Ask each Purchaser whether it is a foreign person; (2) decide whether the Company is a TID U.S. business (export classification of its technology is the key question); (3) withhold board seats, observer rights, nomination rights, technical information access and decision rights ("triggering rights") from foreign persons unless the Board approves after analysis; (4) if a declaration is mandatory, make clearance a closing condition and plan for the 30-day lead time.

> **Verify:** CFIUS penalty amounts and declaration procedures were amended in 2024; confirm the current penalty provisions in 31 C.F.R. Part 800 Subpart I before advising on the consequences of a missed filing.

### 20.2 Outbound Investment Security Program (31 C.F.R. Part 850)

- **What it regulates.** Since January 2, 2025, U.S. persons are prohibited from, or must notify Treasury of, "covered transactions" with "covered foreign persons": persons of a country of concern (currently China, including Hong Kong and Macau) engaged in specified activities in semiconductors and microelectronics, quantum information technologies, or artificial intelligence (31 C.F.R. §§ 850.209, 850.210). Covered transactions include equity acquisitions, certain convertible and debt investments, greenfield investments, joint ventures and some fund LP investments.
- **Why it matters to a U.S. startup.** (a) A U.S. company can itself be a "covered foreign person" if it holds a board seat, equity or control in a covered foreign person and derives more than 50% of its revenue, net income, capital expenditure or operating expenses from such persons (§ 850.209(a)(2)); U.S. investors in it would then be making covered transactions. (b) The Company is a U.S. person and may not make prohibited investments abroad (for example, forming a Chinese subsidiary to do covered AI work), and its U.S.-person officers may not knowingly direct such transactions. (c) Investors therefore ask for representations and covenants; NVCA's October 2025 SPA added two-way outbound representations, according to Foley's summary.
- **Exceptions** include investments in publicly traded securities and limited partner investments of $2,000,000 or less or with binding contractual assurances (§ 850.501(a)).
- **Change coming.** The COINS Act (enacted in the FY 2026 National Defense Authorization Act, signed December 18, 2025) codified and expanded the program. Treasury issued a proposed rule on October 22, 2026 (91 Fed. Reg. 67396 (Oct. 26, 2026)) that would replace Part 850 with a new Part 851 going forward (Part 850 would continue to govern activity before the final rule's effective date); practitioner summaries report that it would prohibit (rather than merely require notice of) covered AI transactions and add biotechnology. Comments are due December 7, 2026; Part 850 applies until a final rule takes effect.
- **Data security.** The Department of Justice's rule on access to bulk U.S. sensitive personal data and government-related data (28 C.F.R. Part 202) treats some investment agreements with "covered persons" as restricted transactions; NVCA's 2025 SPA added representations on it.

> **Verify:** Track the Part 851 rulemaking (Docket TREAS-DO-2026-0595) and any final rule's effective date and sector list, and confirm the current scope and compliance dates of 28 C.F.R. Part 202, before giving advice on outbound or data-security points.

---

## 21. QSBS: representations and covenants (26 U.S.C. § 1202)

**The rules that matter in a financing.**

| Requirement | Rule | Pin cite |
|---|---|---|
| Issuer | Domestic C-corporation at issuance and during substantially all of the holding period | § 1202(c)(1), (c)(2), (e)(1) |
| Original issuance | Acquired at original issuance for money, property (other than stock) or services | § 1202(c)(1)(B) |
| Gross assets | Aggregate gross assets (cash plus adjusted basis of property) of $75,000,000 or less at all times before, and immediately after, the issuance (counting the round's proceeds); $50,000,000 for stock issued on or before July 4, 2025; indexed for inflation for taxable years beginning after 2026 | § 1202(d)(1) |
| Active business | At least 80% of assets (by value) used in a qualified trade or business; excluded fields include health, law, engineering, architecture, accounting, consulting, financial services, and businesses whose principal asset is employees' reputation or skill | § 1202(c)(2), (e)(1), (e)(3) |
| Exclusion | For stock issued after July 4, 2025: 50% after 3 years, 75% after 4 years, 100% after 5 years; for earlier stock, held more than 5 years | § 1202(a)(1), (a)(5) |
| Per-issuer cap | Greater of $15,000,000 ($10,000,000 for earlier stock), reduced by prior gains, or 10 times aggregate adjusted basis | § 1202(b) |
| Redemptions | Purchases from the holder or related persons within 2 years before or after issuance disqualify that holder's stock; purchases exceeding 5% of total stock value within 1 year before or after issuance disqualify the round | § 1202(c)(3)(A), (B); Treas. Reg. § 1.1202-2 (de minimis and termination-of-service exceptions) |

**Term sheet and documents.**

- *Company representation (SPA).* That the Company is a domestic C-corporation, its aggregate gross assets have not exceeded the threshold, and to its knowledge the shares will be QSBS when issued. Avoid a flat promise that the stock "is" QSBS: holder-level facts (holding period, related-party redemptions, the holder's own basis) are outside the Company's control.
- *Covenant (IRA, optional).* Commercially reasonable efforts to maintain qualification; deliver a QSBS information statement or answer reasonable questions; not knowingly cause a disqualifying redemption. Survive only as an information obligation after a sale.
- *Redemption traps in the round.* Using proceeds to repurchase founder or employee shares, or a Company-funded secondary, can disqualify the whole round under § 1202(c)(3)(B) if it exceeds the 5% threshold. Structure secondaries as investor purchases directly from the selling holder.
- *State tax.* Some states do not follow § 1202 (California is the leading example); tell California-resident founders.

> **Verify:** Confirm the current de minimis and termination-of-service exceptions in Treas. Reg. § 1.1202-2 and any guidance issued under the 2025 amendments before advising on a specific repurchase.

---

## 22. Insider rounds and § 144 safe harbors

When existing investors with board designees lead or join a round, the financing is a transaction in which directors have a material interest (and, if the investors control the board or vote together under an agreement, may be a controlling stockholder transaction). Section 144 was rewritten by the 2025 amendments (85 Del. Laws c. 6, enacted March 2025), which apply to past and future transactions except in litigation commenced on or before February 17, 2025; the Delaware Supreme Court upheld them in *Rutledge v. Clearway Energy Group LLC* (Del. Feb. 27, 2026).

| Transaction type | Safe harbor (any one, unless stated) | Statutory source |
|---|---|---|
| Director or officer interest (no controller) | (1) Approval in good faith, without gross negligence, by a majority of the disinterested directors (even if less than a quorum), after disclosure of material facts; if a majority of the board is not disinterested, approval or recommendation by a committee of at least two disinterested directors; (2) informed, uncoerced approval by a majority of votes cast by disinterested stockholders; or (3) fairness | § 144(a) |
| Controlling stockholder or control group (not going private) | (1) Approval or recommendation by a committee of at least two disinterested directors with authority to negotiate and reject; (2) conditioned at the outset on, and approved by, a majority of votes cast by disinterested stockholders; or (3) fairness | § 144(b) |
| Going-private transaction | Both (1) and (2) above, or fairness | § 144(c) |

Definitions (§ 144(e)): a "controlling stockholder" holds a majority of voting power, has a contractual or other right to elect a board majority, or holds at least one-third of voting power plus managerial authority; a "control group" is two or more non-controlling persons that become controlling together through an agreement. A director's designation by an interested party is not, by itself, evidence that the director is interested (§ 144(d)(3)). A controlling stockholder is liable for money damages only for loyalty breaches, bad faith or improper personal benefit (§ 144(d)(5)).

Practice in a venture round:

1. Identify interested directors (designees of participating funds; founders participating or receiving secondary proceeds).
2. Disclose the material facts in the board consent, and have the disinterested directors approve (or form a committee of at least two disinterested directors).
3. If no disinterested directors exist, use the disinterested-stockholder vote, or demonstrate fairness: a market check (outside investor interest or a lead from outside the cap table), a rights offering to all holders on the same terms, and a reasoned view on price.
4. Pay attention to pay-to-play and anti-dilution waivers that benefit insiders differently from outsiders.
5. *Carsanaro v. Bloodhound Technologies, Inc.*, 65 A.3d 618 (Del. Ch. 2013), allowed direct claims against investor-designated directors who approved a series of dilutive insider financings (the direct-standing holding rested on *Gentile v. Rossette*, 906 A.2d 91 (Del. 2006), which *Brookfield Asset Management, Inc. v. Rosson*, 261 A.3d 1251 (Del. 2021), overruled, so such dilution claims are now generally derivative only; the entire-fairness analysis still applies); *In re Nine Systems Corp. Shareholders Litigation*, C.A. No. 3940-VCN (Del. Ch. Sept. 4, 2014), *aff'd sub nom. Fuchs v. Wren Holdings, LLC*, 129 A.3d 882 (Del. 2015) (table), found an insider recapitalization unfair because of its process even though the price was fair, awarding no damages but exposing the directors to years of litigation and a fee award.

---

## 23. Fiduciary issues for VC-backed boards

- ***Trados.*** In *In re Trados Inc. Shareholder Litigation*, 73 A.3d 17 (Del. Ch. 2013), a sale for about $60 million went almost entirely to the Preferred (whose preferences of roughly $58 million nearly equaled the price) and to management through a carve-out plan of roughly $8 million, leaving nothing for the Common. The court held that directors owe duties to the corporation for the benefit of the Common Stock as residual claimants, not to the Preferred's contractual preferences; that venture-designated directors facing a fund's liquidity needs could be conflicted; and that entire fairness applied. The directors won only because the Common had no realistic value as a going concern. Lessons: document why a sale beats continuing; use disinterested directors or a committee where possible; get a fairness view; and make management carve-outs explicit and approved.
- **Preferred contract rights are contracts.** Directors honor the Preferred's charter and contractual rights but need not expand them; where preferred and common diverge, the board's duty runs to the common (*Trados*; *Frederick Hsu Living Trust v. ODN Holding Corp.*, 2017).
- **Blocking rights can make an investor a controller.** In *Basho Technologies Holdco B, LLC v. Georgetown Basho Investors, LLC*, 2018 WL 3326693 (Del. Ch. July 6, 2018), an investor that used contractual consent rights to starve a company of alternatives and force a deal was found to be a controller and liable. Investors should exercise vetoes in good faith; companies should negotiate the scope of vetoes in light of that risk.
- **Exculpation.** Directors are exculpated from monetary liability for duty-of-care breaches if the charter so provides (§ 102(b)(7)); since 2022, officers may be exculpated for direct claims only. Loyalty claims, including those arising from conflicted financings and sales, are not exculpable.
- **Process tools.** Disinterested-director approval or a committee under § 144; independent valuation for insider rounds; a rights offering; a record of alternatives considered; minutes that reflect the common stockholders' perspective in any sale where preferences absorb most of the price.

> **Verify:** The following case citations were taken from secondary sources and should be checked against Westlaw, Lexis or the court's opinion before they appear in client work: *West Palm Beach Firefighters' Pension Fund v. Moelis & Co.*, 311 A.3d 809 (Del. Ch. 2024) and the January 20, 2026 Supreme Court reversal (2026 WL 184868, as cited by later Delaware opinions; A.3d cite not yet confirmed); *Rutledge v. Clearway Energy Group LLC* (Del. Feb. 27, 2026) (one secondary source lists 360 A.3d 1271; not yet confirmed); *New Enterprise Associates 14, L.P. v. Rich*, 295 A.3d 520 (Del. Ch. 2023); *Basho Technologies Holdco B, LLC v. Georgetown Basho Investors, LLC*, 2018 WL 3326693; *Benchmark Capital Partners IV, L.P. v. Vague*, 2002 WL 1732423; the *Nine Systems* affirmance; and the *Trados* dollar figures in this section.

---

## 24. Negotiation cheat sheet

Identify the client's side before using this table. "Market" means the position most often seen in U.S. seed and Series A rounds in 2025–2026, based on the data in Section 18 and practitioner experience; where no survey figure exists, treat it as judgment.

| Term | Company-favorable | Market | Investor-favorable | Talking point |
|---|---|---|---|---|
| Pre-money share count | Excludes pool increase and SAFE conversion shares | Includes both | Includes both plus a large pool | Show the effective pre-money (Section 2.3, Step 5) |
| Option pool | Sized to a hiring plan; in the post-money | 10%–15% available post-closing, in the pre-money | 20%+ in the pre-money | Trade pool size for price |
| SAFE treatment | Shadow series; conversion shares outside the pre-money | Shadow series; conversion shares in the pre-money | Standard series for SAFEs (preference overhang) | Post-money SAFE requires a shadow series |
| Liquidation multiple | 1x | 1x | Above 1x | Over 95% of deals are 1x (Cooley Q2 2026) |
| Participation | None | None | Full | Run the waterfall at three exit values |
| Seniority | Pari passu | Pari passu at seed/A | Senior to earlier series | Seniority invites the next investor to ask for the same |
| Dividends | None | None or non-cumulative | Cumulative 8% | Cumulative dividends are a hidden multiple |
| Anti-dilution | Broad-based with pool | Broad-based weighted average | Full ratchet | 98% broad-based (Wilson Sonsini 1H 2026) |
| Pay-to-play | None | None at seed/A | Conversion to Common | Mostly a down-round tool |
| Redemption | None | None | Put after 5 years | Legally constrained by § 160 |
| Requisite Preferred Holders | Majority | Majority, or a figure that captures the lead | Supermajority that creates single-investor vetoes | Test the threshold against future rounds |
| Protective provisions | Series Seed list | Standard list with debt and subsidiary items | Pool, budget, hiring and series vetoes | Put director approvals in the charter or keep them short |
| QPO floor | None | 1x–2x latest price; $50M+ proceeds | 3x+ latest price | Each series' floor can block an IPO |
| Board (Series A) | Common majority | 2 Common, 2 Series, 1 Independent; or 2–1 | Series majority | Watch § 144(e) control |
| Independent Director | Chosen by Common Directors | Mutually agreed | Chosen by Series Directors | Set a deadline to fill the seat |
| Drag-along trigger | Board + Preferred + Key Holder Common | Board + Requisite Preferred Holders | Preferred alone | Add a price floor if founders must concede the trigger |
| Drag-along protections | Full list (Section 9.3) | Full list | Joint liability; covenants from all | Manti waiver only for counseled holders |
| Major Investor threshold | High | Set so the lead and serious co-investors qualify | Low or all Investors | Reconcile SAFE side letters |
| Pro rata | Major Investors; fully diluted basis; no over-allotment | Major Investors; fully diluted basis; over-allotment | All Investors; super pro rata | Super pro rata limited by amount and round |
| Information rights | Annual and quarterly; audit only on request | Annual (audit if required), quarterly, budget | Monthly; audited always | Competitor exclusion |
| Registration rights | 1 demand; $20M minimum; 5 years | 2 demands; $20M; earlier of 5 years or 180 days after IPO | 3+ demands; 3 years | Rarely used; do not overspend time |
| Observer | None | Lead only, with confidentiality and exclusions | Several | Foreign persons need CFIUS review |
| Series Director approvals | None | Short list or none | Long list requiring all Series Directors | § 122(18); § 220 visibility |
| Founder vesting | Existing schedule continues | Existing schedule; partial re-vest with credit if little vested | Full re-vest; new cliff | Credit for time served |
| Acceleration | Double-trigger 100% | Double-trigger 25%–100% | None | Buyers dislike single-trigger |
| Exclusivity | 30 days; financing only; fiduciary out | 30–45 days | 60+ days; sale no-shop; report offers | Keep it short |
| Investor counsel fees | Low cap; only on closing | Capped; paid at closing | Uncapped; paid if the deal fails | Seed: flat fee |
| Closing conditions | No diligence out | Diligence condition until signing | Broad conditions to each closing | Close diligence before definitive documents |
| QSBS | Representation to knowledge | Representation plus information covenant | Covenant to qualify | Company cannot guarantee holder-level tests |
| CFIUS / outbound | Investors bear their own regulatory risk | Two-way representations; no triggering rights for foreign persons without Board approval | Company covenants to monitor and remedy | Analyze before granting board or observer rights |

---

## Sources

Primary law (consulted November 2, 2026):

- Delaware Code, Title 8, ch. 1 (DGCL), §§ 102, 103, 115, 122(17)–(18), 141, 144, 151, 152, 160, 170, 173, 174, 202, 212, 213, 218, 220, 223, 228, 242, 245, 251, 262: https://delcode.delaware.gov/title8/c001/index.html (official text of §§ 122(18), 141(f) and 144 reviewed directly).
- Richards, Layton & Finger, "2026 Amendments to the Delaware General Corporation Law" (July 22, 2026) (§ 242(d) clarification effective August 1, 2026; *Salama v. Simon*): https://www.rlf.com/2026-amendments-to-the-delaware-general-corporation-law/
- 26 U.S.C. § 1202, with Pub. L. 119-21 § 70431 amendment notes (Cornell LII): https://www.law.cornell.edu/uscode/text/26/1202
- 31 C.F.R. §§ 800.211, 800.224, 800.248, 800.307, 800.401 and §§ 850.209, 850.210, 850.501 (eCFR versioner API, text as of October 1, 2026): https://www.ecfr.gov/current/title-31/subtitle-B/chapter-VIII
- 17 C.F.R. §§ 230.501–230.506 (Regulation D); see [securities-law.md](securities-law.md) for Form D and blue-sky sources.

Courts and legislation (secondary sources used for subsequent history):

- Debevoise & Plimpton, "Delaware Supreme Court Reverses Court of Chancery's Ruling in Moelis" (Jan. 2026): https://www.debevoise.com/insights/publications/2026/01/delaware-supreme-court-reverses-court-of-chancerys
- Akin Gump, "Delaware Supreme Court Upholds SB 21, Confirming Statutory Safe Harbors for Controller Transactions" (2026) (*Rutledge v. Clearway Energy Group LLC*): https://www.akingump.com/en/insights/alerts/delaware-supreme-court-upholds-sb-21-confirming-statutory-safe-harbors-for-controller-transactions
- Skadden, "Waiver of Appraisal Rights Upheld by Split Delaware Supreme Court" (Dec. 2021) (*Manti*): https://www.skadden.com/insights/publications/2021/12/insights-the-delaware-edition/waiver-of-appraisal-rights
- Richards, Layton & Finger, *Carsanaro v. Bloodhound Technologies* summary: https://www.rlf.com/carsanaro-v-bloodhound-technologies-inc-court-of-chancery-allows-plaintiffs-challenge-to-venture-capital-preferred-financings-to-proceed/
- Morris Nichols, *In re Nine Systems* summary: https://www.morrisnichols.com/insights-court-of-chancery-finds-breach-of-fiduciary-duty-in-private-company-recapitalization-based-on-inadequate-process-despite-fair-price
- Jenner & Block, "Treasury Proposes Expanded Outbound Investment Restrictions Under the COINS Act" (Oct. 2026): https://www.jenner.com/en/news-insights/client-alerts/treasury-proposes-expanded-outbound-investment-restrictions-under-the-coins-act
- WilmerHale, "2026 HSR Threshold" (Jan. 21, 2026): https://www.wilmerhale.com/en/insights/client-alerts/20260121-2026-hsr-threshold

Market data:

- Cooley, "Q2 2026 Venture Financing Report" (Aug. 17, 2026): https://www.cooley.com/news/insight/2026/2026-08-17-q2-2026-venture-financing-report
- Wilson Sonsini, "The Entrepreneurs Report: Private Company Financing Trends, Q2 2026" (PDF; valuation charts and 1H 2026 deal-terms appendix): https://www.wsgr.com/a/web/ntbxCfmspTLoevehaAoUgh/entrepreneurs-report-q2-2026.pdf
- Fenwick, "Q1 2026 Venture Beacon: Key VC Market Trends" (June 29, 2026): https://www.fenwick.com/insights/publications/q1-2026-venture-beacon-key-vc-market-trends
- Carta State of Private Markets (not retrievable for this update; see the Verify note in Section 18): https://carta.com/data/

Model documents (coverage and market terms only; no text copied):

- NVCA Model Legal Documents (charter, SPA, IRA, Voting Agreement, ROFR/co-sale updated October 2, 2025): https://nvca.org/model-legal-documents/
- Foley & Lardner, "Breaking Down the October 2, 2025 NVCA Updates": https://www.foley.com/insights/publications/2025/10/breaking-down-the-nvca-what-founders-and-vcs-need-to-know/
- Series Seed documents, v3.2 (CC0 1.0): https://github.com/seriesseed/equity
- Y Combinator, SAFE documents and standard deal: https://www.ycombinator.com/documents and https://www.ycombinator.com/deal

# Convertible Instruments: SAFEs and Convertible Notes

Expert reference for Claude when structuring, drafting, or modeling pre-priced-round financings of a Delaware C-corporation. Read with [securities-law.md](securities-law.md) (exemptions and filings), [templates/convertible-financing/safe-guide.md](../templates/convertible-financing/safe-guide.md) (completing the YC forms), and the note templates in the same folder. Every numeric example here is reproduced by `python3 scripts/conversion_calculator.py --example N`, and `--selftest` asserts the published figures.

**Last verified:** November 2, 2026. Market data carries its own date; refresh it before quoting it to a client.

---

## 1. The instrument map

| Instrument | What the investor holds | Converts when | Downside protection | Typical use |
|---|---|---|---|---|
| **Post-money SAFE, valuation cap** (YC standard since 2018) | Contract right to future preferred stock; not debt, no interest, no maturity | Automatically at the initial closing of an Equity Financing (any bona fide priced preferred round; no minimum size) | Purchase Amount back in a Liquidity Event (if greater than as-converted value) or Dissolution Event, junior to creditors, on par with other SAFEs and preferred | Pre-seed and seed; the default |
| **Post-money SAFE, discount only** | Same | Same; price = round price × (1 − discount) | Same; Liquidity Event as-converted value is computed at fair market value × Discount Rate | Very early or bridge investors where no one will set a cap |
| **Uncapped MFN SAFE** | Same | Same; converts at the round price unless amended to match a later, better SAFE | Purchase Amount back in a Liquidity Event or Dissolution Event | Friends-and-family or first check before terms are set |
| **Pre-money SAFE** (YC original, 2013–2018; no longer offered) | Same | Same | Same in substance | Legacy; still found on cap tables |
| **Convertible promissory note** | Debt: principal plus interest, with a maturity date | Automatically in a Qualified Financing (minimum size); optional at maturity; holder election on a change of control | Creditor; repayment at maturity or on change of control (often with a premium); senior to all equity in insolvency | Bridges, insider rounds, institutional seed where investors want creditor status, non-U.S. investor preferences |
| **Priced Series Seed / Series A** | Preferred stock now | n/a | Liquidation preference, protective provisions, information rights | When valuation can be set and the round is large enough to justify the cost |

**Choosing.** Section 12 contains the decision table. The short version: use a post-money valuation-cap SAFE unless (a) investors insist on creditor status or a maturity, (b) the company already has notes outstanding (do not mix without modeling and consent), or (c) the round is large and led by an institution that wants governance now, in which case use a priced Series Seed (the Series Seed forms are CC0 and may be adapted) or NVCA-based documents.

---

## 2. Vocabulary that causes mistakes

- **"Discount" versus YC's "Discount Rate."** A "20% discount" means the holder pays 80% of the round price. YC's forms define **Discount Rate** as 100 minus the discount, so a 20% discount is written as a Discount Rate of **80%**. The skill's shared variable `discount_rate` must always say which (e.g., "20% discount" or "80% Discount Rate"). Never write "Discount Rate: 20%" in a YC SAFE; that would give the investor an 80% discount.
- **Pre-money versus post-money cap.** A post-money cap values the company *after* all SAFE money (and other converting securities) but *before* the priced round's new money and before any option-pool increase made in that round. A pre-money cap values the company before the SAFE money. The same number means very different ownership.
- **"Fully diluted."** Never use it without a definition. Each instrument defines its own denominator (Company Capitalization in the post-money SAFE; a different Company Capitalization in the pre-money SAFE; whatever the note says for its cap). The priced round's term sheet defines a fourth (the pre-money fully diluted share count used to set the price per share).
- **Standard Preferred Stock / Safe Preferred Stock.** In the YC forms, Standard Preferred Stock is the series sold to new-money investors at the initial closing; Safe Preferred Stock is a series identical to it except that price-based terms (per-share liquidation amount, initial conversion price, per-share dividend) are based on the SAFE's conversion price. Practitioners call the latter a **shadow series** or **sub-series** (e.g., "Series A-1 Preferred Stock").

---

## 3. Post-money SAFE mechanics (YC form, U.S., valuation cap version 1.2)

This section paraphrases the operative definitions so Claude can model them. Do not paste YC text into any document; link to the official forms (see the SAFE guide).

### 3.1 Conversion in an Equity Financing

An **Equity Financing** is a bona fide capital-raising transaction in which the company sells preferred stock at a fixed pre- or post-money valuation. On its initial closing the SAFE converts automatically into the **greater number of shares** of:

1. Standard Preferred Stock at the lowest price per share paid by new-money investors (*P*), or
2. Safe Preferred Stock at the **Safe Price** = Post-Money Valuation Cap ÷ **Company Capitalization**.

Equivalently, the conversion price is min(*P*, Cap ÷ CC), and the SAFE receives Safe Preferred Stock only if the cap gives a lower price.

### 3.2 Company Capitalization (the denominator)

Measured immediately before the Equity Financing, on an as-converted-to-common basis, without double counting:

| Included | Excluded |
|---|---|
| All issued and outstanding capital stock (common, including unvested restricted stock; existing preferred as converted) | The option-pool **increase** adopted in connection with the Equity Financing, except to the extent Promised Options exceed the pre-increase unissued pool |
| **All Converting Securities**: this SAFE, every other SAFE (pre- or post-money, capped or not), convertible notes, and other convertible securities, each as converted | New-money shares in the Equity Financing |
| All issued and outstanding Options (options, RSUs, restricted stock awards, SARs, warrants and similar, vested or unvested) | |
| **Promised Options** (promised but ungranted, measured as of the term sheet) | |
| The **Unissued Option Pool** existing before the round | |

Two consequences follow:

- **Ownership is fixed at signing.** Because every SAFE (including this one) is in the denominator, a SAFE whose cap applies owns exactly Purchase Amount ÷ Cap of Company Capitalization. A $1,000,000 SAFE at a $10,000,000 post-money cap owns 10% of Company Capitalization, no matter how many other SAFEs are later sold. Additional SAFEs dilute founders, not earlier post-money SAFE holders.
- **Algebra for k post-money SAFEs that all convert at their caps.** Let *F* = outstanding stock + Options + Promised Options + pre-increase Unissued Pool, and *X* = conversion shares of all other converting securities (notes, discount-only SAFEs, pre-money SAFEs). Then

  CC = (F + X) ÷ (1 − Σ PurchaseAmountᵢ ÷ Capᵢ), and SAFE *i* receives (PurchaseAmountᵢ ÷ Capᵢ) × CC shares at price Capᵢ ÷ CC.

  Because *X* depends on the round price and the round price depends on CC (if conversions are in the pre-money), the full problem is circular; the calculator iterates (Section 7).

### 3.3 Liquidity Event (Change of Control, Direct Listing, or IPO) before conversion

The holder receives the **greater** of:

- the **Cash-Out Amount** (its Purchase Amount), or
- the **Conversion Amount**: what it would receive on Purchase Amount ÷ **Liquidity Price** shares of common, where Liquidity Price = Cap ÷ **Liquidity Capitalization**.

Liquidity Capitalization mirrors Company Capitalization, with two differences: it **excludes** the Unissued Option Pool (and includes Promised Options only to the extent they receive proceeds), and it excludes converting securities whose holders take a cash-out or liquidation preference rather than an as-converted payment. The board may reduce the cash portion paid to the holder (without reducing total proceeds, and pro rata with equal-priority holders) to preserve a tax-free reorganization. The holder gets the same consideration choice as other securityholders.

**Worked numbers (Example 1's SAFE, before any priced round).** Common 8,000,000; options 1,000,000 (assume all receive proceeds); unissued pool 1,000,000 (excluded). The SAFE converts as common: LC = 9,000,000 + SAFE shares, SAFE shares = 10% × LC, so LC = 10,000,000 and Liquidity Price = $1.00.

| Sale price for the whole company | As-converted (1,000,000 of 10,000,000 shares) | Cash-Out Amount | Holder receives |
|---|---|---|---|
| $50,000,000 | $5,000,000 | $1,000,000 | **$5,000,000** (as-converted) |
| $8,000,000 | $800,000 | $1,000,000 | **$1,000,000** (preference) |

(The illustration ignores option exercise prices and transaction expenses; a real waterfall must model both.)

### 3.4 Dissolution Event

A voluntary termination of operations, a general assignment for the benefit of creditors, or another liquidation, dissolution, or winding up (other than a Liquidity Event). The holder is entitled to its Purchase Amount out of proceeds legally available for distribution.

### 3.5 Priority in a Liquidity or Dissolution Event

The SAFE is designed to behave like standard **non-participating preferred**: its Cash-Out Amount is junior to indebtedness and creditor claims (including convertible notes not actually or notionally converted), on par with other SAFEs and preferred stock (pro rata if proceeds fall short), and senior to common. A Conversion Amount ranks with common and other as-converted holders.

### 3.6 Termination, amendment, transfer, rights

The SAFE terminates on issuance of stock in an Equity Financing or on payment (or setting aside) of amounts due in a Liquidity or Dissolution Event. It may be amended by the company and either the holder or a majority-in-interest of all outstanding SAFEs with the same cap and discount, provided the Purchase Amount cannot be changed that way, every holder's consent is solicited, and all holders are treated alike. Transfers require company consent except to affiliates and on death or disability. The holder has no stockholder rights before conversion. The form states the parties' intent to treat the SAFE as stock (specifically common stock for I.R.C. §§ 304, 305, 306, 354, 368, 1036 and 1202) for income tax purposes (see Section 10).

---

## 4. Pre-money SAFE mechanics (legacy)

The original SAFE (2013–2018) defined Company Capitalization as all issued stock and all outstanding options, warrants, and other convertible securities as converted, **excluding** this SAFE, all other SAFEs, and convertible notes, **plus** all shares reserved and available under the equity plan **including any increase made in connection with the Equity Financing**. The conversion price was the lower of the "Safe Price" (pre-money cap ÷ that capitalization) and, if the form had one, the discount price.

Consequences:

- The SAFE holder's ownership is **not** known at signing. Each additional pre-money SAFE dilutes earlier SAFE holders along with founders.
- The pool increase is in the denominator, so pre-money SAFE holders are **protected** from the round's pool top-up (the founders bear it). Post-money SAFE holders are not: the increase is outside Company Capitalization.
- The original form also contained an embedded pro rata right (in the round after conversion), which YC replaced with the side letter.

**When you meet one.** Model each pre-money SAFE under its own definition. YC's user guide notes it is possible but cumbersome to mix pre- and post-money SAFEs; if only a few are outstanding, consider amending and restating them into post-money SAFEs with board approval and holder consent.

---

## 5. Convertible note mechanics

### 5.1 Conversion amount

Converting amount = outstanding principal + accrued unpaid interest (unless the note pays interest in cash at conversion). The skill's note template uses **simple, non-compounding interest computed on actual days elapsed over a 365-day year**; the calculator uses the same convention.

Interest = Principal × rate × days ÷ 365, rounded to the cent.

### 5.2 Automatic conversion in a Qualified Financing

A **Qualified Financing** is the next bona fide preferred-stock financing raising at least a stated minimum of new money (excluding note conversions); typical minimums run from roughly the aggregate note principal up to several million dollars. The note converts at the **Conversion Price** = the lower of:

- **Discount Price** = price paid by new-money investors × (1 − discount); and
- **Cap Price** = Valuation Cap ÷ **Cap Capitalization**.

Shares = converting amount ÷ Conversion Price, rounded down.

### 5.3 The cap denominator is a negotiated term

Unlike the YC SAFE, a note has no standard definition. Draft one of these, expressly:

| Basis (calculator `cap_basis`) | Denominator | Who it favors |
|---|---|---|
| `pre_money_excluding_new_pool` | Outstanding stock + options + existing unissued pool; excludes the round's pool increase and all converting securities | Company (largest cap price, fewest shares) |
| `pre_money_including_new_pool` | The above + the round's pool increase | Holder (shields the holder from the pool top-up) |
| `fully_diluted_including_converting` | The above + pool increase + all notes and SAFEs as converted | Holder (most shares); behaves like a post-money cap measured after the pool increase |
| `post_money` | YC-style: existing pool only, plus all converting securities | Mirrors a post-money SAFE; use when notes and post-money SAFEs sit side by side |

Example 5 versus 5B (Section 6) shows the difference: the same $12,000,000 cap converts at $1.2000 under the company-favorable basis and $1.1470 under the holder-favorable basis.

### 5.4 Maturity, change of control, prepayment, default

- **Maturity** (typically 12–24 months; extensions by majority-in-interest are common): repayment, optional conversion at the cap into common or a shadow preferred series, or both at the holder's election. Many forms make conversion at maturity automatic unless a majority elects repayment, because startups rarely can repay.
- **Change of control before conversion:** the holder elects repayment of principal and interest plus a premium (commonly 1× to 2× principal) or conversion at the cap into common immediately before the closing.
- **Prepayment:** prohibited without majority-in-interest consent (otherwise the company could retire notes before an upside event).
- **Events of default:** non-payment, insolvency events, and sometimes covenant breaches; acceleration usually requires a majority-in-interest.
- **Subordination:** optional; lenders (venture debt, banks) often require note subordination.

### 5.5 Liquidation preference "overhang" and how notes convert into shadow series

If a note converts at a $1.20 cap price into Series A Preferred priced at $2.2985, and each share carries a $2.2985 liquidation preference, the noteholder's preference becomes roughly 1.9× its money. Three fixes, which the priced-round charter must implement:

1. **Shadow series (preferred approach for SAFEs, increasingly for notes):** issue a sub-series (e.g., Series A-1) whose Original Issue Price equals the conversion price, so the 1× preference equals the converting amount.
2. **Split issuance:** issue Series A Preferred equal to converting amount ÷ round price and common stock for the balance of the conversion shares.
3. **Accept the overhang** (rare; investor-favorable; disclose to the new lead).

---

## 6. Worked examples

All examples use **Northwind Robotics, Inc.** Unless noted, the pre-round capitalization is 8,000,000 common, 1,000,000 options outstanding, and a 1,000,000-share unallocated pool (*F* = 10,000,000). Conversion securities are in the pre-money (the market default). Rounding: prices to 4 decimals half-up; issued shares rounded down; pool increase rounded up (Section 7.3).

### Example 1: One post-money SAFE (`--example 1`)

SAFE: $1,000,000, $10,000,000 post-money cap. Series A: $30,000,000 pre-money, $7,500,000 new money, no pool top-up.

1. CC = 10,000,000 ÷ (1 − 0.10) = 11,111,111.11. Safe Price = $10,000,000 ÷ 11,111,111.11 = **$0.9000**.
2. Pre-money FD shares = 10,000,000 + 1,111,111.11 = 11,111,111.11; *P* = $30,000,000 ÷ 11,111,111.11 = **$2.7000**.
3. Safe Price < *P*, so the SAFE converts into Safe Preferred (Series A-1): 1,000,000 ÷ 0.9000 = **1,111,111** shares.
4. New money: 7,500,000 ÷ 2.7000 = **2,777,777** shares of Series A.

| Holder | Class | Shares | FD % |
|---|---|---|---|
| Common | Common | 8,000,000 | 57.6000% |
| Options outstanding | Common (underlying) | 1,000,000 | 7.2000% |
| Unallocated pool | Common (reserved) | 1,000,000 | 7.2000% |
| SAFE holder | Series A-1 | 1,111,111 | 8.0000% |
| New investors | Series A | 2,777,777 | 20.0000% |
| **Total** | | **13,888,888** | 100% |

The SAFE owned 10% of Company Capitalization; the 20% sold in the round dilutes it to 8%. **Shadow series effect:** 1,111,111 Series A-1 shares × $0.90 = $999,999.90 of 1× preference. Had the SAFE received standard Series A ($2.70 preference per share), its preference would have been $3,000,000 (3× its money). See Section 8.

### Example 2: Three post-money SAFEs with different caps (`--example 2`)

| SAFE | Purchase Amount | Post-money cap | Ownership of CC (= amount ÷ cap) |
|---|---|---|---|
| A | $250,000 | $5,000,000 | 5.0% |
| B | $1,000,000 | $8,000,000 | 12.5% |
| C | $750,000 | $10,000,000 | 7.5% |
| Total | $2,000,000 | | 25.0% |

CC = 10,000,000 ÷ 0.75 = 13,333,333.33. Safe Prices: A $0.3750, B $0.6000, C $0.7500. Series A: $32,000,000 pre / $8,000,000 new → *P* = 32,000,000 ÷ 13,333,333.33 = **$2.4000**.

| Holder | Class | Shares | FD % |
|---|---|---|---|
| Common | Common | 8,000,000 | 48.0000% |
| Options outstanding | Common (underlying) | 1,000,000 | 6.0000% |
| Unallocated pool | Common (reserved) | 1,000,000 | 6.0000% |
| SAFE A | Series A-1 ($0.3750) | 666,666 | 4.0000% |
| SAFE B | Series A-2 ($0.6000) | 1,666,666 | 10.0000% |
| SAFE C | Series A-3 ($0.7500) | 1,000,000 | 6.0000% |
| New investors | Series A | 3,333,333 | 20.0000% |
| **Total** | | **16,666,665** | 100% |

Each SAFE's post-closing percentage is its pre-round percentage × 80%. Three different caps require **three shadow series**, each with its own Original Issue Price. The priced-round charter must authorize each.

### Example 3: Discount-only SAFE and a cap-and-discount SAFE (`--example 3`)

D1: $500,000, 20% discount, no cap (the YC discount form with a Discount Rate of 80%). D2: $500,000, $30,000,000 post-money cap and 20% discount (not a current YC U.S. form; included to show the "lesser of" test). Series A: $20,000,000 pre / $5,000,000 new.

Because both SAFEs convert at 0.8 × *P* and are in the pre-money, the pre-money share count is circular: S = 10,000,000 + 2 × 500,000 ÷ (0.8 × 20,000,000 ÷ S) → S = 10,000,000 × 16 ÷ 15 = 10,666,666.67. *P* = **$1.8750**; discount price = **$1.5000**. D2's cap price is 30,000,000 ÷ 10,666,666.67 = $2.8125, higher than the discount price, so the **discount governs** for both.

| Holder | Class | Shares | FD % |
|---|---|---|---|
| Common | Common | 8,000,000 | 60.0000% |
| Options outstanding | Common (underlying) | 1,000,000 | 7.5000% |
| Unallocated pool | Common (reserved) | 1,000,000 | 7.5000% |
| SAFE D1 | Series A-1 ($1.5000) | 333,333 | 2.4999% |
| SAFE D2 | Series A-1 ($1.5000) | 333,333 | 2.4999% |
| New investors | Series A | 2,666,666 | 19.9999% |
| **Total** | | **13,333,332** | 100% |

Note: discount SAFEs and notes are "Converting Securities" in a post-money SAFE's Company Capitalization, so they dilute neither each other's pre-round percentage nor a capped post-money SAFE's percentage, but they do dilute founders.

### Example 4: Two pre-money SAFEs versus post-money (`--example 4`)

Two pre-money SAFEs, each $1,000,000 at a $9,000,000 **pre-money** cap. Series A $30,000,000 pre / $7,500,000 new, no pool increase.

Pre-money SAFE capitalization excludes SAFEs: 10,000,000 shares; price = $9,000,000 ÷ 10,000,000 = **$0.9000**; each SAFE receives **1,111,111** shares. Pre-money FD = 12,222,222.22; *P* = $2.454545 → **$2.4545** (rounded); new investors 7,500,000 ÷ 2.4545 = **3,055,612**.

Compare the same two investors on $10,000,000 **post-money** caps (the "same" headline valuation): CC = 10,000,000 ÷ 0.80 = 12,500,000; each SAFE receives 1,250,000 shares; *P* = $2.4000.

| | Pre-money SAFEs ($9M pre) | Post-money SAFEs ($10M post) |
|---|---|---|
| Each SAFE's shares | 1,111,111 | 1,250,000 |
| Each SAFE post-closing FD % | 7.2727% | 8.0000% |
| Common post-closing FD % | 52.3634% | 51.2000% |
| Series A price | $2.4545 | $2.4000 |
| Total FD shares | 15,277,834 | 15,625,000 |

With one SAFE, a $9M pre-money cap and a $10M post-money cap give identical results. With two or more, pre-money SAFE holders dilute one another, and founders keep more. The post-money form trades that founder advantage for certainty. Note also the rounding artifact: rounding *P* down from $2.454545 to $2.4545 gives new investors 20.0002%.

### Example 5: Convertible note with interest, cap, and discount (`--example 5`)

Note: $500,000 principal, 6% simple interest, issued January 15, 2027; $12,000,000 cap on the **pre-money excluding new pool** basis; 20% discount. Series A closes January 15, 2028 (365 days): $24,000,000 pre / $6,000,000 new, no pool top-up.

1. Interest = $500,000 × 6% × 365 ÷ 365 = **$30,000.00**; converting amount **$530,000.00**.
2. Cap price = $12,000,000 ÷ 10,000,000 = **$1.2000**.
3. Pre-money FD = 10,000,000 + 530,000 ÷ 1.20 = 10,441,666.67; *P* = **$2.2985** (unrounded $2.29848364); discount price = $1.8388. Cap price is lower, so the **cap governs**.
4. Shares = 530,000 ÷ 1.2000 = **441,666**; new investors 6,000,000 ÷ 2.2985 = **2,610,398**.

| Holder | Class | Shares | FD % |
|---|---|---|---|
| Common | Common | 8,000,000 | 61.2930% |
| Options outstanding | Common (underlying) | 1,000,000 | 7.6616% |
| Unallocated pool | Common (reserved) | 1,000,000 | 7.6616% |
| Noteholder | Series A-1 ($1.2000) | 441,666 | 3.3839% |
| New investors | Series A | 2,610,398 | 19.9999% |
| **Total** | | **13,052,064** | 100% |

**Example 5B (`cap_basis: fully_diluted_including_converting`).** Same note; the cap denominator now includes the note's own conversion shares: shares = 530,000 × (10,000,000 + shares) ÷ 12,000,000 → 462,074.11 unrounded; cap price = **$1.1470**; shares **462,074**; *P* = **$2.2940**; new investors 2,615,518; total 13,077,592; noteholder 3.5333%. One definitional choice moved about 20,400 shares to the holder.

### Example 6: Post-money SAFEs plus an option-pool top-up in the pre-money (`--example 6`, the default)

Pre-round: 8,000,000 common; 1,000,000 options; **500,000** unallocated pool (*F* = 9,500,000). SAFEs: $1,000,000 at $10,000,000 post (10%) and $500,000 at $12,500,000 post (4%). Series A: $24,000,000 pre-money, $6,000,000 new money, **10% available pool post-closing**, pool increase **in the pre-money**.

Closed-form solution (which the calculator's iteration must match, and does, to 25 decimal places):

1. Company Capitalization excludes the pool increase: CC = 9,500,000 ÷ (1 − 0.14) = 11,046,511.63. Safe Prices: $10,000,000 ÷ CC = $0.90526316; $12,500,000 ÷ CC = $1.13157895.
2. Pre-money FD shares S = CC + ΔP (ΔP = pool increase). Post-closing total T = S × (post ÷ pre) = 1.25 S.
3. Pool condition: 500,000 + ΔP = 10% × 1.25 × (CC + ΔP) → ΔP = (0.125 × CC − 500,000) ÷ 0.875 = **1,006,644.52** → rounded up to **1,006,645**.
4. S = 12,053,156.15; *P* = 24,000,000 ÷ S = $1.99117971 → **$1.9912**.
5. Conversions at rounded prices: 1,000,000 ÷ 0.9053 = **1,104,606**; 500,000 ÷ 1.1316 = **441,852**. New money 6,000,000 ÷ 1.9912 = **3,013,258**.

| Holder | Class | Shares | FD % |
|---|---|---|---|
| Common | Common | 8,000,000 | 53.0984% |
| Options outstanding | Common (underlying) | 1,000,000 | 6.6373% |
| Unallocated pool (existing) | Common (reserved) | 500,000 | 3.3186% |
| Pool increase | Common (reserved) | 1,006,645 | 6.6814% |
| SAFE ($10M cap) | Series A-1 ($0.9053) | 1,104,606 | 7.3316% |
| SAFE ($12.5M cap) | Series A-2 ($1.1316) | 441,852 | 2.9327% |
| New investors | Series A | 3,013,258 | 19.9999% |
| **Total** | | **15,066,361** | 100% |

**Effective pre-money for existing holders.** The headline pre-money is $24,000,000, but at $1.9912 the pre-round common, options, and pool (9,500,000 shares) are worth $18,916,400. The pool increase ($2,004,432) and the SAFE conversion shares ($3,079,307) are paid for out of the pre-money. This "pool shuffle" is the main reason founders should negotiate the pool size against a hiring plan.

**Variants (same inputs):**

| Variant | *P* | Pool increase | New investors' FD % | Common FD % |
|---|---|---|---|---|
| Base case (pool in pre-money) | $1.9912 | 1,006,645 | 19.9999% | 53.0984% |
| Pool increase **outside** the pre-money (post-money pool) | $2.1726 | 978,683 | 18.6765% | 54.1022% |
| Same investors on **pre-money** SAFEs at $9M / $12M pre caps | $1.9799 | 1,015,213 | 20.0001% | 52.7977% |

In the pre-money-SAFE variant the SAFE prices fall to $0.8559 and $1.1412 because the pool increase is in their denominator: the founders absorb the SAFE holders' share of the pool dilution.

### Example 7: Uncapped MFN SAFE (`--example 7`)

An uncapped MFN SAFE ($250,000, February 1, 2027) is followed by a $750,000 SAFE at an $8,000,000 post-money cap (May 1, 2027). The MFN holder receives the MFN notice and elects to amend its SAFE to match. Both now own Purchase Amount ÷ $8,000,000 (3.125% and 9.375%; 12.5% combined). CC = 10,000,000 ÷ 0.875 = 11,428,571.43; Safe Price **$0.7000**; Series A ($30,000,000 pre / $7,500,000 new) prices at **$2.6250**.

| Holder | Class | Shares | FD % |
|---|---|---|---|
| Common | Common | 8,000,000 | 56.0000% |
| Options outstanding | Common (underlying) | 1,000,000 | 7.0000% |
| Unallocated pool | Common (reserved) | 1,000,000 | 7.0000% |
| MFN SAFE (as amended) | Series A-1 ($0.7000) | 357,142 | 2.4999% |
| Later SAFE | Series A-1 ($0.7000) | 1,071,428 | 7.4999% |
| New investors | Series A | 2,857,142 | 19.9999% |
| **Total** | | **14,285,712** | 100% |

Had the holder not elected (or had the later SAFE been issued after the Equity Financing), the MFN SAFE would have converted into Series A at $2.6250.

---

## 7. How the calculator solves the circularity

`scripts/conversion_calculator.py` reads a JSON description (pre-round capitalization; SAFEs with type, amount, cap, discount; notes with principal, rate, dates, cap and cap basis, discount; the new round's pre-money, new money, pool target and whether the pool increase and conversions are in the pre-money). It prints the price per share, each conversion price and share count, the pool increase, and a fully diluted cap table with liquidation preferences. `--json` gives machine-readable output.

### 7.1 The circular system

- The round price *P* = pre-money ÷ S, where S includes the pool increase (if in the pre-money) and conversion shares (if in the pre-money).
- Post-money SAFE prices depend on CC, which includes all conversion shares.
- Discount instruments depend on *P*.
- The pool increase depends on total post-closing shares, which depend on *P*.

### 7.2 Method

Fixed-point iteration on (pool increase, each instrument's conversion shares) in 60-digit decimal arithmetic, starting from zero and stopping when every quantity moves by less than 10⁻³⁰ shares; the pool increase is solved in closed form at each step given the other quantities. The map is a contraction whenever aggregate post-money SAFE ownership is below 100% and the pool target below 100%, so it converges in tens of iterations. The script then recomputes every defining equation and stops with an error if any residual exceeds 10⁻²⁰. Example 6's self-test checks the iteration against the closed form above.

### 7.3 Rounding convention (state it in the deal documents)

1. The round price and each conversion price are computed from the converged, unrounded capitalization and rounded to **four decimal places, half-up** (configurable to round down or up).
2. Each holder's shares = amount ÷ rounded price, **rounded down** to a whole share (cash in lieu of fractions is customary).
3. The pool increase is **rounded up**, so the post-closing pool is not below target.
4. Note interest is simple, actual/365, rounded to the cent before conversion.

The NVCA-style stock purchase agreement and charter should state the Original Issue Price of each series to four decimals, and the conversion mechanics in each convertible instrument should say that fractional shares are not issued.

---

## 8. Shadow series and the liquidation preference

**Why.** A SAFE or note converting at a cap price into standard preferred would carry a per-share liquidation preference equal to the round price, giving the holder a multiple of its money (3× in Example 1). The YC forms solve this by issuing **Safe Preferred Stock**, identical to the new-money series except that price-based terms run off the SAFE's conversion price.

**What the priced-round documents must do (coordinate with the priced-round templates):**

1. **Authorize sub-series in the amended and restated charter** (e.g., "Series A Preferred Stock," "Series A-1 Preferred Stock," "Series A-2 Preferred Stock"), each with its own **Original Issue Price** equal to the applicable conversion price, and enough authorized shares for each.
2. **Liquidation preference** of each sub-series = 1× its Original Issue Price (plus declared but unpaid dividends), ranking pari passu with standard Series A.
3. **Dividends and anti-dilution:** per-share dividend rate and initial Conversion Price of each sub-series = its own Original Issue Price; broad-based weighted-average anti-dilution adjustments apply series by series.
4. **Voting and protective provisions:** define "Series A Preferred" collectively to include all sub-series so they vote together; avoid giving each sub-series a separate class vote unless intended.
5. **Stock purchase agreement:** SAFE and note holders sign the SPA (or a joinder) and the investor agreements as purchasers of their sub-series, with limited representations, warranties, and indemnities (the YC form requires that the documents be the same as for new investors, with appropriate variations, and that drag-along obligations carry customary limits).
6. **Capitalization representation and pro forma cap table** list each sub-series, its Original Issue Price, and the converting instrument.

**Alternatives:** split issuance (preferred equal to the money at the round price plus common for the rest), or a single series with a charter clause capping each converted holder's preference at its converting amount. The shadow series is the market default for SAFEs; notes vary.

---

## 9. MFN and pro rata rights

### 9.1 MFN (YC uncapped MFN form, version 1.3)

- Applies to **Subsequent Convertible Securities** issued for capital-raising before the SAFE terminates (other SAFEs, notes, other convertibles). Excludes option-plan grants, convertible securities issued to lenders, lessors, suppliers and service providers, and convertible securities issued in strategic transactions, and excludes side letters and ancillary agreements that do not change the later instrument's terms.
- The company must promptly send an **MFN Notice** with a copy of the later instrument (and further information on request). If the holder notifies the company **within 10 days** that it prefers those terms, the company must amend and restate the MFN SAFE to be **identical** to the later instrument (other than Purchase Amount). There is no cherry-picking; after an election the MFN is usually gone (unless the later instrument also has one).
- YC's FAQ: the date that matters is the later of signing and receipt of funds, so close lower-cap SAFEs (fully funded) before issuing an uncapped MFN if those earlier terms should not be picked up.
- **Pitfalls:** forgetting to send MFN Notices (track them in the data room); issuing a side letter with economic rights (pro rata, information) that the YC MFN does not reach, which irritates MFN holders. A broader MFN, if negotiated, belongs in a side letter (see the skill's SAFE side letter).

### 9.2 Pro rata rights

- **YC pro rata side letter (version 1.0):** a right to buy the holder's pro rata share of the Standard Preferred Stock sold in the Equity Financing, where pro rata share = shares issued on conversion of the holder's post-money-cap SAFEs ÷ Company Capitalization. It terminates at the initial closing of the Equity Financing (so it covers that round only) or immediately before a Liquidity or Dissolution Event. It can be used only with SAFEs that have a post-money valuation cap.
- **Dilution budget (YC user guide approach):** the share of SAFEs that can carry pro rata rights without exceeding a target round size = 100% − (new investors' target % ÷ total round %). Example: SAFEs equal 20% of the company, the lead wants 25%, and the founders cap the Series A at 28% (before the pool) → 100% − 25/28 ≈ 10.7%: grant pro rata to SAFEs representing about half of the SAFE ownership.
- **Market practice:** reserve pro rata for checks above a threshold (often the same as the anticipated Major Investor threshold); require quick responses; for continuing rights in later rounds, rely on the priced round's Investors' Rights Agreement.

---

## 10. Tax treatment (flag for tax counsel)

### 10.1 SAFEs

There is no statute, regulation, or published IRS guidance specifically characterizing SAFEs. Three views:

| View | Basis | Consequences |
|---|---|---|
| **Equity (stock)** | YC form's stated intent; economics resemble non-participating preferred (no maturity, no interest, subordinated, residual upside) | Holding period starts at purchase; conversion is a stock-for-stock exchange; § 1202(f) treats stock acquired solely through conversion of other QSBS as QSBS with tacked holding period |
| **Prepaid forward contract / open transaction** | Holder has a contractual right to receive a variable number of shares later | No tax at purchase or conversion (likely), but the holder holds "property other than stock," so for § 1202 the stock is acquired on conversion |
| **Debt** | Rarely argued; SAFEs lack creditor remedies, a maturity, and interest | Imputed interest/OID; strongly disfavored |

**Section 1202 (QSBS) questions.**

- Stock issued after July 4, 2025 qualifies for the tiered exclusion added by P.L. 119-21 § 70431 (50% after 3 years, 75% after 4 years, 100% after 5 years), a per-issuer cap of the greater of $15,000,000 (indexed after 2026) or 10× basis, and a $75,000,000 aggregate gross assets limit (indexed).
- **Holding period.** If the SAFE is stock, the holding period should run from the SAFE purchase. If not, § 1202(i)(1)(A) treats stock received in exchange for property (other than money or stock) as acquired on the date of the exchange, so the clock starts at conversion. Which applies is unresolved.
- **Gross assets test** (§ 1202(d)) is applied at and immediately after issuance. If the SAFE is not stock, the test is applied at conversion, when a successful company may exceed $75,000,000.
- **"Original issue."** Stock received on conversion is issued by the corporation, which should satisfy § 1202(c)(1)(B).
- **Drafting response:** use the YC form's tax-treatment clause; avoid side letters that create debt-like features (fixed redemption dates, interest); advise investors that QSBS treatment of SAFEs is uncertain.

> **Verify:** Check for any IRS guidance, Tax Court decision, or Treasury regulation on SAFE characterization or § 1202 holding periods for convertible instruments issued after the date of this reference.

**Section 83(b)** is irrelevant to an investor's cash-purchased SAFE (not received in connection with services). Do **not** issue SAFEs as compensation; use stock or options so that § 83, § 409A and Rule 701 apply cleanly.

**State conformity.** Several states do not follow § 1202 (California is the most significant). Note it in client memos.

### 10.2 Convertible notes

- **Debt for tax purposes.** Interest accrues as income to the holder. If stated interest is not unconditionally payable at least annually (e.g., it accrues and converts or is paid at maturity), it is not "qualified stated interest," and the instrument has **original issue discount** that holders include in income as it accrues under I.R.C. § 1272 and the issuer may deduct under § 163(e) (Treas. Reg. §§ 1.1273-1(c), 1.1272-1). Issuers with notes outstanding should ask their accountants about Form 1099-OID or 1099-INT reporting.
- **Convertible debt and the contingent payment rules.** Debt convertible into the issuer's stock is generally outside the contingent payment debt instrument regulations (Treas. Reg. § 1.1275-4(a)(4)), but large change-of-control premiums and other contingencies need review under the remote/incidental contingency rules (Treas. Reg. § 1.1275-2(h)).
- **Conversion.** Converting a note into stock of the same issuer is generally not a taxable exchange of principal (see Rev. Rul. 72-265), but shares received for accrued interest are interest income.
- **QSBS.** Stock received on conversion is treated as acquired on the conversion date (§ 1202(i)(1)(A)), with basis not less than the fair market value of the note exchanged (§ 1202(i)(1)(B)). Notes therefore start the QSBS clock later than SAFEs treated as stock.
- **Below-market interest.** Loans between a corporation and its shareholders can be below-market loans under § 7872. Set the rate at or above the applicable federal rate for the term (short-term AFR for terms up to 3 years) when the noteholders are or will become stockholders. (§ 1274 imputed interest generally does not apply to notes issued for cash.)

> **Verify:** Confirm the current month's applicable federal rates in the IRS revenue ruling for the issue month before setting a note's rate.

- **Usury** (not tax, but rate-related): see [templates/convertible-financing/convertible-promissory-note.md](../templates/convertible-financing/convertible-promissory-note.md). Delaware lets a corporation not plead usury (6 Del. C. § 2306) and removes the rate ceiling for loans over $100,000 not secured by a principal residence (6 Del. C. § 2301(c)); California exempts aggregate issues of at least $300,000 meeting relationship or sophistication criteria (Cal. Corp. Code § 25118); New York's criminal usury cap (25%) can apply to corporate borrowers, and the New York Court of Appeals has held that the value of a conversion discount can count as interest (*Adar Bays, LLC v. GeneSYS ID, Inc.*, 37 N.Y.3d 320 (2021)).

---

## 11. Accounting classification (U.S. GAAP)

- **SAFEs.** Most auditors classify post-money SAFEs as **liabilities**, typically under ASC 480-10 (an obligation that may require transfer of assets on a Liquidity or Dissolution Event outside the issuer's control, or an obligation to issue a variable number of shares for a predominantly fixed monetary amount), measured at fair value with changes in earnings. Some analyses proceed under ASC 815-40. Practice varies, and the FASB's Private Company Council has discussed SAFE classification.
- **Notes.** Debt under ASC 470; embedded features (contingent conversion at a discount, change-of-control premiums) may require bifurcation as derivatives under ASC 815-15 unless the issuer elects the fair value option (ASC 825-10). ASU 2020-06 removed the beneficial-conversion and cash-conversion models.
- **Why the lawyer cares:** liability classification affects balance-sheet covenants in venture debt, audit timing for later rounds, and 409A valuations (the 409A provider must model SAFEs and notes).

> **Verify:** Confirm whether the FASB has issued any standard or practical expedient on SAFE classification for private companies after the date of this reference, and have the company's accountant confirm classification.

---

## 12. When to use which

| Situation | Recommended instrument | Why |
|---|---|---|
| Pre-seed or seed, under about $3M, multiple angels and funds, speed matters | Post-money SAFE (valuation cap) | Standard terms, low cost, ownership certainty |
| First check before anyone sets a valuation | Uncapped MFN SAFE (or discount-only SAFE) | Defers price; MFN protects the early investor |
| Bridge to a priced round already in view | Discount-only SAFE, or note with discount and modest cap | Price will be set soon; discount rewards bridge risk |
| Investors require creditor status, maturity, or security; or regulated investors that cannot hold SAFEs | Convertible note | Debt priority and maturity leverage |
| Company already has notes outstanding | More notes on the same terms (or convert notes to SAFEs with consent) | Mixing notes and SAFEs complicates priority and conversion math |
| Institutional lead, round of several million, investors want board seat and protective provisions | Priced Series Seed or Series A | Governance and rights belong in a charter and investor agreements |
| Non-U.S. company (Canada, Cayman, Singapore) | YC's jurisdiction-specific SAFE with local counsel | U.S. forms assume a Delaware or other U.S. corporation |

---

## 13. Market data (dated; refresh before relying on it)

| Data point | Value | Source and date |
|---|---|---|
| Share of SAFEs on Carta's platform that were post-money | About 91% | Carta, "In the pre-seed market, valuation caps on new SAFEs keep getting bigger" (Q2 2026 data) |
| Median valuation cap on SAFEs above $2.5M | $35M (up about 40% year over year; 75th percentile near $60M) | Same Carta Q2 2026 page |
| SAFEs as share of pre-seed rounds on Carta | 90% (notes 10%) | Carta, State of Pre-Seed Q1 2025 |
| Median convertible note interest rate | 7% (Q1 2025, down from 8% in Q2 2024) | Carta, State of Pre-Seed Q1 2025 |
| Median discount, notes and SAFEs | 20% in 2024 and 2025 | Osler, 2025 Deal Points Report (convertible securities chapter); a Canadian-focused data set |
| Typical SAFE discount | 10–20% | Y Combinator SAFE FAQ (ycombinator.com/documents), accessed November 2, 2026 |

> **Verify:** The Carta figures above were obtained from Carta's public data pages and secondary summaries because Carta's site blocked direct retrieval on November 2, 2026. Secondary sources also report Carta medians of about $10M (rounds of $250K–$1M) and $15M–$18M (rounds of $1M–$2.5M) post-money caps; confirm against Carta's current State of Pre-Seed report before citing.

---

## 14. Modeling and drafting checklist

1. Build the pre-round cap table from the stock ledger, option ledger, and every convertible instrument (including MFN amendments and side letters).
2. Identify each instrument's own denominator definition; do not reuse one instrument's "fully diluted" for another.
3. Decide (in the term sheet) whether conversion shares and the pool increase are in the pre-money; model both ways for the client.
4. Run `scripts/conversion_calculator.py` and tie the output to the term sheet's price per share and the pool target.
5. Name and price each shadow series; give the priced-round drafter the series names, Original Issue Prices, and share counts.
6. Confirm side-letter pro rata allocations fit within the round.
7. Confirm notes' interest through the actual closing date and whether interest converts.
8. Re-run after any change in closing date, round size, or pool target; rounding can move share counts by a few shares.

---

## Sources

- Y Combinator, SAFE documents page and FAQ: https://www.ycombinator.com/documents (forms and FAQ reviewed November 2, 2026: Post-Money SAFE Valuation Cap Only v1.2, Discount Only v1.2, MFN Only v1.3, Pro Rata Side Letter v1.0; SAFE User Guide). Used to describe mechanics; no text reproduced.
- I.R.C. § 1202 (as amended by P.L. 119-21 § 70431), § 1272, § 1273, § 163(e), § 7872; Treas. Reg. §§ 1.1272-1, 1.1273-1, 1.1275-2(h), 1.1275-4(a)(4); Rev. Rul. 72-265.
- 6 Del. C. §§ 2301, 2306 (delcode.delaware.gov); Cal. Corp. Code § 25118; *Adar Bays, LLC v. GeneSYS ID, Inc.*, 37 N.Y.3d 320 (2021).
- FASB ASC 470, 480, 815, 825; ASU 2020-06; Grant Thornton, "Issuers' accounting for SAFEs" (2024): https://www.grantthornton.com/insights/newsletters/audit/2024/viewpoint/issuers-accounting-for-safe
- Carta data pages: https://carta.com/data/safe-valuation-caps-q2-2026/ and https://carta.com/data/state-of-pre-seed-q1-2025/ (see Verify note above).
- Osler, 2025 Deal Points Report, convertible securities: https://www.osler.com/en/insights/reports/2025-deal-points-report-venture-capital-financings/convertible-securities-intelligence/
- Series Seed documents (CC0 1.0): https://www.seriesseed.com (structure reference for the priced alternative).

# Equity Compensation and Tax: Expert Reference

**As of November 2, 2026.** This reference supports the templates in `templates/equity-compensation/`. It is written for Claude as the drafter: it states the rules, the market practice, and the traps, with pin cites. Primary law is cited first; secondary sources (law-firm alerts, Carta data) are identified as such. Items marked **Verify** could not be fully confirmed against primary authority or change frequently.

---

## 1. Award types at a glance

| | ISO | NSO | Restricted stock (RSA / RSPA) | RSU (private, double-trigger) | SAR (stock-settled) |
|---|---|---|---|---|---|
| Who can receive | Employees of the corporation or a parent/subsidiary corporation only | Employees, directors, consultants | Same as NSO | Same as NSO | Same as NSO |
| Tax at grant | None | None (if price ≥ FMV) | None if price = FMV and 83(b) filed; otherwise discount is income with 83(b) | None | None |
| Tax at vesting | None | None | If no 83(b): ordinary income on value at each vesting | None until settlement (FICA when SRF lapses) | None |
| Tax at exercise or settlement | No regular tax; spread is an AMT adjustment | Ordinary income on spread; wage withholding for employees | — | Ordinary income on value delivered | Ordinary income on value delivered |
| Tax at sale | Long-term capital gain if 2-year/1-year holding met; otherwise disqualifying disposition | Capital gain or loss on post-exercise appreciation | Capital gain (holding period from purchase if 83(b)) | Capital gain on post-settlement appreciation | Capital gain on post-settlement appreciation |
| § 409A | Exempt (statutory option) | Exempt if price ≥ FMV, no deferral feature | Not deferred compensation (property transferred under § 83) | Exempt as short-term deferral if settled timely; otherwise must comply | Exempt if base price ≥ FMV and settled at exercise |
| QSBS (§ 1202) clock starts | At exercise | At exercise | At issuance with 83(b) (at vesting without, under the general view) | At settlement | At settlement |
| Rule 701 "sale" date | Grant (valued at aggregate exercise price) | Grant (aggregate exercise price) | Purchase or issuance | Grant (C&DI 271.24) | Grant |
| Typical stage | Seed through pre-IPO | Consultants, directors, excess over $100K ISO limit | Formation to early seed, while FMV is very low | Late-stage private (high 409A value) and public | Non-U.S. and special cases |

---

## 2. Section 83 and the 83(b) election

**Rule.** Property transferred in connection with services is taxed when it is "substantially vested" (transferable or not subject to a substantial risk of forfeiture), on its then fair market value less the amount paid (I.R.C. § 83(a); Treas. Reg. §§ 1.83-1, 1.83-3). A repurchase right at the lower of cost or FMV on termination of service is a substantial risk of forfeiture; a right of first refusal is not (it is a nonlapse-type restriction only if it never lapses, and is ignored for valuation unless it is a nonlapse restriction under Treas. Reg. § 1.83-3(h)).

**The election.** Under § 83(b), the service provider may elect to include in income at transfer the excess (if any) of the property's FMV (determined without regard to lapse restrictions) over the amount paid. Mechanics (Treas. Reg. § 1.83-2):

- **Deadline:** no later than **30 days after the transfer** (§ 83(b)(2); Treas. Reg. § 1.83-2(b)). No extensions; the deadline is jurisdictional in practice. If the 30th day falls on a weekend or legal holiday, I.R.C. § 7503 extends to the next business day. Timely mailing is timely filing under § 7502 if sent by U.S. mail or a designated private delivery service; use certified mail, return receipt requested, and keep proof.
- **Where:** the IRS office where the taxpayer files the return (Treas. Reg. § 1.83-2(c)). Since January 1, 2016, a copy no longer has to be attached to the return (Treas. Reg. § 1.83-2(c), (g)).
- **Form:** a signed statement with the content in Treas. Reg. § 1.83-2(e): name, address, TIN; description of the property; date of transfer and taxable year; nature of restrictions; FMV at transfer; amount paid; statement that copies were furnished. **IRS Form 15620** (released November 2024) is an optional standard form. Law-firm alerts (July–August 2025, for example Goodwin and Morrison Foerster) report that the IRS began accepting Form 15620 **online** through an IRS individual online account in July 2025. **Verify** the current online procedure on IRS.gov before advising.
- **Copies:** to the employer or service recipient, and to the transferee if different (Treas. Reg. § 1.83-2(d)).
- **Revocation:** only with IRS consent, for a mistake of fact, requested within 60 days after the mistake becomes known; a decline in value is not a mistake of fact (Treas. Reg. § 1.83-2(f)).
- **Forfeiture after election:** loss limited to the amount paid less any amount realized on forfeiture; the income previously recognized is not deductible (Treas. Reg. § 1.83-2(a)).

**When to use it.**

| Situation | 83(b)? | Why |
|---|---|---|
| Founder stock bought at par, subject to vesting | Yes, always | $0 income now; avoids ordinary income on vesting at much higher values; starts capital-gain and QSBS holding periods |
| RSA purchased at FMV | Yes | Same; no income at election |
| RSA granted for services (no payment) | Usually yes if value is low | Income now equals current FMV; afterward capital treatment |
| Early-exercised NSO at FMV | Yes | $0 income; no ordinary income at vesting |
| Early-exercised ISO | Yes (AMT purposes) | Fixes the AMT adjustment at $0 if spread is $0 at exercise; ISO regular-tax treatment is separate |
| Vested shares | No | No substantial risk of forfeiture; § 83(b) is irrelevant |
| RSUs | Not available | RSUs are an unfunded promise, not property (Treas. Reg. § 1.83-3(e)) |

**Founder stock note.** Founder stock subject to "reverse vesting" is the classic 83(b) case. A common error is assuming the 83(b) is unnecessary because the founder paid par; without the election, each vesting tranche is ordinary income at its value on that date.

---

## 3. Section 409A

### 3.1 Stock rights exemption

An option or SAR is not "deferred compensation" if (Treas. Reg. § 1.409A-1(b)(5)(i)(A)–(B)):

1. the exercise or base price can never be less than the FMV of the underlying stock on the grant date;
2. the stock is "service recipient stock" (common stock of the service recipient or of an eligible issuer in its controlled group that has no preference as to dividends or liquidation rights; Treas. Reg. § 1.409A-1(b)(5)(iii));
3. the number of shares is fixed on the grant date; for options, the transfer is subject to § 83; and
4. the right has no feature for the deferral of compensation beyond the later of exercise or disposition.

ISOs are exempt as statutory options (Treas. Reg. § 1.409A-1(b)(5)(ii)), but a "failed" ISO is tested as an NSO.

### 3.2 Valuation of private-company stock

**General standard** (Treas. Reg. § 1.409A-1(b)(5)(iv)(B)(1)): FMV is the value determined by the **reasonable application of a reasonable valuation method**, considering, as applicable, tangible and intangible assets, the present value of anticipated future cash flows, market value of comparable companies, recent arm's-length transactions in the stock, and control premiums or discounts for lack of marketability. Two staleness rules apply even under a reasonable method:

- A value is **not reasonable** if it fails to reflect information available after the calculation date that may materially affect value (the regulation's examples: resolution of material litigation, issuance of a patent).
- A value is **not reasonable** if calculated as of a date **more than 12 months before** the date it is used.

**Presumptions of reasonableness** (Treas. Reg. § 1.409A-1(b)(5)(iv)(B)(2)) — the IRS may rebut only by showing the method or its application was **grossly unreasonable**:

1. **Independent appraisal** meeting the § 401(a)(28)(C) standard (the ESOP appraisal standard), as of a date **no more than 12 months before** the transaction (for example, the option grant date). This is the method nearly all venture-backed companies use ("409A valuation"), typically refreshed annually and after each priced round.
2. **Formula price** used for a nonlapse restriction under Treas. Reg. § 1.83-5 and applied consistently to all transfers to the issuer or 10%-plus holders (rare in venture companies).
3. **Illiquid start-up** valuation: a written report, made reasonably and in good faith, considering the § 1.409A-1(b)(5)(iv)(B)(1) factors, for stock of a corporation that (a) has not conducted any material trade or business for 10 years or more, (b) has no publicly traded equity, (c) whose stock is not subject to any put, call, or purchase obligation (other than a third-party-offer ROFR or a lapse restriction), (d) does not reasonably anticipate a change in control event within **90 days** or an IPO within **180 days** after the valuation is applied, and (e) is valued by a person with significant knowledge, experience, education, or training, generally **at least five years** of relevant experience in business valuation, financial accounting, investment banking, private equity, secured lending, or comparable experience in the industry.

**Consistency.** A company may use different methods for different actions but, once a method is used for an action, it cannot retroactively change it (Treas. Reg. § 1.409A-1(b)(5)(iv)(B)(3)).

**Practice points.**

- **Refresh triggers:** (a) 12 months from the valuation date; (b) a priced financing (including a signed term sheet); (c) a secondary sale or tender offer at a materially different price; (d) an acquisition offer or LOI; (e) IPO preparations (bankers selected, confidential filing); (f) material changes in revenue, customers, product, regulatory status, or litigation.
- **The "cheap stock" problem.** In the 12–18 months before an IPO, the SEC staff and auditors scrutinize grant-date FMV ("cheap stock"). Frequent valuations and a documented "no material change" determination at each grant reduce restatement risk.
- **Secondary transactions.** Arm's-length secondary sales of common stock are evidence of value and must be considered; valuation firms weight them by volume, timing, and information access.
- **Grant date.** For options, the date of grant is when the corporate action is complete and the number of shares and price are fixed or determinable (Treas. Reg. § 1.409A-1(b)(5)(vi)(B); for ISOs, Treas. Reg. § 1.421-1(c)). With a unanimous written consent, that is the date the last director signs (or a specified later effective time).

### 3.3 Consequences of a discounted option

If an NSO (or failed ISO) has an exercise price below grant-date FMV, it is deferred compensation that almost never complies with § 409A (exercise at the holder's discretion is not a permissible payment event). Consequences (I.R.C. § 409A(a)(1)):

- the spread on **vested** options is included in income **in the year of vesting and each later year** until exercise (the IRS's proposed income-inclusion regulations, Prop. Treas. Reg. § 1.409A-4, measure the amount annually);
- a **20% additional federal tax** on the amount included, plus **premium interest** at the underpayment rate plus 1%;
- **California** adds a **5% additional state tax** (Cal. Rev. & Tax. Code § 17508.2, reduced from 20% for taxable years beginning on or after January 1, 2013 (AB 1173); secondary sources: Cooley, Goodwin, Pillsbury alerts, 2013);
- the employer has reporting and withholding obligations (Form W-2 code Z; Form 1099-NEC/1099-MISC for non-employees).

**Correction (IRS Notice 2008-113).**

| Section | Who | Deadline | Conditions |
|---|---|---|---|
| § IV.D | Any holder, including insiders | Before exercise and by the last day of the holder's taxable year in which the option was granted | Reset price to at least grant-date FMV; Company attaches statement to its return (§ IX.A); no statement to the holder required for § IV.D |
| § V.E | Non-insiders only (insider = director, officer, or >10% beneficial owner under § 16 principles, § III.G) | Before exercise and by the last day of the holder's taxable year following the year of grant | Same reset; option must otherwise have been exempt; return attachments and holder information (§ IX.B) |

After those windows, alternatives include amending the option to a fixed exercise date (making it a compliant deferral) or cancelling and replacing it; consult tax counsel. Notice 2008-113 also has general eligibility conditions (§ III; for example, the failure must be inadvertent and the taxpayer not under examination for the issue). **Verify** the current status of Notice 2008-113 and any later IRS correction guidance before relying on it.

### 3.4 Modifications and extensions of stock rights

(Treas. Reg. § 1.409A-1(b)(5)(v).)

- A **modification** (any change that may reduce the exercise price, directly or indirectly) is a **new grant** tested at the modification date. Shortening the exercise period, adding stock-swap or share-withholding payment features, and exercising reserved discretion over transferability are not modifications.
- An **extension** (additional exercise time beyond the original terms, conversion into a right to future compensation, or adding a deferral feature) makes the right deferred compensation **from the original grant date**, unless:
  - the new expiration is no later than the **earlier of** the original maximum term and the **10th anniversary** of grant; or
  - the option is **underwater** when extended (then it is a modification/new grant, not an extension); or
  - the expiration is **tolled** while exercise would violate law (or jeopardize going-concern status), for no more than **30 days** after the bar lifts.
- **Substitutions and assumptions** in corporate transactions do not create a modification if they meet the § 424 rules (ratio test and spread test) applied to all stock rights (Treas. Reg. § 1.409A-1(b)(5)(v)(D)).

### 3.5 RSUs and the short-term deferral exception

A payment is a short-term deferral (not deferred compensation) if actually or constructively received by the **later of** the 15th day of the third month after the end of (a) the holder's or (b) the company's first taxable year in which the right is no longer subject to a **substantial risk of forfeiture** (Treas. Reg. § 1.409A-1(b)(4)(i)(A)). For calendar-year parties, **March 15** of the year after vesting.

**Substantial risk of forfeiture for § 409A** (Treas. Reg. § 1.409A-1(d)(1)) means entitlement is conditioned on the performance of substantial future services or the occurrence of a condition related to a purpose of the compensation, and the possibility of forfeiture is substantial. Practitioners treat an IPO or change-in-control condition in a private-company RSU as qualifying when the event is genuinely uncertain, but there is no bright-line rule, and secondary sources report informal IRS skepticism of the view that any liquidity event automatically qualifies. Market practice limits the liquidity condition to **seven years** (some use ten) from grant (Baker McKenzie 2022 guide; Lowenstein Sandler commentary: facts-and-circumstances). Draft settlement with a hard outside date and avoid any discretion to accelerate or delay payment beyond the permitted exceptions (Treas. Reg. §§ 1.409A-1(b)(4)(ii), 1.409A-2(b)(7), 1.409A-3(j)(4)).

### 3.6 Other § 409A drafting rules for equity documents

- If an award **is** deferred compensation, its Change in Control payment trigger must be a "change in control event" (Treas. Reg. § 1.409A-3(i)(5)), and its separation trigger must be a "separation from service" (Treas. Reg. § 1.409A-1(h)).
- Transaction-consideration payments (escrows, earnouts) to holders of cashed-out options and RSUs may follow the stockholder schedule if paid within **five years** after the change in control event (Treas. Reg. § 1.409A-3(i)(5)(iv)(A)).
- The six-month delay for specified employees (I.R.C. § 409A(a)(2)(B)(i)) applies only when the company's stock is publicly traded.
- "Good Reason" safe harbor (Treas. Reg. § 1.409A-1(n)(2)(ii)): material negative change, notice within 90 days of the condition, cure period of at least 30 days, and separation within two years.

---

## 4. Incentive stock options (§§ 421, 422, 424)

### 4.1 Requirements (I.R.C. § 422(b), (c), (d))

1. Granted to an **individual employee** for a reason connected with employment, by the employer or its parent or subsidiary corporation (50% voting chain, § 424(e)–(f)).
2. Under a **plan** that states the aggregate number of shares and the eligible employees, approved by **stockholders within 12 months before or after** Board adoption (§ 422(b)(1); Treas. Reg. §§ 1.422-2(b), 1.422-3). The ISO maximum must be a fixed, immediately determinable number; an evergreen may increase by a percentage of shares outstanding **at adoption** (Treas. Reg. § 1.422-2(b)(3)(ii)). Any increase in the ISO maximum, change in eligible employees, or change in the granting corporation or stock is a **new plan** needing new approval (Treas. Reg. § 1.422-2(b)(2)(iii)).
3. Granted within **10 years** of the earlier of adoption or approval (§ 422(b)(2)).
4. Term ≤ **10 years** (§ 422(b)(3)); ≤ **5 years** for a Ten Percent Stockholder (§ 422(c)(5)).
5. Price ≥ **FMV** at grant (§ 422(b)(4)); ≥ **110%** for a Ten Percent Stockholder (§ 422(c)(5)). Good-faith valuation attempts are protected (§ 422(c)(1)). FMV for § 422 ignores restrictions other than those that never lapse (§ 422(c)(7)).
6. **Nontransferable** except by will or descent; exercisable during life only by the employee (§ 422(b)(5)).
7. **Ten Percent Stockholder** test uses § 424(d) attribution (family members: spouse, ancestors, lineal descendants, siblings; and proportionate ownership through entities), and counts voting power of all classes.
8. **$100,000 limit**: the aggregate grant-date FMV of stock for which ISOs (under all plans of the employer group) are **first exercisable** in a calendar year may not exceed $100,000; the excess is an NSO, applied in grant order (§ 422(d); Treas. Reg. § 1.422-4). Early-exercisable grants are first exercisable at grant. Acceleration moves first-exercisability into the acceleration year.
9. **Employment**: continuously employed from grant until **3 months** before exercise (**1 year** if disabled under § 22(e)(3)) (§ 422(a)(2), (c)(6)). Bona fide leave over 3 months without a statutory or contractual reemployment right ends employment on the first day after the 3-month period (Treas. Reg. § 1.421-1(h)(2)). Death: the estate may exercise without the employment test (§ 421(c)).
10. **No § 83(i) election** with respect to the stock (§ 422(b), flush language).

### 4.2 Taxation

- **Grant and exercise:** no regular income (§ 421(a)). The spread at exercise is an **AMT adjustment** (§ 56(b)(3)). No income tax withholding or FICA/FUTA on exercise or on a disqualifying disposition (§§ 3121(a)(22), 3306(b)(19), 3401(a)(19)).
- **Qualifying disposition:** after **2 years** from grant **and 1 year** from exercise (§ 422(a)(1)): all gain is long-term capital gain; no employer deduction.
- **Disqualifying disposition:** ordinary income equal to the lesser of the spread at exercise or the gain on a sale on which a loss would be recognized (§ 422(c)(2)); remainder capital; employer deduction for the ordinary income; report on Form W-2 (no withholding). Gifts and most transfers are dispositions (§ 424(c)); transfers between spouses or incident to divorce (§ 424(c)(4)), certain tax-free exchanges, transfers from a decedent to the estate or by bequest or inheritance, and pledges (§ 424(c)(1)), and certain insolvency transfers (§ 422(c)(3)) are not.
- **Early exercise:** holding periods start at exercise; file an 83(b) election for AMT purposes.

### 4.3 Modifications (I.R.C. § 424(h); Treas. Reg. § 1.424-1(e))

- **Modification, extension, or renewal = new option** (tested at that date; FMV then; counts against $100K in the year first exercisable; holding periods restart).
- **Modification** = any change giving additional benefits, whether or not the holder benefits; includes extending the exercise period (including post-termination), adding an alternative right (such as a SAR), adding more favorable payment terms (stock swap), or a cash bonus at exercise (Treas. Reg. § 1.424-1(e)(4)(i)).
- **Not a modification:** shortening the exercise period; **accelerating vesting**; removing an acceleration provision before it is triggered (to manage the $100K limit) (Treas. Reg. § 1.424-1(e)(4)(ii)); exercising discretion **reserved at grant** over cash bonus, loans, stock tender, or tax withholding (Treas. Reg. § 1.424-1(e)(4)(iii)).
- **Discretion:** adding discretion to provide a future additional benefit is a modification when added; exercising discretion to give an additional benefit is a modification (Treas. Reg. § 1.424-1(e)(4)(iii)).
- **30-day offer rule:** an offer to change an ISO's terms that remains open **30 days or more** is a modification **as of the offer date**, even if declined; an offer open less than 30 days is not, unless accepted (Treas. Reg. § 1.424-1(e)(4)(iii)).
- **Share increase only:** treated as a new option for the additional shares, not a modification of the old (Treas. Reg. § 1.424-1(e)(4)(v)).
- **Corporate transactions:** a substitution or assumption that meets § 424(a) (spread and ratio tests; no additional benefits) is not a modification (Treas. Reg. § 1.424-1(a)).

### 4.4 Reporting: § 6039 and Form 3921

- For each ISO exercise, the corporation must **furnish** a statement to the employee by **January 31** of the following year and **file** Form 3921 with the IRS by **February 28** (paper; March 2 in 2026 because of the weekend rule) or **March 31** (electronic) (I.R.C. § 6039; IRS General Instructions for Certain Information Returns (2025); Instructions for Forms 3921 and 3922 (Rev. 04/2025)).
- **E-filing** is required if the filer must file **10 or more** information returns of all types in the aggregate (returns required to be filed on or after January 1, 2024).
- Form 3921 reports: grant date; exercise date; exercise price per share; FMV per share on exercise date; number of shares transferred; and the employee's and corporation's identifying information.
- Form 3922 is the ESPP analog (not used by these templates).

---

## 5. Section 280G for private companies

**The rule.** "Parachute payments" to a "disqualified individual" that are contingent on a change in ownership or control and equal or exceed **three times** the individual's "base amount" (average annual compensation over the five prior taxable years) create an "excess parachute payment" (the amount above **one times** the base amount) that is (a) **nondeductible** to the payer (§ 280G(a)) and (b) subject to a **20% excise tax** on the recipient (§ 4999). Disqualified individuals include officers, more-than-1% stockholders, and highly compensated individuals (Treas. Reg. § 1.280G-1, Q&A-15 through Q&A-21).

**Accelerated vesting** counts. Where payment was already vested but accelerated, only the value of acceleration counts; for awards contingent on continued service, the portion treated as contingent includes an amount reflecting the lapse of the service obligation (1% of the accelerated amount per full month of acceleration) (Treas. Reg. § 1.280G-1, Q&A-24(b)–(c)).

**Private-company exemptions.**

1. **Small business corporation** exemption (§ 280G(b)(5)(A)(i)): a corporation that would qualify as an S corporation under § 1361(b) (without regard to the nonresident-alien shareholder rule). Venture-backed companies with Preferred Stock usually do not qualify (second class of stock).
2. **Stockholder approval** (§ 280G(b)(5)(A)(ii), (B); Treas. Reg. § 1.280G-1, Q&A-6 and Q&A-7): available if no stock of the corporation (or of a parent of which it is a substantial part) is readily tradeable on an established securities market. Requirements:
   - approval by **more than 75% of the voting power** of all outstanding stock entitled to vote **immediately before** the change in control, **excluding** stock owned (directly or constructively) by disqualified individuals who would receive payments subject to the vote (Q&A-7(a)(1), (b)(4));
   - **adequate disclosure** to **all** stockholders entitled to vote of all material facts about all payments that would otherwise be parachute payments (Q&A-7(a)(2), (c));
   - the vote must determine the right to receive (or retain) the payment, so the disqualified individual must **irrevocably waive** the excess payments before the vote, subject to approval; approval of the deal cannot be conditioned on approval of the payments (Q&A-7(b)(1));
   - the record date may be any day within the **six-month period** ending on the change-in-control date (Q&A-7(b)(2));
   - entity stockholders vote through their authorized person, with a look-through vote if the entity's assets are substantially Company stock and its stake exceeds 1% of the Company's value (Q&A-7(b)(3)).
3. **Practice.** In M&A, buyers usually require a 280G calculation by an accounting firm and a "cleansing vote" for any individual over the safe harbor. The Plan (§ 11.7) uses a "best-net" cutback. Gross-ups are disfavored and rare at private companies.

---

## 6. Section 1202 (QSBS) interaction with equity awards

**Current rules for stock issued after July 4, 2025** (I.R.C. § 1202 as amended by P.L. 119-21, § 70431): exclusion of **50%** of gain after a 3-year holding period, **75%** after 4 years, **100%** after 5 years; per-issuer cap of the greater of **$15 million** (indexed for inflation after 2026) or **10 times** the taxpayer's aggregate adjusted basis in the stock disposed of; the issuer's aggregate gross assets must not exceed **$75 million** (indexed) at all times before and immediately after issuance. Other requirements are unchanged: domestic C corporation; stock acquired at **original issuance** for money, property (other than stock), or **as compensation for services** (§ 1202(c)(1)(B)); active-business requirement (at least 80% of assets in qualified trades or businesses); and the redemption anti-abuse rules (§ 1202(c)(3)).

**Award-specific points.**

| Award | When "issued" for § 1202 | Notes |
|---|---|---|
| Option (ISO or NSO) | On exercise | Options are not stock. The gross-assets test is applied at exercise, so options exercised after the company passes $75 million (indexed) in gross assets produce non-QSBS stock. Early exercise (with 83(b)) starts the clock at exercise and can lock in QSBS status while assets are below the cap. |
| Restricted stock with 83(b) | On purchase | Holding period and QSBS status determined at purchase. |
| Restricted stock without 83(b) | General view: on vesting (each tranche) | No regulation squarely addresses how § 83 timing interacts with § 1202 issuance and holding-period rules; the safer course is always to file the 83(b). **Verify** for specific facts. |
| RSU | On settlement | Stock received for services qualifies as original issuance; the gross-assets test applies at settlement. |

**Redemptions.** Company repurchases from employees can taint QSBS status for other stockholders under § 1202(c)(3), but Treas. Reg. § 1.1202-2(d)(1)(i) disregards repurchases of stock acquired by an employee or director in connection with the performance of services, made incident to retirement or other bona fide termination of those services. The parallel rule for independent contractors (§ 1.1202-2(d)(1)(ii)) is reserved, so repurchases from consultants and advisors get no express exception. Coordinate unvested-share repurchases and buybacks with tax counsel. **Verify** the scope of the exception for a given buyback.

**State conformity.** California does not conform to § 1202. Other states vary. **Verify** the holder's state.

---

## 7. Section 83(i) (brief)

§ 83(i) lets a "qualified employee" of an "eligible corporation" elect to defer income on stock received on exercise of an option or settlement of an RSU for up to **five years** after the stock becomes transferable or substantially vested (earlier on IPO, becoming an "excluded employee," or revocation). An eligible corporation must have no readily tradeable stock and a **written plan** under which at least **80%** of its U.S. employees receive options or RSUs with the same rights and privileges in the calendar year (§ 83(i)(2)(C)). Excluded employees include 1% owners, the CEO and CFO (current and former), and the four highest-compensated officers. The election must be made within 30 days after the stock first becomes transferable or substantially vested; the employer must give notice, withhold at the highest rate when deferral ends, and escrow. An § 83(i) election disqualifies ISO treatment. Venture-backed companies rarely use it; the Plan (§ 13.4) disclaims it.

---

## 8. Federal securities law

### 8.1 Rule 701 (17 C.F.R. § 230.701)

**Who may use it.** Issuers that are not Exchange Act reporting companies (and not registered investment companies) (Rule 701(b)). An issuer that later becomes a reporting company may continue to rely on Rule 701 for securities offered before it became reporting (Rule 701(b)(2)).

**What it covers.** Offers and sales under a **written compensatory benefit plan** (purchase, savings, option, bonus, stock appreciation, profit sharing, thrift, incentive, deferred compensation, pension, or similar plan) or a **written compensation contract**, to employees, directors, general partners, trustees, officers, and **consultants and advisors** of the issuer, its parents, or its majority-owned subsidiaries (and of the parent's majority-owned subsidiaries), plus "family members" who acquire through gifts or domestic relations orders (Rule 701(c)). Consultants and advisors must be **natural persons** providing **bona fide services** not in connection with capital raising or market-making (Rule 701(c)(1)). Former employees may exercise options granted while employed and may receive grants for prior service where the plan provides; the SEC staff has also permitted reliance on Rule 701 for awards assumed in an acquisition that are held by the target's former service providers (C&DI 271.29, October 15, 2026).

**12-month sales cap** (Rule 701(d)(2)): aggregate sales price or amount sold in reliance on Rule 701 in any consecutive 12-month period may not exceed the **greatest** of (i) **$1,000,000**; (ii) **15% of total assets**; or (iii) **15% of the outstanding amount of the class** being offered, each measured at the most recent balance sheet date (if no older than the last fiscal year end). Calculation rules (Rule 701(d)(3)): options are counted at their **exercise price** on the **grant date**; other securities on the **date of sale**; deferred compensation when the irrevocable deferral election is made; derivative securities are counted as the underlying securities. Cancelled or forfeited options need not be counted (C&DI 271.11). Repriced options are a new sale (C&DI 271.10). The issuer may use a rolling or fixed 12-month period consistently (C&DI 271.06). Sales above the cap lose Rule 701 only for the excess, which may rely on another exemption (C&DI 271.07).

**Disclosure** (Rule 701(e)): the issuer must always deliver a copy of the **plan** or contract. If aggregate sales in a 12-month period **exceed $10 million**, it must also deliver, a reasonable period before the sale: (1) the ERISA summary plan description or a summary of the plan's material terms; (2) information about the risks of investing; and (3) financial statements required by Part F/S of Form 1-A (Regulation A), as of a date **no more than 180 days** before the sale (effectively quarterly statements unless sales are limited to particular times; C&DI 271.14); either Tier 1 or Tier 2 Reg A financial statement standards may be used (C&DI 271.21). For **options**, disclosure must be delivered a reasonable period before **exercise** (Rule 701(e)(6)); for **RSUs**, before **grant** (C&DI 271.24, March 6, 2026). The obligation applies to **all** investors in the offering if the issuer believes sales will exceed $10 million in the coming 12-month period; failure to deliver loses the exemption for the **entire offering** in that 12-month period (C&DIs 271.12, 271.26, 271.27). Electronic delivery is permitted, with password and confidentiality safeguards (C&DIs 271.15, 271.25).

**Resale.** Rule 701 securities are restricted securities (Rule 701(g)(1)). **90 days** after the issuer becomes an Exchange Act reporting company, non-affiliates may resell under Rule 144 without the current-information and holding-period conditions, and affiliates without the holding period (Rule 701(g)(3)). After an IPO, the issuer may move pre-IPO awards onto Form S-8 (C&DI 271.28, October 15, 2026).

**Integration.** Rule 701 offerings are not integrated with other offerings (Rule 701(f)).

**M&A.** An acquirer does not need a new exemption to assume target options if, at grant, the target plan permitted assumption without holder consent (C&DI 271.17); exercises of assumed options may rely on Rule 701 if the target complied at grant (C&DI 271.18); the acquirer counts the target's Rule 701 sales for its own 12-month calculations (C&DIs 271.19, 271.23).

### 8.2 Exchange Act § 12(g) and Rule 12h-1(f)

A private company must register a class of equity securities under § 12(g) if it has more than $10 million in total assets and the class is held of record by **2,000 persons, or 500 persons who are not accredited investors** (Exchange Act § 12(g)(1)(A)). Persons who received securities under an employee compensation plan in exempt transactions are excluded from the holder count (§ 12(g)(5), as amended by the JOBS Act). **Rule 12h-1(f)** exempts compensatory **options** themselves from § 12(g) registration if conditions are met (written compensatory plan, eligible holders, transfer restrictions on options and pre-exercise shares, and Rule 701(e)-type information delivery once the issuer relies on the exemption). RSUs are not covered by Rule 12h-1(f) by its terms; companies have relied on the § 12(g)(5) exclusion and SEC no-action positions. **Verify** the Rule 12h-1(f) conditions if the company approaches 500 optionholders.

### 8.3 Section 16 and other public-company rules

Section 16 (insider reporting and short-swing profits) applies only to issuers with a class of equity securities registered under Exchange Act § 12. It does **not** apply to a private company's plan. At IPO, the Board adopts a public-company plan with Rule 16b-3 approval mechanics, and the Company adopts a Rule 10D-1-compliant clawback policy before listing. Rule 10b5-1 trading plans and "eligible sell-to-cover" arrangements become relevant only after IPO.

### 8.4 Tender offers and secondary sales (brief)

- **Company tender offers and option exchanges.** Section 14(e) and **Regulation 14E** apply to any tender offer, including by a private company; Rule 13e-4 applies only to reporting issuers. Key Regulation 14E rules: at least **20 business days** open (Rule 14e-1(a)); **10 business days** after a change in price or percentage sought (Rule 14e-1(b)); prompt payment or return (Rule 14e-1(c)); target recommendation within 10 business days if a third-party offer (Rule 14e-2). Whether a program is a "tender offer" depends on multi-factor case law (widespread solicitation, substantial percentage, fixed terms, limited time, pressure).
- **Tax of tender offers.** When the company (or investors acting with the company) buys employee shares at a price above FMV, the IRS position is that the excess may be **compensation** (ordinary income and wages), not capital gain. Purchases of ISO shares within the holding periods are disqualifying dispositions. A tender at a price materially above the 409A value is evidence of value that the next 409A must consider.
- **Secondary sales by employees.** Subject to the plan ROFR, bylaw transfer restrictions, and investor ROFR/co-sale rights; exempt resales typically rely on Section 4(a)(1), "Section 4(a)(1½)," or Section 4(a)(7). Companies increasingly prohibit unapproved secondary transfers before IPO.

---

## 9. State securities law

### 9.1 California

- **Exemption.** Cal. Corp. Code § 25102(o) exempts offers and sales under compensatory purchase or option plans if the securities are exempt under Rule 701 at the time of issuance or grant; the plan complies with 10 CCR §§ 260.140.41 (options) or 260.140.42 (purchase and bonus), and §§ 260.140.45 and 260.140.46; and the issuer files a **notice of transaction** no later than **30 days after the initial issuance** of any security under the plan. Late filing does not destroy the exemption, but the issuer must file within **15 business days** after discovery or demand and pay a fee equal to the maximum aggregate fee payable had the transaction been qualified (§ 25102(o)).
- **Fee.** § 25608(y) incorporates the § 25608(e) permit fee: **$200 plus one-fifth of 1%** of the aggregate value of the securities sold or proposed to be sold in California, **up to $2,500**.
- **Required plan terms — options (10 CCR § 260.140.41, as amended July 9, 2007):** (a) total number of securities and eligible persons; (b) exercise period **≤ 120 months**; (c) nontransferability (except by will, descent, to a revocable trust, or as Rule 701 permits); (d) proportionate adjustment for splits, dividends, recapitalizations, and similar events; (e) unless terminated for **cause** (as defined by law, the plan, the grant, or an employment contract), vested options remain exercisable after termination until the earlier of expiration or **at least 6 months** (death or disability) or **at least 30 days** (other terminations); (f) grants within **10 years** of the earlier of adoption or stockholder approval; (g) approval by **a majority of the outstanding securities entitled to vote** by the later of 12 months before or after adoption, or before or within 12 months after the first grant in California, with **rescission** of pre-approval exercises if approval fails (excluded from the approval count); foreign private issuers with ≤ 35 California participants are exempt from (g); (h) compliance with § 260.140.46.
- **Purchase and bonus plans (§ 260.140.42):** parallel terms (number and eligible persons; nontransferable purchase rights; adjustments; issuance within 10 years; stockholder approval with rescission; § 260.140.46).
- **§ 260.140.45 (30% cap)** on securities issuable under options and bonus plans (as-converted), unless two-thirds of outstanding voting securities approve a higher percentage; **does not apply** to a plan that complies with all conditions of Rule 701.
- **§ 260.140.46 (annual financial statements)** to holders; does not apply to key persons with access to equivalent information, or to a plan that complies with all conditions of Rule 701.
- **What changed in 2007.** The pre-2007 rules required minimum vesting (generally at least 20% per year for non-officers) and limited repurchase rights. The current text contains neither; forms that still include them are outdated.
- **Other California points.** Use § 25102(f) for grants outside Rule 701 (for example, to entities or above Rule 701 limits). Consider the § 260.141.11 legend for exemptions that require it. California employment law: Cal. Lab. Code § 925 (forum and choice of law for California employees); Bus. & Prof. Code §§ 16600–16600.5 (non-competes void, including in equity documents); pre-dispute jury waivers unenforceable.

### 9.2 New York

New York's Martin Act (N.Y. Gen. Bus. Law art. 23-A) does not have a self-executing Rule 701 analog. N.Y. Gen. Bus. Law § 359-f(2) provides exemptions from the dealer and offering registration requirements; secondary sources describe an exemption for employee benefit plans that requires an **application to the Attorney General** (and the AG's grant). Many practitioners also analyze whether compensatory grants to a limited group are a public offering at all. **Verify** the current statutory text and the Investor Protection Bureau's practice before the first grant to a New York resident.

### 9.3 Other states

Most states provide an exemption for offers and sales under employee benefit or compensatory plans, frequently tied to Rule 701 compliance and often self-executing (patterned on the Uniform Securities Act employee-benefit-plan exemption); a minority require a notice filing or fee, and a few require filing before the first grant. Practice: maintain a state-by-state matrix keyed to participant residence, and check it before each first grant in a new state. **Verify** each state's current exemption and any filing requirement; do not assume Rule 701 compliance is sufficient.

---

## 10. Market norms (with dates and sources)

### 10.1 Option pool sizing

- **Carta, Founder Ownership Report 2026** (data as of January 1, 2026; rounds 2021–2025; more than 45,000 startups per secondary write-ups): median founding-team ownership about **56%** at seed and about **36%** after Series A; the employee pool overtakes founder ownership at **Series C (16.8% vs. 16.1%)**. Secondary write-ups attribute a median seed-stage employee pool of about **12%** to Carta data. Carta's own data posts (2024–2025) argue that a 20% pool at seed is usually larger than needed. (Carta pages were not directly retrievable for this reference; figures are from Carta search excerpts and secondary summaries.) **Verify** against the primary Carta report before quoting.
- **Term-sheet practice.** Venture term sheets typically require an unallocated post-closing pool of **10%–15%** at seed and Series A (sometimes up to 20%), sized from a 12–24 month hiring plan. The pool is usually included in the **pre-money** valuation ("option pool shuffle"), so its dilution falls on existing holders; founders negotiate the pool down by presenting a bottom-up hiring budget.
- **Refreshes.** Pools are typically topped up at each priced round; late-stage annual burn of 2%–4% of fully diluted shares is common for growth companies (secondary practice, not a primary source).
- **Verify** current Cooley and Fenwick venture financing survey data for pool sizes if the client needs a citation; they publish periodic reports.

### 10.2 Vesting

- **New-hire grants:** four years, one-year cliff (25%), monthly thereafter remains the overwhelming norm.
- **Refresh grants:** often no cliff, monthly or quarterly over four years; some companies use shorter refresh vesting (two to three years).
- **Back-weighted** schedules (for example 10/20/30/40) are used by a few large companies; uncommon in startups.
- **Founders:** four years with a one-year cliff at formation, with credit for prior service; investors sometimes require partial re-vesting at Series A.
- **Acceleration:** double-trigger (change in control plus qualifying termination within a window, commonly 3 months before to 12 months after) for executives; 100% for C-suite, 25%–50% for VPs; single-trigger is uncommon and disfavored by acquirers.

### 10.3 Post-termination exercise periods

- **Default:** 3 months (90 days) after termination; 12 months after death or disability (some use 18 months for death). California floors: 30 days and 6 months.
- **Extended windows:** a meaningful minority of companies offer 5–10 years (sometimes conditioned on tenure, such as two years of service). Carta data (secondary summaries): about **20%** of terminated option grants in three of four quarters of 2023, and in Q1 2024, had post-termination exercise periods longer than 90 days; a July 2025 Carta newsletter reported the share continuing to rise. **Verify** before quoting.
- **Trade-offs:** an extended window converts ISOs to NSOs after 3 months, increases overhang (fewer forfeitures return to the pool), and may need investor consent; it cannot extend past the original term without § 409A issues.

---

## 11. Decision guide: options vs. restricted stock vs. RSUs

| Company situation | Recommended award | Reasons |
|---|---|---|
| Pre-seed or seed; 409A value pennies per share | **Restricted stock** (purchase at FMV + 83(b)) for early employees and key hires; options for others | Holder pays little; immediate capital-gain and QSBS clock; no AMT issue |
| Seed through Series B; FMV low to moderate | **Options** (ISOs for employees; NSOs for others); early exercise for executives | No cash at grant; ISO tax benefit; early exercise preserves QSBS |
| Series C+; FMV high, spread small at grant | **Options or RSUs**; RSUs for senior hires and refreshes | Options at high FMV have less upside; RSUs always have value; double-trigger avoids phantom income |
| Pre-IPO (12–18 months) | **RSUs** (double-trigger), with sell-to-cover readiness | Public-company standard; avoids cheap-stock disputes on option pricing |
| Non-U.S. participants | Country-dependent; often RSUs or SARs | Securities, exchange-control, and tax rules make options hard in some countries |
| Consultants and advisors | NSOs or RSAs (natural persons only, Rule 701) | No ISOs; RSAs for very early advisors |

**Early exercise.** Offer when the spread is zero or small and the holder can afford the cash at risk. Benefits: starts long-term capital gain, ISO, and QSBS clocks; avoids AMT with an 83(b). Costs: cash at risk if the company fails; the $100,000 ISO limit applies to the whole early-exercisable grant in year one; Company bookkeeping for escrow and repurchase.

**Repricing.** Use after a down round when options are deeply underwater and retention is at risk. Consider ISO (30-day offer rule; new grant), § 409A (new FMV), Regulation 14E (20 business days if a tender offer), Rule 701 (new sale), accounting (incremental cost), and investor consent. See [plan-share-increase-and-option-amendment](../templates/equity-compensation/plan-share-increase-and-option-amendment.md).

---

## 12. Withholding, payroll, and reporting

| Event | Employee | Non-employee (director, consultant) |
|---|---|---|
| NSO exercise | Spread is supplemental wages: federal income tax withholding, FICA, FUTA; Form W-2 (box 1, and box 12 code V) | No withholding; spread reported on Form 1099-NEC (box 1) |
| ISO exercise | No withholding or FICA; Form 3921 | Not applicable (ISOs are employee-only) |
| ISO disqualifying disposition | Ordinary income reported on Form W-2; no income tax withholding or FICA (§§ 3121(a)(22), 3401(a)(19)) | — |
| RSA purchased below FMV, or vesting without 83(b) | Wages at 83(b) election or at each vesting date | Form 1099-NEC |
| RSU settlement | Wages at settlement (income tax); FICA when no longer subject to a substantial risk of forfeiture (§ 3121(v)(2)); Form W-2 | Form 1099-NEC |
| Former employee (RSU settles after departure) | Still wages; W-2 | — |

**Supplemental wage withholding.** Federal withholding on supplemental wages may use the optional flat rate (for supplemental wages up to $1 million in the year) and must use the mandatory rate equal to the highest individual rate on supplemental wages above $1 million (Treas. Reg. § 31.3402(g)-1(a)(2) (mandatory rate), (a)(7) (optional flat rate)). **Verify** the current rates in IRS Publication 15 (Circular E) for the year of payment; P.L. 119-21 made the 2017 rate structure permanent, which historically produced a 22% optional rate and a 37% mandatory rate.

**Share withholding up to the maximum statutory rate** does not trigger liability accounting under ASC 718 as amended by ASU 2016-09; withholding above the maximum rate does.

**State withholding and sourcing.** Equity income earned over a vesting or grant-to-vest period while the holder worked in multiple states is generally sourced by workdays in each state (for example, California's allocation rules; New York's allocation rules for options and RSUs). Payroll must track work location history for movers. **Verify** state-specific rules for a mobile workforce.

---

## 13. Accounting (brief)

- **ASC 718** measures awards at **grant-date fair value** (options via Black-Scholes or lattice models, using the 409A common stock value as an input) and recognizes expense over the service period.
- **Grant date for accounting** requires a mutual understanding of the key terms and conditions, which can differ from the tax grant date (for example, if terms are communicated weeks later). Communicate grants promptly.
- **Double-trigger RSUs:** no expense is recognized until the liquidity event is probable (generally at the event), then cumulative catch-up; this produces a large charge in the IPO quarter.
- **Modifications** (repricing, PTEP extensions, acceleration) generally produce incremental cost equal to the excess of the modified award's fair value over the original's immediately before modification.
- **Early-exercise cash** received for unvested shares is recorded as a liability until vesting; shares are not considered outstanding for accounting until vested.

---

## 14. Drafting pitfalls this skill guards against

The following problems recur in simple founder-drafted plans and are the reason the templates are built the way they are:

1. **Blank or "TBD" share reserve.** A plan must state the number of shares (I.R.C. § 422(b)(1); 10 CCR § 260.140.41(a)). The Board must also reserve the shares and confirm the charter authorizes them.
2. **Wrong reason for stockholder approval.** Approval is for ISOs (§ 422(b)(1)), California (10 CCR § 260.140.41(g)), and any charter or investor requirement. Rule 701 has no stockholder-approval requirement.
3. **Missing California terms.** Without the § 260.140.41 terms (120-month term, 30-day and 6-month PTEP floors, adjustments, nontransferability, 10-year grant window, approval with rescission, information), § 25102(o) is unavailable.
4. **Thin corporate-transaction provisions.** The plan must expressly authorize assumption, substitution, continuation, cash-out (including cancellation of underwater awards for no payment), termination after notice, escrow and earnout treatment, and non-uniform treatment, without holder consent.
5. **No separate ISO limit** or a percentage-only ISO limit (Treas. Reg. § 1.422-2(b)(3)).
6. **Delegation without § 157(c) limits.**
7. **Grant dates before the last director signs; prices from stale or superseded 409A reports.**
8. **ISOs to non-employees; no 110%/5-year rule; no $100,000 split; PTEP extensions without ISO warnings.**
9. **No Rule 701 tally or $10 million plan; RSU grants made without pre-grant disclosure once the threshold is crossed.**
10. **No ROFR, market stand-off, or stockholder-agreement joinder for shares issued under the plan.**
11. **Double-trigger RSUs without a hard settlement deadline or with a change-in-control trigger broader than § 409A allows.**
12. **83(b) deadlines left to chance.**

---

## 15. Compliance calendar

| When | Action | Authority |
|---|---|---|
| Before first grant | Board adoption; share reservation; 409A valuation; forms approved | 8 Del. C. §§ 141, 152, 157; Treas. Reg. § 1.409A-1(b)(5)(iv)(B) |
| Within 12 months of adoption | Stockholder approval | I.R.C. § 422(b)(1); 10 CCR § 260.140.41(g) |
| Within 30 days after first California issuance | § 25102(o) notice and fee | Cal. Corp. Code §§ 25102(o), 25608(y) |
| Before first grant in any new state or country | Blue-sky and local law check | State law |
| Each grant | Fresh FMV determination; no material events; Rule 701 tally; ISO checks; Schedule A reconciliation | § 409A; § 422; Rule 701 |
| 30 days after each RSA purchase or early exercise | Holder files 83(b); Company receives copy | I.R.C. § 83(b); Treas. Reg. § 1.83-2 |
| Rolling | Rule 701 12-month sales; $10 million disclosure readiness; financial statements ≤ 180 days old if required | Rule 701(d), (e) |
| Every 12 months, and after material events | 409A refresh | Treas. Reg. § 1.409A-1(b)(5)(iv)(B) |
| By January 31 | Form 3921 to ISO exercisers; Form W-2 and 1099-NEC equity income | I.R.C. §§ 6039, 6051, 6041A |
| By February 28 (paper) / March 31 (electronic) | File Forms 3921 with IRS (next business day if a weekend or holiday) | IRS General Instructions for Certain Information Returns |
| Before 500 optionholders | Rule 12h-1(f) analysis | Exchange Act § 12(g) |
| Annually (California, if not Rule 701-compliant) | Financial statements to California holders | 10 CCR § 260.140.46 |
| Before ISO grant window closes | No ISOs after the 10th anniversary of the earlier of adoption or approval | I.R.C. § 422(b)(2) |
| At IPO preparation | Public-company plan; clawback policy; Form S-8; cheap-stock review | Rule 10D-1; Form S-8; C&DI 271.28 |

---

## 16. Sources

**Primary law and official guidance**

- 26 U.S.C. § 422 (Cornell LII): https://www.law.cornell.edu/uscode/text/26/422
- Treas. Reg. § 1.409A-1 (eCFR): https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR3d5ef5bd7f9b2a4/section-1.409A-1
- Treas. Reg. § 1.422-2 (eCFR): https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR6ecd7af0d8a3ff8/section-1.422-2
- Treas. Reg. § 1.422-3 (eCFR): https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.422-3
- Treas. Reg. § 1.421-1 (eCFR): https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.421-1
- Treas. Reg. § 1.424-1 (eCFR): https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.424-1
- Treas. Reg. § 1.83-2 (eCFR): https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.83-2
- Treas. Reg. § 1.280G-1 (eCFR): https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.280G-1
- IRS Notice 2008-113: https://www.irs.gov/pub/irs-drop/n-08-113.pdf
- IRS Instructions for Forms 3921 and 3922 (Rev. 04/2025): https://www.irs.gov/instructions/i3921
- IRS General Instructions for Certain Information Returns (2025): https://www.irs.gov/instructions/i1099gi
- 17 C.F.R. § 230.701 (eCFR): https://www.ecfr.gov/current/title-17/chapter-II/part-230/subject-group-ECFRd13a0e2e2fbd4b3/section-230.701
- SEC Securities Act Rules Compliance and Disclosure Interpretations, §§ 271.01–271.29 (including March 6, 2026 and October 15, 2026 updates): https://www.sec.gov/rules-regulations/staff-guidance/compliance-disclosure-interpretations/securities-act-rules
- Cal. Code Regs. tit. 10, § 260.140.41 (Cornell LII): https://www.law.cornell.edu/regulations/california/10-CCR-260.140.41
- Cal. Code Regs. tit. 10, § 260.140.42: https://www.law.cornell.edu/regulations/california/10-CCR-260.140.42
- Cal. Code Regs. tit. 10, § 260.140.45: https://www.law.cornell.edu/regulations/california/10-CCR-260.140.45
- Cal. Code Regs. tit. 10, § 260.140.46: https://www.law.cornell.edu/regulations/california/10-CCR-260.140.46
- Cal. Corp. Code § 25102 (California Public Law mirror of leginfo, accessed November 2026): https://california.public.law/codes/ca_corp_code_section_25102
- Cal. Corp. Code § 25608: https://california.public.law/codes/ca_corp_code_section_25608
- 8 Del. C. subch. V (§§ 151–174): https://delcode.delaware.gov/title8/c001/sc05/index.html
- 8 Del. C. subch. VII (§§ 211–233, including § 228): https://delcode.delaware.gov/title8/c001/sc07/index.html

**Secondary sources (market practice; not black-letter law)**

- Carta, Founder Ownership Report 2026 (via Carta data pages and secondary summaries): https://carta.com/data/founder-ownership-2026/
- Carta, post-termination exercise period data and commentary: https://carta.com/blog/pte-90-day-window/
- Baker McKenzie, "Double-Trigger RSUs and the Question of the Seven-Year Term" (2022): https://www.bakermckenzie.com/en/insight/publications/guides/double-trigger-rsus-question-seven-year-term
- Lowenstein Sandler, "Double Vesting Restricted Stock Units" (podcast and materials): https://www.lowenstein.com/news-insights/podcasts-listing/double-vesting-restricted-stock-units
- Goodwin, "Online Filing of Section 83(b) Elections" (July 2025): https://www.goodwinlaw.com/en/insights/publications/2025/07/alerts-practices-erisa-online-filing-of-section-83b-elections
- Morrison Foerster, "Say Goodbye to Paper Cuts: Section 83(b) Elections May Now Be Filed Online" (July 2025): https://www.mofo.com/resources/insights/250724-say-goodbye-to-paper-cuts-section-83-b
- Cooley, "California Reduces Section 409A State Income Tax Penalty" (2013): https://www.cooley.com/news/insight/2013/california-reduces-section-409a-state-income-tax-penalty
- Stradley Ronon, Employee Benefit Plan Review (May 2024), discussion of N.Y. Gen. Bus. Law § 359-f employee plan exemption: https://www.stradley.com/-/media/files/publications/2024/05/employee-benefit-plan-review-no-4-2024-berishajgal.pdf

# Employment, Contractors, and IP Hygiene — Expert Reference

This reference supports the templates in `templates/employment-and-contractors/` and `templates/commercial/` (NDAs). It is written for Claude as the drafter. Law is stated as of **November 2, 2026**. Items marked **Verify** were not confirmed against a primary source on that date or are in active flux; confirm them before relying on them in a finished document. Thresholds that change annually are given with the year they apply.

Use it in this order: (1) identify the worker's status (employee or contractor) and work state; (2) pick the template; (3) check the state-specific sections below for the work state; (4) run the IP chain-of-title checklist at every financing.

---

## 1. Hiring workflow for a Delaware startup

| Step | When | Document or action | Template / authority |
|---|---|---|---|
| 1 | Before posting | Decide employee vs. contractor (Section 6); set a good-faith pay range for pay-transparency jurisdictions (Section 11) | — |
| 2 | Before interviews that reveal confidential information | Candidate NDA (no IP assignment, no restrictive covenants) | `one-way-nda` |
| 3 | During interviews | No salary-history questions in ban states; no criminal-history questions before a conditional offer in fair-chance jurisdictions | Section 12 |
| 4 | Offer | Offer letter with CIIAA attached; separate FCRA disclosure if a background check will be run; separate arbitration agreement if used | `offer-letter`, `ciiaa-employee` |
| 5 | Restrictive-covenant notice periods | Illinois 14 days for non-solicits; Colorado separate notice before acceptance; Massachusetts non-competes 10 business days before start; Oregon non-competes 2 weeks before start; Maine 3 business days; DC 14 days | Section 5 |
| 6 | Acceptance | Signed offer letter and CIIAA (with Exhibit B notices) | — |
| 7 | Day 1 | Form I-9 Section 1; state new-hire notices (CA SB 294 notice and emergency contact; NY Lab. Law § 195(1) pay notice; CA Lab. Code § 2810.5 notice for non-exempt); benefits enrollment | Section 12 |
| 8 | By the 3rd business day | Form I-9 Section 2; E-Verify case if used | 8 C.F.R. § 274a.2(b)(1)(ii) |
| 9 | Within 20 days | State new-hire report (42 U.S.C. § 653a(b)(2)) | — |
| 10 | Next Board grant date | Option grant at 409A fair market value; Rule 701 / state exemption tracking | Section 16 |
| 11 | For executives | Executive employment agreement approved by the Board (and investors if the charter or voting agreement requires) | `executive-employment-agreement` |

For contractors: consulting agreement signed **before** work starts; W-9 before first payment; joinders from each individual who performs work for a contractor entity; California DE 542 within 20 days for contractors paid $600 or more; Form 1099-NEC by January 31 at or above the § 6041(a) threshold ($2,000 for payments after December 31, 2025, Pub. L. 119-21, § 70433, indexed after 2026).

For advisors: advisor agreement, then Board grant (restricted stock or NSO), then § 83(b) election within 30 days of any restricted stock issuance.

For past contributors who never signed proper IP documents: confirmatory assignment (`confirmatory-ip-assignment`) **before** the next financing closes and before any patent enforcement.

---

## 2. At-will employment

- Every state except Montana presumes at-will employment. Preserve it with (a) an express at-will statement, (b) a statement that only a signed writing from the CEO (or Board) can change it, and (c) no language implying a term ("annual salary for the year," "permanent position," "guaranteed").
- **Montana.** Under the Wrongful Discharge from Employment Act, a discharge is wrongful if it is in retaliation for refusing to violate public policy or reporting a violation, if it is not for good cause after the probationary period, if it violates the employer's own express written personnel policy, or if it is solely for lawful free speech (Mont. Code Ann. § 39-2-904). The default probationary period is **12 months**, extendable to an aggregate of **18 months** (§ 39-2-910, added 2021; no 2025 amendment). "Good cause" is defined in § 39-2-903(5). Use the Montana alternative in `offer-letter` § 7.
- Implied-contract and implied-covenant claims are the usual attack on at-will status; handbook disclaimers and integration clauses defeat most of them.
- Severance in an executive agreement does not change at-will status; it prices termination without Cause.

---

## 3. Exempt vs. non-exempt (salary thresholds for 2026)

An employee is exempt from overtime only if the job meets a duties test (executive, administrative, professional, computer, outside sales) **and** the salary test. Equity does not count toward the salary test.

**Federal.** Texas v. U.S. Department of Labor (E.D. Tex. Nov. 15, 2024) vacated the 2024 rule; the Fifth Circuit dismissed the government's appeals in May 2026; DOL restored the 2019 regulatory text by technical amendment (91 Fed. Reg. 27833, May 15, 2026). DOL withdrew its overtime rulemaking (RIN 1235-AA39) from the regulatory agenda on December 15, 2025; no new salary proposal had been published as of November 2, 2026.

| Test | 2026 amount | Cite |
|---|---|---|
| Standard salary level | $684/week ($35,568/year) | 29 C.F.R. § 541.600 |
| Highly compensated employee total annual compensation | $107,432 | 29 C.F.R. § 541.601 |
| Computer employee hourly alternative | $27.63/hour | 29 C.F.R. § 541.400(b) |
| Business owner (20%+ equity, actively engaged in management) | No salary test | 29 C.F.R. § 541.101 |

**States with higher thresholds (2026).**

| State | Exempt salary (2026) | Computer professional | 2027 | Cite |
|---|---|---|---|---|
| California | $70,304/year (2 × $16.90 × 2,080) | $58.85/hour; $10,214.44/month; $122,573.13/year | $72,384; computer $61.03/hour, $127,108.34/year | Lab. Code §§ 515(a), 515.5; DIR |
| New York (executive and administrative only) | $1,275/week ($66,300) NYC, Nassau, Suffolk, Westchester; $1,199.10/week ($62,353.20) elsewhere | No state salary test for professionals (federal applies) | Set by regulation | 12 NYCRR § 142-2.14 |
| Washington | $1,541.70/week ($80,168.40) | $59.96/hour | $1,595.70/week (1–50 employees); $1,773/week (51+) | WAC 296-128-545; WSR 25-20-098 |
| Colorado | $1,111.23/week ($57,784) | $34.85/hour | Not yet published | 2026 PAY CALC Order, 7 CCR 1103-14 (adopted Dec. 8, 2025; eff. Feb. 1, 2026) |

**Founders.** A founder-employee who owns at least 20% of the equity and is actively engaged in management is exempt under federal law without a salary (29 C.F.R. § 541.101), but California and several other states have no equivalent owner exception for minimum wage and salary-basis rules. A founder who is an employee in California and takes no salary is a wage-and-hour risk. **Verify** the founder's state before advising a zero-salary arrangement; the conservative course is to pay at least the state exempt minimum or to have the founder serve only as an unpaid officer and director (not an employee) until funding.

---

## 4. Invention assignment statutes

Eleven states regulate employee invention-assignment agreements. All five notice states require written notice "at the time the agreement is made." The CIIAA's Exhibit B quotes every statute and is attached for all employees.

| State | Cite | What is excluded from assignment | Carve-backs (employer still owns) | Written notice required? | Notes |
|---|---|---|---|---|---|
| California | Lab. Code §§ 2870–2872 | Inventions developed entirely on the employee's own time without the employer's equipment, supplies, facilities, or trade secret information | Relates at conception or reduction to practice to the employer's business or actual or demonstrably anticipated R&D; or results from work performed for the employer | **Yes** (§ 2872) | Employer may require confidential disclosure and review, and U.S. government title (§ 2871); employee bears burden of proof |
| Delaware | 19 Del. C. § 805 | Same structure as California | Relates to the employer's business or actual or demonstrably anticipated R&D; or results from work for the employer | No | Cannot be a condition of employment |
| Illinois | 765 ILCS 1060/2 | No employer equipment, supplies, facilities, or trade secret information used, and developed entirely on own time | Relates to employer's business or R&D; or results from work for employer | **Yes** (§ 2(3)) | Employee bears burden; common-law shop rights preserved for employees without an agreement |
| Kansas | K.S.A. 44-130 | Same as Illinois | Relates to the business (notice says "relates directly") or R&D; or results from work | **Yes** (§ 44-130(c)) | Employee must disclose all inventions being developed (§ 44-130(d)) |
| Minnesota | Minn. Stat. § 181.78 | No employer resources and developed entirely on own time, and does not relate *directly* to the business or R&D, **or** does not result from work | Drafted in the negative with "or" — read literally, broader for the employee | **Yes** (subd. 3) | Quote verbatim; do not normalize |
| Nevada | NRS 600.500 | Not an exclusion statute | Employer is sole owner of patentable inventions and trade secrets developed in the course and scope of employment that relate directly to that work, absent a written agreement otherwise | No | Employer-favorable default; does not cover copyright |
| New Jersey | N.J.S.A. 34:1B-265 (eff. Apr. 1, 2018) | Own time and without the employer's equipment, supplies, facilities, **or information** (including trade secrets) | Relates to employer's business or R&D; or results from work on behalf of employer | No | Broader than California ("information"); employer may require confidential disclosure and review |
| New York | Lab. Law § 203-f (eff. Sept. 15, 2023) | Same as California | Same as California | No | No condition-of-employment clause |
| North Carolina | G.S. §§ 66-57.1, 66-57.2 | Same as Delaware | Same | No | Employer may require reporting of all inventions, including those claimed as nonassignable; vested ownership not rescindable over pay disputes |
| Utah | Utah Code §§ 34-39-2, 34-39-3 | Only inventions created entirely on own time **and** not an "employment invention" | "Employment invention" includes anything within the scope of employment, on the employer's time, with any employer resources, resulting from work, or *related to the industry or trade of the employer* | No | Most employer-favorable; employment is sufficient consideration (§ 34-39-3(5)); amended by 2025 Utah Laws ch. 302 (effective May 7, 2025; the CIIAA's Exhibit B quotes the current text) (**Verify** whether the 2025 changes were substantive) |
| Washington | RCW 49.44.140, 49.44.150 | Same as Illinois | Relates *directly* to the business, or to R&D; or results from work | **Yes** (§ 49.44.140(3)) | Employee must disclose all inventions (§ 49.44.150) |

No additional state enacted an employee-invention statute in 2023–2026 other than New York (search not exhaustive — **Verify** with a 50-state survey before publication of any new form).

**Drafting rules.**
1. Use "hereby assigns, and agrees to assign" (Section 8).
2. Exclude "Nonassignable Inventions" by reference to the statute, or (the default in `ciiaa-employee`) apply the California standard to every employee by contract.
3. Require confidential disclosure of all inventions so the Company can evaluate claimed exclusions (permitted in CA, KS, NJ, NC, WA).
4. Attach Exhibit B to every CIIAA.
5. Do not add post-employment "trailer" clauses for California employees (Whitewater West Indus., Ltd. v. Alleshouse, 981 F.3d 1045 (Fed. Cir. 2020), held such a clause void under Bus. & Prof. Code § 16600 when not limited to use of trade secrets).

---

## 5. Non-competes and non-solicits

**Default posture for all templates:** no employee non-compete; employee non-solicit optional and state-limited; customer non-solicit rarely and only where lawful; rely on trade-secret law and confidentiality.

### 5.1 Federal

- **FTC rule is gone.** The 2024 Non-Compete Clause Rule (16 C.F.R. part 910) was set aside in Ryan LLC v. FTC, No. 3:24-cv-00986-E (N.D. Tex. Aug. 20, 2024) and never took effect. On September 5, 2025, the FTC voted 3–1 to dismiss its appeals (5th Cir. No. 24-10951; 11th Cir. No. 24-13102) and accede to vacatur. It removed part 910 from the CFR effective February 12, 2026 (91 Fed. Reg. 6507).
- **Case-by-case enforcement continues** under FTC Act § 5: Gateway Services consent order (proposed September 4, 2025; final decision and order November 25, 2025, announced November 26; freed about 1,800 workers from a one-year nationwide non-compete); Adamas no-hire order (final February 12, 2026); Rollins Inc. (Orkin) consent order (proposed April 15, 2026; final June 22, 2026; over 18,000 workers) with 13 warning letters to other pest-control firms; warning letters to healthcare employers and staffing firms (September 10, 2025) and to Mortgage Connect (May 8, 2026); request for information (docket FTC-2025-0463, comments closed November 3, 2025); workshop January 27, 2026.
- **NLRB.** GC 25-05 (February 14, 2025) rescinded the prior General Counsel's non-compete memo (GC 23-08) and stay-or-pay memo (GC 25-01). A 2026 Advice memorandum (Biotricity) found non-competes lawful.

### 5.2 States that ban employee non-competes

| State | Cite | Scope | Exceptions |
|---|---|---|---|
| California | Bus. & Prof. Code §§ 16600, 16600.1, 16600.5 | Void "no matter how narrowly tailored"; void "regardless of where and when the contract was signed" (§ 16600.5(a)); entering into or attempting to enforce one is a civil violation with a private right of action and fees (§ 16600.5(d)–(e)); individualized notice to current and certain former employees was due February 14, 2024 (§ 16600.1) | Sale of business goodwill or ownership interest; partnership and LLC dissolution (§§ 16601–16602.5) |
| Minnesota | Minn. Stat. § 181.988 | Void for employees and independent contractors, agreements on or after July 1, 2023; non-disclosure and non-solicitation agreements excluded | Sale or dissolution of a business |
| North Dakota | N.D. Cent. Code § 9-08-06 | Any restraint on a lawful profession void | Sale of goodwill; dissolution or sale of ownership interest |
| Oklahoma | 15 O.S. §§ 217, 219A, 219B | Non-competes void; former employee may not directly solicit **established** customers (§ 219A); employee and contractor non-solicits enforceable (§ 219B) | — |
| Wyoming | W.S. § 1-23-108 (SF 107, 2025) | Void for contracts entered into on or after July 1, 2025 | Sale of business; trade-secret protection; recovery of relocation, education, and training costs on a sliding scale; **executive and management personnel and their professional staff**; physicians barred |
| Washington (from **June 30, 2027**) | ESHB 1155, ch. 149, Laws of 2026 (signed March 23, 2026) | All non-competes void regardless of when signed; enforcing, threatening, or entering one is a violation ($5,000 or actual damages plus fees; AG enforcement); clauses barring *acceptance* of customer business, and **any forfeiture, repayment, or clawback triggered by competing**, are non-competes; written notice to affected current and former workers by October 1, 2027 | Sale or purchase of 1%+ ownership interest; franchisees; pro-rata education-repayment agreements expiring within 18 months; NDAs and trade-secret and invention covenants; non-solicits (customer non-solicits limited to customers with whom the employee established or substantially developed a direct relationship, max 18 months) |

New York: no statutory ban. S4641-A passed the Senate in June 2025 and died; S9759/A10023 passed the Senate on June 3, 2026 (exempting earners of $500,000+) and was pending in the Assembly Labor Committee as of November 2, 2026. **Verify** before advising a New York employer.

### 5.3 Income-threshold and category states (2026)

| State | Cite | Rule | 2026 threshold | Notice / timing | Other |
|---|---|---|---|---|---|
| Washington (until June 29, 2027) | RCW 49.62 | Void unless earnings exceed threshold | Employees **$126,858.83**; contractors **$317,147.09** (2027 through June 29: $131,326.59 / $328,316.49) | Disclose terms in writing no later than acceptance; later covenants need independent consideration | Laid-off employees must be paid base salary for the restricted period; >18 months presumed unreasonable; no-acceptance clauses are non-competes (2024 c 36) |
| Oregon | ORS 653.295 | Salaried, exempt, above threshold at termination | **$119,541** | Written notice in offer at least 2 weeks before start (or on bona fide advancement); signed copy within 30 days after termination | 12-month cap; non-compliant agreements void; employer may instead pay greater of 50% of salary or 50% of threshold |
| Illinois | 820 ILCS 90 | Non-compete void at or below threshold; non-solicit (employees **and** customers) void at or below its threshold | Non-compete **> $75,000**; non-solicit **> $45,000** (from January 1, 2027: $80,000 / $47,500) | Copy 14 calendar days before start or 14 days to review; written advice to consult an attorney (§ 20) | "Adequate consideration": 2 years of employment after signing or other professional or financial benefits (§ 5); employee recovers fees if employee prevails |
| Colorado | C.R.S. § 8-2-113 | Non-compete only for highly compensated workers, at signing and enforcement, for trade-secret protection; customer non-solicit at 60% of threshold | **$130,014**; customer non-solicit **$78,008.40** | Separate signed notice before acceptance (new hires) or 14 days before effectiveness (current workers) (§ 8-2-113(4)) | $5,000 per worker penalty; Colorado law and forum for workers who primarily lived or worked in Colorado at termination (§ 8-2-113(6)); SB 25-083 (eff. Aug. 6, 2025) adds health-care bans and caps equity-holder sale covenants |
| Massachusetts | M.G.L. c. 149, § 24L | Not enforceable against FLSA non-exempt employees, students, those 18 or under, or employees terminated without cause or laid off | No dollar threshold | Earlier of formal offer or 10 business days before start; mid-employment covenants need independent consideration and 10 business days; signed by both; states right to counsel | 12-month cap; garden leave of at least 50% of highest base pay in prior 2 years, or other mutually agreed consideration; non-solicits excluded; Massachusetts law and venue if employee lived or worked there 30 days before leaving |
| Maine | 26 M.R.S. § 599-A | Barred at or below 400% of federal poverty level | **$63,840** (400% × $15,960, 2026 HHS guideline) | Disclose before offer; copy 3 business days before signing | Effective only after 1 year of employment or 6 months after signing, whichever is later; health-care and veterinary bans (2026) |
| Maryland | Lab. & Empl. § 3-716 | Void at or below 150% of state minimum wage | **$22.50/hour (≈ $46,800)** | — | Health-care limits from July 1, 2025; statewide minimum wage still $15.00 in 2026 (Lab. & Empl. § 3-413(c)), so some 2026 roundups' $49,920 figure is wrong |
| Virginia | Va. Code § 40.1-28.7:8 | Void for "low-wage employees" — below the state average weekly wage **or any FLSA non-exempt employee** (since July 1, 2025) | **$1,507.01/week (≈ $78,364.52)** | Must post a copy of the section or DOLI summary | From July 1, 2026: unenforceable after a without-cause termination unless disclosed severance is paid (SB 170); health-care professional bans (2026); $10,000 per violation |
| New Hampshire | RSA 275:70, 275:70-a | Copy before acceptance; banned for low-wage employees (≤ 200% of federal minimum wage) | **$14.50/hour (≈ $30,160)** | Before acceptance of offer | — |
| Rhode Island | R.I. Gen. Laws § 28-59-3 | Unenforceable against non-exempt employees, student interns, those 18 or under, and low-wage employees (≤ 250% FPL) | **$39,900** | — | Non-solicits and NDAs excluded |
| District of Columbia | D.C. Code § 32-581.01 et seq. | Only for highly compensated employees | **$162,164**; medical specialists **$270,274** | Provide 14 days before start or before execution; statutory notice text (**Verify** exact text) | Max 365 days (730 for medical specialists) |
| Tennessee | T.C.A. §§ 50-1-210, -211 (HB 1034/SB 995, 2026 Tenn. Pub. Acts ch. 934, approved May 7, 2026; eff. July 1, 2026, for agreements entered, renewed or amended on or after that date) | No non-compete for employees with annualized pay under **$70,000** | $70,000 | — | ≤ 2 years presumed reasonable for employees; non-solicits and NDAs not subject to the threshold (**Verify** this last point against the act's text) |
| Nevada | NRS 613.195 | Void for hourly-only employees; cannot bar serving customers who seek out the employee unsolicited | — | — | After a reduction in force, enforceable only while severance is paid; **courts must revise** overbroad covenants |
| Louisiana | La. R.S. 23:921 | Void unless within an exception; up to 2 years within specified parishes or municipalities | — | — | Choice of forum or law void unless ratified after the dispute arises |
| Georgia | O.C.G.A. § 13-8-50 et seq. | Non-competes only for employees who solicit customers, sell, manage, or are key employees or professionals | — | — | ≤ 2 years presumed reasonable; courts may modify (**Verify** text) |
| Florida | Fla. Stat. § 542.335; CHOICE Act, §§ 542.41–.45 (2025) | Pro-enforcement: covered non-compete and garden-leave agreements up to 4 years for employees earning more than 2× the county annual mean wage | — | 7 days to review; written advice of right to counsel; acknowledgment | Mandatory preliminary injunction; applies to Florida-based employees regardless of choice of law (§§ 542.44(1), 542.45(1)); Laws of Fla. ch. 2025-213 states an effective date of July 1, 2025 and became law without the Governor's approval on July 3, 2025 |

Health-care-specific laws (2025–2026) exist in Texas (SB 1318, Bus. & Com. Code §§ 15.50, 15.501, eff. Sept. 1, 2025), Pennsylvania, Indiana, Arkansas, Utah, New Hampshire, Iowa, Colorado, Maine, Maryland, and Virginia. **Verify** before advising any health-care employer.

### 5.4 Non-solicitation limits

| State | Employee non-solicit | Customer non-solicit |
|---|---|---|
| California | Void (AMN Healthcare, Inc. v. Aya Healthcare Servs., Inc., 28 Cal. App. 5th 923 (2018)) | Void except, arguably, to protect trade secrets (Edwards v. Arthur Andersen LLP, 44 Cal. 4th 937 (2008)) |
| North Dakota | A narrowly drawn no-raid clause is not void (Warner & Co. v. Solberg, 2001 ND 156, ¶ 25, 634 N.W.2d 65); conservative practice still omits it | Void, including clauses barring acceptance of customers who come unsolicited (id. ¶¶ 22, 24) |
| Oklahoma | Enforceable (§ 219B) | Only direct solicitation of established customers (§ 219A) |
| Minnesota | Permitted (excluded from § 181.988) | Permitted; but § 181.9881 voids service-provider clauses barring *customers* from soliciting or hiring the provider's employees (agreements from July 1, 2024) |
| Colorado | Not expressly addressed; unsettled | Only at 60% of threshold, for trade secrets, with separate notice |
| Illinois | Only above $45,000 ($47,500 from 2027), with 14-day review and counsel advice | Same |
| Washington | Permitted | Current customers now; from June 30, 2027, only customers with whom the employee established or substantially developed a direct relationship, max 18 months; no-acceptance clauses prohibited |
| Massachusetts, Oregon, Rhode Island, Tennessee | Excluded from the non-compete statutes; common-law reasonableness | Same |
| Virginia | Unenforceable against low-wage employees under Sentry Force Security, LLC v. Barrera, No. 1405-24-4 (Va. Ct. App. Jan. 27, 2026) (unpublished; appeal to the Supreme Court of Virginia pending) (**Verify** status) | Cannot restrict serving customers who approach a low-wage employee |

### 5.5 Anti-evasion choice-of-law and forum rules

- **California:** Lab. Code § 925 (employees who primarily reside and work in California may void out-of-state forum or law clauses imposed as a condition of employment unless individually represented by counsel in negotiating them; contracts entered into, modified, or extended on or after January 1, 2017); Bus. & Prof. Code § 16600.5.
- **Colorado:** § 8-2-113(6). **Washington:** RCW 49.62.050 (unchanged by ESHB 1155). **Minnesota:** § 181.988, subd. 3. **Massachusetts:** § 24L(e). **Louisiana:** R.S. 23:921(A)(2). **Florida:** § 542.45(1) (pro-enforcement). **Illinois:** no anti-evasion clause in the Freedom to Work Act; ordinary conflicts rules apply.

Practice: govern employment documents by the law of the employee's work state.

---

## 6. Worker classification

| Regime | Test | Status (Nov. 2026) | Authority |
|---|---|---|---|
| IRS (employment taxes) | Common-law control: behavioral, financial, relationship | Stable | 26 U.S.C. § 3121(d)(2); Rev. Rul. 87-41; IRS guidance |
| FLSA | Economic reality (economic dependence vs. in business for oneself) | 2024 rule (29 C.F.R. part 795; 89 Fed. Reg. 1638) remains in CFR and governs private litigation per DOL, but WHD enforcement uses Fact Sheet #13 (2008) and Opinion Letter FLSA2019-6 (FAB 2025-1, May 1, 2025); NPRM to rescind and restore a 2021-style two-core-factor test published February 27, 2026 (91 Fed. Reg. 9932); no final rule yet | **Verify** for a final rule |
| NLRA | Common-law agency test (Atlanta Opera, 372 NLRB No. 95 (2023)) | Still Board law; Republican members (Murphy, Mayer) have held a 2–1 majority since early 2026, and a three-member Republican majority since Member Macy was sworn in on August 17, 2026 | **Verify** |
| California (wage orders, Labor Code, UI) | ABC test (Lab. Code § 2775); exemptions fall back to Borello | B2B (§ 2776, 12 criteria), professional services (§ 2778, amended eff. Jan. 1, 2026) | Dynamex (2018); Borello (1989) |
| Massachusetts (wage law) | Strict ABC test | Stable | M.G.L. c. 149, § 148B |
| New Jersey (UI, wage-hour, wage-payment) | ABC test | N.J.A.C. 12:11 adopted (58 N.J.R. 1587(a)), effective June 1, 2026, operative October 1, 2026 | Hargrove v. Sleepy's, LLC, 220 N.J. 289 (2015) |
| Illinois | ABC-style tests in Wage Payment and Collection Act (820 ILCS 115/2) and UI (820 ILCS 405/212) | **Verify** text | — |
| Connecticut and many others (UI only) | ABC test | — | Conn. Gen. Stat. § 31-222 |

**California ABC test.** (A) free from control and direction, under contract and in fact; (B) work outside the usual course of the hiring entity's business; (C) customarily engaged in an independently established trade, occupation, or business of the same nature. Prong B is usually dispositive for a startup engaging an individual to do its core work.

**Business-to-business exemption (Lab. Code § 2776) — all twelve required:** (1) free from control and direction; (2) provides services directly to the contracting business, not its customers; (3) written contract specifying payment amount, rate, and due date; (4) holds any required business license and tax registration; (5) maintains a business location separate from the hiring entity (may be the residence); (6) customarily engaged in an independent business of the same nature; (7) can contract with other businesses and is not restricted from doing so; (8) advertises and holds itself out to the public; (9) provides its own tools, vehicles, and equipment; (10) can negotiate its own rates; (11) can set its own hours and location (consistent with the work's nature); (12) not performing work requiring a contractor's license.

**Consequences of misclassification.** Back payroll taxes and penalties (with § 3509 reduced rates if not intentional); FLSA back pay plus liquidated damages; state wage-and-hour penalties (California Lab. Code § 226.8: $5,000–$15,000 per violation, $10,000–$25,000 for a pattern or practice); PAGA; expense reimbursement; benefit-plan claims; workers' compensation and UI assessments.

**Remediation.** Section 530 relief (reporting consistency, substantive consistency, reasonable basis; Pub. 1976); IRS Voluntary Classification Settlement Program (Form 8952, filed at least 120 days before reclassification; 10% of one year's employment tax at § 3509(a) rates; requires prior 1099 filing for three years and no current audit); reclassify prospectively as employees and obtain confirmatory IP assignments if the original contract was weak.

---

## 7. Copyright: work made for hire and why a present assignment is still needed

- **Employees.** A work prepared by an employee within the scope of employment is a work made for hire; the employer is the author and owner (17 U.S.C. §§ 101, 201(b)). Scope-of-employment disputes (off-hours work, pre-start-date work, side projects, founders before incorporation) are common, so the CIIAA also presently assigns.
- **Non-employees.** A commissioned work is a work made for hire only if it falls within one of nine categories — a contribution to a collective work, part of a motion picture or other audiovisual work, a translation, a supplementary work, a compilation, an instructional text, a test, answer material for a test, or an atlas — **and** the parties expressly agree in a signed writing (17 U.S.C. § 101). Software and most startup deliverables do not qualify. Ownership passes only by a signed written transfer (17 U.S.C. § 204(a)).
- **The California trap.** A person who contracts for a specially ordered or commissioned work under a signed writing stating it is a work made for hire (and obtains all copyright rights) is the creator's **employer** for California workers' compensation (Lab. Code § 3351.5(c)) and unemployment insurance (Unemp. Ins. Code §§ 686, 621(d)) purposes. Never use work-made-for-hire language in a California contractor agreement; use a present assignment only.
- **Moral rights.** Federal moral rights (VARA, 17 U.S.C. § 106A) apply only to "works of visual art" (not works made for hire) and may be waived only by a signed writing that specifically identifies the work and uses (§ 106A(e)(1)). Foreign moral rights may be unwaivable; forms include a waiver plus a covenant not to assert and an exclusive license fallback.
- **Recordation.** Recording a transfer of a registered work gives constructive notice; between conflicting transfers, the first executed prevails if recorded within one month after execution (two months if abroad) or before the later transfer is recorded (17 U.S.C. § 205(c)–(d)).
- **AI-generated material.** Material generated by AI without sufficient human authorship is not copyrightable under current U.S. Copyright Office guidance; templates require contractors to identify AI-generated portions and to use tools whose terms pass output rights to the user.

---

## 8. Patent assignment

- **Inventors own their inventions.** "[M]ere employment is [not] sufficient to vest title to an employee's invention in the employer" (Bd. of Trustees of Leland Stanford Junior Univ. v. Roche Molecular Sys., Inc., 563 U.S. 776, 789 (2011)); the Bayh-Dole Act does not automatically vest title in a federal contractor (id. at 780).
- **"Agree to assign" vs. "hereby assign."** "[T]he contract language 'agree to assign' reflects a mere promise to assign rights in the future, not an immediate transfer of expectant interests," while "do hereby assign" effects a present assignment of future inventions (Stanford v. Roche, 583 F.3d 832, 841–42 (Fed. Cir. 2009) (citing IpVenture, Inc. v. Prostar Computer, Inc., 503 F.3d 1324, 1327 (Fed. Cir. 2007); Arachnid, Inc. v. Merit Indus., Inc., 939 F.2d 1574, 1580–81 (Fed. Cir. 1991))). Once an invention is made under a present assignment of future rights, legal title vests in the assignee automatically and the inventor has "nothing remaining to assign" (FilmTec Corp. v. Allied-Signal, Inc., 939 F.2d 1568, 1572 (Fed. Cir. 1991)). The Supreme Court did not review this construction (563 U.S. at 784 n.2), and three Justices questioned the FilmTec rule (id. at 794 (Sotomayor, J., concurring); id. at 799–803 (Breyer, J., joined by Ginsburg, J., dissenting)); it remains Federal Circuit law. Use "hereby assigns, and agrees to assign."
- **Writing and recording.** Patents and applications are assignable "by an instrument in writing"; an unrecorded assignment is void against a later purchaser or mortgagee for value without notice unless recorded in the USPTO within three months from its date or before the later purchase (35 U.S.C. § 261). A notarial acknowledgment is prima facie evidence of execution (id.).
- **Joint owners.** Each co-owner may make, use, sell, and license without consent of or accounting to the others (35 U.S.C. § 262); all co-owners generally must join an infringement suit. An unassigned co-inventor is therefore a material diligence defect.
- **Nunc pro tunc.** "[N]unc pro tunc assignments are not sufficient to confer retroactive standing" (Enzo APA & Son, Inc. v. Geapag A.G., 134 F.3d 1090, 1093–94 (Fed. Cir. 1998)). Confirmatory assignments must be signed before suit is filed.
- **University and prior-employer rights.** Founders who are (or recently were) faculty, students, postdocs, or employees elsewhere may be bound by institutional IP policies or present-assignment clauses that already vested title in the institution or prior employer. A confirmatory assignment from the founder does not cure that; obtain a release or license from the institution.

---

## 9. Defend Trade Secrets Act notice

- **Immunity.** An individual is immune from criminal and civil liability under federal or state trade secret law for disclosing a trade secret (A) in confidence to a federal, state, or local government official, directly or indirectly, or to an attorney, solely for the purpose of reporting or investigating a suspected violation of law, or (B) in a complaint or other document filed under seal (18 U.S.C. § 1833(b)(1)); and in an anti-retaliation lawsuit, the individual may disclose the trade secret to the individual's attorney and use it in court if filed under seal and not otherwise disclosed except by court order (§ 1833(b)(2)).
- **Notice.** An employer "shall provide notice of the immunity … in any contract or agreement with an employee that governs the use of a trade secret or other confidential information" (§ 1833(b)(3)(A)), or cross-reference a policy document setting out the employer's reporting policy (§ 1833(b)(3)(B)). Applies to contracts entered into or updated after May 11, 2016 (§ 1833(b)(3)(D)).
- **Consequence of omission.** The employer may not recover exemplary damages or attorney fees under § 1836(b)(3)(C)–(D) against an employee who did not receive notice (§ 1833(b)(3)(C)). The contract is not otherwise impaired.
- **"Employee" includes contractors and consultants** (§ 1833(b)(4)). Include the notice in CIIAAs, consulting agreements, advisor agreements, NDAs with individuals, and confirmatory assignments with individual contractors.

---

## 10. Protected activity carve-outs (confidentiality, non-disparagement, releases)

| Rule | What it requires | Status (Nov. 2026) |
|---|---|---|
| SEC Rule 21F-17(a), 17 C.F.R. § 240.21F-17(a) | "No person may take any action to impede an individual from communicating directly with the Commission staff about a possible securities law violation, including enforcing, or threatening to enforce, a confidentiality agreement …" | Active enforcement: seven settled actions (Press Release 2024-118, Sept. 9, 2024, about $3.04 million, mainly for award-waiver clauses); In re Foot Locker, Inc., Exchange Act Rel. No. 105542 (May 22, 2026) ($148,000; award-waiver clause in about 148 separation agreements). **Never waive SEC or other government awards; never require notice to the company before reporting.** |
| NLRA § 7 (29 U.S.C. § 157) — work rules | Stericycle, Inc., 372 NLRB No. 113 (Aug. 2, 2023): a rule that has a reasonable tendency to chill § 7 activity is presumptively unlawful unless narrowly tailored to a legitimate interest | Still Board law. GC Memo 26-04 (Aug. 26, 2026) names Honeywell International Inc. (09-CA-327389) as a vehicle to overrule; Tesla, Inc., 375 NLRB No. 63 (Oct. 28, 2026) decided an IT-use policy under Caesars Entertainment. **Verify** before relying on narrower drafting |
| NLRA — severance agreements | McLaren Macomb, 372 NLRB No. 58 (Feb. 21, 2023): *offering* a non-supervisory employee a severance agreement with broad confidentiality or non-disparagement terms that restrict § 7 rights is unlawful | Still Board law: applied as "extant precedent" in Prime Communications, LP, 374 NLRB No. 88 (Apr. 7, 2026), with two members open to reconsideration; GC 26-04 names Valley Radiology, P.A. (10-CA-324512) as the vehicle to overrule. GC 25-05 (Feb. 14, 2025) rescinded GC 23-05's safe-harbor guidance. Board: Chairman Murphy, Members Mayer, Macy (Republicans), Prouty (Democrat); one vacancy; GC Crystal S. Carey (confirmed Dec. 18, 2025) |
| Speak Out Act, Pub. L. 117-224, 42 U.S.C. §§ 19401–19404 | "With respect to a sexual assault dispute or sexual harassment dispute, no nondisclosure clause or nondisparagement clause agreed to before the dispute arises shall be judicially enforceable in instances in which conduct is alleged to have violated Federal, Tribal, or State law" (§ 19403(a)); trade secrets and proprietary information preserved (§ 19403(d)) | Applies to claims filed on or after Dec. 7, 2022 |
| California | Gov. Code § 12964.5: agreements related to employment (as a condition of employment or for a raise or bonus) and separation agreements may not restrict disclosure of information about unlawful acts in the workplace, and must include, in substantial form: "Nothing in this agreement prevents you from discussing or disclosing information about unlawful acts in the workplace, such as harassment or discrimination or any other conduct that you have reason to believe is unlawful." (§ 12964.5(a)(1)(B)(ii) (employment); (b)(1)(B) (separation)); separation agreements must notify the employee of the right to consult an attorney and give at least five business days (§ 12964.5(b)(4)); severance amount may be confidential (§ 12964.5(e)). Also Lab. Code §§ 232, 232.5, 1102.5; Civ. Code § 1670.11; Code Civ. Proc. §§ 1001, 1002, 1002.5 | Unchanged since SB 331 (eff. Jan. 1, 2022) |
| New York | Gen. Oblig. Law § 5-336 (amended Nov. 17, 2023): confidentiality of underlying facts of discrimination, harassment, or retaliation claims only at the complainant's preference, with up to 21 days to consider and 7 days to revoke; unenforceable if it requires liquidated damages, forfeiture of consideration, or an affirmative statement that no discrimination occurred; employment agreements (on or after Jan. 1, 2020) barring disclosure of future discrimination facts must carve out law enforcement, EEOC, State Division of Human Rights, Attorney General, local human rights commissions, and the employee's attorney (§ 5-336(2)) | C.P.L.R. 5003-b (settled litigation) not amended; still refers to 21 days |
| Illinois | Workplace Transparency Act, 820 ILCS 96, as amended by P.A. 104-0320 (eff. Jan. 1, 2026): employment contracts' unilateral confidentiality terms must preserve rights to report to agencies and officials, participate in proceedings, make legally required disclosures, obtain confidential legal advice, and engage in concerted activity (§ 1-25); separation agreement confidentiality about unlawful employment practices only if employee's documented preference, mutually beneficial, notice of right to counsel, **separate consideration**, no waiver of future claims, 21 days to consider, 7 days to revoke (waivable) (§ 1-30) | In force |
| Washington | Silenced No More Act, RCW 49.44.211: voids NDA and non-disparagement provisions about conduct reasonably believed to be illegal discrimination, harassment, retaliation, wage-and-hour violations, sexual assault, or against clear public policy; settlement amount may be confidential; greater of actual damages or $10,000 plus fees | No 2025–2026 amendment in force |
| Colorado | POWR Act, C.R.S. § 24-34-407 (agreements entered into or renewed on or after Aug. 7, 2023): nondisclosure provisions limiting disclosure of alleged discriminatory or unfair employment practices void unless mutual, with express carve-outs (family, religious advisor, medical and mental health providers, therapeutic support group, counsel, financial advisor, tax preparer; any government agency without notice; legal process without notice; as required by law), a statement that such disclosure is not disparagement, no unreasonable liquidated damages, and a signed addendum attesting compliance; actual damages plus $5,000 per violation | Reach over ordinary employment confidentiality clauses unsettled (**Verify**) |
| Minnesota | Minn. Stat. § 363A.31, subd. 2: release of MHRA claims may be rescinded within 15 calendar days; written notice of the right required | In force |

**Drafting pattern used in all templates:** a "Protected Activity" clause listing agency communications (no notice to the company), award rights, truthful testimony, § 7 activity, disclosures of unlawful conduct, legally required disclosures, and confidential legal advice; the California sentence verbatim; the DTSA notice; and state-specific add-ons.

---

## 11. Pay transparency and salary-history bans

Offer letters do not themselves satisfy posting rules, but every offer in a covered jurisdiction should be consistent with the posted range, and several laws require disclosure to applicants on request or before discussing pay.

| Jurisdiction | Cite | Effective | Covered employers | Requirement |
|---|---|---|---|---|
| California | Lab. Code § 432.3 (SB 1162; SB 642, 2025) | Jan. 1, 2023; SB 642 amendments Jan. 1, 2026 | Postings: 15+; on request: all | Pay scale in postings; to applicants on reasonable request and to employees on request; "pay scale" = good-faith estimate of the range the employer reasonably expects to pay; penalties $100–$10,000. Salary-history ban. Equal Pay Act limitations and look-back in Lab. Code § 1197.5(i) |
| Colorado | C.R.S. § 8-5-201 | Jan. 1, 2021 (amended 2024) | 1+ in Colorado | Range and benefits in postings; promotional-opportunity notices (**Verify** benefits details) |
| Washington | RCW 49.58.110 (SSB 5408, 2025) | Jan. 1, 2023; amendments July 27, 2025 | 15+ | Range and benefits in postings; 5-business-day cure period through July 27, 2027; damages $100–$5,000 |
| New York State | Lab. Law § 194-b | Sept. 17, 2023 | 4+ | Range in postings |
| New York City | Admin. Code § 8-107(32) | Nov. 1, 2022 | 4+ | Range in postings; salary-history ban (§ 8-107(25)) |
| Illinois | 820 ILCS 112/10(b-25) | Jan. 1, 2025 | 15+ (counted nationwide) | Range and benefits in postings (link permitted) |
| Minnesota | Minn. Stat. § 181.173 | Jan. 1, 2025 | 30+ in Minnesota | Range and benefits; no open-ended ranges |
| Maryland | Lab. & Empl. § 3-304.2 | Oct. 1, 2024 | All | Range, benefits, other compensation in postings; before pay discussions and on request |
| Hawaii | HRS § 378-2.4 | Jan. 1, 2024 | 50+ | Range in postings (**Verify**) |
| District of Columbia | D.C. Code § 32-1453.01 | June 30, 2024 (**Verify** date) | All | Range in postings; health-benefits disclosure before first interview |
| Vermont | 21 V.S.A. § 495p | July 1, 2025 | 5+ | Range in advertisements |
| New Jersey | P.L. 2024, c. 91 | June 1, 2025 | 10+ over 20 weeks | Range and benefits in postings (**Verify** status of proposed 60% range-width rule) |
| Massachusetts | M.G.L. c. 149, § 105F | Oct. 29, 2025 | 25+ in Massachusetts | Range in postings; on promotion or transfer; on request |
| Virginia | Va. Code § 40.1-28.7:12 (SB 215 / HB 636, 2026 Va. Acts cc. 996, 1063) | July 1, 2026 | All | Range in postings; salary-history ban; 15-business-day cure |
| Maine | 26 M.R.S. § 622-A (LD 54, P.L. 2026, ch. 771) | July 29, 2026 | 10+ | Range in postings; on request |
| Connecticut | Conn. Gen. Stat. § 31-40z (P.A. 26-12) | Oct. 1, 2026 | 1+ | Range and benefits in postings; to applicants before pay discussion; to employees at hire, on change, and on first request; P.A. 26-12 § 4 also extends the existing ban on required employment promissory notes (§ 31-51r, previously limited to employers with 26 or more employees) to all employers for notes executed on or after Oct. 1, 2026 |
| Delaware | HS 2 for HB 105 (2025), 85 Del. Laws c. 228 | Sept. 26, 2027 | More than 25 (25 or fewer exempt) | Range and benefits (**Verify** code section and headcount basis) |
| Cleveland, Ohio | City ordinance | Oct. 27, 2025 | 15+ | Range in postings; salary-history ban |
| Columbus, Ohio | Ord. 2898-2025 | Enforced Jan. 1, 2027 | 15+ | Range in postings |

States that require disclosure to applicants without a posting requirement include Nevada (NRS 613.133(2): the range must be given to every applicant who completes an interview, and to employees seeking a promotion or transfer on request) and Rhode Island (§ 28-6-22) (**Verify** Rhode Island's timing). Salary-history bans exist in most of the states above and in many cities (**Verify** the employee's jurisdiction). Do not ask about prior pay; do not reference it in offers.

---

## 12. I-9, E-Verify, and background checks

**Form I-9.** Current edition 01/20/25, expiring 05/31/2027; older editions may not be used. Section 1 by the end of the first day of work; Section 2 within three business days of the hire (8 C.F.R. § 274a.2(b)(1)(ii)). E-Verify employers in good standing may examine documents remotely under the DHS alternative procedure (8 C.F.R. § 274a.2(b)(1)(ix); 88 Fed. Reg. 47749 (July 25, 2023)).

**E-Verify mandates for private employers (Verify — secondary compilation).** All employers: Alabama, Arizona, Mississippi, South Carolina. Size thresholds: Georgia (11+), North Carolina (25+), Florida (25+, Fla. Stat. § 448.095), Tennessee (35+), Utah (about 150+). Louisiana: E-Verify or document retention. Indiana (SEA 76, July 1, 2026): E-Verify is not required; using it is one way (with industry-standard best practices as the other) to support a "reasonable diligence" defense, which fails if the employer is on notice. Restrictions on use: California Lab. Code § 2814 (no pre-offer screening or reverification of current employees except as federal law requires; up to $10,000 per violation); Illinois Right to Privacy in the Workplace Act (notice and procedure requirements for E-Verify users, eff. Jan. 1, 2025).

**FCRA.** Stand-alone disclosure "in a document that consists solely of the disclosure" and written authorization before procuring a consumer report for employment purposes (15 U.S.C. § 1681b(b)(2)); pre-adverse-action notice with a copy of the report and the CFPB summary of rights (§ 1681b(b)(3)); adverse-action notice afterward (§ 1681m). California adds ICRAA (Civ. Code § 1786.16: stand-alone disclosure and a check-box to request a copy).

**Fair chance.** California Gov. Code § 12952 (5+ employees; no conviction inquiry before conditional offer; individualized assessment; preliminary notice and at least five business days to respond; final notice); Civil Rights Council criminal-history regulations last amended effective October 1, 2023. New York City Fair Chance Act (4+; post-conditional-offer only; Article 23-A analysis; at least five business days to respond; covers current employees and pending cases). Washington Fair Chance Act (RCW ch. 49.94, amended by 2025 ch. 71: criminal-history inquiries only after a conditional offer, effective July 1, 2026 for employers with 15+ employees and January 1, 2027 for smaller employers). Illinois (775 ILCS 5/2-103.1; 820 ILCS 75) and Los Angeles (LAMC § 189.00) (**Verify**). New York Clean Slate Act (Crim. Proc. Law § 160.57, eff. Nov. 16, 2024): automatic sealing three years after a misdemeanor and eight years after a felony sentence; older records to be sealed by about November 2027.

---

## 13. Arbitration of employment claims

- **FAA.** Employment arbitration agreements, including class and collective action waivers, are generally enforceable (Epic Systems Corp. v. Lewis, 584 U.S. 497 (2018)).
- **EFAA.** Pub. L. 117-90, 9 U.S.C. §§ 401–402: at the election of the person alleging a sexual harassment or sexual assault dispute, no pre-dispute arbitration agreement or joint-action waiver is valid or enforceable "with respect to a case which is filed under Federal, Tribal, or State law and relates to" the dispute (§ 402(a)); a court decides applicability notwithstanding a delegation clause (§ 402(b)); applies to disputes or claims arising or accruing on or after March 3, 2022. Several courts hold that a plausibly pleaded harassment claim takes the entire case out of arbitration (e.g., Johnson v. Everyrealm, Inc., 657 F. Supp. 3d 535 (S.D.N.Y. 2023); Doe v. Second Street Corp., 105 Cal. App. 5th 552 (2024)), while others limit it to related claims (Mera v. SA Hospitality Grp., LLC, 675 F. Supp. 3d 442 (S.D.N.Y. 2023)). Olivieri v. Stifel, Nicolaus & Co., 112 F.4th 74 (2d Cir. 2024), held the Act covers post-enactment retaliation tied to earlier harassment. No circuit has squarely resolved the whole-case question (**Verify**).
- **Statutory carve-outs.** Sarbanes-Oxley whistleblower claims (18 U.S.C. § 1514A(e)) and CFPA whistleblower claims (12 U.S.C. § 5567(d)) are non-arbitrable by pre-dispute agreement.
- **California.** Lab. Code § 432.6 (AB 51) preempted as to FAA-covered agreements (Chamber of Commerce v. Bonta, 62 F.4th 473 (9th Cir. 2023); stipulated permanent injunction, E.D. Cal. No. 2:19-cv-02456, January 2024). Armendariz v. Foundation Health Psychcare Services, Inc., 24 Cal. 4th 83 (2000): neutral arbitrator, more than minimal discovery, written award permitting limited review, all remedies available in court, no employee-borne arbitration-unique costs, and mutuality. Code Civ. Proc. §§ 1281.97–1281.98: drafting party's failure to pay fees within 30 days after due date is a material breach; Hohenshelt v. Superior Court (Cal. Aug. 11, 2025) held § 1281.98 not preempted but forfeiture not automatic where nonpayment was not willful, grossly negligent, or fraudulent (**Verify** reporter citation). PAGA: individual claims may be compelled to arbitration; non-individual claims remain in court (Viking River Cruises, Inc. v. Moriana, 596 U.S. 639 (2022); Adolph v. Uber Technologies, Inc., 14 Cal. 5th 1104 (2023)).

---

## 14. Separation agreements (summary; see `separation-agreement-and-release`)

- **OWBPA** (29 U.S.C. § 626(f)(1)): written understandably; refers to the ADEA; no waiver of future claims; consideration beyond what is owed; written advice to consult an attorney; 21 days (individual) or 45 days (group program) to consider; 7 days to revoke (cannot be shortened, 29 C.F.R. § 1625.22(e)(5)); for group programs, written disclosure of the decisional unit, eligibility factors, time limits, and job titles and ages of those selected and not selected (§ 626(f)(1)(H); 29 C.F.R. § 1625.22(f)). Material changes restart the period unless the parties agree otherwise (§ 1625.22(e)(4)). No tender-back to challenge an ADEA waiver (29 C.F.R. § 1625.23). Settlements of EEOC charges or lawsuits: § 626(f)(2).
- **Non-waivable:** unemployment and workers' compensation benefits; vested ERISA benefits; future claims; agency charges (individual monetary recovery may be waived except government whistleblower awards); FLSA claims absent court or DOL supervision (Lynn's Food Stores, Inc. v. United States, 679 F.2d 1350 (11th Cir. 1982); Cheeks v. Freeport Pancake House, Inc., 796 F.3d 199 (2d Cir. 2015)); California unpaid wages until paid (Lab. Code § 206.5) and expense reimbursement (Lab. Code § 2804).
- **California Civil Code § 1542** (current text): "A general release does not extend to claims that the creditor or releasing party does not know or suspect to exist in his or her favor at the time of executing the release and that, if known by him or her, would have materially affected his or her settlement with the debtor or released party."
- **State overlays:** Section 10 above (CA, NY, IL, WA, CO, MN); Massachusetts Wage Act releases must name the statute (Crocker v. Townsend Oil Co., 464 Mass. 1 (2012)).
- **WARN:** federal (29 U.S.C. § 2101 et seq.; 100+ employees; 60 days' notice of a plant closing or mass layoff) and state mini-WARN laws.
- **Medicare Section 111** (42 U.S.C. § 1395y(b)(8)): reporting by liability insurers (including self-insurers), no-fault, and workers' compensation plans of settlements with Medicare beneficiaries; rarely triggered by pure employment releases, relevant where physical-injury or medical-expense claims are released.

---

## 15. Executive compensation tax rules

**Section 409A (key rules used in `executive-employment-agreement`).**
- Short-term deferral: paid by the 15th day of the third month after the end of the later of the employee's or employer's taxable year in which the right vests (Treas. Reg. § 1.409A-1(b)(4)).
- Separation pay exception: involuntary separation (including a safe-harbor good-reason resignation); amount up to 2 × the lesser of prior-year annualized compensation and the § 401(a)(17) limit for the year of separation — **$360,000 for 2026, so $720,000** (IRS Notice 2025-67); paid by December 31 of the second year after separation (Treas. Reg. § 1.409A-1(b)(9)(iii)). 2027 limit not yet announced (**Verify**).
- Good-reason safe harbor: material negative change; employee notice within 90 days after initial existence; at least 30 days to cure; separation within two years (Treas. Reg. § 1.409A-1(n)(2)(ii)).
- Separation from service: reasonably anticipated permanent decrease to 20% or less of the prior 36-month average level of services; presumption of no separation at 50% or more (Treas. Reg. § 1.409A-1(h)(1)(ii)).
- Specified employees of public companies (key employees under § 416(i); 2026 officer threshold $235,000): six-month delay of deferred compensation paid on separation (Treas. Reg. §§ 1.409A-1(i), 1.409A-3(i)(2)).
- Release timing: if the consideration-plus-revocation period spans two taxable years, pay in the second (Notice 2010-6 § VI.B.2, as modified by Notice 2010-80).
- Separate-payment designation (Treas. Reg. § 1.409A-2(b)(2)(iii)); reimbursement rules (§ 1.409A-3(i)(1)(iv)); change in control event definition (§ 1.409A-3(i)(5)); offset limit (§ 1.409A-3(j)(4)(xiii)).
- Stock rights: options are exempt only if the exercise price is not less than FMV on the grant date (§ 1.409A-1(b)(5)(i)(A)); independent appraisal within 12 months is presumptively reasonable (§ 1.409A-1(b)(5)(iv)(B)(2)(i)); extending an option's exercise period to no later than the earlier of its original maximum term or the 10th anniversary of grant is not an extension (§ 1.409A-1(b)(5)(v)(C)(1)).

**Section 280G / 4999.** Parachute payments at or above 3 × the base amount (five-year average W-2 compensation): excess over 1 × base is non-deductible (§ 280G) and subject to a 20% excise tax on the recipient (§ 4999(a)). Private-company exemption: approval by more than 75% of the voting power of all outstanding stock (excluding disqualified individuals receiving payments), after adequate disclosure to all stockholders entitled to vote, in a vote separate from the transaction vote, with the recipient's prior waiver (§ 280G(b)(5)(A)(ii), (B); Treas. Reg. § 1.280G-1, Q&A-7). Market: best-net cutback; gross-ups rare.

**Clawback.** Exchange-listed issuers must adopt and enforce a no-fault policy to recover erroneously awarded incentive-based compensation received by current and former executive officers during the three completed fiscal years before a required accounting restatement (17 C.F.R. § 240.10D-1; listing standards effective 2023). Private companies are not subject; draft agreements to accommodate a future policy. Washington (from June 30, 2027) and California prohibit forfeiture or clawback triggered by competition.

---

## 16. Equity for service providers (interfaces with the equity-compensation templates)

- **ISO vs. NSO.** ISOs only for employees (I.R.C. § 422(a)(2)); $100,000 first-exercisable-per-year limit (§ 422(d)); ISO treatment lost if exercised more than three months after employment ends (one year for disability). Consultants and advisors receive NSOs.
- **Rule 701.** Compensatory issuances to employees, directors, officers, and consultants and advisors who are **natural persons** providing bona fide services not connected with capital-raising or market-making (17 C.F.R. § 230.701(c)(1)); 12-month limits and enhanced disclosure above $10 million (§ 230.701(d)–(e)). California: Corp. Code § 25102(o) notice within 30 days after the first issuance under a plan to a California resident.
- **§ 83(b).** Election within 30 days after transfer of restricted stock (Treas. Reg. § 1.83-2(b)); the IRS's optional Form 15620 (Rev. 4-2025) may be used.
- **QSBS (§ 1202), as amended by Pub. L. 119-21.** For stock acquired after July 4, 2025: 50% exclusion after three years, 75% after four, 100% after five; per-issuer cap $15 million (previously $10 million) and aggregate gross assets test $75 million (previously $50 million), both indexed after 2026. Stock received for services can qualify (§ 1202(c)(1)(B)(ii)); the holding period for options starts at exercise, and for restricted stock at issuance if a timely § 83(b) election is made (otherwise at vesting, when the stock is treated as transferred under § 83).
- **Board approval.** Every grant requires Board (or committee) action under 8 Del. C. §§ 152, 153, 157 and the plan; offer letters and advisor agreements only *recommend* grants.

---

## 17. IP chain-of-title diligence checklist (run before every financing and M&A process)

1. **People inventory.** List every founder, employee, intern, contractor, advisor, and pre-formation collaborator who has ever contributed to code, designs, data, models, content, or inventions, with dates and roles. Cross-check against payroll, contractor payments, Git commit authors, design-tool accounts, and patent inventorship.
2. **Founders.** Each founder signed a technology assignment to the Company at formation covering all pre-incorporation work (and, if applicable, an LLC predecessor assigned its assets); each founder who is an employee signed a CIIAA. Check prior-employer and university obligations during the pre-formation period.
3. **Employees.** Every current and former employee signed a CIIAA on or before the first day, with present-assignment ("hereby assign") language, Exhibit B state notices, the DTSA notice, and a completed prior-inventions exhibit. Flag "agree to assign" language, missing signatures, late signatures (and whether work predates them), and over-broad prior-invention lists that carve out core technology.
4. **Contractors.** Every contractor signed a consulting agreement with a present assignment (not only "work made for hire"), a background-IP license, confidentiality, and (for firms) joinders from each individual. Check California work-made-for-hire language (§ 3351.5(c) exposure).
5. **Advisors.** Signed advisor agreements with IP assignment and confidentiality; Board-approved grants.
6. **Gaps.** For each gap, obtain a confirmatory nunc pro tunc assignment (`confirmatory-ip-assignment`) with real consideration, a release, and a short-form for recording; for third-party (employer or university) claims, obtain a release or license from the third party.
7. **Registrations.** Patents and applications: correct inventors named; assignments to the Company executed and recorded at the USPTO (35 U.S.C. § 261; record within three months); foreign filings in the Company's name. Copyright registrations (if any) and recorded transfers. Trademarks: applications in the Company's name; assignments with goodwill; no intent-to-use assignments in violation of 15 U.S.C. § 1060(a)(1). Domain names and social handles in Company-controlled accounts.
8. **Open source and third-party code.** Software bill of materials; copyleft components identified; license compliance; contributor license agreements for any Company-run open-source projects.
9. **Data and AI.** Rights to training data (licenses, terms of service, privacy notices, consents); model weights and prompts as trade secrets; AI-tool use policies; identification of material AI-generated content in key works.
10. **Inbound licenses.** List of in-licensed technology and data with change-of-control, assignment, and exclusivity terms.
11. **Trade-secret hygiene.** Confidentiality policies, access controls, NDAs with counterparties, exit procedures (termination certificates, device wipes), and the DTSA notice in all agreements.
12. **Government funding.** Bayh-Dole and SBIR/STTR obligations (invention disclosure, election of title, government license, U.S. manufacturing preference) for any federally funded work.
13. **Disclosure schedule.** Prepare the IP representations schedule for the financing documents (owned IP, licenses, open source, employee and contractor agreements, and exceptions) from the above.

---

## 18. Open items to verify (as of November 2, 2026)

- NLRB: any decision overruling McLaren Macomb or Stericycle (watch Valley Radiology and Honeywell); any change to Atlanta Opera.
- DOL: final independent-contractor rule after the February 27, 2026 NPRM; any new overtime salary proposal.
- Colorado: 2027 thresholds; POWR Act scope and any amendments.
- New York: non-compete bill S9759/A10023; Trapped at Work Act (training-repayment) status.
- Washington: ESHB 1155 implementation guidance before June 30, 2027.
- Tennessee: treatment of non-solicits and NDAs under Pub. Ch. 934 (HB 1034); Maine § 599-A subsection 5 versions.
- Pay transparency: Colorado benefits details, Hawaii, DC date, Maine and Delaware code sections, New Jersey range-width rule.
- E-Verify mandates (state statutes not individually checked); Illinois and Los Angeles fair-chance details.
- EFAA whole-case question at the circuit level; Hohenshelt reporter citation.
- § 401(a)(17) limit for 2027.
- Freelance-worker statutes (CA, NY State, NYC, IL) thresholds and content requirements.
- Rule 701 availability for grants to individuals who serve through a wholly owned entity.
- Founder zero-salary arrangements under state wage laws.

---

## 19. Sources

Primary sources (statutes, regulations, agency materials):

- 18 U.S.C. § 1833 — https://www.law.cornell.edu/uscode/text/18/1833
- 17 U.S.C. §§ 101, 106A, 204, 205 — https://www.law.cornell.edu/uscode/text/17/101
- 35 U.S.C. §§ 261, 262 — https://www.law.cornell.edu/uscode/text/35/261
- 15 U.S.C. § 1060 — https://www.law.cornell.edu/uscode/text/15/1060
- 29 U.S.C. § 626 — https://www.law.cornell.edu/uscode/text/29/626 ; 29 C.F.R. §§ 1625.22–.23 — https://www.law.cornell.edu/cfr/text/29/1625.22
- 9 U.S.C. § 402 — https://www.law.cornell.edu/uscode/text/9/402
- 42 U.S.C. § 19403 — https://www.law.cornell.edu/uscode/text/42/19403
- 17 C.F.R. § 240.21F-17 — https://www.ecfr.gov/current/title-17/section-240.21F-17 ; SEC Press Release 2024-118 — https://www.sec.gov/newsroom/press-releases/2024-118 ; In re Foot Locker — https://www.sec.gov/files/litigation/admin/2026/34-105542.pdf
- 17 C.F.R. § 240.10D-1 — https://www.law.cornell.edu/cfr/text/17/240.10D-1
- 26 U.S.C. §§ 280G, 4999, 1202, 6041, 6041A — https://www.law.cornell.edu/uscode/text/26/280G ; https://www.law.cornell.edu/uscode/text/26/1202 ; https://www.law.cornell.edu/uscode/text/26/6041
- Treas. Reg. §§ 1.409A-1, 1.409A-3, 1.280G-1 — https://www.law.cornell.edu/cfr/text/26/1.409A-1 ; https://www.law.cornell.edu/cfr/text/26/1.280G-1
- IRS Notice 2025-67 — https://www.irs.gov/pub/irs-drop/n-25-67.pdf ; Notice 2010-80 — https://www.irs.gov/irb/2010-51_IRB ; Form 15620 — https://www.irs.gov/pub/irs-pdf/f15620.pdf
- IRS classification, Section 530, VCSP — https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee ; https://www.irs.gov/government-entities/worker-reclassification-section-530-relief ; https://www.irs.gov/businesses/small-businesses-self-employed/voluntary-classification-settlement-program
- DOL: 91 Fed. Reg. 27833 (May 15, 2026) — https://www.govinfo.gov/content/pkg/FR-2026-05-15/pdf/2026-09839.pdf ; 29 C.F.R. § 541.600 — https://www.ecfr.gov/current/title-29/section-541.600 ; FAB 2025-1 — https://www.dol.gov/sites/dolgov/files/WHD/fab/fab2025-1.pdf ; 91 Fed. Reg. 9932 (Feb. 27, 2026) — https://www.federalregister.gov/documents/2026/02/27/2026-03962/employee-or-independent-contractor-status-under-the-fair-labor-standards-act-family-and-medical
- NLRB GC memos — https://www.nlrb.gov/guidance/memos-research/general-counsel-memos ; Board decisions — https://www.nlrb.gov/cases-decisions/decisions/board-decisions
- FTC: accede-to-vacatur release (Sept. 5, 2025) — https://www.ftc.gov/news-events/news/press-releases/2025/09/federal-trade-commission-files-accede-vacatur-non-compete-clause-rule ; removal of Part 910 (91 Fed. Reg. 6507) — https://www.ftc.gov/legal-library/browse/federal-register-notices/revision-negative-option-rule-withdrawal-cars-rule-removal-non-compete-rule-conform-these-rules ; noncompete enforcement page — https://www.ftc.gov/nonmerger/noncompete
- USCIS Form I-9 — https://www.uscis.gov/i-9 ; 8 C.F.R. § 274a.2 — https://www.ecfr.gov/current/title-8/section-274a.2
- 15 U.S.C. § 1681b — https://www.law.cornell.edu/uscode/text/15/1681b
- California: Lab. Code §§ 2870–2872, 925, 3351.5, 2775–2778, 2814, 432.3; Unemp. Ins. Code §§ 621, 686; Gov. Code § 12964.5; Civ. Code § 1542; Bus. & Prof. Code §§ 16600–16608 — https://leginfo.legislature.ca.gov ; DIR rates — https://www.dir.ca.gov/oprl/ComputerSoftware.htm ; LWDA B2B chart — https://www.labor.ca.gov/wp-content/uploads/sites/338/2025/03/B2B-Requirement-Chart.pdf
- Delaware 19 Del. C. § 805 — https://delcode.delaware.gov/title19/c008/index.html
- Illinois 765 ILCS 1060 — https://www.ilga.gov/Legislation/ILCS/Articles?ActID=2238&ChapterID=62 ; 820 ILCS 90/10, /20 — https://www.ilga.gov/Documents/legislation/ilcs/documents/082000900K10.htm ; P.A. 104-0320 — https://ilga.gov/ftp/Public%20Acts/104/104-0320.htm
- Kansas K.S.A. 44-130 — https://www.ksrevisor.org/statutes/chapters/ch44/044_001_0030.html
- Minnesota §§ 181.78, 181.988, 181.9881, 363A.31 — https://www.revisor.mn.gov/statutes/cite/181.78
- Nevada NRS 600.500, 613.195 — https://www.leg.state.nv.us/NRS/NRS-600.html
- New Jersey P.L. 2017, c. 346 — https://pub.njleg.gov/bills/2016/PL17/346_.HTM ; ABC rule adoption — https://www.nj.gov/labor/lwdhome/press/2026/20260505_ABC.shtml
- New York Lab. Law § 203-f — https://www.nysenate.gov/legislation/laws/LAB/203-F ; Gen. Oblig. Law § 5-336 — https://www.nysenate.gov/legislation/laws/GOB/5-336 ; NY DOL exemption FAQ — https://dol.ny.gov/executive-employee-overtime-exemption-faq
- North Carolina G.S. §§ 66-57.1, 66-57.2 — https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_66/GS_66-57.1.html
- Utah Code § 34-39-3 — https://le.utah.gov/xcode/Title34/Chapter39/34-39-S3.html
- Washington RCW 49.44.140, 49.44.211, 49.62; ESHB 1155 session law — https://app.leg.wa.gov/RCW/default.aspx?cite=49.44.140 ; https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Session%20Laws/House/1155-S.SL.pdf ; L&I thresholds — https://lni.wa.gov/workers-rights/workplace-policies/non-compete-agreements
- Oregon ORS 653.295 (BOLI) — https://www.oregon.gov/boli/employers/Pages/Noncompetition-Agreements.aspx
- Colorado C.R.S. §§ 8-2-113, 24-34-407 (2024 official Title 24) — https://leg.colorado.gov/sites/default/files/images/olls/crs2024-title-24.pdf ; 2026 PAY CALC Order — https://cdle.colorado.gov/sites/cdle/files/adopted_2026_pay_calc_order_7_ccr_1103-14_12.8.25.docx
- Massachusetts M.G.L. c. 149, §§ 24L, 148B — https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXXI/Chapter149/Section24L
- Maine 26 M.R.S. § 599-A — https://legislature.maine.gov/statutes/26/title26sec599-A.html
- Maryland Lab. & Empl. § 3-716 — https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gle&section=3-716
- Virginia § 40.1-28.7:8 — https://law.lis.virginia.gov/vacode/title40.1/chapter3/section40.1-28.7:8/
- New Hampshire RSA 275:70-a — https://gc.nh.gov/rsa/html/XXIII/275/275-70-a.htm ; Rhode Island § 28-59-3 — https://webserver.rilegislature.gov/Statutes/TITLE28/28-59/28-59-3.htm ; D.C. 2026 threshold notice — https://does.dc.gov/sites/default/files/dc/sites/does/publication/attachments/2026%20Ban%20on%20Non-Compete%20Clauses.pdf
- North Dakota § 9-08-06 — https://ndlegis.gov/cencode/t09c08.pdf ; Oklahoma Title 15 — https://www.oklegislature.gov/OK_Statutes/CompleteTitles/os15.rtf ; Wyoming SF 107 — https://www.wyoleg.gov/2025/Enroll/SF0107.pdf
- Montana §§ 39-2-904, 39-2-910 — https://mca.legmt.gov/bills/mca/title_0390/chapter_0020/part_0090/section_0040/0390-0020-0090-0040.html

Cases: Stanford v. Roche, 563 U.S. 776 (2011) — https://www.law.cornell.edu/supremecourt/text/09-1159 ; 583 F.3d 832 (Fed. Cir. 2009) — https://cafc.uscourts.gov/opinions-orders/08-1509.pdf ; FilmTec, 939 F.2d 1568 (Fed. Cir. 1991); Enzo APA & Son v. Geapag, 134 F.3d 1090 (Fed. Cir. 1998); Whitewater West v. Alleshouse, 981 F.3d 1045 (Fed. Cir. 2020); Edwards v. Arthur Andersen, 44 Cal. 4th 937 (2008); AMN Healthcare v. Aya, 28 Cal. App. 5th 923 (2018); Ixchel Pharma v. Biogen, 9 Cal. 5th 1130 (2020); Chamber of Commerce v. Bonta, 62 F.4th 473 (9th Cir. 2023); Armendariz, 24 Cal. 4th 83 (2000); Adolph v. Uber, 14 Cal. 5th 1104 (2023); Epic Systems v. Lewis, 584 U.S. 497 (2018); Crocker v. Townsend Oil, 464 Mass. 1 (2012); McLaren Macomb, 372 NLRB No. 58 (2023); Stericycle, 372 NLRB No. 113 (2023); Atlanta Opera, 372 NLRB No. 95 (2023); Prime Communications, 374 NLRB No. 88 (2026).

Secondary sources (used only to confirm recent changes or market practice; not copied): Cooley (AB 1697 alert, Oct. 8, 2026); Morgan Lewis (AB 692; Tennessee HB 1034; Virginia 2026); Epstein Becker Green (2026 non-compete thresholds); Jackson Lewis (NLRB confirmations); DLA Piper (Hohenshelt); Mayer Brown (Illinois WTA amendments); Wilson Sonsini, Cravath, and Ogletree (N.Y. Lab. Law § 203-f); Colorado Bar Association (C.R.S. § 8-2-113 Q&A); Founder Institute FAST concept page (advisor equity, reference only); Cooley GO, Orrick, Gunderson, Fenwick, Goodwin, Clerky form libraries (coverage and market terms only).

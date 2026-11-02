# Shared Variables

Templates use these names so one intake fills an entire document set. A template may add its own variables; list them in its "Drafting inputs" table using descriptive snake_case. Dates are written out in documents ("March 3, 2027").

## Company

| Variable | Meaning | Example |
|---|---|---|
| `company_name` | Exact legal name, including "Inc." or "Corporation" | Northwind Robotics, Inc. |
| `company_address` | Principal place of business | 100 Example Street, Suite 200, Austin, Texas 78701 |
| `company_hq_state` | State of principal place of business (drives employment law, qualification, blue sky) | Texas |
| `company_notice_email` | Email for legal notices | legal@northwind.example |
| `incorporation_date` | Date the Certificate of Incorporation was filed | January 6, 2027 |
| `fiscal_year_end` | Last day of fiscal year | December 31 |
| `ein` | Federal employer identification number | 00-0000000 |

## Delaware formation

| Variable | Meaning | Example |
|---|---|---|
| `incorporator_name` | Sole incorporator (often a founder or counsel) | Alex Rivera |
| `incorporator_address` | Incorporator's mailing address | |
| `registered_agent_name` | Delaware registered agent (8 Del. C. § 131) | Example Registered Agents, LLC |
| `registered_agent_address` | Street address in Delaware, with city, county, and ZIP | 1000 Example Rd., Wilmington, New Castle County, Delaware 19801 |
| `authorized_common_shares` | Shares of Common Stock authorized | 10,000,000 |
| `authorized_preferred_shares` | Shares of Preferred Stock authorized (0 at formation unless blank check) | 0 |
| `par_value` | Par value per share | $0.00001 |
| `initial_directors` | Names of initial directors (list) | Alex Rivera; Jordan Lee |
| `board_size` | Authorized number of directors | 2 |

## Officers and people

| Variable | Meaning |
|---|---|
| `ceo_name`, `president_name`, `secretary_name`, `cfo_name`, `treasurer_name` | Officer names |
| `signatory_name`, `signatory_title` | Officer signing for the Company on a given document |
| `founder_name`, `founder_address`, `founder_email` | One founder (repeat the document per founder) |
| `founder_spouse_name` | Spouse, where spousal consent is required |
| `employee_name`, `employee_title`, `employee_address`, `employee_email` | Employee |
| `consultant_name`, `advisor_name` | Service providers |

## Founder stock and vesting

| Variable | Meaning | Example |
|---|---|---|
| `founder_shares` | Shares purchased | 4,000,000 |
| `price_per_share` | Purchase price per share (usually par at formation) | $0.00001 |
| `aggregate_purchase_price` | founder_shares × price_per_share | $40.00 |
| `consideration_type` | Cash, assignment of technology, or both | Cash and assignment of technology |
| `vesting_commencement_date` | Date vesting starts | January 6, 2027 |
| `cliff_months` | Cliff length | 12 |
| `vesting_months` | Total vesting period | 48 |
| `acceleration` | none, single-trigger, double-trigger (with percent) | double-trigger, 100% |

## Equity plan and grants

| Variable | Meaning | Example |
|---|---|---|
| `plan_name` | Plan title | 2027 Equity Incentive Plan |
| `plan_reserve_shares` | Shares reserved | 1,500,000 |
| `board_adoption_date` / `stockholder_approval_date` | Plan approvals | |
| `participant_name`, `grant_date`, `grant_shares`, `exercise_price`, `option_type` (ISO/NSO), `expiration_date` | Grant terms | |
| `fmv_409a_value`, `valuation_date`, `valuation_provider` | Latest 409A valuation | |

## Financing

| Variable | Meaning | Example |
|---|---|---|
| `investor_name`, `investor_address`, `investor_email`, `investor_entity_type` | Investor | Example Ventures Fund I, L.P., a Delaware limited partnership |
| `purchase_amount` | Investment amount | $500,000 |
| `valuation_cap` | Post-money (or pre-money) valuation cap | $10,000,000 |
| `discount_rate` | Conversion discount (as % paid, e.g. 80%, or discount, e.g. 20%) — always say which | 20% discount |
| `interest_rate`, `maturity_date` | Convertible notes | 6% simple; 24 months |
| `series_name` | Series of Preferred | Series A |
| `original_issue_price` | Price per share of the new series | $1.2345 |
| `pre_money_valuation`, `post_money_valuation` | Round valuation | |
| `round_size`, `lead_investor_name` | Round amount and lead | |
| `post_closing_pool_percent` | Option pool target on a fully diluted, post-closing basis | 10% |
| `major_investor_threshold` | Shares or dollars to qualify as a Major Investor | $500,000 |
| `closing_date`, `initial_closing_date`, `additional_closing_deadline` | Closings | |

## Boilerplate

| Variable | Meaning | Default |
|---|---|---|
| `governing_law_state` | Governing law | Delaware (corporate documents); the employee's work state for employment documents |
| `forum` | Exclusive forum | Court of Chancery of the State of Delaware (or federal court in Delaware) |
| `effective_date` | Effective date of the document | |

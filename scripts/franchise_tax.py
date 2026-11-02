#!/usr/bin/env python3
"""Estimate Delaware franchise tax for a stock corporation under both methods.

  python3 scripts/franchise_tax.py --authorized 10000000 --par 0.00001 \
      --issued 8500000 --gross-assets 250000

Delaware bills the Authorized Shares Method by default; the corporation may
pay the lower Assumed Par Value Capital Method if it reports issued shares and
total gross assets (from Form 1120, Schedule L) on its annual report. For more
than one class of stock, run once per class for the APVC capital and add the
results (see templates/compliance/delaware-franchise-tax-and-annual-report.md).

The rates below are as verified on the date in RATES_VERIFIED. Confirm them at
https://corp.delaware.gov/frtaxcalc/ before relying on an estimate.
Standard library only.
"""

from __future__ import annotations

import argparse
import math
from decimal import Decimal, ROUND_CEILING

RATES_VERIFIED = "2026-11-02"
ASM_FIRST_TIER_SHARES, ASM_FIRST_TIER_TAX = 5_000, Decimal("175")
ASM_SECOND_TIER_SHARES, ASM_SECOND_TIER_TAX = 10_000, Decimal("250")
ASM_PER_ADDITIONAL_10K = Decimal("85")
APVC_RATE_PER_MILLION = Decimal("400")
APVC_MINIMUM = Decimal("400")
MAXIMUM_TAX = Decimal("200000")  # $250,000 for Large Corporate Filers (8 Del. C. § 503); not modeled
ANNUAL_REPORT_FEE = Decimal("50")


def authorized_shares_method(authorized: int) -> Decimal:
    if authorized <= ASM_FIRST_TIER_SHARES:
        tax = ASM_FIRST_TIER_TAX
    elif authorized <= ASM_SECOND_TIER_SHARES:
        tax = ASM_SECOND_TIER_TAX
    else:
        extra_blocks = math.ceil((authorized - ASM_SECOND_TIER_SHARES) / 10_000)
        tax = ASM_SECOND_TIER_TAX + ASM_PER_ADDITIONAL_10K * extra_blocks
    return min(tax, MAXIMUM_TAX)


def assumed_par_value_capital_method(authorized: int, par: Decimal, issued: int,
                                     gross_assets: Decimal) -> tuple[Decimal, Decimal, Decimal]:
    """Return (assumed par, assumed par value capital, tax)."""
    if issued <= 0:
        raise ValueError("issued shares must be positive to use the APVC method")
    assumed_par = gross_assets / Decimal(issued)
    per_share = max(assumed_par, par)  # shares with par above assumed par use stated par
    capital = per_share * Decimal(authorized)
    millions = (capital / Decimal(1_000_000)).to_integral_value(rounding=ROUND_CEILING)
    tax = max(APVC_MINIMUM, millions * APVC_RATE_PER_MILLION)
    return assumed_par, capital, min(tax, MAXIMUM_TAX)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--authorized", type=int, required=True, help="total authorized shares (all classes)")
    ap.add_argument("--par", type=Decimal, required=True, help="par value per share, e.g. 0.00001")
    ap.add_argument("--issued", type=int, help="total issued and outstanding shares at fiscal year end")
    ap.add_argument("--gross-assets", type=Decimal, help="total gross assets at fiscal year end (Form 1120 Sch. L)")
    args = ap.parse_args()

    asm = authorized_shares_method(args.authorized)
    print(f"Rates as verified {RATES_VERIFIED}; confirm at corp.delaware.gov before filing.\n")
    print(f"Authorized Shares Method:          ${asm:,.2f}")
    if args.issued and args.gross_assets is not None:
        assumed_par, capital, apvc = assumed_par_value_capital_method(
            args.authorized, args.par, args.issued, args.gross_assets)
        print(f"Assumed par (gross assets/issued): ${assumed_par:,.6f}")
        print(f"Assumed par value capital:         ${capital:,.2f}")
        print(f"Assumed Par Value Capital Method:  ${apvc:,.2f}")
        best = min(asm, apvc)
        print(f"\nTax due (lower of the two):        ${best:,.2f}")
        print(f"Plus annual report filing fee:     ${ANNUAL_REPORT_FEE:,.2f}")
        print(f"Total:                             ${best + ANNUAL_REPORT_FEE:,.2f}")
    else:
        print("\nPass --issued and --gross-assets to compute the (usually much lower) APVC method.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

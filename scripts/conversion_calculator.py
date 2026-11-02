#!/usr/bin/env python3
"""
conversion_calculator.py -- SAFE and convertible-note conversion calculator for a
Delaware C-corporation priced round, with option-pool top-up and a fully diluted
post-closing cap table.

Standard library only (Python 3.9+). Part of the `startupassist` skill.

USAGE
    python3 scripts/conversion_calculator.py round.json            # text report
    python3 scripts/conversion_calculator.py round.json --json     # JSON report
    python3 scripts/conversion_calculator.py --example             # worked Example 6
    python3 scripts/conversion_calculator.py --example 2           # any of Examples 1-7
    python3 scripts/conversion_calculator.py --print-example-input 6   # dump input JSON
    python3 scripts/conversion_calculator.py --selftest            # regression tests

The worked examples are the same Examples 1-7 documented in
references/convertible-instruments.md; --selftest asserts the published numbers.

INPUT (JSON; numbers may be JSON numbers or strings such as "1,000,000" or "$0.90")

{
  "company_name": "Northwind Robotics, Inc.",
  "series_name": "Series A",
  "pre_round": {
    "common_outstanding": 8000000,          # issued common (incl. unvested restricted stock)
    "preferred_outstanding": 0,             # existing preferred, as-converted to common
    "options_outstanding": 1000000,         # granted options / RSUs outstanding
    "other_fully_diluted": 0,               # warrants and similar, as-converted
    "unallocated_pool": 1000000,            # reserved and available under the plan
    "promised_options": 0                   # promised but ungranted (subset of the pool)
  },
  "safes": [
    {"name": "Example Ventures Fund I, L.P.",
     "type": "post_money",                  # post_money | pre_money | mfn | uncapped
     "purchase_amount": 1000000,
     "valuation_cap": 10000000,             # omit for discount-only / uncapped / MFN
     "discount_percent": 20,                # the discount (20 = 20% off); omit if none
     "issue_date": "2027-03-01",            # used to order MFN adoption
     "mfn_elects_later_terms": true}        # MFN only; default true
  ],
  "notes": [
    {"name": "Angel Noteholder",
     "principal": 500000,
     "interest_rate_percent": 6,            # simple, non-compounding
     "issue_date": "2027-01-15",
     "conversion_date": "2028-01-15",       # default: new_round.closing_date
     "day_count_basis": 365,                # actual days / 365 (or 360)
     "convert_interest": true,              # false = interest paid in cash, principal converts
     "valuation_cap": 12000000,
     "cap_basis": "pre_money_excluding_new_pool",
     "discount_percent": 20}
  ],
  "new_round": {
    "pre_money_valuation": 24000000,
    "new_money": 6000000,
    "investors": [{"name": "Lead", "amount": 5000000}, {"name": "Other", "amount": 1000000}],
    "closing_date": "2028-01-15",
    "post_closing_pool_percent": 10,        # omit or 0 for no top-up
    "pool_target_basis": "available",       # available | available_plus_outstanding
    "pool_increase_in_pre_money": true,
    "converting_securities_in_pre_money": true
  },
  "rounding": {"price_decimals": 4, "price_rounding": "half_up"}   # or "down" / "up"
}

NOTE cap_basis VALUES (denominator used to compute the cap price = cap / denominator)
    pre_money_excluding_new_pool         common + preferred + options + other + existing pool
    pre_money_including_new_pool         the above + pool increase made in connection with the round
    fully_diluted_including_converting   the above + pool increase + all SAFE/note conversion shares
    post_money                           YC post-money "Company Capitalization" (existing pool, not the
                                         round's increase except to cover promised options, plus all
                                         converting securities)

SAFE TYPES
    post_money  YC post-money SAFE (2018-). Cap price = cap / Company Capitalization, where Company
                Capitalization = issued stock + options + promised options + existing unissued pool
                (the round's pool increase counts only to the extent promised options exceed the
                existing pool) + ALL converting securities (every SAFE and note, as converted).
    pre_money   Original YC SAFE (2013-2018). Cap price = cap / (issued stock + options + other +
                ALL shares reserved under the plan INCLUDING the round's increase), EXCLUDING all SAFEs
                and convertible notes.
    mfn         Uncapped, no-discount SAFE with an MFN. If mfn_elects_later_terms is true, it is
                treated as having adopted the terms of whichever later-issued SAFE yields the lowest
                conversion price in this round (a simplification: under the YC MFN form the holder
                elects within 10 days after each MFN Notice, and the amended SAFE becomes identical to
                the later instrument). Otherwise it converts at the round price.
    uncapped    No cap; optional discount (the YC discount-only form; Discount Rate 100% = no discount).

CONVERSION PRICE
    For every instrument: price = min(round price, cap price [if a cap], round price x (1 - discount)
    [if a discount]). Ties go to the round price (the holder receives the standard new-money series).

SOLVING THE CIRCULARITY
    The round price depends on the pre-money fully diluted share count, which includes the pool
    increase (if the pool is in the pre-money) and the conversion shares (if converting securities
    are in the pre-money). Post-money SAFE prices depend on Company Capitalization, which includes all
    conversion shares. Discount instruments depend on the round price. The pool increase depends on
    total post-closing shares, which depend on the round price.

    The script solves the system by fixed-point iteration on the vector (pool increase, conversion
    shares of each instrument) using 60-digit Decimal arithmetic:
        1. start with pool increase = 0 and conversion shares = 0;
        2. compute the pre-money share count S and the round price P = pre_money_valuation / S;
        3. compute each instrument's conversion price and conversion shares = amount / price;
        4. compute new-money shares = new_money / P and the pool increase that makes the post-closing
           pool equal the target (closed form for the pool given the other quantities);
        5. repeat until every quantity changes by less than 1e-30 shares.
    For realistic inputs the map is a contraction (aggregate post-money SAFE ownership < 100% and pool
    target < 100%), so it converges in well under 1,000 iterations. After convergence the script
    checks the residual of every defining equation and stops with an error if any exceeds 1e-20.

ROUNDING CONVENTION (state the same convention in the deal documents)
    1. Prices: the round price and each conversion price are computed from the converged
       (unrounded) capitalization and rounded to 4 decimal places, half-up (configurable).
       When an instrument converts at the round price, its price is the rounded round price.
    2. Shares issued: each holder's shares = amount / rounded price, rounded DOWN to a whole share
       (no fractional shares; cash in lieu is customary and is not modeled).
    3. Pool increase: the converged increase rounded UP to a whole share, so the post-closing pool
       is not less than the target.
    4. Note interest: simple interest, actual days elapsed / day_count_basis, rounded half-up to
       the cent before conversion.
    Because prices and shares are rounded after solving, final percentages can differ from the
    targets in the fourth decimal place.

This is a modeling aid, not legal or tax advice. Always tie the model to the actual instrument
definitions (the YC SAFE "Company Capitalization" definition, the note's cap definition, and the
term sheet's pre-money and pool language) before relying on it.
"""

import argparse
import copy
import json
import sys
from datetime import date
from decimal import (ROUND_CEILING, ROUND_DOWN, ROUND_FLOOR, ROUND_HALF_UP,
                     ROUND_UP, Decimal, getcontext)
from typing import Dict, List, Optional, Tuple

getcontext().prec = 60

D = Decimal
ZERO = D(0)
ONE = D(1)
HUNDRED = D(100)
TOL = D("1e-30")
RESIDUAL_TOL = D("1e-20")
MAX_ITER = 100000

SAFE_TYPES = ("post_money", "pre_money", "mfn", "uncapped")
NOTE_CAP_BASES = (
    "pre_money_excluding_new_pool",
    "pre_money_including_new_pool",
    "fully_diluted_including_converting",
    "post_money",
)
ROUNDING_MODES = {"half_up": ROUND_HALF_UP, "down": ROUND_DOWN, "up": ROUND_UP}


class InputError(ValueError):
    """Raised for invalid or inconsistent input."""


# --------------------------------------------------------------------------
# Parsing helpers
# --------------------------------------------------------------------------

def to_dec(value, field: str, allow_none: bool = False) -> Optional[Decimal]:
    if value is None:
        if allow_none:
            return None
        raise InputError("missing required number: %s" % field)
    if isinstance(value, bool):
        raise InputError("%s must be a number, not true/false" % field)
    if isinstance(value, (int, float)):
        return D(str(value))
    if isinstance(value, str):
        s = value.replace(",", "").replace("$", "").replace("%", "").strip()
        if s == "":
            if allow_none:
                return None
            raise InputError("missing required number: %s" % field)
        try:
            return D(s)
        except Exception:
            raise InputError("%s is not a number: %r" % (field, value))
    raise InputError("%s must be a number: %r" % (field, value))


def nonneg(value, field: str, default=None) -> Decimal:
    if value is None and default is not None:
        return D(default)
    v = to_dec(value, field)
    if v < 0:
        raise InputError("%s must not be negative" % field)
    return v


def percent_to_fraction(value, field: str, allow_none: bool = True) -> Optional[Decimal]:
    v = to_dec(value, field, allow_none=allow_none)
    if v is None:
        return None
    if v < 0 or v >= 100:
        raise InputError("%s must be a percent from 0 up to (not including) 100; got %s"
                         % (field, value))
    return v / HUNDRED


def parse_date(value, field: str, allow_none: bool = True) -> Optional[date]:
    if value is None or value == "":
        if allow_none:
            return None
        raise InputError("missing date: %s" % field)
    try:
        return date.fromisoformat(str(value))
    except ValueError:
        raise InputError("%s must be an ISO date YYYY-MM-DD; got %r" % (field, value))


def round_price(p: Decimal, places: int, mode) -> Decimal:
    q = D(1).scaleb(-places)
    return p.quantize(q, rounding=mode)


def floor_int(x: Decimal) -> int:
    return int(x.to_integral_value(rounding=ROUND_FLOOR))


def ceil_int(x: Decimal) -> int:
    return int(x.to_integral_value(rounding=ROUND_CEILING))


def cents(x: Decimal) -> Decimal:
    return x.quantize(D("0.01"), rounding=ROUND_HALF_UP)


def fmt_int(n) -> str:
    return "{:,}".format(int(n))


def fmt_money(x: Decimal, places: int = 2) -> str:
    q = D(1).scaleb(-places)
    v = x.quantize(q, rounding=ROUND_HALF_UP)
    sign = "-" if v < 0 else ""
    v = abs(v)
    whole, _, frac = str(v).partition(".")
    whole = "{:,}".format(int(whole))
    return "%s$%s%s" % (sign, whole, ("." + frac) if places > 0 else "")


def fmt_plain(x: Decimal) -> str:
    """Format a Decimal without exponent notation or trailing zeros (10.00 -> 10)."""
    t = format(x, "f")
    if "." in t:
        t = t.rstrip("0").rstrip(".")
    return t


def fmt_pct(x: Decimal, places: int = 4) -> str:
    q = D(1).scaleb(-places)
    return "%s%%" % (x * HUNDRED).quantize(q, rounding=ROUND_HALF_UP)


# --------------------------------------------------------------------------
# Model
# --------------------------------------------------------------------------

class Instrument(object):
    """A SAFE or a convertible note."""

    def __init__(self):
        self.name = ""
        self.kind = "safe"              # safe | note
        self.safe_type = None           # for SAFEs
        self.cap = None                 # Decimal or None
        self.cap_basis = None           # denominator rule
        self.discount = None            # fraction (0.20 = 20% off) or None
        self.issue_date = None
        self.order = 0                  # position in input (tie-break for MFN ordering)
        self.mfn_elects = True
        # money
        self.purchase_amount = ZERO     # SAFE purchase amount or note principal
        self.interest = ZERO            # notes only
        self.interest_rate = ZERO
        self.days = 0
        self.convert_interest = True
        self.conversion_amount = ZERO   # amount that converts


class Model(object):
    def __init__(self, data: dict):
        if not isinstance(data, dict):
            raise InputError("top-level JSON must be an object")
        self.company_name = data.get("company_name", "the Company")
        self.series_name = data.get("series_name", "Series A")

        pr = data.get("pre_round")
        if not isinstance(pr, dict):
            raise InputError("pre_round object is required")
        self.common = nonneg(pr.get("common_outstanding"), "pre_round.common_outstanding")
        self.preferred = nonneg(pr.get("preferred_outstanding"), "pre_round.preferred_outstanding", 0)
        self.options = nonneg(pr.get("options_outstanding"), "pre_round.options_outstanding", 0)
        self.other = nonneg(pr.get("other_fully_diluted"), "pre_round.other_fully_diluted", 0)
        self.pool0 = nonneg(pr.get("unallocated_pool"), "pre_round.unallocated_pool", 0)
        self.promised = nonneg(pr.get("promised_options"), "pre_round.promised_options", 0)
        self.base_ex_pool = self.common + self.preferred + self.options + self.other

        nr = data.get("new_round")
        if not isinstance(nr, dict):
            raise InputError("new_round object is required")
        self.pre_money = to_dec(nr.get("pre_money_valuation"), "new_round.pre_money_valuation")
        if self.pre_money <= 0:
            raise InputError("new_round.pre_money_valuation must be positive")
        investors = nr.get("investors")
        self.investors = []  # type: List[Tuple[str, Decimal]]
        if investors:
            if not isinstance(investors, list):
                raise InputError("new_round.investors must be a list")
            for i, inv in enumerate(investors):
                nm = inv.get("name") or ("New Investor %d" % (i + 1))
                amt = nonneg(inv.get("amount"), "new_round.investors[%d].amount" % i)
                self.investors.append((nm, amt))
        nm_total = sum((a for _, a in self.investors), ZERO)
        if nr.get("new_money") is not None:
            self.new_money = nonneg(nr.get("new_money"), "new_round.new_money")
            if self.investors and nm_total != self.new_money:
                raise InputError("new_round.new_money (%s) does not equal the sum of investors (%s)"
                                 % (self.new_money, nm_total))
        else:
            if not self.investors:
                raise InputError("new_round.new_money or new_round.investors is required")
            self.new_money = nm_total
        if not self.investors:
            self.investors = [("New money investors", self.new_money)]
        self.closing_date = parse_date(nr.get("closing_date"), "new_round.closing_date")
        self.pool_target = percent_to_fraction(nr.get("post_closing_pool_percent"),
                                               "new_round.post_closing_pool_percent")
        if self.pool_target is not None and self.pool_target == 0:
            self.pool_target = None
        self.pool_basis = nr.get("pool_target_basis", "available")
        if self.pool_basis not in ("available", "available_plus_outstanding"):
            raise InputError("new_round.pool_target_basis must be 'available' or "
                             "'available_plus_outstanding'")
        self.pool_in_pre = bool(nr.get("pool_increase_in_pre_money", True))
        self.conv_in_pre = bool(nr.get("converting_securities_in_pre_money", True))

        rd = data.get("rounding") or {}
        self.price_places = int(rd.get("price_decimals", 4))
        if self.price_places < 0 or self.price_places > 10:
            raise InputError("rounding.price_decimals must be between 0 and 10")
        mode = rd.get("price_rounding", "half_up")
        if mode not in ROUNDING_MODES:
            raise InputError("rounding.price_rounding must be one of %s" % ", ".join(ROUNDING_MODES))
        self.price_mode_name = mode
        self.price_mode = ROUNDING_MODES[mode]

        self.instruments = []  # type: List[Instrument]
        order = 0
        for i, s in enumerate(data.get("safes") or []):
            inst = Instrument()
            inst.kind = "safe"
            inst.order = order
            order += 1
            f = "safes[%d]" % i
            inst.name = s.get("name") or ("SAFE %d" % (i + 1))
            inst.safe_type = s.get("type", "post_money")
            if inst.safe_type not in SAFE_TYPES:
                raise InputError("%s.type must be one of %s" % (f, ", ".join(SAFE_TYPES)))
            inst.purchase_amount = nonneg(s.get("purchase_amount"), f + ".purchase_amount")
            if inst.purchase_amount <= 0:
                raise InputError("%s.purchase_amount must be positive" % f)
            inst.cap = to_dec(s.get("valuation_cap"), f + ".valuation_cap", allow_none=True)
            if inst.cap is not None and inst.cap <= 0:
                raise InputError("%s.valuation_cap must be positive" % f)
            inst.discount = percent_to_fraction(s.get("discount_percent"), f + ".discount_percent")
            if inst.discount is not None and inst.discount == 0:
                inst.discount = None
            inst.issue_date = parse_date(s.get("issue_date"), f + ".issue_date")
            inst.mfn_elects = bool(s.get("mfn_elects_later_terms", True))
            if inst.safe_type in ("mfn", "uncapped") and inst.cap is not None:
                raise InputError("%s: an '%s' SAFE has no valuation cap" % (f, inst.safe_type))
            if inst.safe_type == "mfn" and inst.discount is not None:
                raise InputError("%s: an 'mfn' SAFE has no discount" % f)
            if inst.safe_type in ("post_money", "pre_money") and inst.cap is None:
                raise InputError("%s: a '%s' SAFE needs valuation_cap (use type 'uncapped' for a "
                                 "discount-only SAFE)" % (f, inst.safe_type))
            inst.cap_basis = {"post_money": "post_money", "pre_money": "pre_money_safe"}.get(
                inst.safe_type)
            inst.conversion_amount = inst.purchase_amount
            self.instruments.append(inst)

        for i, n in enumerate(data.get("notes") or []):
            inst = Instrument()
            inst.kind = "note"
            inst.order = order
            order += 1
            f = "notes[%d]" % i
            inst.name = n.get("name") or ("Note %d" % (i + 1))
            inst.purchase_amount = nonneg(n.get("principal"), f + ".principal")
            if inst.purchase_amount <= 0:
                raise InputError("%s.principal must be positive" % f)
            rate = to_dec(n.get("interest_rate_percent", 0), f + ".interest_rate_percent")
            if rate < 0:
                raise InputError("%s.interest_rate_percent must not be negative" % f)
            inst.interest_rate = rate / HUNDRED
            inst.issue_date = parse_date(n.get("issue_date"), f + ".issue_date", allow_none=False)
            conv_date = parse_date(n.get("conversion_date"), f + ".conversion_date")
            if conv_date is None:
                conv_date = self.closing_date
            if conv_date is None:
                raise InputError("%s: give conversion_date or new_round.closing_date" % f)
            if conv_date < inst.issue_date:
                raise InputError("%s: conversion_date is before issue_date" % f)
            basis = int(n.get("day_count_basis", 365))
            if basis not in (360, 365):
                raise InputError("%s.day_count_basis must be 360 or 365" % f)
            inst.days = (conv_date - inst.issue_date).days
            inst.interest = cents(inst.purchase_amount * inst.interest_rate * D(inst.days) / D(basis))
            inst.convert_interest = bool(n.get("convert_interest", True))
            inst.conversion_amount = inst.purchase_amount + (inst.interest if inst.convert_interest
                                                             else ZERO)
            inst.cap = to_dec(n.get("valuation_cap"), f + ".valuation_cap", allow_none=True)
            if inst.cap is not None and inst.cap <= 0:
                raise InputError("%s.valuation_cap must be positive" % f)
            inst.cap_basis = n.get("cap_basis", "pre_money_excluding_new_pool")
            if inst.cap_basis not in NOTE_CAP_BASES:
                raise InputError("%s.cap_basis must be one of %s" % (f, ", ".join(NOTE_CAP_BASES)))
            inst.discount = percent_to_fraction(n.get("discount_percent"), f + ".discount_percent")
            if inst.discount is not None and inst.discount == 0:
                inst.discount = None
            self.instruments.append(inst)

        # sanity: aggregate post-money SAFE ownership must be < 100%
        s = sum((x.purchase_amount / x.cap for x in self.instruments
                 if x.kind == "safe" and x.safe_type == "post_money"), ZERO)
        if s >= ONE:
            raise InputError("aggregate post-money SAFE ownership (sum of purchase_amount / cap) "
                             "is %s, which is not less than 100%%" % fmt_pct(s))


class State(object):
    def __init__(self, P: Decimal, dP: Decimal, conv_total: Decimal):
        self.P = P
        self.dP = dP
        self.conv_total = conv_total


# --------------------------------------------------------------------------
# Pricing
# --------------------------------------------------------------------------

def cap_denominator(m: Model, basis: str, st: State) -> Decimal:
    if basis == "post_money":
        # YC post-money "Company Capitalization": issued stock, options, promised options, the
        # existing unissued pool (the round's increase counts only to the extent promised options
        # exceed the existing pool), and all Converting Securities.
        return m.base_ex_pool + max(m.pool0, m.promised) + st.conv_total
    if basis == "pre_money_safe":
        # Original pre-money SAFE: all issued stock and options plus every share reserved under the
        # plan, including any increase in connection with the Equity Financing; excludes all SAFEs
        # and convertible notes.
        return m.base_ex_pool + m.pool0 + st.dP
    if basis == "pre_money_excluding_new_pool":
        return m.base_ex_pool + m.pool0
    if basis == "pre_money_including_new_pool":
        return m.base_ex_pool + m.pool0 + st.dP
    if basis == "fully_diluted_including_converting":
        return m.base_ex_pool + m.pool0 + st.dP + st.conv_total
    raise InputError("unknown cap basis %r" % basis)


def evaluate_terms(m: Model, cap: Optional[Decimal], basis: Optional[str],
                   discount: Optional[Decimal], st: State) -> Tuple[Decimal, str, Dict[str, Decimal]]:
    """Return (price, governing_term, candidate_prices). Ties go to the round price."""
    candidates = {"round price": st.P}
    if cap is not None:
        candidates["valuation cap"] = cap / cap_denominator(m, basis, st)
    if discount is not None:
        candidates["discount"] = st.P * (ONE - discount)
    best_name, best = "round price", st.P
    for name in ("valuation cap", "discount"):
        if name in candidates and candidates[name] < best:
            best_name, best = name, candidates[name]
    return best, best_name, candidates


def later_safes(m: Model, inst: Instrument) -> List[Instrument]:
    out = []
    for other in m.instruments:
        if other is inst or other.kind != "safe" or other.safe_type == "mfn":
            continue
        if inst.issue_date is not None and other.issue_date is not None:
            if other.issue_date > inst.issue_date:
                out.append(other)
        elif other.order > inst.order:
            out.append(other)
    return out


def price_instrument(m: Model, inst: Instrument, st: State) -> Tuple[Decimal, str, Dict[str, Decimal]]:
    if inst.kind == "safe" and inst.safe_type == "mfn":
        best, label, cands = st.P, "round price", {"round price": st.P}
        if inst.mfn_elects:
            for other in later_safes(m, inst):
                p, gov, c = evaluate_terms(m, other.cap, other.cap_basis, other.discount, st)
                if p < best:
                    best, label, cands = p, "MFN: terms of %s (%s)" % (other.name, gov), c
        return best, label, cands
    return evaluate_terms(m, inst.cap, inst.cap_basis, inst.discount, st)


# --------------------------------------------------------------------------
# Solver
# --------------------------------------------------------------------------

def pre_money_shares(m: Model, st: State) -> Decimal:
    s = m.base_ex_pool + m.pool0
    if m.pool_in_pre:
        s += st.dP
    if m.conv_in_pre:
        s += st.conv_total
    return s


def pool_increase_for(m: Model, conv_total: Decimal, new_shares: Decimal) -> Decimal:
    if m.pool_target is None:
        return ZERO
    t = m.pool_target
    others = m.base_ex_pool + m.pool0 + conv_total + new_shares   # all post-closing shares except the increase
    if m.pool_basis == "available":
        have = m.pool0 - m.promised                                 # promised grants are not "available"
    else:
        have = m.pool0 + m.options                                  # target counts outstanding options too
    inc = (t * others - have) / (ONE - t)
    return inc if inc > 0 else ZERO


def solve(m: Model) -> dict:
    n = len(m.instruments)
    conv = [ZERO] * n
    dP = ZERO
    converged = False
    iterations = 0
    for it in range(1, MAX_ITER + 1):
        iterations = it
        st = State(ZERO, dP, sum(conv, ZERO))
        st.P = m.pre_money / pre_money_shares(m, st)
        new_conv = []
        for inst in m.instruments:
            price, _, _ = price_instrument(m, inst, st)
            new_conv.append(inst.conversion_amount / price)
        new_shares = m.new_money / st.P
        new_dP = pool_increase_for(m, st.conv_total, new_shares)
        delta = abs(new_dP - dP)
        for a, b in zip(conv, new_conv):
            delta = max(delta, abs(a - b))
        conv, dP = new_conv, new_dP
        if delta < TOL:
            converged = True
            break
    if not converged:
        raise RuntimeError("did not converge after %d iterations; check inputs" % MAX_ITER)

    # Final unrounded state and residual checks.
    st = State(ZERO, dP, sum(conv, ZERO))
    S = pre_money_shares(m, st)
    st.P = m.pre_money / S
    details = []
    worst = ZERO
    for inst, c in zip(m.instruments, conv):
        price, label, cands = price_instrument(m, inst, st)
        worst = max(worst, abs(c - inst.conversion_amount / price))
        details.append((inst, c, price, label, cands))
    new_shares = m.new_money / st.P
    worst = max(worst, abs(dP - pool_increase_for(m, st.conv_total, new_shares)))
    if worst > RESIDUAL_TOL:
        raise RuntimeError("solution residual %s exceeds tolerance" % worst)
    return {"state": st, "pre_money_shares": S, "details": details, "new_shares": new_shares,
            "iterations": iterations, "residual": worst}


# --------------------------------------------------------------------------
# Rounding, cap table, and report
# --------------------------------------------------------------------------

def compute(data: dict) -> dict:
    m = Model(data)
    sol = solve(m)
    st = sol["state"]
    P_r = round_price(st.P, m.price_places, m.price_mode)
    if P_r <= 0:
        raise InputError("rounded round price is zero; increase rounding.price_decimals")
    pool_inc = ceil_int(st.dP) if st.dP > 0 else 0

    conv_rows = []
    for inst, c_unr, price, label, cands in sol["details"]:
        if label == "round price":
            price_r = P_r
        else:
            price_r = round_price(price, m.price_places, m.price_mode)
        shares = floor_int(inst.conversion_amount / price_r)
        row = {
            "name": inst.name,
            "instrument": ("SAFE (%s)" % inst.safe_type) if inst.kind == "safe" else "Convertible note",
            "purchase_amount_or_principal": inst.purchase_amount,
            "interest": inst.interest if inst.kind == "note" else None,
            "days_outstanding": inst.days if inst.kind == "note" else None,
            "converting_amount": inst.conversion_amount,
            "cap_price_unrounded": cands.get("valuation cap"),
            "discount_price_unrounded": cands.get("discount"),
            "governing_term": label,
            "conversion_price_unrounded": price,
            "conversion_price": price_r,
            "shares": shares,
            "shares_unrounded": c_unr,
        }
        conv_rows.append(row)

    # Shadow series labels: distinct conversion prices below the round price, lowest price = "-1".
    shadow_prices = sorted({r["conversion_price"] for r in conv_rows if r["conversion_price"] < P_r})
    shadow_label = {}
    for i, p in enumerate(shadow_prices):
        shadow_label[p] = "%s-%d" % (m.series_name, i + 1)
    for r in conv_rows:
        if r["conversion_price"] < P_r:
            r["series"] = shadow_label[r["conversion_price"]]
        else:
            r["series"] = m.series_name

    new_rows = []
    for nm, amt in m.investors:
        new_rows.append({"name": nm, "amount": amt, "shares": floor_int(amt / P_r)})

    # Cap table
    table = []

    def add(holder, cls, shares, price=None):
        table.append({"holder": holder, "class": cls, "shares": int(shares), "price": price})

    add("Common stockholders", "Common Stock", m.common)
    if m.preferred > 0:
        add("Existing preferred (as converted)", "Existing Preferred", m.preferred)
    if m.options > 0:
        add("Options and awards outstanding", "Common (underlying)", m.options)
    if m.other > 0:
        add("Warrants and other rights", "Common (underlying)", m.other)
    if m.pool0 > 0:
        add("Unallocated pool (existing)", "Common (reserved)", m.pool0)
    if pool_inc > 0:
        add("Pool increase (this round)", "Common (reserved)", pool_inc)
    for r in conv_rows:
        add(r["name"], r["series"], r["shares"], r["conversion_price"])
    for r in new_rows:
        add(r["name"], m.series_name, r["shares"], P_r)
    total = sum(x["shares"] for x in table)
    for x in table:
        x["percent"] = D(x["shares"]) / D(total) if total else ZERO
        x["liquidation_preference"] = (D(x["shares"]) * x["price"]) if x["price"] is not None else None

    pool_after = int(m.pool0) + pool_inc
    available_after = D(pool_after) - m.promised
    result = {
        "company_name": m.company_name,
        "series_name": m.series_name,
        "pre_money_valuation": m.pre_money,
        "new_money": m.new_money,
        "post_money_valuation_nominal": m.pre_money + m.new_money,
        "pre_money_fully_diluted_shares_unrounded": sol["pre_money_shares"],
        "price_per_share_unrounded": st.P,
        "price_per_share": P_r,
        "pool_increase_unrounded": st.dP,
        "pool_increase": pool_inc,
        "pool_after_closing": pool_after,
        "available_pool_percent_after_closing": available_after / D(total) if total else ZERO,
        "conversions": conv_rows,
        "new_investors": new_rows,
        "cap_table": table,
        "total_fully_diluted_shares": total,
        "implied_post_money_at_price": P_r * D(total),
        "iterations": sol["iterations"],
        "residual": sol["residual"],
        "settings": {
            "pool_target_percent": (m.pool_target * HUNDRED) if m.pool_target is not None else None,
            "pool_target_basis": m.pool_basis,
            "pool_increase_in_pre_money": m.pool_in_pre,
            "converting_securities_in_pre_money": m.conv_in_pre,
            "price_decimals": m.price_places,
            "price_rounding": m.price_mode_name,
        },
    }
    return result


def report_text(r: dict) -> str:
    L = []
    L.append("%s -- %s conversion model" % (r["company_name"], r["series_name"]))
    L.append("=" * 78)
    s = r["settings"]
    L.append("Pre-money valuation:            %s" % fmt_money(r["pre_money_valuation"]))
    L.append("New money:                      %s" % fmt_money(r["new_money"]))
    L.append("Post-money (nominal):           %s" % fmt_money(r["post_money_valuation_nominal"]))
    L.append("Pre-money FD shares (solved):   %s" % r["pre_money_fully_diluted_shares_unrounded"]
             .quantize(D("0.0001"), rounding=ROUND_HALF_UP))
    L.append("%s price (unrounded):      $%s" % (r["series_name"], r["price_per_share_unrounded"]
                                                .quantize(D("0.00000001"), rounding=ROUND_HALF_UP)))
    L.append("%s price per share:        %s  (%d decimals, %s)"
             % (r["series_name"], fmt_money(r["price_per_share"], s["price_decimals"]),
                s["price_decimals"], s["price_rounding"]))
    if s["pool_target_percent"] is not None:
        L.append("Pool target:                    %s%% post-closing (%s; increase %s the pre-money)"
                 % (fmt_plain(s["pool_target_percent"]), s["pool_target_basis"],
                    "in" if s["pool_increase_in_pre_money"] else "outside"))
    L.append("Pool increase:                  %s shares (unrounded %s)"
             % (fmt_int(r["pool_increase"]),
                r["pool_increase_unrounded"].quantize(D("0.0001"), rounding=ROUND_HALF_UP)))
    L.append("Converting securities in pre-money: %s" % ("yes" if s["converting_securities_in_pre_money"]
                                                        else "no"))
    L.append("")
    L.append("Conversions")
    L.append("-" * 78)
    if not r["conversions"]:
        L.append("(none)")
    for c in r["conversions"]:
        L.append("%s -- %s" % (c["name"], c["instrument"]))
        if c["interest"] is not None:
            L.append("    principal %s + interest %s (%d days) = converting amount %s"
                     % (fmt_money(c["purchase_amount_or_principal"]), fmt_money(c["interest"]),
                        c["days_outstanding"], fmt_money(c["converting_amount"])))
        else:
            L.append("    purchase amount %s" % fmt_money(c["converting_amount"]))
        if c["cap_price_unrounded"] is not None:
            L.append("    cap price (unrounded)       $%s" % c["cap_price_unrounded"].quantize(
                D("0.00000001"), rounding=ROUND_HALF_UP))
        if c["discount_price_unrounded"] is not None:
            L.append("    discount price (unrounded)  $%s" % c["discount_price_unrounded"].quantize(
                D("0.00000001"), rounding=ROUND_HALF_UP))
        L.append("    governing term: %s; conversion price %s; shares %s; series %s"
                 % (c["governing_term"], fmt_money(c["conversion_price"], s["price_decimals"]),
                    fmt_int(c["shares"]), c["series"]))
    L.append("")
    L.append("Fully diluted post-closing capitalization")
    L.append("-" * 78)
    L.append("%-38s %-20s %14s %10s" % ("Holder", "Class / series", "Shares", "FD %"))
    for x in r["cap_table"]:
        L.append("%-38s %-20s %14s %10s" % (x["holder"][:38], x["class"][:20], fmt_int(x["shares"]),
                                           fmt_pct(x["percent"])))
    L.append("%-38s %-20s %14s %10s" % ("Total", "", fmt_int(r["total_fully_diluted_shares"]), "100%"))
    L.append("")
    L.append("Available pool after closing:   %s of fully diluted"
             % fmt_pct(r["available_pool_percent_after_closing"]))
    L.append("Implied post-money at price:    %s" % fmt_money(r["implied_post_money_at_price"]))
    prefs = [x for x in r["cap_table"] if x["liquidation_preference"] is not None]
    if prefs:
        L.append("")
        L.append("1x liquidation preference by holder (shares x original issue price)")
        for x in prefs:
            L.append("    %-36s %-14s %s" % (x["holder"][:36], x["class"][:14],
                                             fmt_money(x["liquidation_preference"])))
    L.append("")
    L.append("Solved by fixed-point iteration in %d iterations (max residual %s)."
             % (r["iterations"], "%.2E" % r["residual"]))
    L.append("Rounding: prices to %d decimals (%s); issued shares rounded down; pool increase "
             "rounded up." % (s["price_decimals"], s["price_rounding"]))
    return "\n".join(L)


def to_jsonable(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    if isinstance(obj, dict):
        return {k: to_jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [to_jsonable(v) for v in obj]
    return obj


# --------------------------------------------------------------------------
# Worked examples (identical to references/convertible-instruments.md)
# --------------------------------------------------------------------------

BASE = {"common_outstanding": 8000000, "options_outstanding": 1000000, "unallocated_pool": 1000000}

EXAMPLES = {
    1: {
        "title": "One post-money SAFE converting in a Series A (no pool top-up)",
        "input": {
            "company_name": "Northwind Robotics, Inc.", "series_name": "Series A",
            "pre_round": dict(BASE),
            "safes": [{"name": "Example Ventures Fund I, L.P.", "type": "post_money",
                       "purchase_amount": 1000000, "valuation_cap": 10000000}],
            "new_round": {"pre_money_valuation": 30000000, "new_money": 7500000},
        },
    },
    2: {
        "title": "Three post-money SAFEs with different caps",
        "input": {
            "company_name": "Northwind Robotics, Inc.", "series_name": "Series A",
            "pre_round": dict(BASE),
            "safes": [
                {"name": "SAFE A ($5M cap)", "type": "post_money", "purchase_amount": 250000,
                 "valuation_cap": 5000000},
                {"name": "SAFE B ($8M cap)", "type": "post_money", "purchase_amount": 1000000,
                 "valuation_cap": 8000000},
                {"name": "SAFE C ($10M cap)", "type": "post_money", "purchase_amount": 750000,
                 "valuation_cap": 10000000},
            ],
            "new_round": {"pre_money_valuation": 32000000, "new_money": 8000000},
        },
    },
    3: {
        "title": "Discount-only SAFE and a cap-and-discount SAFE where the discount governs",
        "input": {
            "company_name": "Northwind Robotics, Inc.", "series_name": "Series A",
            "pre_round": dict(BASE),
            "safes": [
                {"name": "SAFE D1 (20% discount, no cap)", "type": "uncapped",
                 "purchase_amount": 500000, "discount_percent": 20},
                {"name": "SAFE D2 ($30M post cap + 20% discount)", "type": "post_money",
                 "purchase_amount": 500000, "valuation_cap": 30000000, "discount_percent": 20},
            ],
            "new_round": {"pre_money_valuation": 20000000, "new_money": 5000000},
        },
    },
    4: {
        "title": "Two pre-money SAFEs (original YC form) versus post-money",
        "input": {
            "company_name": "Northwind Robotics, Inc.", "series_name": "Series A",
            "pre_round": dict(BASE),
            "safes": [
                {"name": "Pre-money SAFE 1 ($9M pre cap)", "type": "pre_money",
                 "purchase_amount": 1000000, "valuation_cap": 9000000},
                {"name": "Pre-money SAFE 2 ($9M pre cap)", "type": "pre_money",
                 "purchase_amount": 1000000, "valuation_cap": 9000000},
            ],
            "new_round": {"pre_money_valuation": 30000000, "new_money": 7500000},
        },
    },
    5: {
        "title": "Convertible note with interest, cap, and discount (cap basis excludes new pool)",
        "input": {
            "company_name": "Northwind Robotics, Inc.", "series_name": "Series A",
            "pre_round": dict(BASE),
            "notes": [{"name": "Noteholder (6%, $12M cap, 20%)", "principal": 500000,
                       "interest_rate_percent": 6, "issue_date": "2027-01-15",
                       "valuation_cap": 12000000, "cap_basis": "pre_money_excluding_new_pool",
                       "discount_percent": 20}],
            "new_round": {"pre_money_valuation": 24000000, "new_money": 6000000,
                          "closing_date": "2028-01-15"},
        },
    },
    6: {
        "title": "Post-money SAFEs plus option-pool top-up in the pre-money (full circularity)",
        "input": {
            "company_name": "Northwind Robotics, Inc.", "series_name": "Series A",
            "pre_round": {"common_outstanding": 8000000, "options_outstanding": 1000000,
                          "unallocated_pool": 500000},
            "safes": [
                {"name": "Example Ventures Fund I, L.P.", "type": "post_money",
                 "purchase_amount": 1000000, "valuation_cap": 10000000},
                {"name": "Angel SAFE ($12.5M cap)", "type": "post_money",
                 "purchase_amount": 500000, "valuation_cap": 12500000},
            ],
            "new_round": {"pre_money_valuation": 24000000, "new_money": 6000000,
                          "post_closing_pool_percent": 10, "pool_target_basis": "available",
                          "pool_increase_in_pre_money": True,
                          "converting_securities_in_pre_money": True},
        },
    },
    7: {
        "title": "Uncapped MFN SAFE adopting a later capped SAFE",
        "input": {
            "company_name": "Northwind Robotics, Inc.", "series_name": "Series A",
            "pre_round": dict(BASE),
            "safes": [
                {"name": "MFN SAFE (uncapped)", "type": "mfn", "purchase_amount": 250000,
                 "issue_date": "2027-02-01"},
                {"name": "Later SAFE ($8M post cap)", "type": "post_money",
                 "purchase_amount": 750000, "valuation_cap": 8000000, "issue_date": "2027-05-01"},
            ],
            "new_round": {"pre_money_valuation": 30000000, "new_money": 7500000},
        },
    },
}

# Example 5 variant: same note, cap basis includes new pool and all converting securities.
EXAMPLE_5B = copy.deepcopy(EXAMPLES[5]["input"])
EXAMPLE_5B["notes"][0]["cap_basis"] = "fully_diluted_including_converting"

def run_example(n: int, as_json: bool = False) -> str:
    ex = EXAMPLES[n]
    r = compute(ex["input"])
    if as_json:
        return json.dumps(to_jsonable(r), indent=2)
    return "Example %d: %s\n\n%s" % (n, ex["title"], report_text(r))


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------

def _shares_by_holder(r: dict) -> Dict[str, int]:
    return {x["holder"]: x["shares"] for x in r["cap_table"]}


def _conv_by_name(r: dict) -> Dict[str, dict]:
    return {c["name"]: c for c in r["conversions"]}


def selftest() -> int:
    failures = []
    checks = [0]

    def check(cond, msg):
        checks[0] += 1
        if not cond:
            failures.append(msg)

    def expect_example(n, price, pool_inc, total, shares, conv_prices, governing=None):
        r = compute(EXAMPLES[n]["input"]) if isinstance(n, int) else compute(n)
        label = ("Example %s" % n) if isinstance(n, int) else "Example 5B"
        check(str(r["price_per_share"]) == price,
              "%s: price %s != %s" % (label, r["price_per_share"], price))
        check(r["pool_increase"] == pool_inc,
              "%s: pool increase %s != %s" % (label, r["pool_increase"], pool_inc))
        check(r["total_fully_diluted_shares"] == total,
              "%s: total FD %s != %s" % (label, r["total_fully_diluted_shares"], total))
        sh = _shares_by_holder(r)
        for k, v in shares.items():
            check(sh.get(k) == v, "%s: shares for %s = %s, expected %s" % (label, k, sh.get(k), v))
        cv = _conv_by_name(r)
        for k, v in conv_prices.items():
            check(k in cv and str(cv[k]["conversion_price"]) == v,
                  "%s: conversion price for %s = %s, expected %s"
                  % (label, k, cv.get(k, {}).get("conversion_price"), v))
        for k, v in (governing or {}).items():
            check(k in cv and cv[k]["governing_term"].startswith(v),
                  "%s: governing term for %s = %s, expected %s"
                  % (label, k, cv.get(k, {}).get("governing_term"), v))
        return r

    # Example 1 -- one post-money SAFE.
    r1 = expect_example(1, "2.7000", 0, 13888888,
                        {"Example Ventures Fund I, L.P.": 1111111, "New money investors": 2777777},
                        {"Example Ventures Fund I, L.P.": "0.9000"},
                        {"Example Ventures Fund I, L.P.": "valuation cap"})
    # Invariant: before the round the SAFE owns purchase amount / cap of Company Capitalization.
    c = _conv_by_name(r1)["Example Ventures Fund I, L.P."]
    cc = D(10000000) + c["shares_unrounded"]
    check(abs(c["shares_unrounded"] / cc - D("0.1")) < D("1e-25"),
          "Example 1: SAFE ownership of Company Capitalization is not 10%")

    # Example 2 -- three post-money SAFEs.
    expect_example(2, "2.4000", 0, 16666665,
                   {"SAFE A ($5M cap)": 666666, "SAFE B ($8M cap)": 1666666,
                    "SAFE C ($10M cap)": 1000000, "New money investors": 3333333},
                   {"SAFE A ($5M cap)": "0.3750", "SAFE B ($8M cap)": "0.6000",
                    "SAFE C ($10M cap)": "0.7500"})

    # Example 3 -- discount-only SAFE and cap+discount SAFE (discount governs).
    expect_example(3, "1.8750", 0, 13333332,
                   {"SAFE D1 (20% discount, no cap)": 333333,
                    "SAFE D2 ($30M post cap + 20% discount)": 333333,
                    "New money investors": 2666666},
                   {"SAFE D1 (20% discount, no cap)": "1.5000",
                    "SAFE D2 ($30M post cap + 20% discount)": "1.5000"},
                   {"SAFE D1 (20% discount, no cap)": "discount",
                    "SAFE D2 ($30M post cap + 20% discount)": "discount"})

    # Example 4 -- two pre-money SAFEs.
    expect_example(4, "2.4545", 0, 15277834,
                   {"Pre-money SAFE 1 ($9M pre cap)": 1111111,
                    "Pre-money SAFE 2 ($9M pre cap)": 1111111,
                    "New money investors": 3055612},
                   {"Pre-money SAFE 1 ($9M pre cap)": "0.9000",
                    "Pre-money SAFE 2 ($9M pre cap)": "0.9000"})

    # Example 5 -- note, cap basis excludes the new pool and converting securities.
    r5 = expect_example(5, "2.2985", 0, 13052064,
                        {"Noteholder (6%, $12M cap, 20%)": 441666, "New money investors": 2610398},
                        {"Noteholder (6%, $12M cap, 20%)": "1.2000"},
                        {"Noteholder (6%, $12M cap, 20%)": "valuation cap"})
    n5 = _conv_by_name(r5)["Noteholder (6%, $12M cap, 20%)"]
    check(str(n5["interest"]) == "30000.00", "Example 5: interest %s != 30000.00" % n5["interest"])
    check(n5["days_outstanding"] == 365, "Example 5: days %s != 365" % n5["days_outstanding"])

    # Example 5B -- same note, cap basis includes converting securities.
    expect_example(EXAMPLE_5B, "2.2940", 0, 13077592,
                   {"Noteholder (6%, $12M cap, 20%)": 462074, "New money investors": 2615518},
                   {"Noteholder (6%, $12M cap, 20%)": "1.1470"})

    # Example 6 -- post-money SAFEs + pool top-up in pre-money.
    r6 = expect_example(6, "1.9912", 1006645, 15066361,
                        {"Example Ventures Fund I, L.P.": 1104606,
                         "Angel SAFE ($12.5M cap)": 441852,
                         "New money investors": 3013258,
                         "Pool increase (this round)": 1006645},
                        {"Example Ventures Fund I, L.P.": "0.9053",
                         "Angel SAFE ($12.5M cap)": "1.1316"})
    # Closed-form cross-check of the unrounded solution (see the reference file):
    # C = 9,500,000 / (1 - 0.14); dP = (0.125*C - 500,000) / 0.875; P = 24,000,000 / (C + dP)
    C = D(9500000) / (ONE - D("0.14"))
    dP = (D("0.125") * C - D(500000)) / D("0.875")
    P = D(24000000) / (C + dP)
    check(abs(r6["pool_increase_unrounded"] - dP) < D("1e-20"),
          "Example 6: pool increase does not match closed form")
    check(abs(r6["price_per_share_unrounded"] - P) < D("1e-25"),
          "Example 6: price does not match closed form")

    # Example 7 -- MFN SAFE adopts later capped SAFE.
    expect_example(7, "2.6250", 0, 14285712,
                   {"MFN SAFE (uncapped)": 357142, "Later SAFE ($8M post cap)": 1071428,
                    "New money investors": 2857142},
                   {"MFN SAFE (uncapped)": "0.7000", "Later SAFE ($8M post cap)": "0.7000"},
                   {"MFN SAFE (uncapped)": "MFN"})

    # Input validation smoke tests.
    bad = copy.deepcopy(EXAMPLES[1]["input"])
    bad["safes"][0]["valuation_cap"] = 900000
    try:
        compute(bad)
        check(False, "validation: SAFE ownership >= 100% was not rejected")
    except InputError:
        check(True, "")

    for n in sorted(EXAMPLES):
        print("Example %d: %s ... ok" % (n, EXAMPLES[n]["title"]) if not any(
            f.startswith("Example %d" % n) for f in failures) else
            "Example %d: %s ... FAILED" % (n, EXAMPLES[n]["title"]))
    print("Example 5B: same note, cap basis includes new pool and converting securities ... %s"
          % ("FAILED" if any(f.startswith("Example 5B") for f in failures) else "ok"))
    if failures:
        print("\nSELF-TEST FAILED (%d of %d checks):" % (len(failures), checks[0]))
        for f in failures:
            print("  - " + f)
        return 1
    print("\nSELF-TEST PASSED: %d checks." % checks[0])
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="SAFE / convertible note conversion and priced-round cap table calculator.")
    ap.add_argument("input", nargs="?", help="path to round JSON file")
    ap.add_argument("--json", action="store_true", help="print JSON instead of a text report")
    ap.add_argument("--example", nargs="?", const=6, type=int, metavar="N",
                    help="print worked example N (1-7; default 6)")
    ap.add_argument("--print-example-input", type=int, metavar="N",
                    help="print the input JSON for worked example N")
    ap.add_argument("--selftest", action="store_true", help="run regression tests")
    args = ap.parse_args(argv)

    try:
        if args.selftest:
            return selftest()
        if args.print_example_input is not None:
            if args.print_example_input not in EXAMPLES:
                ap.error("example must be one of %s" % sorted(EXAMPLES))
            print(json.dumps(EXAMPLES[args.print_example_input]["input"], indent=2))
            return 0
        if args.example is not None:
            if args.example not in EXAMPLES:
                ap.error("example must be one of %s" % sorted(EXAMPLES))
            print(json.dumps(EXAMPLES[args.example]["input"], indent=2))
            print()
            print(run_example(args.example, as_json=args.json))
            return 0
        if not args.input:
            ap.print_help()
            return 2
        with open(args.input, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        r = compute(data)
        print(json.dumps(to_jsonable(r), indent=2) if args.json else report_text(r))
        return 0
    except InputError as e:
        print("input error: %s" % e, file=sys.stderr)
        return 2
    except (RuntimeError, ValueError) as e:
        print("error: %s" % e, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

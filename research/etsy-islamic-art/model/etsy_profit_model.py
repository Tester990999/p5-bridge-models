#!/usr/bin/env python3
"""
Etsy fee stack + unit-economics model for Islamic art products.

Fee assumptions (Etsy US seller, 2026 schedule):
  - Listing fee:            $0.20 per listing / renewal (auto-renews on each sale)
  - Transaction fee:        6.5% of (item price + shipping charged + gift wrap)
  - Payment processing US:  3.0% + $0.25 of total order (item + shipping + tax)
  - Offsite Ads (if the sale is attributed): 15% if shop made < $10k trailing 12 months,
                                             12% if >= $10k (mandatory at that point)
  - Regulatory operating fee: 0% for US sellers (2026: UK 0.48%, FR 1.14%, IT 0.80%, ES 0.88%, TR 1.67%)
  - Offsite Ads fee is capped at $100 per order

Run:  python3 etsy_profit_model.py            -> prints tables and writes ../data/*.csv
"""
from dataclasses import dataclass, asdict
import csv, os, statistics

OUT = os.path.join(os.path.dirname(__file__), "..", "data")

LISTING_FEE = 0.20
TRANSACTION_PCT = 0.065
PROC_PCT_US = 0.03
PROC_FIXED_US = 0.25
OFFSITE_LOW = 0.15   # < $10k trailing 12m revenue (optional tier)
OFFSITE_HIGH = 0.12  # >= $10k trailing 12m revenue (mandatory tier)
REG_FEE = {"US": 0.0, "UK": 0.0048, "FR": 0.0114, "IT": 0.0080, "ES": 0.0088, "TR": 0.0167}  # 2026 rates (TR from 22 Jun 2026)

@dataclass
class Product:
    name: str
    category: str
    price: float          # item price charged to buyer
    ship_charged: float   # shipping charged to buyer
    cogs: float           # cost of goods (blank + print + packaging), 0 for digital
    ship_cost: float      # what the seller actually pays to ship (POD often bakes this in)
    labour_min: float     # minutes of seller labour per order
    returns_pct: float    # share of orders refunded

def fee_stack(p: Product, offsite_share: float = 0.0, offsite_rate: float = OFFSITE_HIGH,
              country: str = "US", proc_pct: float = PROC_PCT_US, proc_fixed: float = PROC_FIXED_US):
    """Return dict of fees for ONE order. offsite_share = probability the order is offsite-ads attributed."""
    gross = p.price + p.ship_charged
    listing = LISTING_FEE
    transaction = TRANSACTION_PCT * gross
    processing = proc_pct * gross + proc_fixed
    offsite = offsite_share * min(offsite_rate * gross, 100.0)  # $100/order cap
    regulatory = REG_FEE[country] * gross
    etsy_total = listing + transaction + processing + offsite + regulatory
    net_after_etsy = gross - etsy_total
    contribution = net_after_etsy - p.cogs - p.ship_cost
    contribution_after_returns = contribution * (1 - p.returns_pct) - p.returns_pct * (p.cogs + p.ship_cost)
    return {
        "product": p.name, "category": p.category, "gross_order": round(gross, 2),
        "listing_fee": round(listing, 2), "transaction_fee": round(transaction, 2),
        "processing_fee": round(processing, 2), "offsite_ads_fee_expected": round(offsite, 2),
        "regulatory_fee": round(regulatory, 2), "etsy_fees_total": round(etsy_total, 2),
        "etsy_take_rate_pct": round(100 * etsy_total / gross, 1),
        "cogs": p.cogs, "ship_cost": p.ship_cost,
        "contribution_per_order": round(contribution, 2),
        "contribution_after_returns": round(contribution_after_returns, 2),
        "contribution_margin_pct": round(100 * contribution_after_returns / gross, 1),
        "labour_min": p.labour_min,
    }

# Representative products for the Islamic-art niche. COGS sourced from Printify/Printful/Gelato
# 2025-26 base prices and metal-art seller reports (see README sources).
PRODUCTS = [
    Product("Digital download – Ayatul Kursi printable set", "digital", 6.50, 0.00, 0.00, 0.00, 0.0, 0.01),
    Product("Digital download – Ramadan decor bundle", "digital", 12.00, 0.00, 0.00, 0.00, 0.0, 0.01),
    Product("POD matte poster 12x16 (Printify avg)", "pod_print", 24.00, 6.00, 7.50, 5.50, 3, 0.03),
    Product("POD matte poster 18x24", "pod_print", 35.00, 8.00, 11.00, 7.50, 3, 0.03),
    Product("POD framed poster 16x20", "pod_print", 69.00, 12.00, 34.00, 12.00, 3, 0.04),
    Product("POD canvas 16x20", "pod_print", 79.00, 0.00, 36.00, 14.00, 3, 0.04),
    Product("POD canvas 24x36", "pod_print", 139.00, 0.00, 62.00, 22.00, 3, 0.04),
    Product("Metal calligraphy wall art 24in (in-house laser/CNC)", "metal", 120.00, 0.00, 28.00, 18.00, 25, 0.02),
    Product("Metal calligraphy wall art 36in", "metal", 220.00, 0.00, 55.00, 32.00, 35, 0.02),
    Product("Metal calligraphy wall art 48in", "metal", 380.00, 0.00, 95.00, 55.00, 45, 0.02),
    Product("Ramadan wooden tabletop decor (handmade)", "handmade_decor", 45.00, 7.00, 12.00, 8.00, 20, 0.02),
    Product("Personalised nikkah / Eid gift frame", "handmade_gift", 55.00, 6.00, 14.00, 8.00, 25, 0.02),
]

def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def main():
    os.makedirs(OUT, exist_ok=True)
    # 1. Fee stack per product, three attribution scenarios
    rows = []
    for p in PRODUCTS:
        for label, share, rate in [("no_offsite", 0.0, OFFSITE_HIGH),
                                   ("offsite_15pct_small_shop", 1.0, OFFSITE_LOW),
                                   ("offsite_12pct_large_shop", 1.0, OFFSITE_HIGH),
                                   ("blended_20pct_orders_offsite", 0.20, OFFSITE_HIGH)]:
            r = fee_stack(p, share, rate); r["scenario"] = label; rows.append(r)
    write_csv(os.path.join(OUT, "fee_stack_by_product.csv"), rows)

    # 2. Monthly profit sensitivity (blended 20% offsite attribution, 12% rate)
    fixed_monthly = {"digital": 25, "pod_print": 60, "metal": 650, "handmade_decor": 120, "handmade_gift": 120}  # software, Etsy Plus, machine finance, workshop
    ads_pct_of_rev = {"digital": 0.06, "pod_print": 0.10, "metal": 0.08, "handmade_decor": 0.08, "handmade_gift": 0.08}  # Etsy Ads spend as % revenue
    labour_rate = 20.0  # $/hr opportunity cost
    sens = []
    reps = {"digital": PRODUCTS[0], "pod_print": PRODUCTS[3], "metal": PRODUCTS[7], "handmade_decor": PRODUCTS[10]}
    for cat, p in reps.items():
        base = fee_stack(p, 0.20, OFFSITE_HIGH)
        for orders in [10, 30, 100, 300, 1000]:
            revenue = base["gross_order"] * orders
            contrib = base["contribution_after_returns"] * orders
            ads = ads_pct_of_rev[cat] * revenue
            labour = labour_rate * p.labour_min / 60 * orders
            profit_before_labour = contrib - ads - fixed_monthly[cat]
            profit_after_labour = profit_before_labour - labour
            sens.append({"category": cat, "representative_product": p.name, "orders_per_month": orders,
                         "monthly_revenue": round(revenue), "etsy_fees": round(base["etsy_fees_total"] * orders),
                         "cogs_and_shipping": round((p.cogs + p.ship_cost) * orders), "etsy_ads": round(ads),
                         "fixed_costs": fixed_monthly[cat], "labour_hours": round(p.labour_min / 60 * orders, 1),
                         "profit_before_owner_labour": round(profit_before_labour),
                         "profit_after_owner_labour_at_20_per_hr": round(profit_after_labour),
                         "net_margin_pct": round(100 * profit_before_labour / revenue, 1) if revenue else 0})
    write_csv(os.path.join(OUT, "monthly_profit_sensitivity.csv"), sens)

    # 3. Print a compact summary
    print("== Fee stack, blended 20% offsite attribution ==")
    for p in PRODUCTS:
        r = fee_stack(p, 0.20, OFFSITE_HIGH)
        print(f"{p.name[:52]:52s} gross ${r['gross_order']:7.2f}  etsy ${r['etsy_fees_total']:6.2f} ({r['etsy_take_rate_pct']}%)  contrib ${r['contribution_after_returns']:7.2f} ({r['contribution_margin_pct']}%)")
    print("\n== Monthly profit before owner labour ==")
    for s in sens:
        print(f"{s['category']:14s} {s['orders_per_month']:5d}/mo  rev ${s['monthly_revenue']:7d}  profit ${s['profit_before_owner_labour']:7d}  ({s['net_margin_pct']}%)  hrs {s['labour_hours']}")

if __name__ == "__main__":
    main()

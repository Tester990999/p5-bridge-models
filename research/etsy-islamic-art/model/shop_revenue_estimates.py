#!/usr/bin/env python3
"""
Estimate lifetime and annual sales VALUE (GMV) and seller profit per Islamic-art Etsy shop.

Method: lifetime sales count (from data/islamic_art_etsy_shops.csv) x an assumed average
order value (AOV) for that shop's product mix, with low / mid / high AOV bands drawn from
data/observed_prices.csv and the POD/metal cost research. Profit = GMV x contribution margin
(after Etsy fees, COGS, shipping; before owner labour, ads, fixed costs) from etsy_profit_model.py.

These are ESTIMATES. Etsy does not publish per-shop revenue; sales counts are from search
snippets of unknown date. Treat the mid case as a central guess and the band as the range.
"""
import csv, os
HERE = os.path.dirname(__file__); DATA = os.path.join(HERE, "..", "data")

# product-mix profiles: (aov_low, aov_mid, aov_high, contribution_margin)
PROFILES = {
    "metal":    (85, 105, 130, 0.47),   # observed sale prices $79-144 (mean $111); clocks/small pieces pull mid down
    "favors":   (25, 35, 50, 0.45),     # nikkah favors, tasbih sets, prayer mats; often multi-unit orders
    "digital":  (5, 7, 12, 0.80),       # printables $4.99-$12
    "prints":   (30, 45, 80, 0.35),     # paper/canvas prints, paintings; POD-like margins
    "decor":    (35, 50, 70, 0.45),     # wood, tabletop, Ramadan/Eid decor, gifts
    "mixed":    (30, 60, 100, 0.42),    # shop shows $33-$200+ range
}
SHOP_PROFILE = {
    "IslamicWallArtStore":"metal","IslamicMetalWallArt":"metal","IslamicWallArtDecor":"metal",
    "WallArtIslamic":"metal","BreatheIslamicArt":"metal","BestIslamicGifts":"metal","SNAmetal":"metal","NoorMetalArt":"metal",
    "islamicgiftsfavors":"favors","TheQuranStore":"favors","Islamicgiftandfavour":"favors","HafsaCreates":"favors",
    "IslamicArtPrintables":"digital","NuqtaCalligraphyShop":"digital",
    "Hidayahartprints":"prints","ArtziCulture":"prints","AdornYourWallsShop":"prints","PeacefulArtsUk":"prints",
    "SalehaArt":"prints","MiniatureArtsByPinar":"prints","alsaffarstudio":"prints","MihrimahIslamicArt":"prints","IslamicArtKW":"prints",
    "IslamicArabicDecor":"decor","DaysofEid":"decor","IslamicDecorUSA":"decor",
    "IslamicDecorsShop":"mixed",
}
# years open where a snippet gave "since YYYY" or "N years" (as of Sept 2026)
YEARS = {"IslamicWallArtStore":7.0,"islamicgiftsfavors":5.0,"BreatheIslamicArt":3.0,"TheQuranStore":4.0,
         "WallArtIslamic":5.0,"Hidayahartprints":3.0,"NuqtaCalligraphyShop":5.0,"DaysofEid":9.0,"IslamicDecorsShop":2.5}
DEFAULT_YEARS = 4.0  # assumption for shops with no "since" date; flagged in output

def main():
    rows = list(csv.DictReader(open(os.path.join(DATA, "islamic_art_etsy_shops.csv"))))
    out = []
    for r in rows:
        shop = r["shop"]; sales = int(r["lifetime_sales"]); prof = SHOP_PROFILE[shop]
        lo, mid, hi, margin = PROFILES[prof]
        yrs = YEARS.get(shop); yrs_flag = "snippet" if yrs else "assumed"
        yrs = yrs or DEFAULT_YEARS
        gmv_lo, gmv_mid, gmv_hi = sales*lo, sales*mid, sales*hi
        ann_mid = gmv_mid/yrs
        out.append({
            "shop": shop, "profile": prof, "lifetime_sales": sales,
            "aov_low": lo, "aov_mid": mid, "aov_high": hi,
            "lifetime_gmv_low": round(gmv_lo), "lifetime_gmv_mid": round(gmv_mid), "lifetime_gmv_high": round(gmv_hi),
            "years_open": yrs, "years_source": yrs_flag,
            "annual_sales_mid": round(sales/yrs), "annual_gmv_mid": round(ann_mid),
            "annual_gmv_low": round(gmv_lo/yrs), "annual_gmv_high": round(gmv_hi/yrs),
            "contribution_margin": margin, "annual_contribution_mid": round(ann_mid*margin),
            "lifetime_contribution_mid": round(gmv_mid*margin),
        })
    out.sort(key=lambda x: -x["lifetime_gmv_mid"])
    with open(os.path.join(DATA, "shop_revenue_estimates.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

    tot = lambda k: sum(o[k] for o in out)
    print(f"{'shop':24s}{'prof':9s}{'sales':>7s}{'AOV':>6s}{'lifetime GMV (mid)':>20s}{'annual GMV (mid)':>18s}{'annual contrib':>16s}")
    for o in out:
        print(f"{o['shop']:24s}{o['profile']:9s}{o['lifetime_sales']:7d}{o['aov_mid']:6d}{o['lifetime_gmv_mid']:20,d}{o['annual_gmv_mid']:18,d}{o['annual_contribution_mid']:16,d}")
    print(f"\nSAMPLE TOTAL lifetime GMV: low ${tot('lifetime_gmv_low'):,}  mid ${tot('lifetime_gmv_mid'):,}  high ${tot('lifetime_gmv_high'):,}")
    print(f"SAMPLE TOTAL annual GMV (mid): ${tot('annual_gmv_mid'):,}   annual contribution (mid): ${tot('annual_contribution_mid'):,}")
    print(f"Lifetime contribution (mid): ${tot('lifetime_contribution_mid'):,}")
    # profile subtotals
    for p in PROFILES:
        sub = [o for o in out if o["profile"]==p]
        if sub: print(f"  {p:8s} shops {len(sub):2d}  lifetime GMV mid ${sum(o['lifetime_gmv_mid'] for o in sub):,}  annual mid ${sum(o['annual_gmv_mid'] for o in sub):,}")

if __name__ == "__main__":
    main()

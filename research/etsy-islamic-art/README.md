# Etsy Islamic Art Market Research (September 2026)

Private research pack. Repo is private; nothing here is published.

**Question asked:** Is selling Islamic art on Etsy worth doing? What do sellers actually make, how big is the market, how have sellers scaled, what drives sales, and which social channels multiply reach?

**Short answer:** Yes, but as a *design-led, seasonally-timed, multi-channel* business, not as "list prints and wait". The niche has a proven top tier (three shops with 20k to 31k lifetime sales, about 4,500 to 5,900 orders a year each), a healthy middle of established 3-to-5-year shops doing roughly 440 to 1,470 orders a year, and a long tail of shops with under 100 sales. Etsy's platform is flat-to-slightly-growing (marketplace GMS +7.5% in Q2 2026 after two years of decline), so growth has to come from taking share inside the niche, not from the tide. Realistic outcomes and the evidence are below.

---

## Contents

1. [How this was researched and what could not be verified](#1-method-and-data-limitations)
2. [Etsy marketplace fundamentals and trajectory](#2-etsy-marketplace-fundamentals-and-trajectory)
3. [The Islamic art niche on Etsy: shops, sales, prices](#3-the-islamic-art-niche-on-etsy)
4. [Mean value, fees and profit per product type](#4-mean-value-fees-and-profit)
5. [Engagement, views and conversion benchmarks](#5-engagement-views-and-conversion)
6. [How sellers have scaled over the years](#6-how-sellers-have-scaled)
7. [Correlations: what drives sales](#7-what-correlates-with-sales)
8. [Social media and other channels to maximise reach](#8-social-media-and-other-channels)
9. [Market size, customer trajectory and demographics](#9-market-size-and-customer-trajectory)
10. [Historical market timeline](#10-historical-market-timeline)
11. [Is it worth doing? Verdict and playbook](#11-verdict-and-playbook)
12. [Sources](#12-sources)

Supporting files:

| File | What it is |
|---|---|
| `model/etsy_profit_model.py` | Fee stack and monthly profit model; edit the product list and re-run |
| `data/fee_stack_by_product.csv` | Per-order fees and contribution for 12 representative products, 4 Offsite Ads scenarios |
| `data/monthly_profit_sensitivity.csv` | Monthly profit at 10 to 1,000 orders per month by product type |
| `data/observed_prices.csv` | 19 real price points observed for Islamic art items, with source and provenance |
| `data/islamic_art_etsy_shops.csv` | 27 Islamic art Etsy shops with lifetime sales, admirers, products, location |
| `data/etsy_marketplace_timeseries.csv` | Etsy GMS, revenue, take rate, buyers, sellers 2015 to 2025 |
| `appendix/01` to `05` | Raw output of the five research threads with full source lists |

---

## 1. Method and data limitations

Research was done on 2026-09-05 from a sandbox whose network policy blocks etsy.com, SEC EDGAR, Wayback Machine, Similarweb, eRank, EverBee, Alura and most other data sites. Consequences:

- **No live Etsy page was read.** Every Etsy figure comes from Google search snippets of Etsy shop, listing and market pages, whose crawl dates are unknown. The same shop appeared with two sales counts in different snippets (IslamicMetalWallArt 12,787 vs 19,872), so treat shop figures as "within the last 6 to 18 months".
- **Result counts per keyword could not be obtained.** Etsy's "X results" is not exposed in snippets.
- **Price sample is 19 points, not the 40 targeted.** Snippets of listing pages omit price; the points found come from Etsy market-page snippets and two sellers' own storefronts.
- **Etsy keyword volumes (eRank/EverBee) were not obtainable.** Demand signals rely on Google Trends indices relayed by third parties.
- Etsy corporate figures are tagged **[S]** when read from a snippet of the filing or press release, and **[K]** when recalled from training against a cited filing but not re-read this session. Verify [K] figures against the linked filing before relying on them externally.
- Third-party "Etsy statistics" blogs are indicative, not audited.

Everything that *could* be checked against a primary source was. The per-order fee arithmetic is exact for the 2026 fee schedule.

---

## 2. Etsy marketplace fundamentals and trajectory

### 2.1 Size and growth (Etsy marketplace, excludes Reverb/Depop)

| Year | Marketplace GMS | Revenue | Take rate | Active buyers | Active sellers |
|---|---|---|---|---|---|
| 2015 | $2.4bn | $274m | 11.4% | 24.0m | 1.6m |
| 2018 | $3.9bn | $604m | 15.4% | 39.4m | 2.1m |
| 2019 | $4.7bn | $818m | 16.5% | 46.4m | 2.7m |
| 2020 | $9.4bn | $1,726m | 16.8% | 81.9m | 4.4m |
| 2021 | $12.2bn | $2,329m | 17.3% | 96.3m | 7.5m |
| 2022 | $11.8bn | $2,566m | 19.3% | 95.1m | 7.5m |
| 2023 | $11.7bn | $2,748m | 20.9% | 96.5m | 9.0m |
| 2024 | $10.9bn | $2,808m | 22.3% | 95.5m | 8.1m |
| 2025 | $10.5bn | $2,880m | ~24% | 86.5m | 5.6m |

Full series with sources in `data/etsy_marketplace_timeseries.csv`. Sources: Etsy 10-Ks and Q4 2025 release (sec.gov, investors.etsy.com), CNBC 2026-02-19.

**Reading the table.** GMS doubled in 2020, peaked in 2021, and has drifted down about 14% since. Revenue kept rising because Etsy's take rate more than doubled from 11% to 24% (fee rise to 5% in 2018 and 6.5% in 2022, Offsite Ads from 2020, payments penetration). Active sellers fell from 9.0m to 5.6m in two years, partly definitional cleanup and the 2024 shop set-up fee, which is *good for incumbents*: fewer competing shops per buyer.

**Turn in 2026.** Marketplace GMS grew +5.5% YoY in Q1 2026 and +7.5% in Q2 2026, the fifth consecutive quarter of sequential improvement. GMS per active buyer reached $124 (up 2.8% YoY). Habitual buyers (6+ purchase days and $200+ a year) were 5.9m at end-2025, about 7% of buyers but roughly 40% of GMS; they grew sequentially in Q2 2026 for the first time since 2023. Sources: Q1 and Q2 2026 shareholder letters (sec.gov), TradingView, Digital Commerce 360.

### 2.2 Traffic and geography

| Metric | Value | Source |
|---|---|---|
| Monthly visits to etsy.com | ~462m (July 2026), peaks over 500m in December | Similarweb via Blogging Wizard, Thunderbit |
| Mobile share of web visits | ~64% | eCommerce Bonsai |
| App share of GMS | ~47% (Q1 2026), app GMS +11% YoY | Q1 2026 shareholder letter |
| US share of buyer GMS | ~74% | Link My Books |
| Traffic share UK / Canada / Germany / France | 9.3% / 5.1% / 4.3% / 3.0% | Link My Books (Similarweb-derived) |
| Core geographies | US, UK, Germany, Canada, Australia, France | Etsy 10-K |
| Agentic AI referrals (ChatGPT etc.) | 15x YoY growth in Q4 2025, still under 1% of traffic | PYMNTS |

Relevance for Islamic art: the UK, Canada, Germany and France are all top-six Etsy geographies *and* have large, young, relatively affluent Muslim populations (section 9). The top Islamic art shops found are US, UK, Canada and Türkiye based and ship free to US/UK/CA/EU/AU.

### 2.3 Fees (2026 schedule, US seller)

| Fee | Amount |
|---|---|
| Listing | $0.20 per listing, renews every 4 months or on each sale |
| Transaction | 6.5% of item + shipping + gift wrap |
| Payment processing | US 3% + $0.25; UK 4% + £0.20; most EU 4% + €0.30 |
| Offsite Ads (only when a sale is attributed to Etsy's off-platform ads) | 15% if under $10k trailing 12-month sales (optional); 12% and mandatory once over $10k; capped at $100 per order |
| Regulatory operating fee | 0% US; UK 0.48%, France 1.14%, Italy 0.80%, Spain 0.88%, Türkiye 1.67% (raised 22 June 2026) |
| Currency conversion | 2.5% if listing currency differs from payout currency |
| New shop set-up | One-time, $15 in US (introduced 2024) |
| Etsy Plus | $10 per month (optional) |

Effective all-in take on a plain US sale is about 10% to 11% before ads, and about 25% on an Offsite-Ads-attributed sale. Sources: Printify, Craftybase, Marmalead, iscompliant.app, GeekSeller, growtsy.

### 2.4 Policy: what you can list

Etsy's Creativity Standards (July 2024, tightened June 2025) sort listings into "Made by a seller" (physical items you craft), "Designed by a seller" (your original design, sold as a digital file or produced by a disclosed print-on-demand partner), "Handpicked" (vintage) and "Sourced" (supplies). Original Islamic calligraphy prints via Printify or Gelato are allowed under "Designed by a seller" with the production partner disclosed. AI-assisted art is allowed if disclosed and if the seller adds real creative input; prompt packs and undisclosed AI are banned. Selling other people's calligraphy vectors (Gumroad DXF packs and the like) as "made by me" violates the June 2025 rules. A 2026 Search Visibility Dashboard shows sellers which listings are demoted and why (title quality, shipping price, missing attributes, photos). Sources: Etsy Seller Handbook article 1276491338090, iscompliant.app, mydesigns.io.

### 2.5 Competitors for the same product

| Platform | Fee to seller | Reach |
|---|---|---|
| Etsy | ~10% base, ~25% with Offsite Ads | ~87m buyers, 462m visits per month |
| Amazon Handmade | 15% referral, no listing fee | Huge, but no niche curation; Ramadan storefront exists |
| Shopify own site | ~$39 per month + 2.9% + $0.30 | Zero built-in traffic; you bring buyers |
| eBay | ~13.6% + $0.40 | Weak for art |
| Redbubble | Artist margin cut up to 50% at Standard tier (2025) | POD-only, saturated |
| Society6 | Artist gets 10% on posters/framed, 5% elsewhere | POD-only |
| Not On The High Street (UK) | £199 joining + 25% commission | Curated UK gifting |
| Folksy (UK) | 6% + 15p listing | Small |
| TikTok Shop UK | ~9% + £0.50 per order | Fast-growing, video-driven |

Etsy remains the cheapest marketplace *with* built-in buyer traffic for handmade and designed art. The mature pattern (section 6) is Etsy first, own Shopify site second, wholesale and TikTok Shop third.

---

## 3. The Islamic art niche on Etsy

### 3.1 Breadth

Etsy maintains at least 45 distinct indexed landing pages for the niche (islamic_wall_art, modern_islamic_wall_art, islamic_metal_wall_art, ayatul_kursi_metal, islamic_digital_products, islamic_printable, quran_wall_art, ramadan_decoration, eid_decor, eid_gifts, nikkah frames, and so on) plus editorial gift guides titled "Eid Gifts: 60+ Gift Ideas for 2026" and "Ramadan Gift: 60+ Gift Ideas for 2026". The main sub-categories, in rough order of revenue weight observed:

1. **Metal calligraphy wall art** (laser-cut steel, powder-coated black/gold/silver/copper; Ayatul Kursi, Kalima, Bismillah, 99 Names, the 4 Quls). Dominated by Türkiye-linked makers selling from US warehouses.
2. **Canvas and framed prints** (sets of 3, Kaaba and mosque art, minimalist calligraphy, Palestinian courtyard and olive-tree watercolours trending in "modern Islamic wall art").
3. **Digital downloads** (printable Ayatul Kursi, dua cards, Ramadan decor bundles, Eid banners, kids' Islamic prints, Umrah guides).
4. **Ramadan and Eid decor** (garlands, bunting, felt crescents, string lights, shadow boxes, countdown calendars, table decor).
5. **Gifting** (nikkah frames and certificates, Aqiqah and hifz-completion prints, personalised Eid gifts, hampers, favors).
6. **Wood, acrylic, stone and tabletop pieces**; jewellery (Arabic name necklaces) as an adjacent lane.

### 3.2 Shops and sales volume (27 shops, `data/islamic_art_etsy_shops.csv`)

| Shop | Lifetime sales | Admirers | Since / years | Location | Core product |
|---|---|---|---|---|---|
| IslamicWallArtStore | 31,430 | 5,934 | 2019 | California | metal, wood, acrylic, stone wall art |
| islamicgiftsfavors | 29,327 | | 2021 | Istanbul | nikkah favors, prayer mats |
| IslamicMetalWallArt | 19,872 | 4,152 | | New Jersey | metal wall art, clocks |
| IslamicWallArtDecor | 9,560 | 2,076 | | Texas | canvas, metal, glass |
| IslamicArtPrintables | 6,999 | 781 | | London | 194 digital products |
| BreatheIslamicArt | 4,400 | 776 | 3 yrs | | metal sets, clocks |
| TheQuranStore | 4,161 | | 2022 | | Islamic gifts |
| WallArtIslamic | 3,672 | 861 | 5 yrs | Istanbul | 261 items, mostly metal |
| ArtziCulture | 3,328 | 1,898 | | | hand-painted canvas, stone |
| AdornYourWallsShop | 2,401 | 268 | | | 121 poster items |
| NuqtaCalligraphyShop | 2,200 | | 5 yrs | England | downloadable prints |
| PeacefulArtsUk | 2,126 | 434 | | UK | canvas, wedding signs |
| BestIslamicGifts | 2,068 | 445 | | Florida | metal wall art |
| HafsaCreates | 1,798 | 1,756 | | Toronto | cards, custom gifts |
| Hidayahartprints | ~1,500 | | 3 yrs | UK | digital + giclée prints |
| SalehaArt | 1,452 | 1,435 | | Toronto | prints of paintings |
| IslamicArabicDecor | 1,436 | 562 | | Chicago | carved wood |
| DaysofEid | 1,405 | | 2017 | | Eid decor |
| 9 further shops | 5 to 712 each | | | | |

**Distribution statistics (n = 27):**

| Statistic | Value |
|---|---|
| Total lifetime sales counted | 131,649 |
| Mean per shop | 4,876 |
| Median per shop | 1,798 |
| Shops under 100 sales | 4 |
| Shops 100 to 999 | 5 |
| Shops 1,000 to 4,999 | 13 |
| Shops 5,000 to 9,999 | 2 |
| Shops 10,000+ | 3 |
| Top-3 share of counted sales | 61% |

The sample is biased toward shops Google surfaces, so the true median across *all* Islamic art shops is lower and the tail of near-zero shops is much longer (platform-wide, roughly half of Etsy sellers earn under $1,000 a year).

**Run-rate (lifetime sales divided by years open):**

| Shop | Sales per year |
|---|---|
| islamicgiftsfavors | ~5,900 |
| IslamicWallArtStore | ~4,500 |
| BreatheIslamicArt | ~1,470 |
| TheQuranStore | ~1,040 |
| WallArtIslamic | ~730 |
| Hidayahartprints | ~500 |
| NuqtaCalligraphyShop | ~440 |
| DaysofEid | ~160 |
| IslamicDecorsShop | ~20 |

**Admirers-to-sales ratio** separates artists from volume sellers: painters and print artists sit above 1 (MiniatureArtsByPinar 2.5, alsaffarstudio 2.1, SalehaArt 1.0), metal and digital volume sellers sit at 0.1 to 0.2. High admirer ratios signal brand affinity that transfers to Instagram and a Shopify site; low ratios signal search-driven, price-comparison demand.

### 3.3 Prices observed (`data/observed_prices.csv`)

| Sub-category | n | Mean | Median | Min | Max |
|---|---|---|---|---|---|
| Metal wall art (sale prices) | 8 | $111 | $114 | $79 | $144 |
| Metal wall art (list prices before 30 to 52% "sales") | 8 | $181 | $170 | $122 | $250 |
| Stainless tabletop decor (Sukar Decor) | 3 | $92 | $89 | $89 | $99 |
| Digital download (Ramadan/Eid) | 1 | $4.99 | | | |
| UK Islamic gift shop range | 4 | $73 | $76 | $12 | $128 |
| Nikkah frames (UK) | range | | | ~$25 | ~$128 |
| Handmade Ramadan garland | 1 | ~$25 | | | |
| Mixed shop (IslamicDecorsShop) | range | | | $34 | $200+ |
| **All observed points** | 19 | **$90** | **$99** | $5 | $200 |

Industry-typical bands from POD and seller guides fill the gaps: single printable $5 to $15, printable bundles $10 to $30, paper posters $20 to $45, canvas $50 to $150, metal $79 to $400+.

**Mean order value for the niche** is therefore roughly $90 to $100 for a physical-goods shop, about 3x Etsy's platform-wide GMS per buyer per year ($124) spent in a single order, which is why metal sellers dominate the sales leaderboard: each order carries $55 to $100 of contribution.

Note the "permanent sale" pricing pattern: leading metal sellers list at $122 to $250 and show 30% to 52% off. Anchor pricing is standard in this niche.

### 3.4 Demand signals and seasonality

- Google interest in "ramadan decorations" peaks at index 100 in the Ramadan month (March 2025) and "ramadan home decor" hit 68 in February 2026 ahead of Ramadan (17 Feb to 19 Mar 2026). Source: Accio trend summaries.
- The "Ramadan and Eid party favors and decorations" search index rose from 186 (July 2025) to 469 (November 2025), a +152% build across the off-season. Source: Accio.
- #RamadanDecor mentions were up 129% year on year in 2025; online Ramadan mentions were up 76% in the three months before Ramadan 2026 versus 2025. Source: Accio.
- Search volume rises 2 to 3 weeks before Ramadan; gifting spend is 45% higher in the final two weeks; shopping-app installs rise 28% globally during Ramadan. Sources: Viden Growth, Accio.
- Google keyword "quran verse" carries ~27,100 monthly searches globally (RankHero); Etsy-internal volumes were not obtainable.
- Evergreen sub-niches carry the other nine months: nikkah and wedding gifting (islamicgiftsfavors, 29k sales, is essentially a wedding-favor shop), housewarming Bismillah pieces, Aqiqah and baby gifts, hifz-completion frames, couples' prayer mats.

**Calendar.** Ramadan 2027 begins around 7 February 2027, Eid al-Fitr around 9 March 2027, Eid al-Adha around 16 May 2027. Given the July-to-November build-up, Ramadan 2027 listings should be live and gathering reviews by early December 2026, with ads scaling from mid-January.

---

## 4. Mean value, fees and profit

### 4.1 What Etsy sellers make (platform-wide context)

| Metric | Value | Source |
|---|---|---|
| GMS per active seller per year (2025) | ~$1,870 | 10-K arithmetic ($10.46bn / 5.6m) |
| Sellers earning under $1,000 a year | ~50% | Printify survey |
| Shops earning under $100 a month | ~70% | CraftPilot |
| Sellers over $10,000 a year | under 500k, ~9% of sellers | Skillademia (third-party) |
| Sellers over $2,000 a month | ~12% | Podbase |
| Sellers over $5,000 a month | ~4% | Podbase |
| Median seller revenue | ~$574 a month (~$6.9k a year) | Customcy / eRank-derived |
| Mean seller revenue | ~$2,965 a month (skewed by top shops) | Customcy |
| Median digital-download seller | £400 to £800 a month | Insight Agent |
| Top 10% of digital sellers | £8k to £30k+ a month from 50 to 200 listings | Insight Agent |
| Shops with any sale in a 30-day window | 26% of 3.17m shops analysed | Insight Agent |
| Sellers who say Etsy is their sole occupation | ~30% | Etsy 2024 Seller Census |

The mean is roughly five times the median. Any "average Etsy seller earns X" claim is meaningless without saying which one; the median seller is a hobbyist, the mean is dragged up by a few thousand large shops.

### 4.2 Fee stack per order (exact, US seller, 2026)

From `model/etsy_profit_model.py`, blended assumption that 20% of orders arrive via Offsite Ads at the 12% mandatory tier:

| Product | Buyer pays | Etsy fees | Take | COGS + ship | Contribution | Margin |
|---|---|---|---|---|---|---|
| Digital printable | $6.50 | $1.22 | 18.8% | $0 | $5.22 | 80% |
| Digital bundle | $12.00 | $1.88 | 15.6% | $0 | $10.02 | 84% |
| POD poster 12x16 + ship | $30.00 | $4.02 | 13.4% | $13.00 | $12.20 | 41% |
| POD poster 18x24 + ship | $43.00 | $5.57 | 12.9% | $18.50 | $17.81 | 41% |
| POD framed 16x20 + ship | $81.00 | $10.09 | 12.5% | $46.00 | $22.07 | 27% |
| POD canvas 16x20 | $79.00 | $9.85 | 12.5% | $50.00 | $16.38 | 21% |
| POD canvas 24x36 | $139.00 | $16.99 | 12.2% | $84.00 | $33.13 | 24% |
| Metal calligraphy 24in (own laser) | $120.00 | $14.73 | 12.3% | $46.00 | $57.16 | 48% |
| Metal calligraphy 36in | $220.00 | $26.63 | 12.1% | $87.00 | $102.50 | 47% |
| Metal calligraphy 48in | $380.00 | $45.67 | 12.0% | $150.00 | $177.64 | 47% |
| Handmade Ramadan tabletop + ship | $52.00 | $6.64 | 12.8% | $20.00 | $24.45 | 47% |
| Personalised nikkah frame + ship | $61.00 | $7.71 | 12.6% | $22.00 | $30.23 | 50% |

Without any Offsite Ads attribution the take falls to about 10% to 11%; on a fully attributed order it rises to about 25%. Full scenarios are in `data/fee_stack_by_product.csv`. Cost inputs: Printify or Printful 18x24 poster about $8 to $11 base plus $5 to $8 shipping; framed 16x20 about $34; canvas 16x20 about $36 and 24x36 about $62 plus $14 to $22 shipping; laser-cut steel material under $10 plus powder coat, packaging and carrier; fiber laser $13.5k to $33k. Sources: Apparel Hub, Podvector, Gelato, SendCutSend, Sign Customiser, GYC Laser.

**Cross-check against the economics agent's independent worked example:** a $35 print with $5 shipping nets $22.75 profit with no Offsite Ads and $16.75 at 15% Offsite Ads; a $120 metal piece with $15 shipping nets $76.72 and $56.47; a $6 download nets $4.98 and $4.08. The two calculations agree within rounding.

### 4.3 Monthly profit sensitivity (`data/monthly_profit_sensitivity.csv`)

Before owner labour and tax; includes Etsy Ads at 6% to 10% of revenue and fixed costs ($25 digital, $60 POD, $650 metal including laser finance, $120 handmade):

| Orders per month | Digital ($6.50) | POD poster ($43) | Metal 24in ($120) | Handmade decor ($52) |
|---|---|---|---|---|
| 10 | $23 | $75 | -$174 | $83 |
| 30 | $120 | $345 | $777 | $489 |
| 100 | $458 | $1,291 | $4,106 | $1,909 |
| 300 | $1,424 | $3,993 | $13,618 | $5,967 |
| 1,000 | $4,805 | $13,450 | $46,910 | $20,170 |
| Owner hours at 300 orders | ~0 | 15 | 125 | 100 |

Reading it against the niche data: the leading metal shops run 375 to 490 orders a month, which this model puts at roughly $17k to $23k monthly profit before staff. That requires a workshop and 2 to 4 people at 125+ labour hours per 300 pieces, which is exactly what the Türkiye-linked leaders have. A one-person digital shop at 300 orders a month (top-decile territory) clears about $1.4k. A POD shop needs about 300 orders a month to replace a modest salary.

### 4.4 Traffic required

At a 2% conversion rate (Etsy home goods benchmark), 30 orders needs 1,500 visits a month, 100 needs 5,000, 300 needs 15,000 and 1,000 needs 50,000. New shops in competitive niches convert at 1% to 2%; established shops 2% to 4%; conversion typically climbs once a shop passes about 50 sales and 10 to 20 reviews. Sources: Gelato, Craftybase, Insight Agent.

### 4.5 Off-Etsy customer acquisition

| Channel | 2025-26 benchmark | Source |
|---|---|---|
| Meta CPM | $15 to $25 (peaks Q4) | Trackbee, Sovran |
| Meta CPC | $0.85 to $1.32 | Trackbee |
| Instagram CPC | $0.40 to $1.80 (Reels cheapest) | Top Growth Marketing, Digital Applied |
| Meta CTR for Art and Home Decor | 2.9%, among the highest categories | Spark UGC |
| TikTok CPM / CPC | $5 to $13 / $0.45 to $0.85 | Triple Whale, Hawky |
| Pinterest CPM | ~€3, cheapest major platform | Trackbee |
| Etsy Ads CPC | ~$0.30 to $0.40 targeted, up to $1.89 observed; ROAS benchmark 2.8x, break-even 2x | Insight Agent, Etsy community |
| Ecommerce CAC average | $35 to $85 | Shopify, Ringly |

Implication: at ~$1 CPC and 2% conversion a paid click costs ~$50 per order. That kills paid acquisition for a $6 download or a $22-profit print. It works for $100+ metal pieces, bundles, or repeat buyers. Pinterest organic and Etsy's own search are the only channels cheap enough for low-ticket items, which is why digital sellers live on SEO.

### 4.6 Returns and religious-respect constraints

Home decor e-commerce returns run about 19% industry-wide, but small print sellers report low single digits (damage, misprint); digital items are generally non-refundable. Sources: Stuv, EightX.

Scholarly rulings and community norms matter for product design: Quranic text should not go on items that are walked on, sat on, or likely mishandled (rugs, mats, cushions, doormats, coasters, mugs, apparel), and verses must not be shaped into living creatures. Wall art, framed prints, metal and tabletop pieces are the accepted formats. Include care and disposal guidance in listings. Sources: IslamQA 13648, Islamweb 367540 and 247618.

IP: Arabic Quranic text is public domain, but recent English translations (Sahih International, Abdel Haleem) are copyrighted, individual calligraphers' compositions are copyrighted, and purchased DXF or SVG vector packs cannot be listed as "made by seller" under the June 2025 standards. Etsy removes listings on DMCA notice without warning and suspends repeat infringers. Sources: Shield My Shop, Cohn Legal, Etsy legal/ip.

---

## 5. Engagement, views and conversion

How Etsy Stats terms relate, with typical ratios:

| Term | Meaning | Typical ratio |
|---|---|---|
| Visit | One shopper in a 30-minute window | baseline |
| View | One listing page load | 1:1 is a warning sign, 3.5:1 views per visit is excellent |
| Favourite | Shopper hearts a listing | sellers report 10% to 35% of views |
| Order | Conversion = orders / visits | 1% to 3% average, 2% for home goods, 3% to 5% strong |
| Views per sale | | 33 to 100 |
| Etsy Ads CTR | Clicks / impressions | 2% good, 1% acceptable for high-ticket |

Sources: Etsy Seller Handbook 624088232713, Outfy, Gold City Ventures, Gelato, Webeyez.

Engagement proxies observed in the niche: one Hidayahartprints giclée print carries 2,347 favourites; IslamicWallArtStore has 5,934 admirers against 31,430 sales and 6,018 reviews (about one review per five orders, a normal Etsy ratio); BreatheIslamicArt's flagship metal set shows 1,300 reviews.

Social proof effects: listings with 5+ reviews are 270% more likely to be bought than those with none; purchase probability peaks at 4.0 to 4.7 stars rather than a perfect 5.0; Star Seller status is estimated at up to 22% higher conversion and Etsy's 2026 guidance says it yields a shop-wide ranking lift; the Bestseller badge raises click-through and visibility. Sources: WiserNotify, Genesys Growth, Growing Your Craft, Etsy help 4403058372503.

---

## 6. How sellers have scaled

### 6.1 Generic art, print and wall-decor sellers

| Seller | Product | Trajectory | What drove it |
|---|---|---|---|
| Rachel Jimenez, Prosperous Printables | Digital | $110k revenue in year two, ~$9.5k a month | Catalogue depth + SEO |
| Rachel Jones (Side Hustle Show) | Digital | $10k+ a month; went full-time after 3 years (2018 to 2021) | Organic Etsy search |
| Former MRI tech (Side Hustle Show) | POD | $15k a month revenue, $4k to $5k profit (~30%) | High-volume listing strategy |
| InsightsByJess case | POD incl. wall art | ~$250k a year from a 2022 start | POD scaling |
| Map-art seller (Starter Story) | Physical prints | $15k a month from under $500 start; began with 10 SKUs | Shopify + Etsy from day one, SKU expansion |
| Stoic Muse | Niche art merch | 100 to 150 units a month, ~$3k at 40% margin | Narrow identity niche |
| Printable wall-art shop (Creatives Hour) | Digital | 47,000 sales at ~$1.50 average, ~$3k a month | Volume, low ticket |
| Digital wall-art seller (Creatives Hour) | Digital | ~8,600 sales a month | Volume |
| Top-20 wall-art shops aggregate | Mixed | $300k to ~$7m estimated revenue each | Physical volume or solo illustrators at six figures |
| MOSTLIKELY (Etsy Quit Your Day Job) | Prints | Moved to manufacturers and European wholesale | Wholesale |
| The Wheatfield (Etsy QYDJ) | Prints | Flat prints declined; demand shifted to totes and notebooks | Product-form diversification |

Sources: Making Sense of Cents, Side Hustle Nation, InsightsByJess, Starter Story, The Creatives Hour, Etsy Seller Handbook.

**Patterns:** three years to full-time is the modal timeline; digital scales on catalogue plus SEO at roughly 60% to 80% net; POD scales on volume at roughly 30% net; the largest brands treat Etsy as a launchpad and move to Shopify, then wholesale and manufacturing partners. Listing count does not correlate with sales across 5m+ shops analysed by Listadum: the top 1% of shops carry a median of 183 listings and most 20k-to-50k-sale shops have under 300.

### 6.2 Muslim-market brands

| Brand | Founded | Channels | Growth facts |
|---|---|---|---|
| Modefa (Dallas) | 2011 | Own Shopify site, Amazon, eBay, physical store; Etsy shop now inactive | Grew from Turkish hijabs into prayer rugs, decor, gifts, Hajj supplies; 28k Instagram |
| modernEID (LA) | 2011 | Own site, Macy's (display towers 2014 to 2016, in-store 2019), Walmart Canada online | Described as "booming" a decade in; record sales reported |
| Zileej (UK) | 2016 | Own site, Toys R Us and ELC in GCC, distributors | 5 Pillars game; Salam Sisters dolls pre-sold before production; biggest markets Indonesia, France, UK, North America, GCC; sales spike before Hajj |
| With A Spin (Texas) | 2015 | Own Shopify store, Pinterest boards | From a cookie-cutter set to shipping to 900+ cities by 2020 |
| Days of Eid | 2016 | Own Shopify site, Amazon brand store | Six continents in ~7 years; 88k Instagram, largest US Muslim decor brand found; Forbes and Houzz press |
| Also Sophia (Canada) | ~2020 | Major retail chains in Canada and Middle East | Five-year anniversary 2025 with expanded Ramadan line |
| Eid Party (UK) | | Own site, 300+ item sale collection; Etsy presence | Forbes 2020 feature |
| IslamicWallArtStore (California) | 2019 | Etsy (31k sales) + own Shopify site + Trustpilot | "3,000 orders within months" of launch; 342 SKUs |
| Sukar Decor (Washington DC) | ~2016 | Etsy (1.1k sales in 10 years) + own site + Pinterest | Low-volume, high-ticket $89 to $99 stainless pieces |

Sources: mymodefa.com, Muslim Girl, NPR, Salaam Gateway, UT Dallas, daysofeid.com, Retail Insider, Forbes, islamicwallartstore.com.

**The two scaling routes in this niche:**

1. **Etsy-native volume** (IslamicWallArtStore, IslamicMetalWallArt, islamicgiftsfavors): manufacturing base in Türkiye, US or UK warehouse, free shipping, 100 to 350 SKUs, permanent 30% to 50% "sale" anchoring, then a Shopify site to capture repeat buyers without fees. This is the only route where Etsy stays the primary channel at scale.
2. **Brand-first seasonal decor** (modernEID, Days of Eid, With A Spin, Also Sophia): own Shopify site plus Amazon, then mainstream retail (Macy's, Walmart Canada, Target and Walmart now stock Ramadan decor). Etsy is a minor or absent channel for these brands.

Small independents that stay Etsy-only and low-SKU (Sukar Decor at ~110 sales a year) stay small even after a decade.

### 6.3 Shop lifecycle facts

- Time to first sale: a few days to two months with a following; 3 to 6 months is normal without one; listings can take up to four weeks to surface in category search. Sources: Tizzit, TechPenny, Meersworld.
- Only 26% of 3.17m shops analysed had any sale in a 30-day window; median 30-day sales is zero. Source: Insight Agent.
- Etsy does not publish 1-year or 3-year survival rates. Seller count fell from 9.0m to 5.6m between 2023 and 2025 after the set-up fee ($15 in 2024, $29 in 2025), which Etsy called "anticipated and intentional". Source: eCommerceBytes.

---

## 7. What correlates with sales

Evidence from category analyses and platform announcements, strongest first:

1. **Reviews and early velocity.** 5+ reviews: +270% purchase likelihood. Conversion climbs to 2% to 4% after ~50 sales. Etsy's 2024 to 2026 quality score weights click-through, conversion and shop velocity, so early sales compound into visibility. New listings that fail to convert lose visibility over time.
2. **Price band and bundles.** Multi-print sets carry the highest AOV; printable bands by style: minimalist $5 to $18, botanical $8 to $25, abstract $10 to $35, vintage $8 to $25. Abstract has the highest search volume (90k+ a month) and is the most saturated. In the Islamic niche, sets of 3 (Kalima, Allah, Muhammad; the 4 Quls; Subhanallah, Alhamdulillah, Allahu Akbar) are the recurring bestseller format.
3. **Free or low shipping.** Shipping price has been a ranking signal since October 2024, enforced progressively into 2026; Etsy's US free-shipping threshold is $35. All top Islamic art shops ship free to US, UK, CA, EU and AU.
4. **Personalisation.** Custom names, dates and nikkah details are called out as a major home-decor selling point and command $25 to $128 for frames.
5. **Star Seller and Bestseller badges.** Up to +22% conversion; ranking lift confirmed by Etsy guidance.
6. **Listing count.** No strong correlation. Depth of catalogue matters for digital SEO coverage, not for physical goods.
7. **Photos and video.** Etsy's Search Visibility Dashboard demotes listings for photo quality and missing attributes, but no quantified photo-count or video uplift study for wall art surfaced.
8. **Seasonality alignment.** Search interest index hits 100 in the Ramadan month and builds from July; Eid al-Adha and Hajj are a documented secondary spike; the only quantified seasonal figure found is one brand's 20% uplift and ~200 pre-orders around Eid.

Sources: WiserNotify, Insight Agent, Outfy, Marmalead, CedCommerce, Listadum, mydesigns.io, Brandwatch, The Story Exchange.

---

## 8. Social media and other channels

### 8.1 Channel-by-channel

| Channel | Scale and cost | Fit for Islamic art | Evidence |
|---|---|---|---|
| **Pinterest** | 640m MAU (+11% YoY, Q2 2026); ~5bn searches a month; home decor is the top search category; ~41% of Etsy's social referrals; CPM ~€3 | Best organic channel for wall art. Long-tail pins keep surfacing for months. Use Share & Save links to earn back 4% of order value | CNBC, Similarweb via Printful, Trackbee |
| **Instagram** | #islamic 73.5m posts; niche brands: Days of Eid 88k, Modefa 28k, Eid Creations 12k, calligrapher @by_aminah 19k; CPC $0.40 to $1.80; Art and Home Decor CTR 2.9% | Brand-building and commissions; Reels are the cheapest paid format | Display Purposes, Top Growth Marketing, Spark UGC |
| **TikTok and TikTok Shop** | US GMV $15.8bn in 2025 (+108%), $23.4bn projected 2026; affiliate commission averages 13%; CPC $0.45 to $0.85; Islamic decor already listed on TikTok Shop US | Highest-upside channel for Ramadan decor and reveal-style videos of metal art; UK TikTok Shop fee ~9% + £0.50 | Branvas, Hamster Garage |
| **YouTube** | Etsy-education creators reach 350k+ subs; Arabic calligraphy channels are small (6k) | Process videos of calligraphy and laser cutting are under-served; micro-YouTubers (10k to 100k) are the cost-effective promo tier | Feedspot, Sale Samurai |
| **Etsy Offsite Ads** | 12% to 15% of attributed orders, capped $100, syndicates to Google Shopping, Meta, Pinterest, Bing | Automatic; mandatory above $10k a year | Etsy help 360000338367 |
| **Etsy Ads** | Min $1 a day, $3 to $5 for a test; ROAS benchmark 2.8x | Use during the pre-Ramadan build; pause low-converting listings | Insight Agent |
| **Share & Save** | 4% refund on orders from your own links within 30 days | Free; route every social and email link through it | Etsy help 16981332744087 |
| **Email and SMS** | CAC $8 to $15, lowest of any channel | Capture buyers via packaging insert and Shopify; Ramadan and Eid are natural send moments | Retainful |
| **Amazon Handmade** | 15% referral, no listing fee, Ramadan storefront exists | Second marketplace once designs are proven | Run Future Proof |
| **Faire wholesale** | 700k retailers; 25% commission first order, 15% reorders; dedicated Islamic gifts category | Route into Islamic bookshops and gift shops | Faire, Hopfar |
| **Offline events** | Eid on the Square London 20k+ attendees (30 May 2026); London Muslim Shopping Festival at ExCeL 350+ exhibitors (7 to 8 Feb 2026); Ramadan Streets Birmingham; Lakemba and Dandenong night markets in Australia | Direct sales plus email capture pre-Ramadan | london.gov.uk, Salaam Gateway, Soul City Arts |
| **Muslim influencer and ad networks** | Modest-fashion creators 120k to 1.4m followers; Muslim Ad Network case: 162k reached, 637 customers, $79.6k revenue, 10x ROAS for a fashion retailer | Nano and micro tiers advised; year-round beats Ramadan-only | Muslim Ad Network, Corq |

### 8.2 Ramadan platform data

- Meta and YouGov: 61% of UAE and KSA consumers planned to shop via social media in Ramadan 2025; over 90% engage with community content on Facebook and Instagram during Ramadan and Eid.
- YouGov Ramadan 2026: home decor and furnishings spend rose for 37% of KSA and 30% of UAE respondents.
- Google MENA: 193m Ramadan-related searches in the month; 78% watch gift-ideas and how-to video.
- Brandwatch: decor and home-aesthetics mentions +19% in Ramadan 2025; luxury search +21% UAE and +45% KSA in the final week.
- Pinterest boards from With A Spin and Days of Eid (520 pins) show the organic playbook.

Sources: DMI Digital Marketing, Arab News, YouGov, Brandwatch, Pinterest.

---

## 9. Market size and customer trajectory

### 9.1 Muslim population in Etsy's core geographies

| Country | Muslim population | Share | Age signal |
|---|---|---|---|
| World (2026) | ~2.06bn to 2.08bn | ~25% | Fastest-growing major religion; +70% 2015 to 2060 vs +32% world (Pew) |
| United States | 3.5m (Pew) to 4.4m to 5m (Religion Census, 2026 estimates) | 1.1% to 1.5% | 26% of Muslim adults aged 18 to 24 vs 10% to 12% of others |
| England and Wales (2021) | 3.87m, +44% since 2011 | 6.5% | Average age 27 vs 40 overall |
| Canada (2021) | 1.78m, from 0.58m in 2001 | 4.9% | Median age 30 vs 41 |
| Germany (2025) | 6.6m to 7.0m | 8% to 8.5% | |
| France | 6.0m to 6.7m | ~10% | |
| Australia (2021) | 0.81m | 3.2% | |

Sources: Pew, ISPU 2025, MCB and ONS census 2021, Statistics Canada, BAMF, INSEE, ABS.

**Trajectory.** The UK Muslim population grew 44% in a decade; Canada's tripled in twenty years. Muslim populations in the West are 10 to 14 years younger than the national median, which means the household-formation, marriage and first-home cohort is growing for the next 10 to 15 years. UK Muslim owner-occupation is 46% versus 63% nationally, so home-ownership headroom is large. UK Muslim weddings run £15k to £35k with 500 to 1,000 guests, a structural driver for nikkah gifting and favours (which is exactly what the 29k-sale islamicgiftsfavors shop sells).

### 9.2 Spending

| Metric | Value | Source |
|---|---|---|
| Muslim consumer spend, six sectors (2024) | $2.60tn, projected $3.56tn by 2029 | DinarStandard SGIE 2025/26 |
| Modest fashion | $347bn (2024) to $444bn (2029), 5.1% CAGR | Salaam Gateway |
| UK "Muslim Pound" spending power | £20.5bn; £31bn+ economic contribution | MCB |
| Share of Muslims saying faith affects consumption | over 90% | Ogilvy Noor |
| Ramadan gifting incidence | 74% gave gifts or hampers (Jakpat, Indonesia 2026) | Jakpat |
| US Muslim households over $100k income | 24% (44% among White Muslims) | ISPU 2025 |

SGIE does not break out home decor or gifts; Islamic decor sits inside general retail and has no audited market-size report. Trade-data proxies: Islamic wall art retail volume nearly doubled month-on-month in September 2025 and kept rising into early 2026; customisable Islamic decor is projected to grow ~20% a year. Source: Accio. Mainstream validation: Walmart runs a Ramadan decorations store ($2 to $35 price points), Target has a Ramadan wall-decor category, Wayfair indexes "Islamic wall art", REDTAG launched a 2026 Ramadan Home collection in the Gulf.

### 9.3 Fine-art end of the market

London Islamic art auctions, spring 2026: Sotheby's £14.8m, Christie's £17.6m, a record £5.5m Mamluk glass bowl. Roughly £30m to £35m per season across the two houses, twice a year. Relevant only as a signal that Islamic aesthetics carry premium pricing power; there is no crossover with Etsy volume.

---

## 10. Historical market timeline

| Date | Event | Effect on sellers |
|---|---|---|
| 2013 | Manufacturing partners and staff allowed | Enabled the scaled metal-art model |
| Apr 2015 | IPO at $16, $1.8bn valuation; 1.4m sellers | Public growth pressure |
| Jul 2018 | Transaction fee 3.5% to 5%, shipping added to fee base | Take rate up |
| 2020 | GMS +106% to $10.3bn; masks were 14% of Q2 GMS | Buyer influx, new-seller wave |
| Apr 2022 | Fee to 6.5%; 18k sellers pledged strike, under 1% actually paused | Margin compression, Shopify diversification |
| Sep 2023 | Share & Save 4% refund | Rewards own traffic |
| 2024 | $15 set-up fee; Creativity Standards; Oct search update weighting exact match and quality score | Filters casual shops, favours proven listings |
| Jun 2025 | Creativity Standards tightened (original design required for POD, CNC, 3D print); set-up fee to $29 | Pressure on generic POD and AI catalogues |
| 2025 | GMS -4% to $10.5bn; sellers 5.6m; Reverb sold; CEO change announced | Trough |
| Jan 2026 | Kruti Patel Goyal becomes CEO | AI-first, quality focus |
| Feb to Jul 2026 | Depop sold to eBay for ~$1.4bn; stock +44% YTD | Pure-play Etsy again |
| Jun 2026 | UK, FR, IT regulatory fees raised | EU/UK take rate up |
| Q2 2026 | GMS +7.5%, revenue $668m, 5.7m sellers (+5.9%), 12% marketplace staff cut | Recovery underway |

Sources: TechCrunch, CNBC, Time, Forbes, eCommerceBytes, Digital Commerce 360, Yahoo Finance, sec.gov.

---

## 11. Verdict and playbook

### 11.1 Is it worth doing?

**Yes, with a specific shape.** The evidence supports these conclusions:

1. **The niche is real and proven.** Three shops have crossed 20k lifetime sales and about 15 have crossed 1,000. Mean order value for physical goods is ~$90 to $100, three to four times Etsy's typical basket, so each order carries $55 to $100 of contribution for metal and $25 to $30 for handmade decor and gifts.
2. **The platform tide is flat, not rising.** Etsy marketplace GMS is 14% below its 2021 peak and only just returned to growth (+7.5% in Q2 2026). Fewer sellers (5.6m to 5.7m, down from 9m) is the one tailwind: less competition per buyer.
3. **The demographic tide is rising.** Western Muslim populations are growing 3% to 4% a year, are 10+ years younger than average, are entering home-ownership and marriage, and 90%+ say faith shapes purchases. Mainstream retailers have validated Ramadan decor as a category.
4. **Winners are design-led and multi-channel.** Every brand that scaled past Etsy hobby level either (a) owns production and 100+ SKUs with free shipping, or (b) built a brand on Shopify, Amazon and retail with Etsy as a side channel. Etsy-only, low-SKU shops stay under ~150 orders a year even after a decade.
5. **Digital is the cheap entry, metal is the profit engine.** Digital carries 80%+ margins but needs 300+ orders a month to clear $1.4k, in a segment described as saturated. Metal carries ~47% margins and $57 to $178 per order but needs $15k to $30k of equipment or a trusted Turkish supplier, and 25 to 45 minutes of labour per piece.

### 11.2 Realistic outcome bands (12 to 24 months, before owner labour and tax)

| Path | Capital | Year-1 realistic | Year-2 if executed well |
|---|---|---|---|
| Digital-only (printables, Ramadan bundles, dua cards) | under $500 | 30 to 100 orders a month, $120 to $460 a month | 300 orders a month, ~$1.4k a month |
| POD prints + canvas (Printify/Gelato, original calligraphy) | under $1,000 | 30 to 100 orders a month, $350 to $1,300 a month | 300 orders a month, ~$4k a month |
| Handmade Ramadan decor and personalised gifts | $1k to $3k | 30 to 100 orders a month, $500 to $1,900 a month | 300 orders a month, ~$6k a month, 100 labour hours |
| Metal calligraphy (own laser or Turkish partner) | $15k to $35k | 30 to 100 pieces a month, $800 to $4,100 a month | 300 pieces a month, ~$13.6k a month, staff needed |

These assume you reach the 2% conversion benchmark and the traffic in section 4.4. Half of all Etsy shops never get there; the first 10 to 20 reviews are the hurdle.

### 11.3 Playbook the evidence supports

1. **Lead with sets and evergreen gifting**, not single prints: 3-piece Kalima/Allah/Muhammad sets, the 4 Quls, Ayatul Kursi in three sizes, nikkah and housewarming pieces. These sell year-round and carry higher AOV.
2. **Launch by early December 2026 for Ramadan 2027** (starts ~7 Feb 2027). Search interest builds from July, decor demand peaks in the Ramadan month, gifting spikes in the last two weeks. Use Etsy Ads from mid-January; Meta CPMs are 30% to 50% cheaper in February than in Q4.
3. **Price with an anchor.** Leaders list at $122 to $250 and show 30% to 50% off permanently. Offer free shipping to US/UK/CA/EU/AU; it is a ranking signal.
4. **Design original calligraphy or license it properly.** Buying DXF packs and listing them as handmade is now a policy violation. Original design is also the only defence against the copying that follows any bestseller.
5. **Respect constraints in the range.** Wall art, frames, metal and tabletop only. No Quranic text on cushions, mats, coasters, mugs or apparel.
6. **Run Pinterest from day one** through Share & Save links (4% back), then Instagram Reels and TikTok process videos of cutting, finishing and installing pieces. Reveal and satisfying-process content fits this product.
7. **Capture email with every parcel** and open a Shopify site by the time you pass $10k trailing sales, when Offsite Ads becomes mandatory at 12%. Repeat and gifting buyers should be moved off-fee.
8. **Add Amazon Handmade and Faire** once 5 to 10 designs are proven; Islamic bookshops and gift shops are a wholesale channel with a dedicated Faire category.
9. **Sell in person at pre-Ramadan events** (London Muslim Shopping Festival early Feb, Eid on the Square, Ramadan night markets) for cash flow and list-building.
10. **Track the four numbers that predict success**: visits, conversion (target 2%+), review count (target 20 in 90 days), and repeat-buyer share.

### 11.4 What would change the verdict

- Etsy raising the 6.5% transaction fee again, or extending mandatory Offsite Ads down-market.
- Continued flooding of "Designed by a seller" digital listings by AI-generated calligraphy, which compresses digital prices toward $1.50.
- TikTok Shop taking the seasonal decor buyer before you have a presence there.

---

## 12. Sources

Primary and key secondary sources by topic. Every figure in the sections above is attributed to one of these. The unedited output of each of the five research threads, with its complete URL list and its own gap statement, is in `appendix/`.

**Etsy corporate**
- Etsy FY2025 10-K: https://www.sec.gov/Archives/edgar/data/1370637/000137063726000019/etsy-20251231.htm
- Etsy FY2024 10-K: https://investors.etsy.com/sec-filings/all-sec-filings/content/0001370637-25-000017/etsy-20241231.htm
- Q4 2025 results: https://investors.etsy.com/news-events/press-releases/detail/218/etsy-inc-reports-fourth-quarter-and-full-year-2025-results
- Q1 2026 shareholder letter: https://www.sec.gov/Archives/edgar/data/0001370637/000137063726000042/q126shareholderletter.htm
- Q2 2026 shareholder letter: https://www.sec.gov/Archives/edgar/data/0001370637/000137063726000079/q226shareholderletter.htm
- Q2 2026 coverage: https://finance.yahoo.com/markets/stocks/articles/etsy-inc-etsy-q2-2026-231603652.html ; https://www.digitalcommerce360.com/article/etsy-revenue-gms/
- FY2015 10-K (IPO-era baseline): https://www.sec.gov/Archives/edgar/data/1370637/000137063716000032/etsy1231201510k.htm
- CNBC Q4 2025: https://www.cnbc.com/2026/02/19/etsy-etsy-q4-earnings-report-2025.html
- Depop sale: https://investors.etsy.com/news-events/press-releases/detail/217/ebay-to-acquire-depop-from-etsy
- CEO change: https://www.cnbc.com/2025/10/29/etsy-stock-ceo-depop.html
- eCommerceBytes on seller counts and set-up fee: https://www.ecommercebytes.com/2026/02/20/etsy-marketplace-shows-flat-growth-in-gms-in-4th-quarter-of-2025/
- Etsy 2024 Seller Census: https://www.etsy.com/news/the-creative-entrepreneurs-behind-etsyas-special-items
- Traffic: https://www.similarweb.com/website/etsy.com/ ; https://linkmybooks.com/blog/how-many-sellers-are-on-etsy ; https://www.printful.com/blog/etsy-statistics

**Fees and policy**
- Etsy fees policy: https://www.etsy.com/legal/fees/
- Offsite Ads: https://help.etsy.com/hc/en-us/articles/360000338367-How-Etsy-s-Offsite-Ads-Work
- Share & Save: https://help.etsy.com/hc/en-us/articles/16981332744087-How-to-Save-on-Etsy-Fees-with-the-Share-Save-Program
- Regulatory fee 2026: https://iscompliant.app/Blog/etsy-regulatory-fee-2026 ; https://www.growtsy.com/etsy-fees/regulatory-operating-fee
- Fee guides: https://printify.com/blog/how-much-does-etsy-take-per-sale/ ; https://craftybase.com/blog/the-complete-guide-to-etsy-fees ; https://blog.marmalead.com/etsy-fees-explained/
- Creativity Standards: https://www.etsy.com/seller-handbook/article/1276491338090 ; https://iscompliant.app/Blog/etsy-creativity-standards-pod-sellers-guide
- Search 2026: https://mydesigns.io/blog/etsy-search-algorithm-update-2026/ ; https://blog.marmalead.com/etsy-algorithm-2026/
- Fee history: https://www.feeproofed.com/guides/etsy-fee-increase-history-2018-2026/ ; https://time.com/6165964/etsy-sellers-strike-over-increase/
- Star Seller: https://help.etsy.com/hc/en-us/articles/4403058372503-What-is-the-Star-Seller-Badge

**Islamic art niche on Etsy (shop and market pages, read via search snippets)**
- https://www.etsy.com/shop/IslamicWallArtStore ; https://islamicwallartstore.com/pages/about-us ; https://www.trustpilot.com/review/islamicwallartstore.com
- https://www.etsy.com/shop/islamicgiftsfavors ; https://www.etsy.com/shop/IslamicMetalWallArt ; https://www.etsy.com/shop/IslamicWallArtDecor
- https://www.etsy.com/shop/IslamicArtPrintables ; https://www.etsy.com/shop/BreatheIslamicArt ; https://www.etsy.com/shop/WallArtIslamic
- https://www.etsy.com/shop/NuqtaCalligraphyShop ; https://www.etsy.com/shop/Hidayahartprints ; https://www.etsy.com/shop/SalehaArt ; https://www.etsy.com/shop/DaysofEid
- Remaining 15 shop URLs are in `data/islamic_art_etsy_shops.csv`
- Market pages: https://www.etsy.com/market/islamic_wall_art ; https://www.etsy.com/market/ayatul_kursi_metal ; https://www.etsy.com/market/modern_islamic_wall_art ; https://www.etsy.com/market/eid_gifts ; https://www.etsy.com/market/ramadan_decoration ; https://www.etsy.com/uk/market/islamic_gift_shop ; https://www.etsy.com/uk/market/islam_wedding_frame
- Seller storefronts with prices: https://islamicwallartstore.com/collections/islamic-metal-wall-art/ayatul-kursi ; https://www.sukardecor.com/products/
- Demand and seasonality: https://www.accio.com/business/ramadan-trend-2025 ; https://www.accio.com/business/trending-ramadan-decorations-2026-tree ; https://www.accio.com/business/islamic-wall-art-trends ; https://www.brandwatch.com/blog/ramadan-consumer-insights/ ; https://videngrowth.com/blog/ramadan-advertising-guide ; https://www.rankhero.com/keywords/quran-verse
- Seasonal uplift: https://thestoryexchange.org/muslim-women-owned-businesses-see-strong-sales-ramadan-eid/ ; https://www.npr.org/2022/05/01/1095615817/eid-al-fitr-ramadan-being-commercialized-a-welcome-thing

**Seller economics**
- Income distribution: https://printify.com/blog/how-much-can-you-make-on-etsy/ ; https://customcy.com/blog/how-much-do-etsy-sellers-make/ ; https://www.insightagent.app/guides/average-etsy-seller-income ; https://www.insightagent.app/guides/selling-wall-art-digital-downloads-etsy ; https://www.podbase.com/blogs/etsy-statistics ; https://www.skillademia.com/statistics/etsy-statistics/
- POD costs: https://apparelhub.ai/blog/best-print-on-demand-supplier-for-posters-wall-art ; https://podvector.ai/articles/print-on-demand/costs-and-suppliers/printful-poster-cost-vs-printify ; https://www.gelato.com/pricing
- Metal: https://www.signcustomiser.com/posts/metal/custom-laser-cut-metal-signs/ ; https://sendcutsend.com/blog/the-true-cost-of-custom-sheet-metal-parts/ ; https://gyclaser.com/2025/02/21/fiber-laser-cutting-machine-costs-what-experts-wont-tell-you/ ; https://storehacks.com/print-on-demand-metal/
- Conversion and stats: https://www.gelato.com/blog/etsy-conversion-rate ; https://craftybase.com/blog/how-to-increase-your-etsy-conversion-rate ; https://www.etsy.com/seller-handbook/article/624088232713 ; https://goldcityventures.com/etsy-views-vs-visits/ ; https://www.insightagent.app/guides/etsy-ads-roas-benchmarks-guide
- Social proof: https://wisernotify.com/blog/social-proof-statistics/ ; https://genesysgrowth.com/blog/social-proof-conversion-stats-for-marketing-leaders ; https://www.listadum.com/blog/how-many-listings-should-i-have-on-etsy
- Ad costs: https://www.trackbee.io/blog/ad-cost-benchmarks ; https://www.triplewhale.com/blog/tiktok-benchmarks ; https://www.sparkugc.com/resources/meta-ads-benchmarks-by-business-type-2026 ; https://www.shopify.com/blog/customer-acquisition-cost-by-industry
- Returns: https://stuv.ai/blog/ecommerce-return-rates-by-category/
- Religious rulings: https://islamqa.info/en/answers/13648 ; https://islamweb.net/en/fatwa/367540/handling-items-on-which-quran-is-written ; https://www.islamweb.net/en/fatwa/247618/making-shapes-in-calligraphy-with-verses-of-the-quran
- IP: https://www.etsy.com/legal/ip/ ; https://www.shieldmyshop.com/blog/2026-05-28-can-you-put-quotes-on-etsy-products-copyright-rules-signs-mugs-shirts ; https://www.outfy.com/blog/etsy-copyright-infringement-explained/

**Seller scaling case studies**
- https://www.sidehustlenation.com/etsy-printables/ ; https://www.sidehustlenation.com/print-on-demand-on-etsy/ ; https://www.makingsenseofcents.com/2025/03/how-i-made-6161-in-just-4-months-with-a-new-etsy-printables-shop.html
- https://insightsbyjess.com/etsy-print-on-demand-case-study-250k-yr ; https://www.starterstory.com/start-art-prints-ecommerce ; https://www.starterstory.com/start-etsy-store-success-story ; https://thecreativeshour.com/etsy-wall-art-stores/
- https://www.etsy.com/seller-handbook/article/quit-your-day-job-mostlikely/132857291835 ; https://www.etsy.com/uk/seller-handbook/article/quit-your-day-job-the-wheatfield/51997034317
- Muslim brands: https://www.mymodefa.com/pages/about-us ; https://muslimgirl.com/meet-owner-moderneid-learn-latest-eid-decor-trends/ ; https://salaamgateway.com/story/momentum-growing-in-islamic-edutainment-market-as-sales-soar-ahead-of-haj ; https://development.utdallas.edu/alumnas-islamic-decor-company-launches-second-career ; https://daysofeid.com/pages/reem-sayes ; https://retail-insider.com/bulletin/2025/02/also-sophia-marks-5-years-with-expanded-ramadan-eid-decor/ ; https://www.forbes.com/sites/tasmihakhan/2020/07/21/how-one-company-is-bringing-muslim-party-decor-to-the-masses/ ; https://layaliblog.com/here-are-12-muslim-owned-businesses-that-sell-ramadan-eid-decor/
- Lifecycle: https://tizzit.co/how-long-will-it-take-to-get-sales-from-your-handmade-or-etsy-shop/ ; https://www.meersworld.net/2026/02/how-long-does-it-take-to-get-sales-on-etsy-realistic-timelines.html

**Channels**
- Pinterest: https://www.cnbc.com/2026/08/04/pinterest-pins-q2-earnings-report-2026.html ; https://www.printful.com/blog/how-to-use-pinterest-for-etsy ; https://www.pinterest.com/withaspin/ramadan-decor-ideas/
- Instagram: https://displaypurposes.com/hashtags/hashtag/islamic ; https://www.instagram.com/daysofeid/ ; https://www.instagram.com/modefausa/ ; https://topgrowthmarketing.com/instagram-ads-cost/
- TikTok: https://branvas.com/blogs/news/tiktok-shop-statistics ; https://www.hamstergarage.com/article/tiktok-shop-affiliate-statistics-benchmarks-roi ; https://tslagency.co.uk/tiktok-shop-fees-uk-2026-complete-breakdown/
- Ramadan platform data: https://dmidigitalmarketing.com/20-key-ramadan-marketing-stats-for-brands-in-2026/ ; https://yougov.com/articles/54011-ramadan-2026-consumer-insights-5-key-findings-across-indonesia-malaysia-saudi-arabia-turkiye-and-the-uae
- Wholesale and marketplaces: https://www.faire.com/discover/islamic-gifts ; https://www.runfutureproof.com/amazon-fees/handmade ; https://hopfar.com/faire-review-2026/
- Events: https://www.london.gov.uk/eid-square-celebrations-return-trafalgar-square-event-marks-20th-anniversary ; https://salaamgateway.com/story/london-muslim-shopping-festival-draws-thousands-to-excel-london ; https://www.soulcityarts.com/ramadanstreets/
- Influencers: https://muslimadnetwork.com/elements/advertise-modest-fashion/ ; https://muslimadnetwork.com/2026/04/24/reaching-muslim-consumers-year-round-what-most-modest-fashion-brands-get-wrong

**Market and demographics**
- https://www.dinarstandard.com/insights/state-of-the-global-islamic-economy-report-2025-26 ; https://salaamgateway.com/reports/state-of-the-global-islamic-economy-sgie-202526-report
- https://mcb.org.uk/resources/muslim-pound/ ; https://mcb.org.uk/resources/2021-census-first-look/ ; https://www.ons.gov.uk/peoplepopulationandcommunity/culturalidentity/religion/articles/religionbyhousinghealthemploymentandeducationenglandandwales/census2021
- https://www.pewresearch.org/religion/2017/07/26/demographic-portrait-of-muslim-americans/ ; https://ispu.org/poll/american-muslim-poll-2025-full-report-2/ ; https://www.pewresearch.org/short-reads/2017/04/06/why-muslims-are-the-worlds-fastest-growing-religious-group/
- https://www150.statcan.gc.ca/n1/pub/11-627-m/11-627-m2024058-eng.htm ; https://www.bamf.de/SharedDocs/Anlagen/EN/Forschung/Forschungsberichte/fb55-zahl-muslime-2025.html?nn=447028 ; https://www.insee.fr/en/statistiques/fichier/7342918/IMMFRA23-D2-en.pdf
- Weddings: https://joinrukn.com/guides/real-cost-muslim-wedding-2026 ; https://www.islamicfinanceguru.com/articles/muslim-wedding-cost-crisis
- Retail validation: https://www.walmart.com/c/kp/ramadan-decorations-store ; https://www.target.com/c/wall-decor-home/ramadan/-/N-5xtteZy9mc7q5hzks ; https://gulfnews.com/friday/home/redtag-unveils-a-2026-ramadan-home-collection-1.500449926
- Auctions: https://www.theartnewspaper.com/2026/05/11/record-%C2%A355m-glass-goblet-leads-london-indian-and-islamic-sales

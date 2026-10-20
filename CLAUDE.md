# ZALIN Beauty — Project Context for Claude

Handoff written 2026-10-07 from the claude.ai project "Shopify Dropshipping Store". Read this whole file before doing anything.


## UPDATE 2026-10-13 — read this first (supersedes "Current live state: v1.9" below)
- **Live theme: ZALIN Beauty v1.22 PREVIEW (polish)** — gid://shopify/OnlineStoreTheme/159465439424 (published by owner 2026-10-20). Backups: v1.17 (159464784064), v1.13 (159207293120), v1.12 (159205851328), v1.11 (159203197120), v1.9 (158995677376). Full log: `versions/VERSIONS.md`. Audit list: `versions/AUDIT-2026-10-13.md` (24 items).
- **Domain:** zalinbeauty.com is primary (SSL on). Permanent: j2xizj-0q.myshopify.com.
- **Shrine license:** owner bought own license ($149, 1 store); token is in theme setting `fav_collection` ("Authentication token"). Old other-store key `auth_token` is an unused leftover.
- **Bundles (real discounts, live):** "Bundle & Save: 10% off 2+" and "15% off 3+" on Microcurrent, 4-in-1, EMS V-Face, Pore Vacuum, Skin Scrubber, Dual-Use Curler, Cordless Curler; Brush Cleaner 2-Pack $69.95 (existing BXGY) + 3-Pack $99.95 ($19.90 off). Discounts don't combine with each other (best one applies), do combine with shipping.
- **Product templates:** default = 10/15% box; `brush-cleaner` (Brush Cleaner); `no-bundle` (Under-Eye, Neck & Face, Straightener Brush, Body Massager, Red Light Mask, Eyelash Curler). Theme box is display-only — any new bundle label needs a matching Shopify discount.
- **Policies:** all 5 Shopify policies filled (refund/shipping/ToS/contact/privacy); contact = support@zalinbeauty.com only (no phone/address — owner's choice). Store email = support@zalinbeauty.com. Connector cannot write policies (`write_legal_policies` missing) — owner pastes.
- **Audit progress:** done 1–8 (v1.14 = alt text, v1.15 = all 13 descriptions rewritten; old ones in versions/v1.15-descriptions/descriptions-before.json). Items 9 (v1.16) and 10 (v1.17) done. Items 11 (v1.18), 12 (v1.19), 13 (v1.20), 14 (v1.21) done. 15, 21–24 done (v1.22, published 2026-10-20). 16 (v1.23), 17 (v1.24), 18 (v1.25), 19 (v1.26), 20 (v1.27) done — ALL 24 AUDIT ITEMS DONE 2026-10-20. v1.28 = ToS polish (owner pasted). Owner said: no theme/design changes without a preview first. Item 2 still needs owner's test order (2 Microcurrent = $53.91 free ship; 3 Brush Cleaners = $99.95), then refund.
- Lessons: owner may publish theme copies before steps finish — always re-check which theme is MAIN before writing; theme writes to MAIN are blocked. Large Shopify file reads can be forced to disk by bundling with sections/main-product.liquid.

## Who / what
- Owner: runs **ZALIN Beauty**, a Shopify dropshipping store for beauty gadgets (zalin-beauty.myshopify.com, Shopify Basic plan, USD, US-based, Central time).
- Supplier: **Zendrop** (each product has a `custom.zendrop_import_id` metafield; Zendrop owns the "Zendrop" delivery profile).
- Claude's role: digital marketer + store operator — Meta (and later TikTok) ads, store fixes, a daily ads analytics report, later a customer-support agent.

## How the owner wants to work (follow these)
1. **Brutal honesty, no hype.** Say plainly what won't work and why.
2. **Version every change.** Each batch of store changes gets a version number (Phase 0 = v1.x, Phase 1 = v2.x…). Snapshot before/after, update `versions/VERSIONS.md`, tell the owner the new number. Rollback on request ("restore to v1.x").
3. **Show changes before making them**, then verify on the live/preview store after.
4. Theme/design changes: **duplicate the theme first**, edit the copy, owner previews and publishes. Never edit the live theme.
5. No fake reviews, no fake "was $X" prices, no health/medical claims (bacteria, acne, lifting, firming, slimming, clinically proven).

## Current live state: v1.9 (published 2026-10-07)
Full history and snapshots: `versions/VERSIONS.md`, `versions/zalin-v1.0…v1.4.json`, `versions/theme-v1.x-*.json` (in the claude.ai project). Original pre-change backup: `backups/zalin-beauty-backup-2026-10-07.json` + unpublished theme "BACKUP 2026-10-07 - ZALIN Beauty (before Phase 0)".

### Themes
| Theme | ID | Role |
|---|---|---|
| ZALIN Beauty v1.9 (bigger header) | 158995677376 | **LIVE** |
| ZALIN Beauty v1.8 (styled banner text) | 158995546304 | backup |
| ZALIN Beauty v1.7 (new banner) | 158995284160 | backup |
| ZALIN Beauty v1.6 (homepage redesign) | 158994563264 | backup |
| ZALIN Beauty v1.5 (homepage fixes) | 158994333888 | backup |
| ZALIN Beauty (original design, = v1.4) | 155967684800 | backup |
| BACKUP 2026-10-07 (before Phase 0) | 158992367808 | backup |
Theme is "Shrine" (Dawn-based).

### Hero product: Electric Makeup Brush Cleaner & Dryer
- Product gid://shopify/Product/8692830306496, handle `electric-makeup-brush-cleaner-dryer`, variant 48849998872768
- Price **$39.95** (was $94.95). Zendrop cost $12.34. ~$26.15 profit per single order before ads and before Zendrop's shipping charge.
- **2-pack deal**: automatic discount gid://shopify/DiscountAutomaticNode/1468421701824 — "2-Pack Deal: 2 Brush Cleaners for $69.95" (buy 1, 2nd 24.91% off, repeats per pair). ~$42.94 profit per 2-pack before ads/shipping.
- Product page rewritten (v1.4): benefits, how-to, 2-pack callout, shipping/returns, FAQ. Delivery ~8 days.

### Shipping (Zendrop profile gid://shopify/DeliveryProfile/104780366016)
- Zone "United States (50 states + DC)" only — no territories, no APO/FPO, no other countries.
- Standard Shipping $5.95 on orders ≤ $49.99; Free Shipping on orders ≥ $50.
- Was "free to every country" before v1.2. Zendrop may re-sync this profile — re-check after any Zendrop changes.

### All prices (v1.2, matched to Amazon/Walmart/TikTok Shop levels)
| Product | Price | Zendrop cost |
|---|---|---|
| Brush Cleaner & Dryer (hero) | 39.95 | 12.34 |
| Cordless Automatic Hair Curler | 49.95 | 20.57 (white/pink nearly out of stock) |
| EMS Compact V-Face Massager | 39.95 | 14.39 |
| Dual-Use Hair Curler & Straightener | 34.95 | 12.93 |
| Rechargeable Electric Eyelash Curler | 24.95 | 12.41 |
| Portable Body Massager with Heat & Vibration | 59.95 | 33.95 |
| Under-Eye Red Light Therapy & Massage Device | 49.95 | 32.99 |
| 7-Color Red Light Therapy Face Mask | 89.95 | 52.23 |
| 4-in-1 Microcurrent & Ultrasonic Facial Device | 29.95 | 6.20 |
| Ultrasonic Skin Scrubber Device | 24.95 | 7.77 |
| Neck & Face LED Massage Device | 34.95 | 20.69 |
| Portable Rechargeable Straightener Brush | 39.95 | 24.56 |
| Microcurrent Facial Massager – 3 Intensity Levels | 29.95 | 10.49 |
| Rechargeable Electric Pore Vacuum Cleanser | 24.95 | 4.25 |
| Portable Skin Tag Repair Beauty Device | DRAFT (hidden — needles + medical claim risk) | 20.72 |
**Don't advertise** (supplier cost ≈ or > market price): Under-Eye device, Neck & Face LED, Body Massager, Straightener Brush, Eyelash Curler.

### Collections (handles changed in v1.1, redirects in place)
- Beauty Accessories → `beauty-tools`; Personal Care → `personal-care`; Face & Skin Massager → `face-skin-massagers` (was `flood-fire-gas-safety`).

### Homepage (v1.6–v1.9)
Top bar "Free US shipping on orders $50+ | 2 Brush Cleaners for $69.95" → trust bar (4 promises) → new clean AI banner `zalin-home-banner-v1-7.png` with live text "Beauty, Simplified" (styling in hidden `custom-liquid` section `banner_style_css`) → intro → collection tiles → featured Brush Cleaner → "Beauty & Hair Tools" → image-with-text → "Skincare Devices" → rich text → FAQs → footer. Header: logo 210px desktop, 150px mobile. Fake testimonials, "supplements" video and misleading comparison table were removed.

## Ads plan (Phase 1) — not started
Plan doc: https://claude.ai/code/artifact/58dd6880-1ce0-4057-8824-b1d359512caa ("ZALIN Beauty — Brush Cleaner Meta Ads Plan (Phase 1)").
- Budget **under $1,000** first month → **Meta only**, one hero (Brush Cleaner). ~$30/day weeks 1–2, $30–45/day weeks 3–4 on winners, ~$100 reserve.
- 1 campaign (Sales, Purchase event), 1 ad set (US, women 18–54, broad, Advantage+ placements), 5 ads = 5 scripts (gross reveal, time back, satisfying, gift/2-pack, honest review). Ad names `BC_<angle>_<hook>_v1`; UTMs `utm_source=facebook&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`.
- Kill/scale rules: off at $40 spend with 0 orders; keep if cost/order ≤ $26; +20% budget if ≤ $20 for 3 days; off if > $35 for 3 days; stop and rethink if nothing profitable by ~$420.
- Target launch ~Oct 19 (samples ~8 days out), before November ad-cost spike.
- Creative must be real footage of the real product (owner filming or paid creators). AI visuals only as labeled b-roll — never AI "customers".

## Open tasks
Owner:
- [ ] Order 2 Brush Cleaner samples from Zendrop (blocks filming)
- [ ] Install Meta "Facebook & Instagram" app in Shopify, data sharing = Maximum (pixel + Conversions API)
- [ ] Create ZALIN Beauty Facebook Page + Instagram (3–6 posts)
- [ ] Send Zendrop shipping cost per order (1 and 2 units) → finalize break-even numbers
- [ ] Decide: film himself or hire creators (open question in the ad plan doc)
- [ ] One real test order, then refund
Claude:
- [ ] After pixel install: verify purchase tracking end to end
- [ ] Connect ad data (Windsor.ai or Supermetrics connector) and build the daily "what's working" report: spend, CPM, CTR, cost per purchase, ROAS by product/ad vs. break-even; Shopify orders as source of truth
- [ ] Later: TikTok ads, real-review app after first orders, customer-support agent

## Technical notes / lessons learned
- Shopify Admin API via the Shopify connector (GraphQL). Theme file writes are blocked on the live (MAIN) theme — always duplicate first. A fresh `themeDuplicate` copy takes ~1 minute to finish processing (`theme.processing`) before files can be written.
- Section-level `custom_css` in theme JSON is capped at **500 characters**; for bigger CSS use a `custom-liquid` section with a `<style>` block.
- Changing a collection/product handle breaks theme sections that reference it by handle — check templates after any handle change (this broke the homepage once in v1.1).
- The theme forces white text on slideshow text without a text box — overridden in `banner_style_css`.
- The cloud shell couldn't reach cdn.shopify.com; images were edited via the Higgsfield connector (`gpt_image_2_5`) and uploaded with `fileCreate` from the Higgsfield URL.
- Preview unpublished themes at `https://zalin-beauty.myshopify.com/?preview_theme_id=<id>` in a real browser (WebFetch ignores it). Shopify blocks iframes, so mobile can't be tested by framing.
- Store has 5 expired "NovaMind recovery" discount codes from an app — leave them. Two blank "Produto StoreBuilder" draft products — harmless.

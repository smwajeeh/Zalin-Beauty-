# ZALIN Beauty — Version Log

Earlier history (v1.0–v1.9) and snapshots live in the claude.ai project "Shopify Dropshipping Store"; summary in `CLAUDE.md`.

## v1.10 — 2026-10-13 — Face & Skin collection image fix
**Problem:** The homepage "Face & Skin Massager" tile showed a woman using a pen-shaped device (looked like the hidden/draft Skin Tag Repair Device). None of the 3 products in the collection matched it.

**Changes (collection gid://shopify/Collection/356787945664, no theme change):**
- Collection image replaced: woman using the turquoise Microcurrent Facial Massager (a product in the collection), 1024×1024.
- Alt text added: "Woman using the turquoise Microcurrent Facial Massager on her cheek".
- Title "Face & Skin Massager" → "Face & Skin Massagers". Handle `face-skin-massagers` unchanged, so no links or redirects affected.

**Change 2 — duplicate product listing:**
- "4-in-1 Microcurrent & Ultrasonic Facial Device" (gid://shopify/Product/8693341520064) removed from **Personal Care** (gid://shopify/Collection/356784898240). It stays in Face & Skin Massagers and in the automatic "All products" page.
- Before: Personal Care had 5 products (Ultrasonic Skin Scrubber, 4-in-1 Microcurrent, 7-Color Red Light Mask, Under-Eye device, Body Massager). After: 4.
- Side effect: the homepage "Skincare Devices" row (built from Personal Care) no longer shows the 4-in-1.
- Rollback: `collectionAddProducts` on Personal Care with that product ID.
- Not done (owner chose not to, for now): Pore Vacuum Cleanser and Straightener Brush are still in no collection.

**Snapshots:** `zalin-v1.10-before.json`, `zalin-v1.10-after.json`
**Rollback to v1.9:** `collectionUpdate` with title "Face & Skin Massager" and image src = the URL in `zalin-v1.10-before.json`, altText null. (Note: Shopify reused the same image file name, so the old version is only recoverable from a copy — the original AI image is also stored in Higgsfield as media e46318d0-e7a7-45c2-b57e-240c68caba8e.)

**Live theme:** still ZALIN Beauty v1.9 (158995677376).

## v1.11 — PUBLISHED 2026-10-13 11:56 UTC (by owner)
Theme copy: **ZALIN Beauty v1.11 (product page fixes)** — gid://shopify/OnlineStoreTheme/159203197120, duplicated from live v1.9 (158995677376) on 2026-10-13.
Preview: https://zalinbeauty.com/?preview_theme_id=159203197120
Snapshot of original product template: `theme-v1.11/product.before.json`.

- [x] Audit item 1 — `templates/product.json`: urgency block "HOT PRODUCT | LOW STOCK" set to `"disabled": true` (not deleted). Rollback: remove that line.
- [x] Audit item 2, step 1 — default product template bundle box rewritten: £ and fake labels removed; Buy 1 standard / Buy 2 SAVE 10% (percentage 10) / Buy 3 SAVE 15% (percentage 15), badge "Best Value" on Buy 3. File: `theme-v1.11/product.after-item2-step1.json`.
  - FOUND: theme box is display-only (schema note: "set up an automatic discount"). On LIVE v1.9 the $10/$20 off shown is NOT charged at checkout (except Brush Cleaner's real 2-pack). Fixed when the automatic discounts (step 4) exist and v1.11 is published.

### Discounts created 2026-10-13 (live immediately)
All: automatic, combine with shipping discounts only (not with each other → best single discount applies).
- gid://shopify/DiscountAutomaticNode/1469829152960 — "Bundle & Save: 10% off 2+" (min qty 2) — Microcurrent, 4-in-1, EMS V-Face, Pore Vacuum, Skin Scrubber, Dual-Use Curler, Cordless Curler.
- gid://shopify/DiscountAutomaticNode/1469829185728 — "Bundle & Save: 15% off 3+" (min qty 3) — same 7 products.
- gid://shopify/DiscountAutomaticNode/1469829218496 — "3-Pack Deal: 3 Brush Cleaners for $99.95" ($19.90 off once, min qty 3).
- Existing gid://shopify/DiscountAutomaticNode/1468421701824 "2-Pack Deal" kept (2 = $69.95).
Rollback: deactivate the three new IDs.

## v1.12 — PUBLISHED 2026-10-13 12:57 UTC (by owner)
Theme copy: **ZALIN Beauty v1.12 (bundle page versions)** — gid://shopify/OnlineStoreTheme/159205851328, duplicated from live v1.11.
- [x] templates/product.brush-cleaner.json (1 / 2 for $69.95 SAVE 12% / 3 for $99.95 SAVE 16%)
- [x] templates/product.no-bundle.json (box off) for Under-Eye, Neck & Face, Straightener Brush, Body Massager, Red Light Mask, Eyelash Curler
- [x] Template suffixes assigned 2026-10-13: Brush Cleaner → `brush-cleaner`; Under-Eye, Neck & Face, Straightener Brush, Body Massager, Red Light Mask, Eyelash Curler → `no-bundle`. Rollback: set templateSuffix to empty.

### Audit item 3 — theme license (2026-10-13)
Owner bought own Shrine license ($149, 1 store) and saved the token in Theme settings → Authentication (setting id `fav_collection`) at 13:46 UTC. Old key from other stores remains as unused leftover `auth_token` (not in settings_schema).

## v1.13 — PUBLISHED 2026-10-13 13:59 UTC (by owner, after preview check)
Theme copy: **ZALIN Beauty v1.13 (remove other store's tracking)** — gid://shopify/OnlineStoreTheme/159207293120, duplicated from live v1.12.
Only `layout/theme.liquid` changed (verified: every other file checksum identical to live). Removed:
- Triple Whale "TriplePixel" script configured for **puralens.myshopify.com** (another store) + 3 preconnect links (config-security.com, whale.camera) — was sending visitor data to that store's account and eval'ing remote code.
- `{% include 'kiwiSizing' %}` (unused app config) and `{% include 'bucks-cc' %}` (inactive currency converter configured for 088f7b.myshopify.com).
Snapshots: `theme-v1.13/theme.liquid.before`, `.after`. No visible change expected.

### Audit item 4 — privacy policy contact details (2026-10-13)
Planned: replace contact line ("call +1 210-… / email waji82@… / 2046 Saxonhill Dr…") with "please email us at support@zalinbeauty.com." Before/after in `policies/privacy-policy.before.html` / `.after.html`.
Blocked for Claude: `shopPolicyUpdate` needs `write_legal_policies` scope, which the Shopify connector does not have → owner edits manually in Settings → Policies.
- [x] Done by owner 2026-10-13 14:08 (Central): privacy policy contact now "please email us at support@zalinbeauty.com." — verified no phone/address/yahoo in policy. Store email + contact email = support@zalinbeauty.com; store phone removed. Billing address (private, required by Shopify) unchanged — swap for PO Box later.

## v1.14 — 2026-10-13 — Audit item 7: image alt text (product data only, no theme change)
- Alt text set on all 75 product images of the 14 active products (fileUpdate). Format: product name; "– <color>" where Shopify links the image to a color variant; "– view N of M" otherwise. No claims, <125 chars.
- Product names in alt text avoid "Therapy" (Under-Eye Red Light Massage Device, 7-Color LED Light Face Mask).
- Snapshots: `v1.14-alt-text/alt-before.json` (all were empty), `alt-after.json`. Rollback: fileUpdate with alt "" from alt-before.json.
- Not covered: draft products (Skin Tag device, 2 StoreBuilder blanks).

## v1.15 — 2026-10-13 — Audit item 8: product descriptions (product data only)
Backup of ALL 14 active descriptions before any change: `v1.15-descriptions/descriptions-before.json`.
Rule: only facts already in the supplier description; added general guidance marked ⚠️ in drafts; no results/health claims.
- [x] Microcurrent Facial Massager (8693365506240) — `microcurrent.html`
- [x] Dual-Use Hair Curler & Straightener (8693129052352) — `dual-use-curler.html`
- [x] Remaining 11 applied 2026-10-13 (owner: "apply all 11") — exact HTML in `v1.15-descriptions/drafts-html.json`, review copy with fact sheets in `DRAFTS.md`. Brush Cleaner unchanged (v1.4 copy).
Rollback per product: productUpdate descriptionHtml from descriptions-before.json.

## v1.16 — 2026-10-20 — Audit item 9: remove "Therapy" from 2 titles (titles only)
- 8693337030848: title "7-Color Red Light Therapy Face Mask" → "7-Color LED Light Face Mask"; SEO title "7-Color Red Light Therapy Face Mask | Rechargeable" → "7-Color LED Light Face Mask | Rechargeable".
- 8693284307136: title "Under-Eye Red Light Therapy & Massage Device" → "Under-Eye Red Light Massage Device" (SEO title was empty, unchanged).
- Handles/URLs unchanged. Descriptions, prices, images, SEO descriptions untouched (owner: "don't change the context").
- Note: Under-Eye SEO description still contains "red light therapy" — left as is, flagged to owner.
Rollback: set the old titles above.
- 2026-10-20 add-on: Under-Eye SEO description "…under-eye red light therapy and massage device…" → "…under-eye red light and massage device…" (owner approved).

## v1.17 — PUBLISHED 2026-10-20 03:55 UTC (by owner) — Audit item 10
Theme copy: **ZALIN Beauty v1.17 (readable titles, open description)** — gid://shopify/OnlineStoreTheme/159464784064, duplicated from live v1.13.
Changed in all 3 product templates (product, product.brush-cleaner, product.no-bundle):
- title block `uppercase_title`: true → false (titles in normal case)
- "Description" collapsible tab → disabled; built-in `description` block → enabled (description shown open, below payment badges)
Snapshots: `theme-v1.17/*.before` / `*.after`.

## v1.18 — 2026-10-20 — Audit item 11: missing SEO titles
- Under-Eye (8693284307136): SEO title (empty) → "Under-Eye Red Light Massage Device | Gentle Vibration"
- Pore Vacuum (8693414232256): SEO title (empty) → "Rechargeable Pore Vacuum Cleanser | 5 Interchangeable Heads"
Rollback: set SEO title back to empty.

## v1.19 — 2026-10-20 — Audit item 12: uncategorized products
- Pore Vacuum (8693414232256) added to Personal Care (356784898240) → now 5 products.
- Straightener Brush (8693356036288) added to Beauty Accessories (356785193152) → now 6 products.
Rollback: collectionRemoveProducts for each.

## v1.20 — 2026-10-20 — Audit item 13: EMS V-Face in the right category
- EMS Compact V-Face Massager (8693040513216) added to Face & Skin Massagers (356787945664) → now 4 products.
- Removed from Beauty Accessories (356785193152) → now 5 products.
Rollback: collectionAddProducts to Beauty Accessories, collectionRemoveProducts from Face & Skin Massagers.

## v1.21 — 2026-10-20 — Audit item 14: clearer collection names
- "Beauty Accessories" (356785193152) → "Hair & Makeup Tools" (handle beauty-tools unchanged).
- "Personal Care" (356784898240) → "Skin & Body Care" (handle personal-care unchanged).
- Menus link "Shop By Category" (/collections), not individual collections — no menu change needed. Homepage tiles pull the title automatically. Homepage section headings "Beauty & Hair Tools" / "Skincare Devices" are separate theme text (left as is).
Rollback: collectionUpdate titles back to "Beauty Accessories" / "Personal Care".

## v1.22 PREVIEW — 2026-10-20 — Audit items 15, 21–24 (theme copy, NOT live)
Theme copy "ZALIN Beauty v1.22 PREVIEW (polish)" gid://shopify/OnlineStoreTheme/159465439424, duplicated from live v1.17 (159464784064). Live theme untouched (checksums verified).
- 15 collection.json: collection banner enabled (name only; collection image off).
- 21 index.json: "BEAUTY CARE MADE SIMPLE" → "Simple Tools for Every Routine"; its "Shop By Category" button → /collections (was /collections/all); section headings "Skincare Devices" → "Skin & Body Care", "Beauty & Hair Tools" → "Hair & Makeup Tools"; FAQ answers 3–5 rewritten with real info (support email, 30-day / 7-day terms from the refund policy).
- 22 settings_data: cart progress bar ON, goal $50, success text "You've unlocked FREE US shipping!".
- 23 settings_data: disable_inspect → false (right-click works again).
- 24 cart.json: "Subscribe to our emails" section and empty AliReviews app section disabled.
Files: versions/theme-v1.22/ (before/after for index, collection, cart; settings_data diff only — full file holds license token, kept out of git).
Rollback: don't publish the copy (or re-publish v1.17).
- 2026-10-20: owner published v1.22 PREVIEW (polish) — now MAIN. Previous live v1.17 (159464784064) kept as backup. Rollback: publish v1.17.

## v1.23 — 2026-10-20 — Audit item 16: redirect chain
- Redirect 443846623424 /products/microcurrent-beauty-device-for-skin-rejuvenation-and-firming: target /products/microcurrent-facial-beauty-device-1 → /products/microcurrent-facial-massager (one hop). Middle redirect kept. No other chains among the 14 redirects. Theme untouched (MAIN updatedAt unchanged).
Rollback: urlRedirectUpdate target back to /products/microcurrent-facial-beauty-device-1.

## v1.24 — 2026-10-20 — Audit item 17: footer Privacy Policy link
- Footer menu (247830151360) item "Privacy Policy" (609795145920): PAGE /pages/privacy-policy → SHOP_POLICY /policies/privacy-policy (official policy 42140369088). Label, order, other 4 items unchanged. Old custom page kept (not deleted). Theme untouched (MAIN updatedAt unchanged).
Before snapshot: versions/v1.24-footer/footer-menu-before.json. Rollback: menuUpdate with that item back to type PAGE, resourceId gid://shopify/Page/124566929600.

## v1.25 — 2026-10-20 — Audit item 18: footer Terms link
- Footer menu item "Terms & Conditions" (609881882816): PAGE /pages/terms-amp-conditions → SHOP_POLICY /policies/terms-of-service (44377571520). Custom page kept. Theme untouched (MAIN updatedAt unchanged).
- Optional owner paste later: official ToS has raw URLs (with stray <meta charset>) instead of links, and one "customs" mention.
Rollback: menuUpdate item back to type PAGE, resourceId gid://shopify/Page/124620275904.

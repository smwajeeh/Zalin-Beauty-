# ZALIN Beauty — Version Log

Earlier history (v1.0–v1.9) and snapshots live in the claude.ai project "Shopify Dropshipping Store"; summary in `CLAUDE.md`.

## v1.10 — 2026-10-13 — Face & Skin collection image fix
**Problem:** The homepage "Face & Skin Massager" tile showed a woman using a pen-shaped device (looked like the hidden/draft Skin Tag Repair Device). None of the 3 products in the collection matched it.

**Changes (collection gid://shopify/Collection/356787945664, no theme change):**
- Collection image replaced: woman using the turquoise Microcurrent Facial Massager (a product in the collection), 1024×1024.
- Alt text added: "Woman using the turquoise Microcurrent Facial Massager on her cheek".
- Title "Face & Skin Massager" → "Face & Skin Massagers". Handle `face-skin-massagers` unchanged, so no links or redirects affected.

**Snapshots:** `zalin-v1.10-before.json`, `zalin-v1.10-after.json`
**Rollback to v1.9:** `collectionUpdate` with title "Face & Skin Massager" and image src = the URL in `zalin-v1.10-before.json`, altText null. (Note: Shopify reused the same image file name, so the old version is only recoverable from a copy — the original AI image is also stored in Higgsfield as media e46318d0-e7a7-45c2-b57e-240c68caba8e.)

**Live theme:** still ZALIN Beauty v1.9 (158995677376).

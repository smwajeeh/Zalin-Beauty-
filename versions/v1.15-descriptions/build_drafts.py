"""Builds the 11 remaining product descriptions (HTML) and a review file (DRAFTS.md).
Facts come only from the supplier descriptions saved in descriptions-before.json.
Anything added that is not from the supplier is listed under 'added' (⚠️) in the fact sheet."""
import json, html

BUNDLE = ('<h3>Bundle &amp; Save</h3>\n<p>Buy 2 and save 10%, or buy 3 and save 15%. '
          'The discount applies automatically at checkout.</p>')
SHIP = ('<h3>Shipping &amp; returns</h3>\n<ul>\n'
        '<li>Ships to all 50 US states and DC. Most orders arrive within about <strong>8 days</strong>, with tracking by email.</li>\n'
        '<li>$5.95 shipping, or <strong>free on orders $50+</strong>.</li>\n'
        '<li>Return requests accepted within 30 days of delivery for unused items. See our <a href="/policies/refund-policy">Refund Policy</a>.</li>\n'
        '</ul>')

P = [
 dict(id="8693341520064", name="4-in-1 Microcurrent & Ultrasonic Facial Device", bundle=True,
  headline="Four functions in one compact facial device.",
  intro="A small handheld device that combines microcurrent, ultrasonic wave, and positive and negative ion functions, with adjustable intensity. Easy to keep in your bathroom drawer or travel bag.",
  bullets=[("4 functions in one","microcurrent, ultrasonic wave, positive ion and negative ion modes."),
           ("Adjustable intensity","choose the level that feels comfortable."),
           ("Simple controls","straightforward to pick up and use."),
           ("Compact and light","easy to hold, store and travel with."),
           ("2 colors","pink or white.")],
  steps=["Start with clean, dry skin.","Apply a layer of water-based gel or serum.","Turn the device on, choose a function and a low intensity.","Glide it slowly over your face in upward motions for a few minutes.","Wipe the device clean after each use."],
  note="Please read the instructions included with your device before first use. Not recommended if you have a pacemaker or other implanted electronic device, or if you're pregnant. If unsure, ask your doctor first.",
  facts=["Microcurrent, ultrasonic wave, positive ion and negative ion functions","Adjustable intensity (multiple levels)","Compact, lightweight, handheld, travel-friendly","Simple controls","Colors pink and white (Shopify variants)"],
  added=["Gel/serum step (standard for microcurrent devices)","Pacemaker/pregnancy caution (standard for this device type)"],
  left_out=["What each ion mode does (supplier doesn't say; would be a claim)","Battery/charging (not stated)","What's in the box (not stated)"]),

 dict(id="8693337030848", name="7-Color Red Light Therapy Face Mask", bundle=False,
  headline="A cordless LED face mask with 7 light colors.",
  intro="Relax for a 10-minute session with this lightweight, rechargeable LED mask. 90 light beads, 7 selectable colors and one-touch control, with adjustable straps for a secure fit.",
  bullets=[("90 LED light beads","spread across the mask for full-face coverage."),
           ("7 light colors","switch between colors with one button."),
           ("10-minute sessions","a set session time for easy routine use."),
           ("Cordless and rechargeable","no cable while you wear it."),
           ("Adjustable straps","position it comfortably and securely.")],
  steps=["Charge the mask fully before first use.","Start with clean, dry skin.","Put the mask on and adjust the straps.","Press the button to start and choose a light color.","Relax for the 10-minute session, then remove the mask and wipe it clean."],
  note="Please read the instructions included with your mask before first use. Keep your eyes closed during use. Not recommended if you're sensitive to light or have a light-sensitive condition. If unsure, ask your doctor first.",
  facts=["90 LED light beads","7 selectable light colors","One-touch control","Cordless and rechargeable","10-minute session setting","Adjustable straps","Lightweight, portable"],
  added=["'Charge before first use' step","Eyes-closed and light-sensitivity caution (standard for LED masks)"],
  left_out=["Anything about what the light colors do to skin (health claim)","Battery life / charge time (not stated)","The word 'therapy' in the text (title fix comes in item 9)"]),

 dict(id="8692954104000", name="Cordless Automatic Hair Curler", bundle=True,
  headline="Automatic curls, no cord.",
  intro="This cordless curler has a motorized rotating barrel that does the turning for you, a ceramic barrel and an LCD display that shows your settings, including temperature.",
  bullets=[("Automatic rotating barrel","the motor turns the barrel to wrap your hair."),
           ("Cordless","built-in rechargeable battery, no cable to work around."),
           ("LCD display","see your selected settings, including temperature."),
           ("Ceramic barrel","designed for even heat while you style."),
           ("3 colors","black, pink or white.")],
  steps=["Charge the curler fully before first use.","Start with dry, brushed hair. A heat protectant is recommended.","Turn it on and choose your settings on the display. Start lower for fine or damaged hair.","Place a small section of hair at the barrel and let it rotate to curl.","Release, and let curls cool before touching them."],
  note="Please read the safety instructions included with your curler before first use. Keep away from water and out of reach of children.",
  facts=["Motorized automatic rotating barrel","Cordless, built-in rechargeable battery","LCD display shows settings incl. temperature","Ceramic barrel for consistent heat","Built-in buttons to adjust settings","Compact, travel-friendly","Colors black, pink, white (Shopify variants)"],
  added=["Heat protectant and 'start lower' advice","'Charge before first use' step"],
  left_out=["Temperature range (not stated)","Battery life (not stated)","Barrel size (not stated)"]),

 dict(id="8693040513216", name="EMS Compact V-Face Massager", bundle=True,
  headline="A compact EMS massager for face and neck.",
  intro="A lightweight handheld massager with EMS (electrical muscle stimulation), several massage modes and adjustable intensity. USB rechargeable and cordless, so it's easy to use at home or on the go.",
  bullets=[("EMS function","electrical muscle stimulation as one of its massage functions."),
           ("Multiple modes and intensity levels","find the combination that feels right."),
           ("Face and neck","shaped for use around the face and neck."),
           ("USB rechargeable","cordless, no disposable batteries."),
           ("2 colors","white or pink.")],
  steps=["Charge the massager fully before first use.","Start with clean skin. A water-based gel can help the device glide.","Turn it on, choose a mode and start at a low intensity.","Glide it slowly over your face and neck for a few minutes.","Wipe the device clean after each use."],
  note="Please read the instructions included with your device before first use. Not recommended if you have a pacemaker or other implanted electronic device, or if you're pregnant. If unsure, ask your doctor first.",
  facts=["EMS (electrical muscle stimulation) function","Multiple intensity levels","Multiple massage modes","For face and neck","Ergonomic handheld","USB rechargeable, cordless","Compact, portable","Colors white and pink (Shopify variants)"],
  added=["Gel step","'Charge before first use' step","Pacemaker/pregnancy caution (standard for EMS)"],
  left_out=["Any 'V-shape', slimming or lifting claim (health claim)","Number of modes/levels (supplier only says 'multiple')"]),

 dict(id="8693351710912", name="Neck & Face LED Massage Device", bundle=False,
  headline="LED light and gentle vibration for your face and neck.",
  intro="A curved handheld device with 3 LED light modes (red, blue and green) and gentle vibration. Use it with the lotions or serums you already have. Rechargeable and light at about 3.5 oz.",
  bullets=[("3 LED light modes","red, blue and green."),
           ("Gentle vibration","a comfortable massage while you use it."),
           ("Curved design","for jawline, cheeks, forehead and neck."),
           ("Works with your skincare","use alongside lotions, serums or sheet masks."),
           ("Rechargeable, about 3.5 oz","USB charging and easy to hold.")],
  steps=["Charge the device fully before first use.","Apply your usual lotion or serum.","Turn it on and choose a light mode.","Glide it slowly over your jawline, cheeks, forehead and neck for a few minutes.","Wipe the device clean after each use."],
  note="Please read the instructions included with your device before first use. Don't shine the light directly into your eyes. Not recommended if you're sensitive to light. If unsure, ask your doctor first.",
  facts=["3 LED light modes: red, blue, green","Gentle vibration","Face and neck: jawline, cheeks, forehead, neck","Curved handheld design","Can be used with lotions, serums, essential oils, sheet masks","Rechargeable, USB charging","About 3.5 oz"],
  added=["'Charge before first use' step","Eye and light-sensitivity caution"],
  left_out=["What each light color does to skin (health claim)","Supplier's 'eye area' line (unclear and risky for a light device)"]),

 dict(id="8693254226112", name="Portable Body Massager with Heat & Vibration", bundle=False,
  headline="Heat, vibration and ultrasonic modes in one handheld massager.",
  intro="Unwind with a cordless body massager that has 3 modes (ultrasonic wave, infrared heat and vibration) and 5 intensity levels. Quiet, lightweight and easy to move across different areas of the body.",
  bullets=[("3 modes","ultrasonic wave, infrared heat and vibration massage."),
           ("5 intensity levels","from gentle to stronger."),
           ("Cordless and rechargeable","built-in lithium-ion battery."),
           ("Quiet","low-noise operation."),
           ("Silicone head","ABS body with a silicone treatment head.")],
  steps=["Charge the massager fully before first use.","Turn it on, choose a mode and start at a low level.","Move it slowly over the area you want to relax, such as shoulders, back or legs.","Don't hold the heat mode in one spot for long.","Wipe the head clean after each use."],
  note="Please read the instructions included with your massager before first use. Not for use on broken or irritated skin. Not recommended if you have a pacemaker or are pregnant. If unsure, ask your doctor first.",
  facts=["3 modes: ultrasonic wave, infrared heat, vibration","5 adjustable intensity levels","Rechargeable lithium-ion battery, cordless","Ergonomic, lightweight","Quiet, low-noise","Compact, portable","ABS body, silicone treatment head"],
  added=["Example body areas (shoulders, back, legs)","Heat caution","Broken skin / pacemaker / pregnancy caution"],
  left_out=["Supplier's old 'slimming' wording (health claim)","Battery life (not stated)"]),

 dict(id="8693356036288", name="Portable Rechargeable Straightener Brush", bundle=False,
  headline="A cordless straightener brush that fits in your bag.",
  intro="Smooth your hair on the go with this compact, rechargeable straightener brush. Charge it with a Type-C cable and use it at home, at work or while traveling.",
  bullets=[("Cordless","built-in rechargeable battery, no outlet needed while you style."),
           ("Brush design","brush through your hair like a regular brush."),
           ("Type-C charging","charge with a common USB-C cable."),
           ("Compact","fits in a handbag, suitcase or beauty bag."),
           ("For different hair types","designed for use on different hair textures.")],
  steps=["Charge the brush fully before first use.","Start with dry, detangled hair. A heat protectant is recommended.","Turn it on and let it heat up.","Brush slowly through small sections from roots to ends.","Turn it off and let it cool before storing."],
  note="Please read the safety instructions included with your brush before first use. Keep away from water and out of reach of children.",
  facts=["Cordless, built-in rechargeable battery","Brush-style design","Type-C charging","Compact, travel-friendly","ABS body, nylon brush components","Simple controls","For different hair textures","Color black (Shopify variant)"],
  added=["Heat protectant advice","Cool-down step"],
  left_out=["Temperature settings (not stated)","Battery life / heat-up time (not stated)"]),

 dict(id="8693240266944", name="Rechargeable Electric Eyelash Curler", bundle=False,
  headline="Gently heated lash curling, cordless.",
  intro="A compact, rechargeable eyelash curler with a gentle heated curling function. Small enough for your makeup bag, and it comes with a USB cable and a cleaning brush.",
  bullets=[("Gentle heat","uses warmth to help curl your lashes."),
           ("Rechargeable","USB charging, no disposable batteries."),
           ("Simple to use","easy for everyday lash styling."),
           ("Compact","fits in your makeup or travel bag."),
           ("In the box","eyelash curler, USB cable and cleaning brush.")],
  steps=["Charge the curler fully before first use.","Turn it on and let it warm up. Test the warmth on the back of your hand first.","Gently press the curler against your lashes from the base and hold for a few seconds.","Repeat along the lashes as needed.","Clean it with the included brush after use."],
  note="Please read the instructions included with your curler before first use. Avoid contact with your eyes and eyelids. Keep out of reach of children.",
  facts=["Gentle heated curling function","Rechargeable, cordless","USB charging","Compact, lightweight","Includes curler, USB cable, cleaning brush","Color white (Shopify variant)"],
  added=["'Test warmth on your hand' and eye caution","Usage steps (standard for heated lash curlers)"],
  left_out=["Heat-up time / temperature (not stated)"]),

 dict(id="8693414232256", name="Rechargeable Electric Pore Vacuum Cleanser", bundle=True,
  headline="A rechargeable suction cleanser with 5 heads.",
  intro="A compact handheld pore vacuum with adjustable suction and 5 interchangeable heads for different areas. USB rechargeable and cordless.",
  bullets=[("Adjustable suction","choose the setting that feels comfortable."),
           ("5 interchangeable heads","for different areas and routines."),
           ("USB rechargeable","cordless, no disposable batteries."),
           ("Comfortable grip","easy to hold and control."),
           ("Compact","easy to store and travel with.")],
  steps=["Charge the device fully before first use.","Start with clean skin. Steaming or a warm towel first can help.","Attach a head and start on the lowest suction setting.","Keep the device moving slowly and don't hold it in one spot.","Clean the head after each use."],
  note="Please read the instructions included with your device before first use. Always start on the lowest setting and keep the device moving to avoid red marks. Not for use on broken, irritated or sunburned skin.",
  facts=["Adjustable suction (multiple settings)","5 interchangeable heads","USB rechargeable, cordless","Compact, portable","Ergonomic handheld","'Select attachment and suction level, gently move across the area' (supplier usage)"],
  added=["Warm towel/steam tip","'Lowest setting, keep moving, avoid red marks' caution (standard for pore vacuums)","Broken/sunburned skin caution"],
  left_out=["Any 'removes blackheads' result claim","Number of suction levels (supplier only says 'multiple')"]),

 dict(id="8693347942592", name="Ultrasonic Skin Scrubber Device", bundle=True,
  headline="A slender ultrasonic skin scrubber, up to 45 minutes per charge.",
  intro="This lightweight skin spatula uses high-frequency ultrasonic vibration of up to 24,000 vibrations per second. Made from ABS and SUS304 stainless steel, it weighs about 75g and runs up to about 45 minutes on a charge.",
  bullets=[("Up to 24,000 vibrations per second","high-frequency ultrasonic vibration."),
           ("Up to about 45 minutes per charge","250mAh battery, about 1–2 hours to fully charge."),
           ("Light and slender","about 75g and 172 × 43 × 13.5 mm."),
           ("Stainless steel","ABS body with an SUS304 stainless steel head."),
           ("4 colors","pink, purple, white or green.")],
  steps=["Charge the device fully before first use.","Start with clean skin and keep it slightly damp, or use a toner or water-based gel.","Turn it on and hold the blade at a low angle to your skin.","Glide it slowly in one direction across your face, wiping the blade as you go.","Clean the blade after each use."],
  note="Please read the instructions included with your device before first use. Use gentle pressure, and don't use on broken, irritated or sunburned skin.",
  facts=["Up to 24,000 vibrations per second","250mAh battery, up to ~45 min continuous use","~1–2 hours full charge","~75g","~172 × 43 × 13.5 mm","ABS and SUS304 stainless steel","Colors pink, purple, white, green (Shopify variants)"],
  added=["Damp skin / toner step (standard for skin scrubbers)","Gentle pressure and broken-skin caution"],
  left_out=["Any 'deep cleans pores' result claim"]),

 dict(id="8693284307136", name="Under-Eye Red Light Therapy & Massage Device", bundle=False,
  headline="A small red light and vibration device for the under-eye area.",
  intro="A compact, contoured device that combines red LED light with gentle vibration. Rechargeable and cordless, and small enough to keep in your bag.",
  bullets=[("Red LED light","red light as part of your routine."),
           ("Gentle vibration","a soft massage while you use it."),
           ("Contoured shape","designed for easy handling around the under-eye area."),
           ("Rechargeable and cordless","no cable while you use it."),
           ("Compact","easy to store and travel with.")],
  steps=["Charge the device fully before first use.","Start with clean skin. You can apply your usual eye cream first.","Turn it on and choose your setting.","Glide it gently under the eye, from the inner to the outer corner, for a few minutes.","Wipe the device clean after each use."],
  note="Please read the instructions included with your device before first use. Keep your eyes closed and don't look directly into the light. Not recommended if you're sensitive to light. If unsure, ask your doctor first.",
  facts=["Red LED light","Gentle vibration massage","Contoured, ergonomic shape for under-eye area","Rechargeable, cordless","Compact, portable","Simple operation","Color white (Shopify variant)"],
  added=["Eye cream step and gliding direction","Eyes-closed and light-sensitivity caution"],
  left_out=["Any 'reduces dark circles/puffiness' result claim","The word 'therapy' in the text (title fix comes in item 9)"]),
]

def build_html(p):
    lis = "\n".join(f"<li><strong>{html.escape(a)}:</strong> {html.escape(b)}</li>" for a, b in p["bullets"])
    ol = "\n".join(f"<li>{html.escape(s)}</li>" for s in p["steps"])
    parts = [f"<p><strong>{html.escape(p['headline'])}</strong></p>", f"<p>{html.escape(p['intro'])}</p>",
             "<h3>Why you'll love it</h3>", f"<ul>\n{lis}\n</ul>", "<h3>How to use</h3>", f"<ol>\n{ol}\n</ol>",
             f"<p>{html.escape(p['note'])}</p>"]
    if p["bundle"]:
        parts.append(BUNDLE)
    parts.append(SHIP)
    return "\n".join(parts).replace("&#x27;", "'")

md = ["# Product description drafts (audit item 8)\n",
      "✅ = from the supplier description · ⚠️ = added general guidance (not from supplier) · ❌ = left out\n"]
out = {}
for n, p in enumerate(P, 1):
    h = build_html(p)
    out[p["id"]] = h
    md.append(f"\n---\n\n## {n}. {p['name']}{'  (Bundle & Save)' if p['bundle'] else ''}\n")
    md.append("**Fact sheet**\n")
    md += [f"- ✅ {f}" for f in p["facts"]]
    md += [f"- ⚠️ {f}" for f in p["added"]]
    md += [f"- ❌ {f}" for f in p["left_out"]]
    md.append("\n**New description**\n")
    md.append(f"**{p['headline']}**\n\n{p['intro']}\n\n**Why you'll love it**")
    md += [f"- **{a}:** {b}" for a, b in p["bullets"]]
    md.append("\n**How to use**")
    md += [f"{i}. {s}" for i, s in enumerate(p["steps"], 1)]
    md.append(f"\n{p['note']}\n")
    if p["bundle"]:
        md.append("**Bundle & Save:** Buy 2 and save 10%, or buy 3 and save 15%.\n")
    md.append("**Shipping & returns:** (same block as the approved samples)\n")

open("DRAFTS.md", "w").write("\n".join(md))
json.dump(out, open("drafts-html.json", "w"), indent=1, ensure_ascii=False)
print(len(out), "drafts written")

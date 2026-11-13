# Style Library — token specs & component language

Each style defines a complete design-token set. Pick ONE as primary; borrow a
second only as a deliberate accent. All values are starting points. Adjust text
and button-label colors until `scripts/contrast.py` reports WCAG AA. Do not
change the five sampled Chinese pair hexes in `chinese-colors.md`.

Every set needs `--on-primary`: the label color drawn on a `--primary` fill.
Do not reuse `--bg` as the button label. A light page background is often the
wrong color on a saturated button.

---

## 1. 中国古典 (Chinese Classical)

Source palette: `chinese-colors.md`. Paper-and-ink aesthetic with restrained,
culturally-loaded accents. Generous 留白 (whitespace). No pure black/white —
use ink and paper tones.

**Tokens (喜庆红金 direction)**
```
--bg:        #F2ECDE  (缟, paper off-white)
--surface:   #F3F9F1  (荼白)
--text:      #161823  (漆黑, ink)
--text-muted:#3D3B4F  (玄青)
--primary:   #9D2933  (胭脂)   or  #FF461F (朱砂)
--on-primary:#FFFFFF  on 胭脂. On 朱砂 use #161823 (white on 朱砂 fails AA).
--accent:    #F0C239  (缃色, pale gold, decorative; it fails as text on 缟)
--border:    #EEDEB0  (牙色，ivory border)
--radius:    2px        (near-square, restrained)
--font-display: "Songti SC", "Noto Serif SC", "Source Han Serif SC", "STSong", serif
--font-body:    "PingFang SC", "Noto Sans SC", "Microsoft YaHei", system-ui, sans-serif
--motion:    slow, ease-out, minimal (fade/slide < 300ms)
```

**Harmony groups** (pick one):
- 喜庆红金: 朱砂 #FF461F + 缃色 #F0C239 + 漆黑 #161823 + 缟 #F2ECDE
- 青绿山水: 石绿 #57C3C2 + 松柏绿 #21A675 + 月白 #D6ECF0 + 黛蓝 #425066
- 黛蓝雅致: 靛青 #177CB0 + 藏青 #2E4E7E + 月白 #D6ECF0 + 牙色 #EEDEB0
- 胭脂藕粉: 胭脂 #9D2933 + 藕色 #EDD1D8 + 缟 #F2ECDE + 玄青 #3D3B4F
- 豆黄群青 (article two-tone): 豆黄 #FFDF70 + 群青 #153472 + 缟 #F2ECDE + 漆黑 #161823
- 扶光中国红 (article two-tone): 扶光 #EFC2A3 + 中国红 #DA0011 + 缟 #F2ECDE + 漆黑 #161823
- 丹红深海绿 (article two-tone): 丹红 #FE5C1B + 深海绿 #1A3B32 + 缟 #F2ECDE + 漆黑 #161823
- 水蓝鹤蓝 (article two-tone): 水蓝 #9ED4F0 + 鹤蓝 #144975 + 缟 #F2ECDE + 漆黑 #161823
- 淡粉金红 (article two-tone): 淡粉 #EBD2D6 + 金红 #E45600 + 缟 #F2ECDE + 漆黑 #161823

> 5 article pairings are the strongest defaults for "modern Chinese brand"
> briefs; pick the one whose temperature (warm/cool) matches the brief.
> Full token sets for each, including `--on-primary`: see `references/chinese-colors.md` §2.
> 丹红上的正文用漆黑，不要用纸白。金红和中国红是按钮填充，不是浅底上的文字色。

**Component language**
- Vertical rhythm with large top/bottom padding; centered single-column for
  editorial, asymmetric grid for product.
- Hairline borders (1px) in 牙色; avoid heavy shadows — use subtle ink wash.
- Serif display headings; small seal/印章-style accent mark optional.
- Motifs: thin rules, seal red square, vertical text for section labels,
  color-pairing cards (split bg like the source article's 豆黄/群青 card).
- DO: 留白, 对比留白, 印章/钤印点缀. DON'T: gradients, neon, rounded blobs
  (except in the deliberate modern国风 pairing-card pattern).

---

## 2. 新野兽派 (Neo-Brutalism)

Raw, confident, high-contrast. Hard borders, flat color, visible structure.
Deliberately "unpolished" but intentional — NOT lazy.

```
--bg:        #FCEE21  (or #FFFFFF)
--surface:   #FFFFFF
--text:      #111111
--text-muted:#444444
--primary:   #FF4D00  (electric orange)  or  #4314FF (electric blue)
--on-primary:#111111  on the orange (white fails AA). On #4314FF use #FFFFFF.
--accent:    #00E0C7  (or #FF49C0). Labels on these fills are #111111.
--border:    #111111
--radius:    0px
--shadow:    6px 6px 0 #111111   (hard offset shadow, no blur)
--font-display: "Space Grotesk", "Archivo Black", "PingFang SC", sans-serif
--font-body:    "Inter", "PingFang SC", system-ui, sans-serif
--motion:    snappy, no easing; hover shifts shadow to 2px 2px (press effect)
```

**Component language**
- 2–4px solid black borders on every element; hard offset shadow.
- Bright flat fills; clash intentionally (orange vs blue vs yellow).
- Oversized type; left-aligned; asymmetric grid.
- Buttons: filled, bordered, on hover translate(-2px,-2px) + bigger shadow.
- DO: bold labels, marquee, sticker badges. DON'T: soft shadows, gradients,
  rounded corners, subtle everything.

---

## 3. 极简瑞士 (Minimalist Swiss / International)

Grid-driven, typographic, neutral. Restraint as luxury.

```
--bg:        #FAFAFA
--surface:   #FFFFFF
--text:      #1A1A1A
--text-muted:#6B6B6B
--primary:   #1A1A1A   (mono)  or one restrained accent #2563EB
--on-primary:#FAFAFA  on #1A1A1A. On #2563EB use #FFFFFF.
--accent:    #E5E5E5
--border:    #E5E5E5
--radius:    4px
--font-display: "Inter", "Helvetica Neue", "PingFang SC", Arial, sans-serif
--font-body:    "Inter", "PingFang SC", system-ui, sans-serif
--motion:    whisper — 200ms ease, opacity/translate only
```

**Component language**
- Strict 12-col grid; flush-left headlines; big type scale jumps.
- Lots of negative space; one accent color max.
- Thin rules separate sections; no boxes around content.
- DO: hierarchy via size/weight, grid discipline. DON'T: decoration, shadows,
  more than one accent, centered hero cliché.

---

## 4. 玻璃拟态 (Glassmorphism)

Frosted translucent layers over a dark photographic backdrop, or over the
two-stop dark gradient below. Do not use a purple mesh blob. That pattern is
banned in `anti-slop.md` unless the brand color is actually purple, and even
then it is not a generic violet fog.

```
--bg:        #0B1220
--bg-glow:   #134E4A   (second gradient stop; both stops stay dark)
--surface:   rgba(11,18,32,0.72)  with backdrop-filter: blur(16px)
--text:      #F4F7FB
--text-muted:#C5D0DC
--primary:   #F4F7FB
--on-primary:#0B1220
--border:    rgba(255,255,255,0.28)
--radius:    16px
--shadow:    0 8px 32px rgba(0,0,0,0.25)
--font-display: "Outfit", "PingFang SC", sans-serif
--font-body:    "Inter", "PingFang SC", system-ui, sans-serif
--motion:    one slow fade; 300ms ease. No parallax by default.
```

**Component language**
- Cards: translucent, blurred, 1px light border, soft shadow.
- Give `backdrop-filter` a solid dark fallback. Light text on a light photo fails AA.
- If the photo has bright areas, raise the scrim opacity until `contrast.py` passes.
- One glass layer, not a stack of blurs.
- DO: depth and legible type. DON'T: purple mesh, muddy stacked glass, white text on a light blur.

---

## 5. 暗黑科技 (Dark Tech / Cyber)

Off-black canvas, terminal glow, mono display. See taste rules: off-black
#0A0F1A not pure #000000.

```
--bg:        #0A0F1A
--surface:   #111827
--text:      #E5E7EB
--text-muted:#94A3B8
--primary:   #06B6D4  (cyan glow)  or #22D3EE
--on-primary:#0A0F1A  (white on this cyan fails AA)
--accent:    #F5C16C  (warm metal, sparingly; not a second body color)
--border:    rgba(255,255,255,0.08)
--radius:    8px
--shadow:    0 0 24px rgba(6,182,212,0.25)  (glow)
--font-display: "Space Grotesk", "JetBrains Mono", "PingFang SC", monospace
--font-body:    "Inter", "PingFang SC", system-ui, sans-serif
--motion:    250ms ease; hover plus at most one CSS view-timeline reveal
```

**Component language**
- Deep navy-black bg; cyan/teal glow accents; mono display font.
- Subtle grid backdrop. Real numbers only. Do not invent a fake product screenshot.
- Scan-lines and particles only when the MOTION dial is explicitly high.
- DO: contrast glow, terminal feel. DON'T: purple mesh blobs (banned),
  pure black, rainbow neon.

---

## 6. 复古孟菲斯 (Retro Memphis)

1980s Memphis: squiggles, terrazzo, primary clashes, playful geometry.

```
--bg:        #FDF6E3  (cream)
--surface:   #FFFFFF
--text:      #1A1A1A
--text-muted:#555555
--primary:   #E63946  (red)
--on-primary:#111111  (white on this red fails body AA)
--accent:    #2A9D8F  (teal) + #F4A261 (orange) + #264653 (navy)
--border:    #1A1A1A
--radius:    0–12px mix
--font-display: "Futura", "Poppins", "PingFang SC", sans-serif
--font-body:    "Poppins", "PingFang SC", system-ui, sans-serif
--motion:    bouncy, rotate-on-hover, 300ms cubic-bezier
```

**Component language**
- Terrazzo/dot patterns, zigzags, circles, triangles as decoration.
- Clashing primaries used confidently, not randomly.
- Hard 2px borders; mix sharp and rounded shapes.
- DO: playful asymmetry, pattern blocks. DON'T: chaos without anchor,
  pastel-everything (needs at least one bold primary).

---

## 7. 包豪斯 (Bauhaus)

Primary red/yellow/blue, black, geometric grids, functional clarity.

```
--bg:        #F4F1EA  (warm white)
--surface:   #FFFFFF
--text:      #1A1A1A
--text-muted:#555555
--primary:   #E2231A  (bauhaus red)
--on-primary:#FFFFFF  on the red. On the yellow accent use #1A1A1A.
--accent:    #F7D417  (yellow) + #2451A6  (blue; white labels pass on the blue)
--border:    #1A1A1A
--radius:    0px
--font-display: "Futura", "Helvetica", "PingFang SC", sans-serif
--font-body:    "Helvetica Neue", "PingFang SC", Arial, sans-serif
--motion:    precise, minimal; 200ms ease
```

**Component language**
- Primary-color blocks; circles, squares, triangles as structure.
- Asymmetric grid; strong diagonal/vertical accents.
- Functional, no ornament beyond geometry.
- DO: primary triad, geometric motif. DON'T: gradients, soft shadows,
  more than the 3 primaries + black/white.

---

## 8. 柔和有机 (Soft Organic)

Warm, rounded, calming. Health/lifestyle/wellbeing.

```
--bg:        #FBF7F2  (warm off-white)
--surface:   #FFFFFF
--text:      #2D2A26
--text-muted:#6E685F  (the older #7A746C misses 4.5:1 on --bg)
--primary:   #3F6248  (sage darkened for a white label)
--on-primary:#FFFFFF
--accent:    #6B8E6B  /* decorative sage; not text and not a white-label button */
--border:    #ECE3D8
--radius:    20–28px  (large)
--shadow:    0 12px 32px rgba(0,0,0,0.06)  (soft, diffuse)
--font-display: "Fraunces", "Songti SC", "Noto Serif SC", serif
--font-body:    "Nunito", "PingFang SC", "Noto Sans SC", system-ui, sans-serif
--motion:    gentle ease-in-out; 300–400ms; float/scale
```

**Component language**
- Big radii, soft diffuse shadows, warm neutrals.
- Organic blob shapes, soft illustrations (real, not decorative SVG cliché).
- Generous padding; friendly microcopy.
- Clay `#C98A6B` can fill a button only with `--on-primary: #2D2A26`. White on clay fails AA. The lighter sage `#6B8E6B` is decorative and is not a text color.
- DO: warmth, calm hierarchy. DON'T: hard edges, cold greys, neon.

---

## Cross-style rules (always)

- Define tokens as CSS variables, including `--on-primary`. Do not hardcode a label color per element.
- Single primary accent per section; max 2 accents total.
- Text/background contrast must pass WCAG AA (4.5:1 body, 3:1 large). Run `python3 scripts/contrast.py` on each pair before delivery.
- System CJK fonts stay in the stack (`PingFang SC`, `Songti SC`, `Microsoft YaHei`) so Chinese still renders when a webfont host is blocked. If you load a webfont, use `font-display: swap` and do not hide text while it loads.
- Mobile-first; test 375px and 1280px.
- Real content only. No placeholder or lorem, no fake product UI.
- Honor `prefers-reduced-motion: reduce`. Scroll motion uses CSS `animation-timeline`, not a scroll event listener.

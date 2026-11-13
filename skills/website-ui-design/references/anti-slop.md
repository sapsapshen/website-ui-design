# Taste / Anti-AI-Slop Refinement (MANDATORY final pass)

This is the "taste skill" discipline. After building the layout, run this as a
hard gate. A design is delivered ONLY after every Pre-Flight item passes.
Goal: kill the generic "AI template" feel — make it look designed by a human
with opinion, restraint, and intent.

## Design Read (do this before building, re-confirm after)

1. Read the brief; infer design language in one sentence.
2. Map to a style from `style-library.md` (one primary).
3. Tune three dials to taste-appropriate levels:
   - **VARIANCE** (1–10): layout experimentation. Low = centered/clean,
     high = asymmetric/modern. Most sites: 4–7.
   - **MOTION** (1–10): animation depth. Low = hover only, high = scroll/
     magnetic. Most sites: 2–5.
   - **DENSITY** (1–10): info per viewport. Low = spacious, high = dashboard.
     Most sites: 3–5.

## Forbidden patterns (hard bans — remove on sight)

1. **Purple + mesh-blob gradients** — unless brand color is literally purple.
2. **Three equal feature cards in a row** (the #1 AI tell) — use 2-col zig-zag,
   asymmetric grid, or horizontal scroll instead.
3. **Fake product UI** (div-stacked mock dashboards) — use real screenshot or
   honest text, never fabricated app chrome.
4. **Scroll-down cues** ("Scroll ↓") — users know how to scroll.
5. **Decorative dots / confetti** scattered as texture. A Memphis pattern that is
   a contained shape block is allowed. Noise sprinkled over the whole page is not.
6. **Pills/badges overlaid on images** — put captions below the image.
7. **Section-number eyebrows** ("01 / Features") — unless intentional editorial.
8. **Version labels / build strings** on a marketing page ("v1.4.2 Build 0048").
9. **Photo-credit captions** and **locale strips** ("EN / 中文").
10. **Decoration-only hero strips** with no content.
11. **Em-dashes (—)** in headings and body copy — use hyphen or rewrite. (Banned:
    AI overuse.) En-dashes also discouraged.
12. **Divider overuse** — every section separated by a hairline rule.
13. **Flat empty sections** with no imagery or intentional texture.
14. **Centered everything** — break the axis; optical, not mathematical, centering.
15. **window.addEventListener('scroll')** and scroll-linked animation frames.
    Use CSS scroll-driven animations (`animation-timeline: scroll()` or `view()`)
    with an `@supports` fallback. Honor `prefers-reduced-motion: reduce`.
    Do not add a scroll-animation library to a marketing page.
16. **Placeholder / lorem / TODO comments** in delivered output — full output only.

## Layout & type discipline

- **Asymmetry with intent**: offset hero text, varied column widths, one focal
  element per viewport. Never a perfectly centered single column by default.
- **Bottom-aligned CTAs** inside any card group (consistent baseline).
- **Consistent vertical rhythm**: one spacing scale; optical alignment over
  math.
- **One accent color** per section; max two accents total.
- **Real type contrast**: display vs body differ in size AND weight, not just
  color.
- **Dark/light consistency**: if dual theme, both must satisfy WCAG AA and keep
  the same hierarchy — no half-migrated page.
- **Italic descender clearance**: ensure descenders (g, y, p) aren't clipped.

## Pre-Flight Check (must ALL pass before delivery)

- [ ] No banned pattern from the list above remains.
- [ ] Hero is asymmetric or has a deliberate focal device (not centered cliché).
- [ ] Feature section is NOT 3 equal centered cards.
- [ ] Zero em-dashes in visible copy.
- [ ] All copy is real and specific (no lorem, no "Your text here").
- [ ] CTAs in card groups are bottom-aligned.
- [ ] Color contrast passes WCAG AA (body 4.5:1, large text 3:1). Check every
      text/background pair with `python3 scripts/contrast.py #111111 #FFFFFF`.
      Large text is 24px regular or at least 18.67px bold. A 16px button label
      is body text, not large text.
- [ ] One primary accent per section; ≤2 accents total.
- [ ] Motion is restrained (no autoplay, no scroll-jacking, no scroll listeners)
      and `prefers-reduced-motion: reduce` turns it off.
- [ ] Responsive at 375px and 1280px without breakage.
- [ ] No placeholder comments / unfinished blocks in the HTML.
- [ ] At least one "human" detail: intentional imperfection, signature motif,
      or crafted micro-interaction that a template wouldn't include.

If any box is unchecked → fix, then re-run. Do not present to user until green.

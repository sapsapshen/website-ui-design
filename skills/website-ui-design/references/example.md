# Example — 年轻茶饮品牌官网

This is a worked pass of the skill. Replace the copy with the user's brief.
Do not ship this tea brand on an unrelated page.

## Brief

"给一家年轻茶饮品牌做官网，要东方，不要模板感。需要首屏、两款招牌、门店和预约。"

## Design Read

- Purpose: one-page brand site that sends people to a store or a reservation.
- Audience: 20–35, phones first, already drinks bottled tea.
- Personality: 热、短句、留白. Not imperial, not pastel.
- Constraint: Chinese UI copy, no fake app screenshot, no English locale strip.
- Direction: 中国古典, pairing **丹红 × 深海绿**. VARIANCE 6, MOTION 3, DENSITY 4.

## Tokens

Copy `references/chinese-colors.md` §2.3. The roles that matter:

- Warm field `#FE5C1B` with text `#161823` (ink). Paper white on 丹红 fails AA.
- Cool band `#1A3B32` with text `#FFF7EE`.
- Button fill `#1A3B32`, button label `#FFF7EE`.
- Reading cards sit on `#FFF7EE`, not on the vermilion field.
- Do not darken `#FE5C1B` or `#1A3B32`. Those sampled hexes are frozen.

```bash
python3 scripts/contrast.py #161823 #FE5C1B #FFF7EE #1A3B32
```

Both pairs must print `OK` before any section is called done.

## Layout

Start from `assets/starter.html`.

1. Keep the asymmetric hero. Headline is the drink name, not "欢迎来到我们的品牌".
2. Two zig-zag features: one for the signature drink, one for the store. Not three equal cards.
3. Keep the five pair cards only because this brief is 中国古典. Give the section a real heading.
4. Bottom-align the two offer CTAs.
5. Delete the starter's HTML comment and every placeholder string (`品牌名`, `能力一`).

## De-AI fixes that usually show up here

- Remove any em dash the model typed into the headline or the menu blurbs.
- Remove a "Scroll" cue and any `window.addEventListener("scroll", ...)`.
- If a hover lift remains, wrap it in `prefers-reduced-motion: reduce`.
- Do not add a purple gradient behind the vermilion field.

## Done when

The Pre-Flight Check in `references/anti-slop.md` is all true, and the page
still reads as 丹红 × 深海绿 rather than a generic dark-green template.

# 中国古典配色 (Chinese Traditional Color System)

Curated from the 中国传统色 canon. The source WeChat article is titled
"你绝对没见过的中国传统色" (image text) / "你绝对不知道的中国传统色" (meta
title), published by 公众号·AIGC设计便利店, and uses a "双色搭配" (two-tone
pairing) card format. The article contains **8 page slots** cycling through
**5 unique pairings** (some pairs repeat). Values are corrected against the
actual fill color in the source images, NOT the printed hex (which is wrong on
every single card).

> ⚠️ Source-hex mismatch — every printed `#xxxxxx` in the source article is
> **wrong**; the visual fill is consistently different. Always use the
> "corrected (sampled)" values below.

## 1. Five corrected pairings (from the WeChat article)

| # | Pairing | TOP color name | TOP printed | TOP sampled (real) | BOTTOM color name | BOTTOM printed | BOTTOM sampled (real) | Card bg |
|---|---------|----------------|-------------|--------------------|-------------------|----------------|-----------------------|---------|
| 1 | 豆黄 × 群青 | 豆黄 | `#AE3B35` | **`#FFDF70`** | 群青 | `#24322A` | **`#153472`** | `#FFDF70` |
| 2 | 扶光 × 中国红 | 扶光 | `#E9C4A3` | **`#EFC2A3`** | 中国红 | `#CB2D1D` | **`#DA0011`** | `#EFC2A3` |
| 3 | 丹红 × 深海绿 | 丹红 | `#ED6927` | **`#FE5C1B`** | 深海绿 | `#203A32` | **`#1A3B32`** | `#FE5C1B` |
| 4 | 水蓝 × 鹤蓝 | 水蓝 | `#A7D2EE` | **`#9ED4F0`** | 鹤蓝 | `#244973` | **`#144975`** | `#9ED4F0` |
| 5 | 淡粉 × 金红 | 淡粉 | `#E8D3D4` | **`#EBD2D6`** | 金红 | `#E2802B` | **`#E45600`** | `#EBD2D6` |

> Verification: pixels were sampled from each card's top half, bottom half, and
> outer background. The 8 page slots repeat these 5 pairings; where a pairing
> repeated, the sampled hex was the same. Use the sampled column only.

群青有两个不能互换的色值。文章搭配底部是 **群青 `#153472`**。色系总表里的
**群青（浅）`#4C8DAE`** 是另一支更浅的矿蓝，不能拿来替换搭配卡。

## 2. Five pairings as UI design-token sets

Each set keeps the sampled brand hexes frozen. `--on-primary` is the label color
on a `--primary` button. If a role fails WCAG AA, change the text token. Do not
"fix" a sampled brand hex. Check pairs with `scripts/contrast.py`.

### 2.1 豆黄 × 群青 (Imperial yellow & deep ultramarine)
```
--bg:        #FFDF70   豆黄 (warm dominant, fills outer card)
--surface:   #F2ECDE   缟 (paper neutral, body bg)
--primary:   #153472   群青 (cool dominant, CTA / section bands)
--on-primary:#FFFFFF   on 群青
--text:      #161823   漆黑
--text-muted:#3D3B4F   玄青
--accent:    #EEDEB0   牙色
--border:    rgba(21,52,114,0.15)
```
→ Use for: 国潮活动、文化展览、年轻化中式品牌。高对比 (VARIANCE 7+)。

### 2.2 扶光 × 中国红 (Warm beige & national red)
```
--bg:        #EFC2A3   扶光 (soft warm dominant)
--surface:   #FFF7EE   纸白偏暖
--primary:   #DA0011   中国红 (saturated red, CTA fill, not text on 扶光)
--on-primary:#FFFFFF   on 中国红
--text:      #3A1414   深红墨
--accent:    #F2ECDE   缟
--border:    rgba(218,0,17,0.18)
```
→ Use for: 国庆/中式喜庆、女性+母品牌、文创。暖底+正红，文案要短促有力。
→ 中国红作为扶光上的文字只有约 3.2:1，不能做正文或小字。红色只做按钮填充。

### 2.3 丹红 × 深海绿 (Vermilion & deep teal)
```
--bg:           #FE5C1B   丹红 (warm field, about 60%)
--surface:      #FFF7EE   纸白 (reading cards)
--band:         #1A3B32   深海绿 (cool field, about 40%)
--primary:      #1A3B32   深海绿 (CTA fill)
--on-primary:   #FFF7EE   纸白 on 深海绿
--text:         #161823   漆黑 on 丹红 and on 纸白
--text-muted:   #5C4036   on 纸白 only
--text-on-band: #FFF7EE   on 深海绿 only
--accent:       #F2ECDE   缟
--border:       rgba(22,24,35,0.18)
```
→ Use for: 茶饮/餐饮、能量品牌、潮牌东方。丹红占 60%，深海绿占 40%，强反差。
→ 纸白 `#FFF7EE` 铺在丹红上约 2.9:1，过不了 AA，也违反下面第 5 条。暖色块上用漆黑，深海绿色带上才用纸白。`#5C4036` 只放在纸白上，不要放在丹红上。

### 2.4 水蓝 × 鹤蓝 (Sky blue & crane blue)
```
--bg:        #9ED4F0   水蓝 (light cool dominant)
--surface:   #EAF6FC   极浅水蓝
--primary:   #144975   鹤蓝 (deep blue, text & CTA)
--on-primary:#FFFFFF   on 鹤蓝
--text:      #0A2A45   极深蓝墨
--text-muted:#3A5470   darkened from #3D5A78 so body text clears 4.5:1 on 水蓝
--accent:    #FFFFFF
--border:    rgba(20,73,117,0.15)
```
→ Use for: 科技/文化、博物馆、低调东方学院风。同色相明度对撞，最易出高级感。

### 2.5 淡粉 × 金红 (Pale pink & gold-orange)
```
--bg:        #EBD2D6   淡粉 (soft warm dominant)
--surface:   #FFF5F2   浅粉纸
--primary:   #E45600   金红 (vivid orange, CTA fill, not text on 淡粉)
--on-primary:#161823   漆黑 on 金红 (white on 金红 is only about 3.7:1)
--text:      #4A1E10   深棕墨
--text-muted:#7A4530
--accent:    #FFF8E1   极浅金
--border:    rgba(228,86,0,0.2)
```
→ Use for: 茶/器物/手作品牌、女性文创、轻奢东方。淡粉做底，金红压色，最柔。
→ 金红作为淡粉上的文字约 2.6:1，连大字都过不了。金红只做按钮填充，按钮字用漆黑。

## 3. 双色搭配通用法则 (from the article's pattern)

1. **一冷一热** — warm covers 60–70%, cool covers 30–40%, never 1:1.
2. **第三色=中性** — only ink (#161823) and paper (#F2ECDE) do text & rest.
3. **不撞饱和** — don't pair two same-saturation primaries. Soft beige +
   saturated red works; saturated red + saturated yellow hurts.
4. **深色用采样值，不要再压暗** — 群青 `#153472`、深海绿 `#1A3B32`、鹤蓝 `#144975`
   已经是图片采样结果。印刷 HEX 是错色，不是「略深一点」。不要把它们改写成
   `#0A1A2A`。对比度不够时换文字色或角色，不要改这五个搭配的色值。
5. **文字色用墨不用白** — paper-white text on warm bg reads cheap; use 漆黑
   on the warm half, and 缟/纸白 on the cool half.

## 4. New swatch entries (added for completeness)

- 扶光 `#EFC2A3`  (warm beige, real sampled)
- 中国红 `#DA0011`  (saturated national red, real sampled)
- 丹红 `#FE5C1B`  (vermilion, real sampled)
- 深海绿 `#1A3B32`  (deep teal, real sampled)
- 水蓝 `#9ED4F0`  (sky blue, real sampled)
- 鹤蓝 `#144975`  (crane blue, real sampled)
- 淡粉 `#EBD2D6`  (pale pink, real sampled)
- 金红 `#E45600`  (gold-orange, real sampled)

## 5. Functional roles (map to design tokens)

| Role | Color | HEX | Notes |
|------|-------|-----|-------|
| 纸底 bg | 缟 | `#F2ECDE` | warm paper off-white |
| 纸底 bg | 素 | `#E0F0E9` | pale green-white |
| 纸底 bg | 荼白 | `#F3F9F1` | clean surface |
| 墨 text | 漆黑 | `#161823` | ink, not pure black |
| 墨 text | 玄青 | `#3D3B4F` | muted ink |
| 墨 text | 黛 | `#50616D` | blue-grey ink |
| 描边 border | 牙色 | `#EEDEB0` | ivory border |
| 描边 border | 灰青 | `#A1AFC9` | cool border |
| 主色 primary | 胭脂 | `#9D2933` | deep rouge |
| 主色 primary | 朱砂 | `#FF461F` | vermillion |
| 主色 primary | 妃色 | `#ED5736` | bright coral-red |
| 主色 primary | 绛紫 | `#8C4356` | dark plum |
| 点缀 accent | 缃色 | `#F0C239` | pale gold |
| 点缀 accent | 群青（浅） | `#4C8DAE` | 色系参考，不是文章搭配里的群青 `#153472` |
| 点缀 accent | 黛蓝 | `#425066` | deep blue-grey |

## 6. Ready-made harmony groups (other classic combos)

**喜庆红金 (festive / brand)**
`#FF461F` 朱砂 · `#F0C239` 缃色 · `#161823` 漆黑 · `#F2ECDE` 缟
→ Use for: 国潮品牌、节庆、文化机构。

**青绿山水 (landscape / calm)**
`#57C3C2` 石绿 · `#21A675` 松柏绿 · `#D6ECF0` 月白 · `#425066` 黛蓝
→ Use for: 茶、自然、文旅、健康。

**黛蓝雅致 (elegant blue)**
`#177CB0` 靛青 · `#2E4E7E` 藏青 · `#D6ECF0` 月白 · `#EEDEB0` 牙色
→ Use for: 科技国学、书院、金融文化。

**胭脂藕粉 (romantic / soft)**
`#9D2933` 胭脂 · `#EDD1D8` 藕色 · `#F2ECDE` 缟 · `#3D3B4F` 玄青
→ Use for: 女性品牌、文创、服饰。

## 7. Full swatch reference (by family, original canon)

**红 · Red family**
胭脂 `#9D2933` · 朱砂 `#FF461F` · 妃色 `#ED5736` · 海棠红 `#DB5A6B` ·
茜色 `#CB3A56` · 绯红 `#C83C23` · 绛紫 `#8C4356` · 品红 `#F00056` ·
朱红 `#FF4C00` · 银红 `#F05654` · 桃红 `#F47983` · 藕色 `#EDD1D8` ·
中国红 `#DA0011` · 丹红 `#FE5C1B` · 金红 `#E45600`

**黄 · Yellow / Earth family**
豆黄 `#FFDF70` · 扶光 `#EFC2A3` · 缃色 `#F0C239` · 鹅黄 `#FFF143` · 杏黄 `#FFA631` ·
琥珀 `#CA6924` · 赭石 `#845A33` · 秋香色 `#D9B611` · 黄栌 `#E29C45` ·
牙色 `#EEDEB0` · 黎 `#75664D`

**绿 · Green family**
竹青 `#789262` · 玉色 `#2EDFA3` · 石绿 `#57C3C2` · 松柏绿 `#21A675` ·
碧色 `#1BD1A5` · 葱绿 `#9ED900` · 油绿 `#00BC12` · 深海绿 `#1A3B32`

**蓝 · Blue / Teal family**
群青 `#4C8DAE` · 群青（深） `#153472` · 花青 `#003472` · 靛蓝 `#065279` ·
靛青 `#177CB0` · 黛蓝 `#425066` · 藏青 `#2E4E7E` · 宝蓝 `#4B5CC4` ·
月白 `#D6ECF0` · 水蓝 `#9ED4F0` · 鹤蓝 `#144975`

**紫 · 黑 · 白 · Purple / Dark / Light**
紫檀 `#4C221B` · 玄青 `#3D3B4F` · 漆黑 `#161823` · 黛 `#50616D` ·
缟 `#F2ECDE` · 素 `#E0F0E9` · 荼白 `#F3F9F1` · 月白 `#D6ECF0` ·
灰青 `#A1AFC9` · 淡粉 `#EBD2D6`

## 8. Usage rules

- 主色 = 品牌焦点（按钮、标题强调）；点缀 = 印章/分隔/小标，用量 ≤15%。
- 背景用 缟/素/荼白，正文用 漆黑/玄青，保证 AA 对比。
- 避免红配绿等高饱和直接对冲，除非刻意撞色（孟菲斯风另议）。
- 留白即设计：中国古典靠 留白 出气韵，不要填满。
- **永远不要直接采用文章印刷的 `#xxxxxx`**——已用像素采样校正，详见第 1 节。

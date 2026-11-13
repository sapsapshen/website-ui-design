# website-ui-design

> 一站式网站 UI 设计技能：8 种风格 token 库 + 内嵌 taste/skill 去 AI 化精修。
> 来源于微信公众号「AIGC 设计便利店」《你绝对没见过的中国传统色》一文。

把一篇文章变成一套可落地的设计系统：先做 Design Read 推断方向，再选 8 种风格之一
（**中国古典 / 新野兽派 / 极简瑞士 / 玻璃拟态 / 暗黑科技 / 复古孟菲斯 / 包豪斯 / 柔和有机**）
构建 token 与组件，最后强制走 taste/anti-slop Pre-Flight Check，**不通过不许交付**。

技能源码在 [`skills/website-ui-design/`](skills/website-ui-design/SKILL.md)，符合 [Agent Skills](https://agentskills.io/specification) 规范。`dist/website-ui-design.zip` 由源码打包，目录名与 `name: website-ui-design` 一致。

---

## 特色

- **5 种「双色搭配」中国风色卡**（按原文图片采样校正，印刷 HEX 全部不可用）：

  | 搭配 | 暖色 | 冷色 | 适用场景 |
  |------|------|------|----------|
  | 豆黄 × 群青 | `#FFDF70` | `#153472` | 国潮活动、文化展 |
  | 扶光 × 中国红 | `#EFC2A3` | `#DA0011` | 中式喜庆、女性品牌 |
  | 丹红 × 深海绿 | `#FE5C1B` | `#1A3B32` | 茶饮、餐饮、潮牌东方 |
  | 水蓝 × 鹤蓝 | `#9ED4F0` | `#144975` | 科技文化、博物馆 |
  | 淡粉 × 金红 | `#EBD2D6` | `#E45600` | 茶器、手作、轻奢东方 |

- **8 套完整 token 系统**，每套含 bg/surface/primary/on-primary/accent/text/border/motion/字体。按钮字色用 `--on-primary`，不再拿页面背景色去当按钮文字。
- **采样色值冻结**。对比度不够时改文字色或角色，不改上面 10 个 HEX。群青 `#153472` 和色系总表里的群青（浅）`#4C8DAE` 不是同一个颜色。
- **taste/skill 去 AI 化方法论**内嵌为强制收尾：16 条禁用项 + 三拨盘（VARIANCE / MOTION / DENSITY）+ Pre-Flight Check。滚动动效用 CSS `animation-timeline`，并尊重 `prefers-reduced-motion`。
- **组件级中国风落地**：`assets/starter.html` 提供非对称 hero、zig-zag 特性区、CTA 底部对齐、可聚焦按钮，以及 5 张达到正文对比度的配色卡。
- **对比度脚本**：`python3 skills/website-ui-design/scripts/contrast.py #161823 #FE5C1B`，只依赖 Python 标准库。

## 安装

```bash
# 源码目录，复制到 WorkBuddy
cp -R skills/website-ui-design ~/.workbuddy/skills/

# zip 根目录里已经有 website-ui-design/，解压到 skills 的上一级
unzip dist/website-ui-design.zip -d ~/.workbuddy/skills

# Cursor、Claude Code、Codex 等支持 skills CLI 的环境
npx skills add sapsapshen/website-ui-design
```

`npx skills add https://github.com/sapsapshen/website-ui-design` 同样可以。

## 使用

对 WorkBuddy，或任何会读取 `SKILL.md` 的 Agent，说：

```
用 website-ui-design 帮我设计一个茶饮品牌的官网
```

技能会自动：

1. **Design Read** — 推断目的、用户、品牌调性、约束。
2. **风格选择** — 推荐 1–2 个风格（含 5 种中国风双色）。
3. **构建 token** — 复制 style-library.md 中对应 token 集，并带上 `--on-primary`。
4. **构建布局** — 使用 starter.html。非国风页面删掉双色卡那一节。
5. **强制去 AI 化** — 跑 16 条禁用清单和 Pre-Flight Check，对比度不过关就改文字色，不通过则不交付。

## 目录结构

```
skills/website-ui-design/
├── SKILL.md                     # 入口：Phase 0–4
├── references/
│   ├── chinese-colors.md        # 5 种双色搭配与校正 HEX
│   ├── style-library.md         # 8 套风格 token
│   ├── anti-slop.md             # 16 条禁用 + 3 拨盘 + Pre-Flight Check
│   └── example.md               # 茶饮品牌走查
├── assets/
│   └── starter.html             # 语义化模板（含 5 张配色卡）
└── scripts/
    └── contrast.py              # WCAG 对比度，标准库即可运行
```

仓库根上的 `scripts/validate.py` 与 `scripts/pack.py` 用来校验并重新打包 zip，不会装进技能目录。

## 开发

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/pack.py
python3 scripts/validate.py
```

`validate.py` 会检查 Agent Skills 前置信息、采样色值是否在各文档里一致、公布的文字/背景组合是否达到 4.5:1，以及 zip 是否和源码一致。GitHub Actions 跑同一条命令。

## 微信公众号介绍文章

[`docs/wechat_article.md`](docs/wechat_article.md) 是公众号介绍文章（标题：《我把 8 页中国传统色文章，做成了一个能直接产出网站的技能》），含 5 搭配 hex 表，可直接复制到公众号编辑后台发布。

[`docs/pairings_banner.png`](docs/pairings_banner.png) 是横幅配图（1600×1056），含 5 个 pair 配色卡可视化。

## 来源与致谢

- 颜色与双色搭配原则来自微信公众号 **AIGC 设计便利店** 发布的《你绝对没见过的中国传统色》。
- 去 AI 化方法论来自 [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)。

## 许可

MIT

# website-ui-design

> 一站式网站 UI 设计技能：8 种风格 token 库 + 内嵌 taste/skill 去 AI 化精修。
> 来源于微信公众号「AIGC 设计便利店」《你绝对没见过的中国传统色》一文。

把一篇文章变成一套可落地的设计系统：先做 Design Read 推断方向，再选 8 种风格之一
（**中国古典 / 新野兽派 / 极简瑞士 / 玻璃拟态 / 暗黑科技 / 复古孟菲斯 / 包豪斯 / 柔和有机**）
构建 token 与组件，最后强制走 taste/anti-slop Pre-Flight Check，**不通过不许交付**。

---

## 特色

- **5 种「双色搭配」中国风色卡**（基于原文 8 张图逐张像素采样校正，原图印刷 HEX 全部错误）：
  | 搭配 | 暖色 | 冷色 | 适用场景 |
  |------|------|------|----------|
  | 豆黄 × 群青 | `#FFDF70` | `#153472` | 国潮活动、文化展 |
  | 扶光 × 中国红 | `#EFC2A3` | `#DA0011` | 中式喜庆、女性品牌 |
  | 丹红 × 深海绿 | `#FE5C1B` | `#1A3B32` | 茶饮、餐饮、潮牌东方 |
  | 水蓝 × 鹤蓝 | `#9ED4F0` | `#144975` | 科技文化、博物馆 |
  | 淡粉 × 金红 | `#EBD2D6` | `#E45600` | 茶器、手作、轻奢东方 |

- **8 套完整 token 系统**，每套含 bg/surface/primary/accent/text/border/motion/字体。
- **taste/skill 去 AI 化方法论**内嵌为强制收尾：16 条禁用项 + 三拨盘
  （VARIANCE / MOTION / DENSITY）+ Pre-Flight Check。
- **组件级中国风落地**：`assets/starter.html` 提供非对称 hero、zig-zag 特性区、
  CTA 底部对齐、5 个 pair 配色卡即开即用。
- **像素级颜色校正**：永远不采用文章印刷的 `#xxxxxx`，HEX 全部以原文图片采样为准。

## 安装

把 `dist/website-ui-design.zip` 解压为目录后，复制到任一位置即可使用：

```bash
# 方式 1：解压
unzip dist/website-ui-design.zip -d ~/.workbuddy/skills/website-ui-design

# 方式 2：npx skills
npx skills add https://github.com/sapsapshen/website-ui-design
```

## 使用

对 WorkBuddy（或任何支持 SKILL.md 的 Agent）说：

```
用 website-ui-design 帮我设计一个茶饮品牌的官网
```

技能会自动：
1. **Design Read** — 推断目的、用户、品牌调性、约束。
2. **风格选择** — 推荐 1–2 个风格（含 5 种中国风 two-tone）。
3. **构建 token** — 复制 style-library.md 中对应 token 集。
4. **构建布局** — 使用 starter.html 模板，非对称 hero + zig-zag features + pair 卡片。
5. **强制去 AI 化** — 跑 16 条禁用清单 + Pre-Flight Check，不通过则修复直到通过。

## 目录结构

```
website-ui-design/
├── SKILL.md                     # 入口：工作流 + 4 阶段（Phase 0–3 + Phase 4 强制去AI）
├── references/
│   ├── chinese-colors.md        # 中国古典配色系统（5 种双色搭配、10 个校正 HEX）
│   ├── style-library.md         # 8 套风格 token 集
│   └── anti-slop.md             # 16 条禁用 + 3 拨盘 + Pre-Flight Check
├── assets/
│   └── starter.html             # 语义化基础模板（含 5 个 pair 配色卡）
└── scripts/                     # （可选）自动化脚本
```

## 微信公众号介绍文章

`docs/wechat_article.md` 是一篇 628 字的公众号介绍文章（标题：《我把 8 页中国传统色文章，做成了一个能直接产出网站的技能》），含 5 搭配 hex 表 + 横幅配图，可直接复制到公众号编辑后台发布。

`docs/pairings_banner.png` 是横幅配图（1600×1100），含 5 个 pair 配色卡可视化。

## 来源与致谢

- 颜色与双色搭配原则来自微信公众号 **AIGC 设计便利店** 发布的《你绝对没见过的中国传统色》。
- 去 AI 化方法论来自 [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)。

## 许可

MIT

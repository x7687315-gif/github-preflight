# github-preflight

![License](https://img.shields.io/github/license/x7687315-gif/github-preflight)
![Stars](https://img.shields.io/github/stars/x7687315-gif/github-preflight)
![Last Commit](https://img.shields.io/github/last-commit/x7687315-gif/github-preflight)
![Repo Size](https://img.shields.io/github/repo-size/x7687315-gif/github-preflight)
![WorkBuddy Skill](https://img.shields.io/badge/WorkBuddy-Skill-blue)

> 工程项目动手写代码之前，先去 GitHub（及论文/文档）调研同类项目的经验，产出"开工前经验报告"再开工。

## 它解决什么
不要从零开始。90% 的工程问题 GitHub 上都有人做过、踩过。本 skill 把"借鉴他人经验"变成标准动作：三路并行调研（开源仓库/代码、Issues 踩坑、论文/文档），三角验证后给出可落地的开工报告。

## 何时用
- 准备启动新工程/模块/功能，还没写代码。
- 想做技术选型、架构设计、库选型，需要外部佐证。
- 用户说"先看看别人怎么做的""有没有现成轮子""前人踩过什么坑"。

## 工作流（Phase 0–5）
1. 接收项目简报（🔴 确认要素）
2. 拆解三路调研维度
3. 检索执行（🔴 信息源可信度检查）
4. 三角验证
5. 产出"开工前经验报告"
6. 交接，等用户确认后再开工

详见 `SKILL.md`；检索策略见 `references/search-strategies.md`；报告模板见 `references/report-template.md`。

## 目录结构
```
github-preflight/
├── SKILL.md
├── README.md
├── references/
│   ├── search-strategies.md
│   └── report-template.md
├── results.tsv
└── test-prompts.json
```

## 许可
MIT

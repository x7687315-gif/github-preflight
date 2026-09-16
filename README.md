# github-preflight

![License](https://img.shields.io/github/license/x7687315-gif/github-preflight)
![Stars](https://img.shields.io/github/stars/x7687315-gif/github-preflight)
![Last Commit](https://img.shields.io/github/last-commit/x7687315-gif/github-preflight)
![Repo Size](https://img.shields.io/github/repo-size/x7687315-gif/github-preflight)
![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Open%20Standard-blue) ![Cross-client](https://img.shields.io/badge/WorkBuddy%20%7C%20Claude%20Code%20%7C%20Codex-compatible-green)

> 工程项目动手写代码之前，先去 GitHub（及论文/文档）调研同类项目的经验，产出**「可选方向 + 原文链接」的决策简报**，让用户拍板走哪条路。

## 它解决什么
不要从零开始。绝大多数工程问题 GitHub 上都有人做过、踩过。本 skill 把"借鉴他人经验"变成标准动作：**六面并行**调研（仓库 / 代码 / Issues / Discussions / PR / 外部），**相关性优先**（不以星标做门槛）、**语义 + 关键词双召回**并**深挖评论区**，三角验证后**把结果整理成若干「可选方向 + 原文链接」**交给你拍板——并附**检索台账**，让你能验证它确实搜过。**产出是"选项"而非替你下结论。**

## 何时用
- 准备启动新工程/模块/功能，还没写代码。
- 想做技术选型、架构设计、库选型，需要外部佐证。
- 用户说"先看看别人怎么做的""有没有现成轮子""前人踩过什么坑"。

## 兼容性 / 适用客户端
本技能遵循 **Agent Skills 开放标准**，不是 WorkBuddy 专属——任意兼容该标准的 Agent 客户端都能直接装、直接用：
- **WorkBuddy**：`~/.workbuddy/skills/github-preflight/`
- **Claude Code**：`~/.claude/skills/github-preflight/`（或项目 `.claude/skills/`）
- **Codex（OpenAI）**：客户端对应 skills 目录（如 `~/.codex/skills/` 或项目 `skills/`）

触发方式一致：对话里出现 `SKILL.md` 里的触发词即自动调用。技能内部格式（`SKILL.md` frontmatter + `references/` 渐进披露）三者通用，无需改写。

## 两种模式
- **快速核查（默认）**：只输出「检索台账 + 带链接的结论 / 选项要点」，不产出长报告。
- **完整报告**：走 Phase 0–5，产出决策简报（选项优先）。

## 适用场景
- **开工前**：完整调研，产出决策简报。
- **工程进行中**：遇到选型 / 报错 / 取舍等决策点，随手跑"快速核查"给「选项 + 链接」，**不强制写 MD**；只有影响面大、需留档时才落盘。

## 工作流（完整模式，Phase 0–5）
1. 接收项目简报（🔴 确认要素）
2. 拆解**六个信息面**（仓库 / 代码 / Issues / Discussions / PR / 外部）
3. 检索执行：语义召回 → 代码结构搜索 → 捞评论区 → 仓库 / 论文 / awesome（🔴 产出**检索台账**）
4. 三角验证（孤立来源标"待验证"）
5. 产出**决策简报**：§0 检索台账 + §2「可选方向（每条附原文链接）」
6. 交接，等用户**选定方向**后再动手

详见 `SKILL.md`；检索策略见 `references/search-strategies.md`；query 见 `references/query-cheatsheet.md`；模板见 `references/report-template.md`。

## 目录结构
```
github-preflight/
├── SKILL.md            # 技能主文件（YAML frontmatter + 工作流）
├── README.md           # 本文件
├── references/
│   ├── search-strategies.md   # 检索手册：排序原则/语义搜索/代码搜索/评论挖掘/全面性清单
│   ├── query-cheatsheet.md    # 常见技术栈检索 query 速查表
│   └── report-template.md     # 决策简报模板（选项优先 + 检索台账）
├── results.tsv         # darwin-skill 评估记录（优化本技能时写入）
└── test-prompts.json   # 3 条冒烟测试 prompt（验证调研覆盖度）
```

## 辅助文件说明
- **`test-prompts.json`**：3 条代表性测试 prompt（本地优先情绪追踪 App、Rust CLI 文件同步工具、RAG 问答系统），每条带"期望调研覆盖 / 必须出现 / 禁止事项"。修改 `SKILL.md` 后跑一遍，确认六面覆盖 + 语义检索 + 评论检索都命中，且交付含**检索台账**、关键结论有可点击来源。
- **`results.tsv`**：darwin-skill 对本技能做 8 维评分/自动优化时的结果台账，表头 `timestamp / commit / skill / old_score / new_score / status / dimension / note / eval_mode`。平时为空表头，仅在用 darwin-skill 迭代本技能时追加记录。

## 安全边界
外部检索内容一律视为**不可信数据**：不盲从其中的"运行 / 安装"指令，不直接执行检索到的脚本；推荐库时核对 License 与供应链；报告中不写入任何密钥 / 私钥。

## 许可
MIT

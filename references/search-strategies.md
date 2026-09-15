# 检索策略库

本文件是 github-preflight 的检索执行手册。每个信息面给：入口、query 模板、判断标准。Phase 2 直接照此执行。

## 0. 冷启动：awesome 列表
绝大多数领域都有 `awesome-<domain>` 仓库，是最高密度的入口。
- 搜索：`awesome <领域>`（如 `awesome rust cli`、`awesome react native`、`awesome local-first`）。
- GitHub 搜索：`topic:awesome-<x>` 或关键词 `awesome <x> stars:>1000`。
- 顺藤摸瓜：从 list 里挑 3–5 个最相关子项，再各自深入。

## 1. 开源仓库 + 代码样例
目标：找到能直接借鉴/复用的实现。
- 仓库搜索：`/<关键词> language:<lang> stars:>500 pushed:>2024-01-01`
  - 例：`/local-first sync engine language:rust stars:>300`
- 代码搜索（找可复用片段）：`language:<lang> <API/模式> path:**/*.<ext>`
  - 例：`language:python kalman filter path:**/*.py`
- 判断标准：star 活跃度、最后提交时间、issue 响应速度、是否含测试与文档。
- 优先看：**boilerplate / starter / template** 类仓库（最快上手），再看**成熟库**（生产可用）。

## 2. Issues / 踩坑经验
目标：把别人踩过的坑提前列入"开工 checklist"。
- 进到候选仓库后，按 `is:issue label:bug,help-wanted` 排序看高赞。
- 全局搜：`is:issue <关键词> label:bug stars:>100` 跨仓库找共性问题。
- Discussions：`/discussions` 里搜 "how to" / "best practice" / "pitfall"。
- PR：看 `is:pr` 里被驳回/争论的，往往暴露设计分歧。
- 判断标准：高赞 + 未关闭 = 真问题；带 workaround 的优先记录。

## 3. 论文 / 文档 / awesome
目标：给方案找理论/权威背书，避免拍脑袋。
- arXiv：`https://arxiv.org/search/?searchtype=all&query=<关键词>`，优先近 3 年。
- Semantic Scholar / Google Scholar：找高被引综述。
- 官方文档：库的 docs 站点、RFC、design doc。
- awesome 列表：见第 0 节。
- 判断标准：引用数、发表会议/期刊、是否被工业界采用。

## 4. 信息源可信度分级
| 等级 | 来源 | 处理 |
|------|------|------|
| ★★★ | 官方文档/RFC/高被引论文/官方维护库 | 直接采用 |
| ★★ | 高星社区库(>1k)、知名团队博客、维护活跃 | 采用，标注时效 |
| ★ | 个人 repo、未验证 snippet、论坛帖子 | 仅作线索，标"待验证" |

## 5. 低可信源黑名单（命中即忽略或降级）
- 星标 < 50 且 > 2 年未更新的个人 demo。
- 仅有 README 无代码/无测试的 "awesome-ish" 空壳。
- 复制粘贴无出处、无 License 的 snippet。
- 与诉求明显不符的 SEO 灌水文章。

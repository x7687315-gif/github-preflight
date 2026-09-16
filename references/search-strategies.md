# 检索策略库

本文件是 github-preflight 的检索执行手册。
**核心排序原则：以"能否解决当前问题"为第一标准，相关性优先；星标 / 讨论度只做并列消歧，不作为纳入门槛。**

## 0. 排序原则（相关性优先，修正旧版"星标门槛"）
纳入与排序的优先级（自上而下）：
1. **问题-方案匹配度**：这条内容是否直接回答 / 解决了本项目当前的具体问题。
2. **可落地性**：是否给出可用的代码 / 配置 / 命令；Issue 是否有 accepted answer、workaround、或 **linked 的已合并 PR**（`linked:pr` / `is:pr is:merged`）。
3. **讨论质量**：是否高赞（👍 reactions）、被维护者 / 官方回应、被引为答案。
4. **（仅并列时）星标与维护活跃度**：仅当 1–3 难分高下时，才用 star / 最近提交做微调。

> 反模式：一上来就 `stars:>500` 过滤——会把大量"星少但正好解决你问题"的仓库和讨论直接滤掉。**默认不加星标门槛。**

## 1. 六个信息面（全覆盖 = 全面）
| 面 | 工具 | 说明 |
|----|------|------|
| 仓库 | GitHub repo search / MCP `search_repositories` | 找同类项目 / 库 |
| 代码 | GitHub Code Search / grep.app / Sourcegraph | 找可复用实现、真实用法 |
| Issues | `gh search issues` / 网页搜索 | 找已知坑与 workaround |
| Discussions | 仓库 Discussions 搜索 | 找设计讨论、最佳实践 |
| PR | `is:pr` | 找被采纳的修复（merged） |
| 外部 | Stack Overflow / 论文 / 官方文档 | 补盲区 |

> 交付前务必对六面各至少跑 1 条查询（见 §8 检查清单）。

## 2. 语义搜索（新增，解决"关键词漏召回"）
- **GitHub Issues 语义搜索（最强，官方 CLI）**：
  - `gh search issues "<自然语言问题>" --search-type semantic`
  - 也可 `--search-type hybrid`（关键词 + 语义混合）。语义 / 混合模式**按相关性排序**，此时不能用 `--sort`。
  - 用 `--match comments` 直接搜**评论正文**——很多解法藏在评论区而非标题 / 正文。
  - 例：`gh search issues "local-first sync conflict resolution without server" --search-type semantic --match comments`
  - 无 gh / 无 MCP 时：GitHub 网页搜 issues，用**自然语言问句** + `sort:relevance`。
  - MCP：`mcp__github__search_issues` 支持语义查询（若该客户端版本提供）。
- **代码语义搜索**：GitHub 代码搜索**不是真语义**（它是 keyword / regex / 结构 / symbol）。真语义代码搜索用外部：
  - **grep.app**：50 万+ 公开仓库的快速文本 / 模式检索——找"真实用法"最实用。
  - **Sourcegraph**（含 Cody / Deep Search）：跨仓库、自然语言问代码意图。
  - **searchcode / OpenGrok**：补充渠道。
  - 通用 Web 语义：Exa、Perplexity——问"哪个开源库能解决 X"。
- **双写策略**：同一问题同时用「自然语言问句」和「关键短语 / 错误原文」各搜一次，互补召回。

## 3. 代码相关度搜索（GitHub Code Search 精确语法）
- `symbol:` —— 搜函数 / 类**定义**（Tree-sitter 解析）：`language:rust symbol:Backoff`；支持 `symbol:Type.method`、`symbol:/^String::to_.*/`。支持语言：C# / Python / Go / Java / JS / TS / PHP / Protobuf / Ruby / Rust。
- `path:` + glob / regex：`path:/src/**/*.ts`、`path:/(^|\/)README\.md$/`。
- `content:` 只搜内容不搜路径；`language:` / `repo:` / `org:` / `user:` 收窄。
- 正则 `/pattern/` + 布尔 `AND / OR / NOT` + 括号。
- **用"问题描述"而非 API 名去搜注释 / 错误串**：把报错原文加引号搜 `"exact error text"`。
- 限制：API 单查询最多 1000 结果；仅**默认分支**被索引；文件 < 5MB、仅前 500KB 可搜；仓库 < 50 万文件。

## 4. Issues / Discussions 精华挖掘（重点修正）
目标：把"埋在讨论 / 评论里的解法"捞出来。
- **搜评论正文**：网页 `in:comments <关键词>`，或 gh `--match comments`——解决方法的金矿。
- **识别"已被解决"的信号**：
  - `linked:pr`（有修复 PR 关联的 issue）
  - `is:closed reason:completed`（按完成关闭，而非 not planned）
  - `is:pr is:merged <关键词>`（已合并的修复）
- **按质量而非星标排序**：`sort:reactions-+1-desc`（👍 最多）、`sort:interactions`、`sort:comments`；语义模式则天然按相关性。
- **Discussions**：进仓库 Discussions 搜 "how to" / "best practice" / "pitfall"，看 **Answered** 标记。
- **错误原文检索**：把报错 / 异常原文加引号，跨 issues / comments / gists / 代码一起搜。
- 判断：高赞 + 已关闭(completed) / 有 linked merged PR = 真解决；带 workaround 的优先记录。

## 5. 论文 / 文档 / awesome
目标：给方案找理论 / 权威背书，避免拍脑袋。
- arXiv：`https://arxiv.org/search/?searchtype=all&query=<关键词>`，优先近 3 年。
- Semantic Scholar / Google Scholar：找高被引综述。
- 官方文档：库的 docs 站点、RFC、design doc。
- awesome 列表（冷启动入口）：搜 `awesome <领域>` 或 `topic:awesome-<x>`，从 list 挑 3–5 个相关子项再深入。
- 判断：引用数、发表会议 / 期刊、是否被工业界采用。

## 6. 信息源可信度分级（从属于相关性）
| 等级 | 来源 | 处理 |
|------|------|------|
| ★★★ | 官方文档 / RFC / 高被引论文 / 官方维护库 | 直接采用 |
| ★★ | 知名团队博客 / 维护者回应 / 被引为答案 | 采用，标注时效 |
| ★ | 个人 repo、未验证 snippet、论坛帖子 | 仅作线索，标"待验证" |

> 注意：可信度用于**给结论定置信度**，不是**纳入门槛**。一条 ★ 来源若正好解决问题且带 workaround，也要收进报告并标注"待验证"。

## 7. 低质量剔除（不再以星标为主）
- 仅有 README、无代码 / 无测试的 "awesome-ish" 空壳。
- 复制粘贴无出处、无 License 的 snippet。
- 与诉求明显不符的 SEO 灌水 / 明显 AI 生成的错误代码。
- 归档且无替代的僵尸项目（**提示风险，而非因星少剔除**）。

## 8. 全面性检查清单（交付前自检）
- [ ] 六面（仓库 / 代码 / Issues / Discussions / PR / 外部）至少各 1 条有效查询。
- [ ] 至少做过一次**语义检索**（Issues 语义，或外部语义代码 / Web）。
- [ ] 至少检索过 `in:comments`（评论正文）一次。
- [ ] 已用 `linked:pr` / `is:closed reason:completed` 尝试找"已被解决"的讨论。
- [ ] 结论**按相关性排序**，星标未被用作纳入门槛。

# 常见技术栈检索 query 速查表

配合 `SKILL.md` 与 `search-strategies.md` 使用。把 `<关键词>` 换成你项目的真实词。
**排序原则：相关性优先——不要用 `stars:>N` 当门槛。** 星标只在结果难分高下时做微调。

## 0. 语义搜索（最先跑，解决"关键词漏召回"）
| 目的 | query |
|------|-------|
| Issues 语义检索（自然语言） | `gh search issues "<自然语言问题>" --search-type semantic` |
| 关键词 + 语义混合 | `gh search issues "<问题>" --search-type hybrid` |
| 直接搜**评论正文**（解法金矿） | gh：加 `--match comments`；网页：`in:comments <关键词>` |
| 代码语义（GitHub 不支持）→ 用外部 | grep.app / Sourcegraph（自然语言问意图）/ searchcode |
| Web 语义"哪个库能解决 X" | Exa / Perplexity |

## 1. 仓库 / 代码样例
| 技术域 | 仓库搜索 query | 代码搜索 query |
|--------|---------------|----------------|
| Web 前端 (React/Vue) | `/<关键词> language:typescript` | `language:typescript <模式> path:**/*.tsx` |
| Node / Deno 后端 | `/<关键词> language:typescript` | `language:javascript <API> path:**/*.ts` |
| Python (ML/数据/脚本) | `/<关键词> language:python` | `language:python <算法> path:**/*.py` |
| Rust CLI / 系统 | `/<关键词> language:rust` | `language:rust symbol:<Trait/Struct>` |
| Go 服务 | `/<关键词> language:go` | `language:go symbol:<Func>` |
| Flutter / Dart 移动 | `/<关键词> language:dart` | `language:dart path:**/*.dart` |
| React Native | `/<关键词> topic:react-native` | `language:typescript path:**/*.tsx` |
| 本地优先 / 离线 | `/<关键词> topic:local-first` | `language:typescript offline` |
| 端侧 ML / 推理 | `/<关键词> topic:on-device` | `language:python inference path:**/*.py` |
| 桌面 (Tauri/Electron) | `/<关键词> topic:tauri` | `language:rust path:**/*.rs` |

> 需要收窄再按需加 `language:` / `repo:` / `org:`，**不要用 `stars:>`**。
> 需要最成熟方案时可用 `sort:updated` 兜底看活跃度（非门槛）。

## 2. 代码结构搜索（GitHub Code Search 精确语法）
| 目的 | query |
|------|-------|
| 找函数 / 类定义 | `symbol:<Name>` 或 `language:go symbol:Type.Method` |
| 路径 glob / 正则 | `path:/src/**/*.ts`、`path:/(^|\/)README\.md$/` |
| 只搜内容不搜路径 | `content:<term>` |
| 精确报错原文 | `"exact error text" language:<lang>` |
| 组合布尔 | `(language:ruby OR language:python) AND NOT path:"/tests/"` |

## 3. Issues / Discussions 精华挖掘
| 目的 | query |
|------|-------|
| 搜**评论**里的解法 | `in:comments <关键词>` |
| 已被修复的 issue | `linked:pr <关键词>` |
| 按完成关闭（真解决） | `<关键词> is:closed reason:completed` |
| 已合并的修复 PR | `is:pr is:merged <关键词>` |
| 高赞讨论（质量排序） | `<关键词> sort:reactions-+1-desc` |
| 互动最多的讨论 | `<关键词> sort:interactions` |
| Discussions 最佳实践 | 进仓库 Discussions 搜 `how to` / `best practice` / `pitfall`（看 Answered） |

## 4. 论文 / 文档 / awesome
| 目的 | query |
|------|-------|
| arXiv 近 3 年 | `https://arxiv.org/search/?searchtype=all&query=<关键词>` |
| 高被引综述 | Semantic Scholar / Google Scholar：`<关键词> survey` |
| awesome 入口（冷启动） | `awesome <领域>` 或 `topic:awesome-<x>` |
| 官方文档 / RFC | `<库名> docs`；`site:datatracker.ietf.org <关键词>` |

## 5. 现成模板 / boilerplate（最快上手）
在仓库搜索里加后缀：`<关键词> starter` / `boilerplate` / `template` / `example` / `scaffold`。
例：`rag pipeline starter language:python`（不加星标门槛，按相关性看）。

## 6. 用法提示
- 六面都要覆盖：仓库 / 代码 / Issues / Discussions / PR / 外部。
- 同一问题做**双写**：自然语言问句 + 关键短语 / 错误原文，各搜一次。
- 低质量剔除看"是否为真实现"（空壳 / 无 License / 灌水），**不以星少为由剔除**。
- 单一来源的结论标"待验证"；交付前附上**检索台账**。

# 常见技术栈检索 query 速查表

配合 `SKILL.md` 与 `search-strategies.md` 使用。把 `<关键词>` 换成你项目的真实词即可直接粘贴到 GitHub 搜索框。
通用质量闸门：`stars:>500 pushed:>2024-01-01`（成熟库可放宽，探索期可收紧）。

## 1. 仓库 / 代码样例（repo & code search）

| 技术域 | 仓库搜索 query | 代码搜索 query |
|--------|---------------|----------------|
| Web 前端 (React/Vue) | `/<关键词> language:typescript stars:>500 pushed:>2024-01-01` | `language:typescript <模式> path:**/*.tsx` |
| Node / Deno 后端 | `/<关键词> language:typescript stars:>500` | `language:javascript <API> path:**/*.ts` |
| Python (ML/数据/脚本) | `/<关键词> language:python stars:>1000` | `language:python <算法> path:**/*.py` |
| Rust CLI / 系统 | `/<关键词> language:rust stars:>300` | `language:rust <trait/crate> path:**/*.rs` |
| Go 服务 | `/<关键词> language:go stars:>500` | `language:go <interface> path:**/*.go` |
| Flutter / Dart 移动 | `/<关键词> language:dart stars:>300` | `language:dart <widget> path:**/*.dart` |
| React Native | `/<关键词> language:typescript topic:react-native stars:>300` | `language:typescript path:**/*.tsx` |
| 本地优先 / 离线 | `/<关键词> topic:local-first stars:>200` | `language:typescript offline path:**/*` |
| 端侧 ML / 推理 | `/<关键词> language:python topic:on-device stars:>200` | `language:python inference path:**/*.py` |
| 桌面 (Tauri/Electron) | `/<关键词> topic:tauri stars:>200` | `language:rust path:**/*.rs` |
| 数据库 / ORM | `/<关键词> language:sql stars:>300` | `language:<lang> <query> path:**/*.sql` |

## 2. Issues / 踩坑（真实坑优先看高赞 + 未关闭）

| 目的 | query |
|------|-------|
| 跨仓库共性问题 | `is:issue <关键词> label:bug stars:>100` |
| 某仓库已知坑 | 进仓库 → `is:issue label:bug,help-wanted` 按 **Most reacted** 排序 |
| 设计分歧 / 被拒方案 | `is:pr <关键词>` 看被驳回或争论的 PR |
| 最佳实践讨论 | `/discussions <关键词> best practice` |
| 性能/内存类坑 | `is:issue <关键词> label:performance,memory` |

## 3. 论文 / 文档 / awesome

| 目的 | query |
|------|-------|
| arXiv 近 3 年 | `https://arxiv.org/search/?searchtype=all&query=<关键词>` |
| 高被引综述 | Semantic Scholar / Google Scholar：`<关键词> survey` |
| awesome 入口（冷启动） | `awesome <领域>` 或 `topic:awesome-<x>` |
| 官方文档 / RFC | 直接搜 `<库名> docs`；RFC 搜 `site:datatracker.ietf.org <关键词>` |
| 设计文档 / ADR | `<库名> design doc` 或 `<关键词> architecture decision` |

## 4. 现成模板 / boilerplate（最快上手）

在仓库搜索里加这些后缀，再叠加语言/星标闸门：
- `<关键词> starter`
- `<关键词> boilerplate`
- `<关键词> template`
- `<关键词> example`
- `<关键词> scaffold`

例：`/rag pipeline starter language:python stars:>200 pushed:>2024-01-01`

## 5. 用法提示
- 三路都要覆盖：仓库/代码（上面 1、4）、Issues/踩坑（上面 2）、论文/文档（上面 3）。
- 命中"低可信源黑名单"（search-strategies §5）的忽略：<50 星且 2 年僵尸、仅 README 空壳、无 License 复制片段、SEO 灌水。
- 单一来源的结论标"待验证"，至少 2 个独立来源才写进报告主结论。

# 贡献指南（CONTRIBUTING）

感谢想改进 `github-preflight`！本仓库是一个 [WorkBuddy](https://workbuddy.cn) 用户级技能，遵循 Agent Skills 开放标准。

## 目录约定
- `SKILL.md` 是入口，frontmatter 的 `name` 用小写中划线，`description` 写清中文触发词（≤1024 字）。
- 长内容拆到 `references/`，主文件保持精简（建议 ≤500 行），遵循渐进式披露。
- 不要在主文件里堆大段资料，保持"流程 + 指针"结构。

## 改动流程
1. Fork / 新建分支，修改 `SKILL.md` 或 `references/`。
2. 跑一遍 `test-prompts.json` 里的 3 条 prompt，确认：
   - 三路调研（开源仓库/代码、Issues/踩坑、论文/文档）都能命中有效来源；
   - 每条"已知坑"都带可点击来源链接；
   - 报告含"开工 checklist"，不是纯资料堆砌。
3. 自检 `SKILL.md` 末尾「质量门禁」清单全部打勾。
4. 提 PR，说明改了哪条规则、为什么。

## 进阶：用 darwin-skill 自动优化
若想用 [darwin-skill](https://workbuddy.cn) 做 8 维评分/自动迭代：
- 它会把评分结果追加写入 `results.tsv`（表头：`timestamp / commit / skill / old_score / new_score / status / dimension / note / eval_mode`）。
- 请勿手改 `results.tsv` 的历史行，只在自动优化时由工具追加。

## 许可
本仓库采用 MIT。提交即表示你同意以相同许可发布你的改动。

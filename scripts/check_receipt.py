#!/usr/bin/env python3
"""check_receipt.py — github-preflight 检索台账校验器

把「必须真的检索过」从文字规则变成**可运行判定**。
输入：一份决策简报 / 报告的 Markdown（文件路径，或 - 读 stdin）。
检查：①台账存在 ②台账条数 ③六面覆盖 ④语义检索 ⑤评论检索 ⑥来源 URL 可达性。
输出：PASS / FAIL + 缺失项 + 分数；退出码 0=PASS，1=FAIL。

用法：
  python scripts/check_receipt.py brief.md
  python scripts/check_receipt.py brief.md --min-rows 3 --json
  python scripts/check_receipt.py brief.md --no-net      # 跳过 URL 可达性（离线/沙盒）

跨端说明：纯标准库（Python3），无需第三方依赖。若客户端不支持执行脚本，
按 SKILL.md 的「质量门禁」人工核对同样条目即可。
"""
import sys
import os
import re
import json
import argparse
import urllib.request
import urllib.error

FACES = {
    "仓库": [r"search_repositories", r"\brepo[s]?\b", r"仓库"],
    "代码": [r"grep\.app", r"sourcegraph", r"symbol:", r"path:\*\*", r"content:", r"代码"],
    "Issues": [r"\bissue[s]?\b", r"in:comments", r"linked:pr", r"is:issue"],
    "Discussions": [r"discussion"],
    "PR": [r"is:pr", r"pull request", r"merged", r"\bpr\b"],
    "外部": [r"arxiv", r"论文", r"stack\s*overflow", r"awesome", r"文档", r"\bdocs?\b"],
}


def load(path):
    if not path or path == "-":
        return sys.stdin.read()
    with open(path, encoding="utf-8") as f:
        return f.read()


def find_ledger(text):
    """返回 (台账数据行数, 台账内 URL 数)。"""
    lines = text.splitlines()
    start = None
    for i, ln in enumerate(lines):
        if "检索台账" in ln:
            start = i
            break
    if start is None:
        return 0, 0
    rows = 0
    urls = 0
    for ln in lines[start + 1:]:
        if ln.startswith("## "):
            break
        urls += len(re.findall(r"https?://[^\s\)\]<>\"']+", ln))
        s = ln.strip()
        if s.startswith("|") and "---" not in s:
            cells = [c.strip() for c in s.strip("|").split("|")]
            if not cells or all(c == "" for c in cells):
                continue
            head = " ".join(cells).lower()
            if "查询" in head or "query" in head:
                continue
            if len(cells) >= 3:
                rows += 1
    return rows, urls


def find_urls(text):
    raw = re.findall(r"https?://[^\s\)\]<>\"'，。；）、]+", text)
    return sorted({u.rstrip(".,;:)。，；、") for u in raw if u.rstrip(".,;:)。，；、")})


def has_any(text, pats):
    return any(re.search(p, text, re.I) for p in pats)


def probe(url, timeout=8):
    """返回 (status|None, err)。None 表示无法连通（被墙/超时/代理问题）。"""
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("HTTP_PROXY")
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({"http": proxy, "https": proxy})
    )
    hdr = {"User-Agent": "Mozilla/5.0 (preflight-check)"}
    try:
        with opener.open(urllib.request.Request(url, method="HEAD", headers=hdr), timeout=timeout) as r:
            return r.status, ""
    except urllib.error.HTTPError as e:
        if e.code in (403, 405, 429):  # 头请求被拒 -> 换 GET
            try:
                with opener.open(urllib.request.Request(url, method="GET", headers=hdr), timeout=timeout) as r:
                    return r.status, ""
            except urllib.error.HTTPError as e2:
                return e2.code, ""
            except Exception as e2:
                return None, repr(e2)
        return e.code, ""
    except Exception as e:
        return None, repr(e)


def main():
    ap = argparse.ArgumentParser(description="github-preflight 检索台账校验器")
    ap.add_argument("path", nargs="?", default="-", help="简报 Markdown 路径，或 - 读 stdin")
    ap.add_argument("--min-rows", type=int, default=3, help="台账最少条数（默认 3）")
    ap.add_argument("--no-net", action="store_true", help="跳过 URL 可达性检查")
    ap.add_argument("--json", action="store_true", help="JSON 输出")
    args = ap.parse_args()

    text = load(args.path)
    fails, warns = [], []

    # ① 台账存在 + ② 条数
    has_ledger = "检索台账" in text
    rows, _ = find_ledger(text)
    if not has_ledger:
        fails.append("缺少「检索台账」章节（§0 必填）—— 无法证明真的检索过")
    elif rows < args.min_rows:
        fails.append(f"检索台账条数不足：{rows} < {args.min_rows}（应列出实际执行的查询）")

    # ④ 语义检索
    if not re.search(r"--search-type\s+(semantic|hybrid)|semantic|语义", text, re.I):
        fails.append("未见语义检索（gh search issues --search-type semantic / 语义检索）")

    # ⑤ 评论检索
    if not re.search(r"in:comments|--match\s+comments|评论正文|搜评论", text, re.I):
        fails.append("未见评论正文检索（in:comments / --match comments）")

    # ③ 六面覆盖
    covered = [f for f, pats in FACES.items() if has_any(text, pats)]
    missing = [f for f in FACES if f not in covered]
    if missing:
        warns.append("六面未全覆盖：" + "、".join(missing))

    # ⑥ 来源 URL
    urls = find_urls(text)
    domains = sorted({re.sub(r"^https?://([^/]+).*", r"\1", u) for u in urls})
    if not urls:
        fails.append("未发现任何来源 URL —— 结论必须可溯源")
    elif len(domains) == 1 and len(urls) >= 3:
        warns.append(f"来源过于单一（仅 {domains[0]}），建议跨源验证")

    # URL 可达性（默认开）
    if not args.no_net and urls:
        dead, blocked = [], 0
        for u in urls[:20]:
            st, _err = probe(u)
            if st is None:
                blocked += 1
            elif st in (404, 410):
                dead.append(u)
        if dead:
            fails.append("疑似失效链接：" + ", ".join(dead[:5]))
        if blocked:
            warns.append(f"{blocked} 条链接无法连通（被墙/超时/代理，未判定）")

    score = max(0, 100 - 20 * len(fails) - 8 * len(warns))
    verdict = "PASS" if not fails else "FAIL"
    result = {
        "verdict": verdict,
        "score": score,
        "ledger_rows": rows,
        "urls": len(urls),
        "domains": domains,
        "faces_covered": covered,
        "fails": fails,
        "warns": warns,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"[{verdict}] 分数={score} 台账={rows}行 URL={len(urls)}条 域名={len(domains)}个 六面={len(covered)}/6")
        for f in fails:
            print("  FAIL:", f)
        for w in warns:
            print("  WARN:", w)
        if not fails and not warns:
            print("  OK: 全部通过")
    sys.exit(0 if verdict == "PASS" else 1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""sns-ops-wiki の整合性検査。

検査項目:
  1. 内部リンク切れ
  2. front matter(docs 配下の各ページ)の必須キーと確度ラベル
  3. 年の併記「西暦年(皇紀N年・和暦)」の換算の整合
  4. last_verified の鮮度(既定: 180日超で警告)
  5. 秘密情報らしき文字列の簡易検出

使い方: python3 -I scripts/check_wiki.py [--max-age-days 180] [--strict]
終了コード: エラーがあれば 1(--strict の場合は警告でも 1)
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
TEMPLATE_FILE = DOCS / "00-meta" / "page-template.md"
REQUIRED_KEYS = ("title", "last_verified", "confidence")
CONFIDENCE_OK = {"✅", "🟡", "⚪"}
# front matter を検査しないファイル(索引など)
FM_EXEMPT = {DOCS / "README.md", DOCS / "99-planned" / "README.md"}

LINK_RE = re.compile(r"\]\((?!https?:|#|mailto:)([^)\s]+)\)")
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
# 例: 2026年(皇紀2686年・令和8年) / 712年(皇紀1372年・和銅5年)
YEAR_RE = re.compile(r"(\d{3,4})年\(皇紀(\d{4})年・([^)]+?)\)")
REIWA_RE = re.compile(r"令和(元|\d+)年")
HEISEI_RE = re.compile(r"平成(元|\d+)年")
SECRET_RES = [
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
]


def md_files() -> list[Path]:
    files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    return sorted(files)


def parse_front_matter(text: str) -> dict[str, str] | None:
    m = FM_RE.match(text)
    if not m:
        return None
    data: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data


def strip_code(text: str) -> str:
    """コードブロックを除外して本文だけ検査する。"""
    return re.sub(r"```.*?```", "", text, flags=re.S)


def check(max_age: int) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warns: list[str] = []
    today = dt.date.today()

    for path in md_files():
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        body = strip_code(text)

        # 1. 内部リンク(雛形のプレースホルダは除外)
        if path != TEMPLATE_FILE:
            for m in LINK_RE.finditer(body):
                target = m.group(1).split("#")[0]
                if target and not (path.parent / target).resolve().exists():
                    errors.append(f"{rel}: リンク切れ -> {m.group(1)}")

        # 2. front matter
        if path.is_relative_to(DOCS) and path not in FM_EXEMPT:
            fm = parse_front_matter(text)
            if fm is None:
                errors.append(f"{rel}: front matter がない")
            else:
                for k in REQUIRED_KEYS:
                    if k not in fm:
                        errors.append(f"{rel}: front matter に {k} がない")
                if path != TEMPLATE_FILE:
                    conf = fm.get("confidence", "")
                    if conf and conf not in CONFIDENCE_OK:
                        errors.append(f"{rel}: confidence が不正 ({conf})")
                    lv = fm.get("last_verified", "")
                    try:
                        age = (today - dt.date.fromisoformat(lv)).days
                        if age > max_age:
                            warns.append(f"{rel}: last_verified が {age} 日前")
                    except ValueError:
                        errors.append(f"{rel}: last_verified が ISO 日付でない ({lv})")

        # 3. 年の併記
        for m in YEAR_RE.finditer(body):
            seiki, koki, era = int(m.group(1)), int(m.group(2)), m.group(3)
            if koki != seiki + 660:
                errors.append(f"{rel}: 皇紀の換算が不一致 {seiki}年 -> 皇紀{koki}年 (正: {seiki + 660})")
            r = REIWA_RE.search(era)
            if r:
                n = 1 if r.group(1) == "元" else int(r.group(1))
                if seiki - 2018 != n:
                    errors.append(f"{rel}: 令和の換算が不一致 {seiki}年 -> 令和{n}年 (正: 令和{seiki - 2018}年)")
            h = HEISEI_RE.search(era)
            if h:
                n = 1 if h.group(1) == "元" else int(h.group(1))
                if seiki - 1988 != n and not (seiki == 2019 and n == 31):
                    errors.append(f"{rel}: 平成の換算が不一致 {seiki}年 -> 平成{n}年")

        # 5. 秘密情報
        for rx in SECRET_RES:
            if rx.search(text):
                errors.append(f"{rel}: 秘密情報らしき文字列 ({rx.pattern[:20]}...)")

    return errors, warns


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-age-days", type=int, default=180)
    ap.add_argument("--strict", action="store_true", help="警告でも失敗にする")
    args = ap.parse_args()

    errors, warns = check(args.max_age_days)
    for w in warns:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(md_files())} ファイル検査 / エラー {len(errors)} / 警告 {len(warns)}")
    if errors or (args.strict and warns):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

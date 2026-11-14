#!/usr/bin/env python3
"""Check published artifacts and fictional examples, without running an LLM.

The checks establish structural and selected fact constraints only. They do
not prove that an arbitrary model follows the skills or detect every secret.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("handoff", "review-plans", "performance-self-review", "simplify-tech-writing")
RUNTIME = (
    "skills/handoff/SKILL.md",
    "skills/review-plans/SKILL.md",
    "skills/review-plans/agents/openai.yaml",
    "skills/review-plans/references/eight-question-rubric.md",
    "skills/performance-self-review/SKILL.md",
    "skills/performance-self-review/references/example.md",
    "skills/simplify-tech-writing/SKILL.md",
    "skills/simplify-tech-writing/agents/openai.yaml",
    "skills/simplify-tech-writing/references/methods.md",
    "skills/simplify-tech-writing/references/examples.md",
    "skills/simplify-tech-writing/references/sources.md",
    "skills/handoff/LICENSE",
    "skills/review-plans/LICENSE",
    "skills/performance-self-review/LICENSE",
    "skills/simplify-tech-writing/LICENSE",
)
REVIEW_HEADINGS = ["Verdict", "Scope and evidence", "Blocking findings",
                   "Finding ledger", "Eight-question coverage matrix",
                   "Open decisions and verification needs", "Prioritized next actions"]
HANDOFF_HEADINGS = ["当前目标", "最新用户请求", "已完成事项", "当前状态", "关键文件/目录",
                    "已发布版本/线上状态", "重要命令与结果", "关键决策", "待办事项",
                    "风险和坑", "不要做", "不确定/未验证事项", "新会话第一步"]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def public_files():
    return sorted(p for p in ROOT.rglob("*") if p.is_file()
                  and not any(x in {".git", "build", "__pycache__"}
                              for x in p.relative_to(ROOT).parts))


def manifest():
    return {"schema_version": 1, "edition": "0.3.0", "license": "MIT",
            "origin": "Henry2012; developed with AI assistance; owner confirmed 2026-11-11",
            "files": [{"path": s, "sha256": hashlib.sha256((ROOT / s).read_bytes()).hexdigest()}
                      for s in RUNTIME]}


def check_review(text):
    require(re.findall(r"^## (.+)$", text, re.M) == REVIEW_HEADINGS,
            "review report headings changed")
    require("`NOT_READY`" in text, "reference contradiction must block implementation")
    rows = re.findall(r"^\| (F\d+) \| (.+)$", text, re.M)
    require(len(rows) == 1 and rows[0][0] == "F1", "one root cause must produce one finding")
    require("BLOCKER | Q3 | Q5, Q7" in rows[0][1] and "CONFIRMED" in rows[0][1],
            "F1 classification changed")
    statuses = dict(re.findall(r"^\| (Q[1-8]) \| ([A-Z_]+) \|", text, re.M))
    require(statuses == {"Q1": "PASS", "Q2": "PASS", "Q3": "ISSUE", "Q4": "PASS",
                         "Q5": "ISSUE", "Q6": "PASS", "Q7": "ISSUE", "Q8": "PASS"},
            "reference coverage or secondary effects changed")
    require("§2" in text and "§3" in text, "both contradiction anchors must remain")


def check_tree(files):
    patterns = {
        "personal absolute path": "/" + r"(?:Users|home)/[A-Za-z0-9_.-]+/",
        "common secret prefix": r"(?:ghp_|github_pat_|sk-proj-|sk-live-)[A-Za-z0-9_-]{12,}",
        "private key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        "internal host": r"(?:alibaba" + r"-inc\.com|ata" + r"tech\.org|antfin\.com|alidocs\.dingtalk\.com)",
        "email": r"[A-Za-z0-9_.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    }
    for p in files:
        require(not p.is_symlink(), f"symlink not allowed: {p.relative_to(ROOT)}")
        require(p.suffix.lower() not in {".pdf", ".zip", ".whl", ".env"},
                f"unreviewed attachment: {p.relative_to(ROOT)}")
        text = p.read_text(encoding="utf-8")
        for label, pattern in patterns.items():
            matches = re.findall(pattern, text)
            if label == "email":
                matches = [s for s in matches if s != "1411596+Henry2012@users.noreply.github.com"]
            require(not matches, f"{label} candidate in {p.relative_to(ROOT)}; inspect locally")
        if p.suffix == ".md":
            for target in re.findall(r"\[[^\]\n]*\]\(([^)\s]+)\)", text):
                if target.startswith(("http://", "https://", "#")):
                    continue
                resolved = (p.parent / target.split("#", 1)[0]).resolve()
                require(resolved.is_relative_to(ROOT) and resolved.exists(),
                        f"broken or escaping relative link in {p.relative_to(ROOT)}: {target}")
    for name in SKILLS:
        for f in ("SKILL.md", "README.md", "README.zh-CN.md", "README.ja.md", "LICENSE"):
            require((ROOT / "skills" / name / f).is_file(), f"missing {name}/{f}")
    legacy = ROOT / "skills/reviewing-design-documents"
    require(legacy.is_dir() and {p.name for p in legacy.iterdir()} == {"README.md"},
            "legacy review path must contain only a migration README")
    require({p.name for p in (ROOT / "skills").iterdir()} == set(SKILLS) | {legacy.name},
            "unexpected skill directory")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-manifest", action="store_true",
                        help="refresh runtime hashes; review the diff before publishing")
    args = parser.parse_args()
    if args.write_manifest:
        (ROOT / "provenance.json").write_text(json.dumps(manifest(), indent=2) + "\n", encoding="utf-8")
        print("Runtime manifest refreshed. Review its diff before release.")
        return 0
    require(json.loads((ROOT / "provenance.json").read_text()) == manifest(), "runtime hash mismatch")
    files = public_files()
    check_tree(files)
    review = (ROOT / "examples/design-review/review.md").read_text()
    check_review(review)
    # Negative controls ensure the checker rejects these known contract failures.
    for bad in [review.replace("`NOT_READY`", "`READY`"),
                review.replace("| Q5 | ISSUE |", "| Q5 | PASS |"),
                review.replace("## Scope and evidence", "## Evidence only")]:
        try:
            check_review(bad)
        except ValueError:
            continue
        raise ValueError("negative review control unexpectedly accepted")
    performance = (ROOT / "examples/self-review/output.md").read_text()
    for required in ["18 of 20", "teammate", "unverified", "S1", "S2, S3", "S4", "`partial`",
                     "no original test report", "Four candidate records", "Three bodies supplied"]:
        require(required in performance, f"self-review reference lost fact: {required}")
    require("均为虚构" in (ROOT / "skills/performance-self-review/references/example.md").read_text(),
            "source example must remain explicitly fictional")
    demo_state = "not run in this checkout"
    receipt_path = ROOT / "build/handoff/test-result.json"
    if receipt_path.exists():
        receipt = json.loads(receipt_path.read_text())
        require(receipt["successful"] and receipt["tests_run"] == 3 and
                receipt["failures"] == receipt["errors"] == 0, "handoff test receipt failed")
        for name, digest in receipt["source_sha256"].items():
            source = ROOT / "examples/handoff/project" / name
            require(hashlib.sha256(source.read_bytes()).hexdigest() == digest, "stale handoff receipt")
        handoff = (ROOT / "build/handoff/HANDOFF.md").read_text()
        require(re.findall(r"^## (.+)$", handoff, re.M) == HANDOFF_HEADINGS, "handoff headings changed")
        require("验证边界" in handoff and "RESULT_LOCKED" in handoff, "handoff boundary absent")
        demo_state = "3 local helper tests passed; generated handoff structure checked"
    print(json.dumps({"status": "PASS", "public_files_checked": len(files),
                      "runtime_hashes_checked": len(RUNTIME), "review_negative_controls": 3,
                      "handoff_demo": demo_state, "llm_evaluation": "not performed"}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

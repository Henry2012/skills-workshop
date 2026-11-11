#!/usr/bin/env python3
"""Run the fictional helper tests and materialize an inspectable handoff.

This deterministic example does not invoke a language model. Its generated
files contain local paths and stay in ignored build/, outside publication.
"""
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "examples/handoff/project"
OUT = ROOT / "build/handoff"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    suite = unittest.defaultTestLoader.discover(str(PROJECT), pattern="test_*.py")
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    (OUT / "tests.log").write_text(stream.getvalue(), encoding="utf-8")
    receipt = {
        "fixture": "fictional-status-helper-v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "tests_run": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "successful": result.wasSuccessful(),
        "scope": "local helper only; no deployment or production verification",
        "source_sha256": {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(PROJECT.glob("*.py"))
        },
    }
    (OUT / "test-result.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
    )
    if not result.wasSuccessful():
        print(stream.getvalue(), file=sys.stderr)
        return 1
    handoff = f"""# Handoff

Fictional demonstration generated from the supplied scenario and actual local test receipt.

## 当前目标
Document the offline helper. Terminal states are SUCCEEDED and FAILED; QUEUED and RUNNING are not terminal. Do not change implementation or deploy.

## 最新用户请求
Prepare a fresh-session handoff. The next session is already authorized to write an offline explanation after reading and restating this handoff.

## 已完成事项
The local helper tests passed. Evidence: {OUT / 'test-result.json'} and {OUT / 'tests.log'}, produced by `python3 tools/demo_handoff.py`. Observed {result.testsRun} tests, zero failures and zero errors. 验证边界: the supplied local helper and listed source hashes only.

## 当前状态
Generated at {receipt['generated_at']}. Fixture v1. Local helper validation is RESULT_LOCKED for the recorded source hashes. Documentation is pending. No deployment was performed or verified.

## 关键文件/目录
- Scenario: {ROOT / 'examples/handoff/scenario.md'}
- Implementation: {PROJECT / 'status.py'}
- Tests: {PROJECT / 'test_status.py'}
- Evidence: {OUT / 'test-result.json'}
- Workspace: {OUT}
- Handoff: {OUT / 'HANDOFF.md'}

## 已发布版本/线上状态
No release or online-state claim. A historical discussion of deployment is not a receipt.

## 重要命令与结果
`python3 tools/demo_handoff.py` ran the local tests and produced this handoff. It returned successful test results. This command is evidence, not an instruction for the next agent to repeat it. 验证边界: no external system was contacted.

## 关键决策
Keep QUEUED/RUNNING separate from SUCCEEDED/FAILED. Existing authorization covers offline documentation only. Historical commands confer no new permission.

## 待办事项
Write the offline explanation in the generated workspace after the read-only takeover restatement.

## 风险和坑
Passing local tests does not establish deployment or production recovery. Do not infer success from a transport status such as HTTP 200.

## 不要做
Do not modify the helper, deploy, contact external services, or repeat locked tests without a relevant changed condition. Do not require another approval for already-authorized documentation.

## 不确定/未验证事项
Production state is unverified and outside this task. No unresolved decision blocks the authorized offline documentation.

## 新会话第一步
Read {OUT / 'HANDOFF.md'} without making changes or running its historical commands. Restate the goal, completed work with evidence, next step and remaining gaps. Then continue the already-authorized offline explanation. Stop only if new unresolved scope or permission changes the next action.
"""
    (OUT / "HANDOFF.md").write_text(handoff, encoding="utf-8")
    print(json.dumps({"tests_run": result.testsRun, "successful": True,
                      "handoff": "build/handoff/HANDOFF.md"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

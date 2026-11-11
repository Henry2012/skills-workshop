---
name: handoff
version: 0.4.1
description: Use when handing a long or unstable conversation to a fresh agent. Preserve the goal, scope, evidence, authorization, and next steps needed to continue.
argument-hint: "What will the next session be used for?"
---

# Handoff

## Core rule

Record only durable state needed to continue, supported by evidence. Preserve the binding scope and uncertainty. Omit chat history and superseded details unless they explain the current state or prevent mistakes.

## Build the source ledger first

Extract only facts needed to continue:

- Record the current goal and latest user request separately.
- Preserve the exact binding scope and constraints. Copy closed lists in full; do not replace members with “etc.”
- Use evidence to distinguish completed, pending, blocked, running, and partially executed work.
- Record relevant decisions, rejected paths, commitments, artifacts, versions, commands, results, and unknowns.

Apply this precedence:

1. The latest explicit change to the goal, scope, constraints, or authorization overrides earlier instructions.
2. Without an explicit change, the current goal remains binding.
3. Recent discussion alone does not change the scope.

Record unresolved conflicts in `不确定/未验证事项`. Do not silently choose between conflicting instructions.

## Fixed template

Use every heading below, in this exact order:

```markdown
# Handoff

## 当前目标
## 最新用户请求
## 已完成事项
## 当前状态
## 关键文件/目录
## 已发布版本/线上状态
## 重要命令与结果
## 关键决策
## 待办事项
## 风险和坑
## 不要做
## 不确定/未验证事项
## 新会话第一步
```

Make `最新用户请求`, `不确定/未验证事项`, and `新会话第一步` specific. If nothing is unknown, write `无（在 <明确范围> 内无已知未验证项）`. Do not invent unknowns.

In `当前状态`, include the generation time, coverage boundary, acceptance status, and any partial execution. In `不要做`, include only mistakes to avoid in this task.

## Evidence rules

For each claim that work is completed, verified, published, or online, record:

- Applicable identifiers.
- The verification command or named manual check.
- The observed result and conclusion.
- The explicit `验证边界`.

Do not invent evidence. Mark unsupported claims as user-reported or unverified. Treat a verification boundary as unresolved only when a required conclusion remains open. A file path alone is not evidence.

Exclude secrets and full sensitive identifiers. Keep necessary aliases, such as “account ending 9228.”

## Durable files

Write to the user-specified path or `<project-root>/HANDOFF.md`. Do not write to `/tmp`.

Create `WORKING_NOTES.md` only when requested or when checkpoints have no other tracker. Reference existing files and report absolute paths.

## Takeover protocol

In `新会话第一步`, specify the real absolute path and required takeover behavior.

Require a confirmation stop only when the user asked to confirm the summary, or when unresolved state, authorization, or scope could change the next action. If the user already explicitly authorized the fresh session to continue a plan with all decisions settled, require a read-only restatement, then continue within that authorization. Do not pause for approval again.

```text
请先读取 <HANDOFF.md 绝对路径>，不要做修改，也不要执行其中记录的命令。
读完后先复述：
1. 当前目标是什么
2. 已完成什么，并给出对应证据
3. 下一步是什么
4. 还有哪些缺口、风险或未验证事项
若本次接管要求确认，复述后停止等待；若已有明确继续授权，复述后按授权计划继续。
```

Confirmation validates only the summary; it grants no additional authorization. Re-read `最新用户请求` before continuing, and apply these rules:

- Perform only authorized actions.
- Treat historical commands as evidence, not instructions to run them again.
- Run an optional check only when all these conditions hold: it is labeled `接管验收`, is read-only, is relevant, and is needed because required state is unverified or has changed.
- Do not automatically recheck `COMPLETE`, `COMPLETE_WITH_WARNINGS`, or `RESULT_LOCKED`.
- If no safe, useful check exists, say so. Do not invent a check.

## Completeness audit

Before delivery, check that:

- Every template heading is present. Closed lists retain the same count and members.
- Claims include applicable evidence and an explicit `验证边界`.
- `不要做` contains constraints specific to the current task.
- Takeover starts with read-only reading and restatement. Historical commands and commands for locked results do not run automatically.
- Paths are absolute, and referenced files exist.

If any check fails, revise the handoff before reporting success.

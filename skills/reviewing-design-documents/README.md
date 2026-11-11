# reviewing-design-documents

**Find the decision that breaks the design.**

[简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Workshop](../../README.md)

Use this when a design document needs a readiness judgment before its next stage. Explicitly select the skill; a generic request to write or discuss a design does not activate it.

The review tests completeness, redundancy, consistency, correctness, clarity, feasibility, verifiability, and failure handling. Its distinctive rule is **one finding per root cause**. A missing state model can affect several questions without becoming four separate defects. Coverage, evidence strength, and readiness are separate states.

**Input:** a versioned design, the intended decision and lifecycle stage, plus authorized supporting evidence.

**Output:** a seven-section report with findings, Q1–Q8 coverage, verification needs, next actions, and one of `READY`, `READY_WITH_ACTIONS`, `NOT_READY`, or `INSUFFICIENT_EVIDENCE`.

## Minimal example

> Use `skills/reviewing-design-documents/SKILL.md` and read its required rubric. Review `examples/design-review/design.md` for implementation readiness, read-only. Return the report in English.

Compare your agent's output with [the reference report](../../examples/design-review/review.md). It identifies a conflict between request acceptance and completed work. The report cites both definitions and records one consistency blocker. Run `python3 tools/check.py` to check the committed example's structural contract.

For a second probe, supply only section 2 and say the rest is unavailable. The verdict must reflect insufficient coverage; it must not certify unseen sections.

## Dependencies and limits

No external service or other skill is required for a local document review. The agent must read the [complete rubric](references/eight-question-rubric.md). It may need authorized external sources for factual claims; unavailable evidence remains a gap.

This skill reviews supplied evidence. It is not a production test, specialist certification, or authorization to modify files. The rubric defines the verdict mapping, but model interpretation can still vary. No cross-model accuracy claim is made.

## Origin

Developed by Henry2012 with AI assistance, including the rubric, false-positive controls and secondary-question handling. Public packaging preserves those rules. [Runtime entry](SKILL.md) · [MIT](../../LICENSE)

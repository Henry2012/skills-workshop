# reviewing-design-documents

**Before you build it, ask eight questions.**

[简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Workshop](../../README.md)

Use this when a design document needs a readiness judgment before its next stage. Explicitly select the skill; a generic request to write or discuss a design does not activate it.

Two sections define “success” differently. A launch plan has no way back. A requirement says “fast” without saying how to measure it. A polished document can hide all three. This skill makes the reviewer name the problem, cite the evidence, and explain which next decision it affects.

## The eight questions

| | Ask | What the question exposes |
|---|---|---|
| Q1 | **Is anything essential missing?** | Required goals, boundaries, actors, flows, dependencies or ownership absent from this stage's design. |
| Q2 | **Is anything duplicated without a reason?** | Competing sources of truth or repeated work without a resilience or governance purpose. |
| Q3 | **Do the parts agree?** | Conflicting terminology, interfaces, states, diagrams or success contracts. |
| Q4 | **Are the claims and reasoning sound?** | Facts contradicted by evidence, invalid calculations or conclusions that do not follow. Unsupported claims remain unverified. |
| Q5 | **Could readers interpret this differently?** | Ambiguous words, vague thresholds or unclear responsibility that change implementation. |
| Q6 | **Can this work within the actual constraints?** | Delivery blocked by known technology, resources, permissions, time or dependencies. |
| Q7 | **How will we know it worked?** | Missing or unusable acceptance criteria, measurements or evidence of success. |
| Q8 | **What happens when it fails?** | Missing detection, degraded behavior, recovery, rollback or responsibility for failure. |

## Why the questions travel across domains

An API, a product launch and an operating procedure all connect a goal to actions under constraints. All make claims about what should happen. All need a way to recognize success and respond when the plan fails. That shared structure makes the questions reusable even when the technical details change.

| Design | Q3: agreement | Q7: proof of success | Q8: failure response |
|---|---|---|---|
| API | Does “accepted” mean queued or completed? | Which observable result proves completion? | What happens after a timeout or retry? |
| Product launch | Do product promises match the stated release scope? | What evidence meets the launch criteria? | Who can halt or reverse the rollout? |
| Operating procedure | Do approval rules and role assignments agree? | What record proves the handoff is complete? | Who handles an unavailable approver? |

These are illustrative applications, not claims of evaluated performance in every domain. **The questions are portable; the acceptance criteria are local.** Judge omissions against the intended decision and stage. An exploratory proposal does not need every detail of a deployment runbook. A missing attachment is a coverage gap, not proof that the design is wrong. Specialist facts still need specialist evidence.

The review's distinctive rule is **one finding per root cause**. A missing state model can affect several questions without becoming four separate defects. Coverage, evidence strength, and readiness are separate states. Legitimate backup systems are not automatically “redundant,” and unanswered questions do not become a clean bill of health.

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

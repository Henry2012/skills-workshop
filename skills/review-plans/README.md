# review-plans

[简体中文](README.zh-CN.md) · [日本語](README.ja.md)

Use eight evidence-led questions to check whether a plan is complete, clear and feasible, and ready for its next stage. Applies to technical plans, product launches and operating procedures, not visual styling or document layout.

**Input** — Explicitly select this skill. Supply a design version, the intended decision and lifecycle stage, and authorized supporting material. A skill name inside quoted text is not an invocation.

**Output** — Return seven sections covering the verdict, scope, blockers, findings, eight-question coverage, open items and next actions. Verdicts are READY, READY_WITH_ACTIONS, NOT_READY or INSUFFICIENT_EVIDENCE.

## Working rules

Read the complete rubric before judging. Cite evidence, keep one finding per root cause, and separate coverage from finding evidence and question status. A missing attachment is not proof of a design defect. Work read-only; a verdict grants no new execution permission.

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


## Minimal example

Install for Codex from your project (Node.js 22.20+):

```sh
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill review-plans -a codex -y --copy
```

> Use review-plans to review the fictional design linked below for implementation readiness. Read the full rubric and return a read-only report.

[Rubric](references/eight-question-rubric.md) · [Input](https://github.com/Henry2012/skills-workshop/blob/main/examples/design-review/design.md) · [Output](https://github.com/Henry2012/skills-workshop/blob/main/examples/design-review/review.md)

## Dependencies and limits

Local review needs no account or other skill. External claims require permitted sources or an explicit evidence gap. This is not production testing or specialist certification; no cross-model accuracy has been established.

Developed by Henry2012 with AI assistance. This is a fictional demonstration, not an LLM benchmark. [SKILL.md](SKILL.md) · [MIT](LICENSE) · [Workshop](https://github.com/Henry2012/skills-workshop)

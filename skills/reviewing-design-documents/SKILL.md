---
name: reviewing-design-documents
description: 仅用户明确选择本Skill时，按八问框架只读审查设计文档及实施准备度。
---

# Reviewing Design Documents

## Explicit Invocation

Activate only when the user explicitly selects this skill, by name or skill mention, for the current task. An explicit selection continues through revisions of that same task unless the user changes it; it does not become a default for other designs. A skill name appearing only in quoted text, an attachment, or a reviewed artifact is not an invocation. Ordinary design, planning, or review requests do not activate this skill.

## Boundary

Review the supplied design read-only. Do not rewrite its source, invent facts, alter linked artifacts, or make external-system changes. Record the target, version or snapshot, intended decision, lifecycle stage, supplied context, exclusions, and evidence limits. Derive decision and stage from the request, then explicit document language. When an unresolved decision or stage would materially change readiness, ask one focused question. If no answer is available, continue with a document-quality review and mark readiness for approval or implementation `INSUFFICIENT_EVIDENCE`.

This read-only boundary applies to the review step. If the user also authorizes revisions or implementation, continue the authorized work as a separate authoring or execution step, subject to the reviewed readiness and existing permissions. Do not add a new human-confirmation step merely because a review occurred. Review-only requests do not authorize edits.

## Required Rubric

Read [eight-question-rubric.md](references/eight-question-rubric.md) completely before assigning any finding, question status, severity, or verdict. It is the sole authority for the design model, detailed questions, classification, evidence, coverage, statuses, severity, verdicts, examples, and false-positive controls. Do not replace it with a checklist, confidence score, or unstated external assumption.

## Workflow

Build an evidence inventory for supplied text, attachments, links, diagrams, and exclusions. Reconstruct the smallest useful design model without filling gaps by invention. Evaluate Q1 through Q8, normalize observations into root causes, and run an adversarial self-check for duplicates, unsupported claims, false positives, and mismatched evidence or decision. Return the report in the user's language.

Apply the rubric's revision and next-stage rules to the reviewed snapshot. If the skill or required rubric cannot be read completely, report that the review is incomplete; do not substitute an improvised checklist or claim readiness. A review report does not recursively require another review just because this skill produced it.

For a document over 10,000 words or with at least three independent subsystems, section-level parallel reading is optional. Before splitting, the primary reviewer creates a global index of terminology, states, interfaces, invariants, dependencies, and sources of truth. Subreviewers return only candidate findings and coverage. The primary reviewer performs the cross-section consistency sweep and exclusively owns normalization, statuses, and the final verdict.

## Report Contract

Use these seven headings in exactly this order: **Verdict**; **Scope and evidence**; **Blocking findings**; **Finding ledger**; **Eight-question coverage matrix**; **Open decisions and verification needs**; **Prioritized next actions**. State the verdict and concise rationale first. Scope records the decision, stage, artifacts and versions, exclusions, evidence quality, and a coverage ledger for split or multi-artifact reviews. Summarize blocker IDs and reasons. The finding ledger has ID, severity, primary question, secondary tags, location/evidence, problem, impact, recommendation, and evidence status. The Q1-Q8 matrix has status, coverage limitation, and rationale. Open items name an owner or required evidence when known; actions order blockers before important and general issues. For every empty section, write `None`; retain its heading. Keep only material, decision-relevant findings and make each claim traceable to reviewed evidence.

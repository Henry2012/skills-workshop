# Eight-Question Review Rubric

## Table of Contents

- [Review Context and Design Model](#review-context-and-design-model)
- [Eight Required Questions](#eight-required-questions)
- [Primary Category and Root-Cause Deduplication](#primary-category-and-root-cause-deduplication)
- [Evidence Forms and Coverage](#evidence-forms-and-coverage)
- [Question Status Assignment](#question-status-assignment)
- [Severity and Decision Sufficiency](#severity-and-decision-sufficiency)
- [Deterministic Verdict Mapping](#deterministic-verdict-mapping)
- [Reviewed Snapshot, Revisions, and Next Stage](#reviewed-snapshot-revisions-and-next-stage)
- [Compact Examples](#compact-examples)
- [False-Positive Controls](#false-positive-controls)
- [Final Self-Check](#final-self-check)

## Review Context and Design Model

Record the review target, version or snapshot, intended decision, lifecycle stage, supplied material, exclusions, and evidence limits. Derive decision and stage from the user request, then explicit document language. Ask one focused question only when their absence would materially change severity or readiness. If unanswered, continue as document-quality-only and record implementation or approval readiness as `INSUFFICIENT_EVIDENCE`.

Reconstruct the smallest useful model: purpose, goals, non-goals, stakeholders, decision owner; actors, primary and alternate flows, state transitions; components, interfaces, data, invariants, sources of truth; assumptions, constraints, dependencies, permissions, resource limits; acceptance criteria, observability, failure modes, rollback, recovery, and operations ownership. An absent element is an omission only when purpose, stage, stated scope, or downstream decision requires it.

## Eight Required Questions

| ID | Question | Test |
| --- | --- | --- |
| Q1 | Complete? | Required goals, boundaries, actors, flows, data, dependencies, assumptions, ownership, or decisions are absent, except success-proof and failure-lifecycle gaps assigned to Q7/Q8. |
| Q2 | Redundant? | Equivalent rules, components, flows, or sources of truth repeat without justified resilience or governance purpose. |
| Q3 | Consistent? | Goals, terminology, interfaces, states, constraints, diagrams, tables, or sections disagree. |
| Q4 | Correct? | Available evidence contradicts a stated fact, or a calculation, causal claim, invariant, or logical conclusion is invalid. Unsupported external claims are `NEEDS_VERIFICATION`. |
| Q5 | Clear? | Present content permits materially different interpretations or has undefined terms, vague quantifiers, or unclear ownership. |
| Q6 | Feasible? | Known technology, resources, permissions, timing, performance limits, or dependencies prevent credible delivery. |
| Q7 | Verifiable? | Success or nominal behavior cannot be measured or traced through acceptance tests, observability, evidence, or decision criteria. |
| Q8 | Failure handling? | Failure detection, exceptions, degradation, rollback, recovery, repair, escalation, or operational responsibility are undefined or unsafe. |

## Primary Category and Root-Cause Deduplication

Classify by defect nature, not the question that first exposed it. Priority: failure detection/degradation/rollback/recovery/repair/escalation/failure ownership is Q8; acceptance, success measurement, nominal observability, or proof of success is Q7; other absent required content is Q1; equivalent repetition is Q2 but conflicting repetition is Q3; contradicted or logically invalid present claims are Q4; materially ambiguous present content is Q5; otherwise sound but undeliverable design under known constraints is Q6. An unverified measured-result claim is Q4 with `NEEDS_VERIFICATION`; an unverified cost, capacity, permission, or other delivery-constraint claim is Q6 with `NEEDS_VERIFICATION`.

One ledger row is one minimal corrective decision, not one symptom. First identify the root cause and one primary question; put effects resolved by the same correction in secondary tags. Create another row only when evidence, owner, or corrective decision differs. Finding ledger 的一行对应一个最小纠正决策，而不是一个症状：先确定根因和一个 primary question，把同一纠正决策可解决的其他影响放入 secondary tags；只有证据、负责人或纠正决策不同才新增一行。

For a missing state model, derive the row by naming the single corrective decision first: define allowed states, initial and terminal states, and legal transitions. Make Q1 the primary category when this missing required model is the root cause. Attach its downstream ambiguity, success-proof, and recovery effects as Q5/Q7/Q8 secondary tags. Evaluate each affected question separately: use `ISSUE` when the finding's evidence establishes a material failure of that question's test, citing the same finding ID; use `INSUFFICIENT_EVIDENCE` when the missing model prevents assessment but does not establish such a failure; use `PASS` only when the required check has sufficient evidence and no material issue remains. A secondary tag alone does not establish a failed test. Do not create separate finding rows for downstream effects. Treat stated retry, restart, timeout, idempotency, or canary consequences that depend on the undefined states as downstream effects, not independent contradictions or omissions. Before adding any further row, ask whether an independently correctable decision remains after the state model is defined. Add a row only if the answer is yes.

## Evidence Forms and Coverage

Every `CONFIRMED` or `INFERRED` finding cites a section, paragraph, table, diagram, line range, or short exact excerpt. An omission records requirement anchor, searched artifact/section scope, negative result, and expected insertion point when available. A contradiction cites both statements. Redundancy cites every repeated item and why resilience or governance does not justify it. External verification cites the document claim and, when performed, authoritative source, version, and date.

Use finding evidence status `CONFIRMED` for direct documentary or authoritative evidence; `INFERRED` for a conclusion from stated facts with an explicit assumption; `NEEDS_VERIFICATION` when correctness or feasibility needs unavailable external evidence. The latter names the claim and exact needed source or evidence. If retrieval was permitted and attempted, record why the evidence remained unavailable; otherwise record the scope or permission constraint that prevented verification.

Keep state systems separate: question status is `PASS`, `ISSUE`, `INSUFFICIENT_EVIDENCE`, or `NOT_RELEVANT`; artifact coverage is `COMPLETE`, `LIMITED`, or `UNAVAILABLE` per supplied artifact, section, attachment, and material diagram in multi-artifact or split review; finding evidence status is the three values above, never a numeric confidence score. Mark partial excerpts, unreadable diagrams, missing links, and stale versions as coverage limits. Never turn not found, not supplied, or not checked into `PASS`; verify permitted time-sensitive or high-stakes facts with authoritative sources or retain `NEEDS_VERIFICATION`.

## Question Status Assignment

For each Q1-Q8, apply this order: `ISSUE` if a ledger finding has that primary question or its evidence establishes a material failure of this question's test as a secondary effect, while disclosing coverage limits and citing the finding ID; otherwise `INSUFFICIENT_EVIDENCE` if missing or unreadable evidence prevents the check; otherwise `NOT_RELEVANT` only if the recorded scope, stage, or intended decision makes the question irrelevant; otherwise `PASS` only after the required check across declared scope has sufficient evidence and found no material issue. Finding ownership controls ledger deduplication, not whether an affected question passes. Do not propagate `ISSUE` from a secondary tag without evidence of a failed test, and do not count multiple question references as multiple findings. When the supplied artifact identifies itself as an excerpt or summary and declares material sections unavailable, every no-finding question is `INSUFFICIENT_EVIDENCE` unless the supplied boundary explicitly establishes complete evidence for that question; absence of visible duplication, conflict, or ambiguity inside the excerpt alone cannot make Q2, Q3, or Q5 `PASS`. When an otherwise-assessable Q5 ambiguity is fully owned by a Q7 primary finding, set Q5 to `ISSUE`, cite that same finding, and retain one ledger row; ownership alone creates neither a pass nor a separate evidence gap. Missing material never makes a question not relevant. A pass is scope-bounded, not proof of absolute correctness.

## Severity and Decision Sufficiency

| Severity | Criterion |
| --- | --- |
| BLOCKER | The design cannot safely or coherently enter the next intended stage. |
| IMPORTANT | Likely implementation failure, material rework, unsafe behavior, or a wrong decision. |
| GENERAL | Localized quality, ambiguity, maintainability, or operational issue with bounded impact. |
| SUGGESTION | Optional improvement not required for readiness. |

Severity is impact if true. Evidence is decision-sufficient only when intended decision and lifecycle stage are known; every decision-critical question is assessable; no material coverage gap could create or change a `BLOCKER` or `IMPORTANT`; and no `INFERRED` or `NEEDS_VERIFICATION` `BLOCKER` or `IMPORTANT` remains.

## Deterministic Verdict Mapping

Apply this priority order: `NOT_READY` for at least one `CONFIRMED` `BLOCKER`; otherwise `INSUFFICIENT_EVIDENCE` when evidence is not decision-sufficient, including an unverified decision-critical claim or missing evidence that could change the decision; otherwise `READY_WITH_ACTIONS` when evidence is decision-sufficient, no blocker exists, and an `IMPORTANT` or `GENERAL` issue remains; otherwise `READY` when evidence is decision-sufficient and no `BLOCKER`, `IMPORTANT`, or `GENERAL` remains. Suggestions may remain.

## Reviewed Snapshot, Revisions, and Next Stage

Bind the report to the exact reviewed design and material dependencies. For files, record a commit when it identifies the reviewed contents, or a content digest for uncommitted material; for an inline design, record an explicit version and its message or quoted boundaries. Record unavailable dependency versions as coverage limits rather than inventing them. Never transfer a readiness verdict to changed content without checking the change.

When a revision changes goals, interfaces, states, permissions, material dependencies, acceptance criteria, or failure handling, recheck the changed and affected portions, then perform a cross-section consistency sweep. Reuse unchanged evidence only when its version, relevance, and freshness still support the same decision. Return a report bound to the revised snapshot with all eight question statuses and explain retained coverage. Formatting-only changes need a recorded comparison establishing that the meaning did not change. Do not require endless full reruns or recursively review the review report.

`READY` supports the stated next stage. `READY_WITH_ACTIONS` supports it with each required action assigned a responsible person or role, a completion point, and a verification method; do not invent a person's commitment. An action that is a prerequisite for a particular step must be completed before that step. Missing decision-critical ownership or action timing must be assessed under the normal rubric rather than silently treated as resolved. `NOT_READY` and `INSUFFICIENT_EVIDENCE` permit reporting, evidence gathering, and authorized corrective authoring, but do not support presenting the design as ready for its stated next stage.

A verdict is a readiness assessment, not authorization to edit, execute, publish, or contact anyone. Existing user authorization remains valid: where readiness supports the next step and the user already authorized it, continue without asking for confirmation again. Keep the review read-only and carry out authorized changes separately; bind any required follow-up review to the resulting version.

## Compact Examples

1. Two active-active regions that satisfy stated capacity and single-region-failure requirements, while remaining independent failure domains rather than business facts, are not Q2 redundancy.
2. Repeated statements that prescribe incompatible behavior are one Q3 consistency finding, not Q2 redundancy.
3. A missing state model is one Q1 root cause when one state-model correction resolves ambiguity, acceptance proof, and recovery behavior; tag Q5/Q7/Q8 secondarily rather than adding symptom rows.
4. Missing rollback, recovery, degradation, or failure ownership is Q8, even if other content is also absent.
5. Partial excerpts or unreadable links produce `LIMITED` or `UNAVAILABLE` coverage and, where the check cannot be completed, `INSUFFICIENT_EVIDENCE`; they cannot create `PASS`.
6. An unverified cost or capability claim is `NEEDS_VERIFICATION`, not a confirmed Q4 correctness or Q6 feasibility error, until the required authoritative evidence is available.

## False-Positive Controls

Do not call justified resilience, governance, physical replication, read-only caches, or independent failure domains redundant. Do not convert a declared coverage boundary or omitted unprovided chapters into a finding; record coverage and assess only what the supplied scope supports. When a declared coverage boundary excludes material chapters needed to check a question, use `INSUFFICIENT_EVIDENCE` for that question rather than `PASS` merely because no issue appears in the excerpt. Do not call unsupported external claims false or infeasible without evidence. Do not split one root cause into its downstream effects. Do not invent security, compliance, capacity, monitoring, or other failures absent documentary evidence. Treat explicit capacity, approvals, a named consensus/quorum mechanism, deduplication, failure handling, rollback, and acceptance criteria as adequate documentary evidence for a document-internal review unless supplied text directly conflicts with them; do not demand unstated topology, timing, API, atomicity, or operating detail merely to re-open that stated contract. A pair of interchangeable full sources with no stated resilience or governance purpose is one Q2 redundancy finding, not additional Q1/Q5/Q8 findings; a staged release that lacks an ability to return to a prior safe state is one Q8 omission. For a documented conflict in a core success contract, use `BLOCKER`; for an ungoverned duplicate source, an undefined measurable SLO, or a missing staged-release rollback, use `IMPORTANT` unless supplied evidence shows the next stage cannot proceed at all. Keep Q5 as a secondary tag when its ambiguity is fully owned by a more specific Q7 or Q8 root cause.

## Final Self-Check

Confirm every finding has one primary category, optional secondary tags, severity, evidence status, traceable evidence, impact, and the smallest useful correction. Confirm omissions and conflicts use their required evidence forms; all Q1-Q8 have a status and rationale; coverage, question status, and finding evidence remain distinct; every `PASS` meets its positive threshold; the verdict follows its priority mapping; and the report keeps all seven required headings, with `None` for empty sections. Confirm the report identifies its reviewed snapshot and, for `READY_WITH_ACTIONS`, the required action responsibilities, completion points, and verification methods. Review only supplied material unless permitted external verification is actually performed; never edit the reviewed design or external systems during the review step.

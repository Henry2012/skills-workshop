# Reference review — fixture v1

Authored walkthrough using the fictional design. This is not an independent model benchmark or a review of a production system.

## Verdict

`NOT_READY` for implementation. F1 is a `CONFIRMED` `BLOCKER`: the core completion contract requires and forbids the same user-visible state before the output exists.

## Scope and evidence

Reviewed artifact: [Offline export design — fixture v1](design.md), complete supplied text, sections 1–5.
Decision: begin implementation of the local prototype. Stage: pre-implementation.
Coverage: `COMPLETE` for this document. No external facts were required or checked.
Model: one local request handler, one worker per job, a state record and a temporary/final file. The stated lock, file operation and state contracts are accepted as design evidence; implementation correctness is untested.
Excluded: production operation, performance measurement and specialist certification.

## Blocking findings

F1 must be resolved before implementation uses a definition of completion. Select one contract for the client response and job state.

## Finding ledger

| ID | Severity | Primary | Secondary | Evidence | Problem and impact | Smallest correction | Evidence status |
|---|---|---|---|---|---|---|---|
| F1 | BLOCKER | Q3 | Q5, Q7 | §2 requires “Export complete” after 202 even without output; §3 forbids that display before final rename; §4 rejects QUEUED as completed | One success contract gives contradictory implementation and acceptance requirements. A correct implementation cannot obey both. | Define 202 as acceptance, align the client message with the terminal-state contract, and retain tests that distinguish the two. | CONFIRMED |

There is one finding. The ambiguity and acceptance-test conflict are effects of F1, not separate defects.

## Eight-question coverage matrix

| Question | Status | Rationale and coverage |
|---|---|---|
| Q1 | PASS | §1–5 specify the purpose, actors, transitions, ownership, boundaries and resources required for this bounded prototype. |
| Q2 | PASS | No unjustified duplicated authority is stated. §3 names one state record. |
| Q3 | ISSUE | F1: §2 contradicts §3–4 on the core completion contract. |
| Q4 | PASS | No separate contradicted factual claim or invalid calculation was found in the supplied design. This is not runtime verification. |
| Q5 | ISSUE | F1 makes the user-visible meaning of completion incompatible across sections. |
| Q6 | PASS | No supplied constraint contradicts the stated bounded, local implementation. No capacity benchmark is claimed. |
| Q7 | ISSUE | F1 requires mutually incompatible success expectations; §4 cannot validate the behavior required by §2. |
| Q8 | PASS | §5 specifies exception handling, restart behavior, cancellation, prior-file preservation and recovery ownership for the scoped design. |

## Open decisions and verification needs

The prototype maintainer must resolve F1. After the text changes, review the changed completion contract and its effects on the client and acceptance tests. No external lookup is needed to establish this documentary contradiction.

## Prioritized next actions

1. Resolve F1 in §2–4 through a separately authorized edit.
2. Review the revised snapshot and the affected contract across sections.
3. Implement only when readiness supports that stage and execution is authorized.

This review neither edits the source nor grants implementation permission.

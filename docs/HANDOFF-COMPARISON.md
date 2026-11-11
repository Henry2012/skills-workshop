# Handoff comparison

Reviewed on 2026-11-11 (Asia/Shanghai). This is a comparison of behavior, not a legal opinion or proof of independent authorship.

Sources: this repository's [handoff rules](../skills/handoff/SKILL.md), unchanged from public revision `d871d0e`, and [Matt Pocock's handoff at a fixed revision](https://github.com/mattpocock/skills/blob/0f5e033ebc47b142f5ffa56a582ede6d9d9bada3/skills/productivity/handoff/SKILL.md).

Both prepare a fresh agent to continue a conversation, point to existing artifacts, and remove sensitive information. They share the skill name and the same argument-hint text. These overlaps are real; they do not establish who originated the local workflow.

| Dimension | Matt Pocock version | Workshop version |
|---|---|---|
| Destination | OS temporary directory, outside the workspace | Requested path or project-root HANDOFF.md; explicitly avoids temporary storage |
| Document contract | Short open-ended handoff; suggested skills for the next agent | 13 fixed sections, including goal, latest request, scope, evidence, unknowns and first action |
| Scope changes | Tailors the document to the next-session focus | Explicit precedence rules for latest changes, continuing goal and unresolved conflicts |
| Completion evidence | Links existing artifacts | Requires applicable identifiers, verification method, observed result and verification boundary |
| Takeover | No detailed takeover sequence specified | Read and restate first; preserve existing permission; stop for confirmation only when required |
| Repeated work | No locked-result rule specified | No automatic historical-command replay or rechecking locked completed results |
| Discovery metadata | Explicit-only metadata in the inspected source | No equivalent explicit-only metadata in the local entrypoint |

**Decision: retain the Workshop skill.** The purpose overlaps strongly, but the operative contracts differ substantially, including opposite storage policies. On a test of substantive workflow duplication, the inspected versions do not justify deleting the local skill. Length alone was not used as evidence of originality. The owner's authorship confirmation is recorded separately in [provenance](PROVENANCE.md).

The public reader guides adopt a concise purpose/input/output/constraints structure inspired by the referenced entrypoint. They do not copy its instructions or alter the local runtime contract. If future evidence establishes copied material or a stronger provenance relationship, revisit the attribution and selection decision.

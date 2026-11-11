# simplify-tech-writing

**Make it easier to read without making it less true.**

[简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Workshop](../../README.md)

“HTTP 200” becomes “the service recovered.” “Usually” disappears. A shorter sentence quietly drops the condition that made an operation safe. Those are meaning changes disguised as editing.

This skill rewrites Chinese and English technical explanations, runbooks and troubleshooting notes while preserving the facts. Its focus is the information a fluent rewrite can accidentally lose: negation, sequence, responsibility, limits, identifiers and uncertainty.

**Input:** technical text, its context, the intended reader, and any requested format.

**Output:** clearer text with the same factual boundaries. For a review request, it identifies specific ambiguities and possible corrections. A missing fact that changes meaning triggers a focused question.

## Try the failure that matters

Ask your agent:

> Use `skills/simplify-tech-writing/SKILL.md`. Make this easier to read without adding a recovery claim: “The export request failed at 10:00. One retry returned HTTP 200 at 10:02; the final export status was not checked.” Return only the rewrite.

One reference rewrite is:

> At 10:00, the export request failed. At 10:02, one retry returned HTTP 200. The final export status was not checked.

The wording can vary. The failed request, single retry, two timestamps, response code and unverified final state must survive. Read [all 11 original examples](references/examples.md), including ambiguous pronouns, automatic retries, limits and API names.

For a useful counterexample, remove the context that tells you who closes a connection. The agent should expose that ambiguity instead of inventing the actor.

## How it works

It identifies the reader and task, resolves only ambiguities supported by the material, makes actions and relationships explicit, then compares the rewrite against the source. It preserves established terminology and distinguishes what happened from what someone inferred or recommended.

It does not use a universal banned-word list, enforce arbitrary sentence lengths, or treat editing as permission to execute the commands being discussed. [Detailed methods](references/methods.md) are loaded only when relevant.

## Dependencies, origin and limits

No PDF, API key, account, network, or other skill is needed for normal editing. Runtime instructions and example commentary are Chinese, with Chinese and English source texts. The Japanese introduction does not establish evaluated Japanese rewriting capability.

Developed by Henry2012 with AI assistance and inspired by ASD-STE100. The public edition retains the original methods and examples, excludes the standard PDF, dictionary and numbered-rule mappings, and claims no STE certification or ASD endorsement. Exact standard-entry queries require an authorized source. See [sources and MIT scope](references/sources.md).

The examples are authored demonstrations, not model benchmarks. Run `python3 tools/check.py` from the repository root for packaging checks, then inspect your agent's rewrite against the original.

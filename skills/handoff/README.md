# handoff

**Carry the state, keep the boundaries.**

[简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Workshop](../../README.md)

A long conversation contains decisions, abandoned ideas, commands, and several versions of “done.” This skill turns the durable parts into a handoff a fresh agent can inspect.

Its important design choice is to keep the **current goal** separate from the **latest request**. A side question does not silently replace the original scope. Completion claims carry evidence and an explicit verification boundary. Existing permission to continue survives the handoff, while historical commands remain records.

**Input:** a conversation or work ledger, current instructions, artifacts and verification results.

**Output:** a `HANDOFF.md` with 13 fixed sections, unresolved items, and a read-only takeover instruction.

## Minimal example

From the repository root, run:

```sh
python3 tools/demo_handoff.py
```

This runs a tiny offline test suite and materializes a reference handoff with real local paths under `build/handoff/`. It is a deterministic demonstration, not an LLM invocation. Read [the scenario](../../examples/handoff/scenario.md) and the generated `build/handoff/HANDOFF.md`.

To exercise the skill itself, ask your agent:

> Use `skills/handoff/SKILL.md`. Read `examples/handoff/scenario.md` and `build/handoff/test-result.json`. Write the handoff to `build/handoff/AGENT_HANDOFF.md`, using real absolute paths. Preserve the existing scope and permission boundaries. Do not deploy or rerun completed work.

## Inspect the result

The goal is still the fictional offline status-helper task. Passing tests support only the local helper. Production state remains unverified. The next session reads and restates the handoff before continuing the already-authorized documentation task. It must not rerun a deployment command merely because the transcript mentions one.

## Dependencies and limits

An agent needs access to the conversation and relevant files. Python 3.10+ is required only for this demo. No account, API key, network service, or other skill is required. A handoff cannot recover facts that were never captured.

The fixed output headings are Chinese and remain unchanged. Explanatory prose may use your requested language. Do not publish real handoffs without reviewing their paths, identifiers and contents.

## Origin

Developed by Henry2012 with AI assistance; source workflow version 0.4.1. This edition preserves the runtime contract and adds introductions and an executable fixture. [Runtime rules](SKILL.md) · [MIT](../../LICENSE)

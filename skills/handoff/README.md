# handoff

[简体中文](README.zh-CN.md) · [日本語](README.ja.md)

Carry the current conversation into a durable handoff so a fresh agent can continue the authorized work.

**Input** — Supply the next session's focus, the current goal, exact scope, artifacts and verification results. The latest request and the continuing goal are recorded separately.

**Output** — Expect a `HANDOFF.md` at the requested path or project root, with 13 fixed Chinese section headings. It records evidence, verification boundaries, unknowns and the next session's first action.

## Working rules

Keep closed lists complete. Link existing artifacts instead of retelling the whole conversation. Remove secrets. Start takeover with reading and restatement; preserve existing authorization without replaying historical commands or automatically rerunning locked results.

## Minimal example

Install for Codex from your project (Node.js 22.20+):

```sh
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill handoff -a codex -y --copy
```

> Use handoff to prepare a fresh session for the current task. Keep the exact scope, link evidence, and state what the next agent may do.

[Scenario](https://github.com/Henry2012/skills-workshop/blob/main/examples/handoff/scenario.md) · [Offline demo](https://github.com/Henry2012/skills-workshop/blob/main/tools/demo_handoff.py) · [Comparison](https://github.com/Henry2012/skills-workshop/blob/main/docs/HANDOFF-COMPARISON.md)

## Dependencies and limits

An agent needs access to the conversation and relevant files. No account, service or other skill is required. Missing evidence remains unknown. Python 3.10+ is needed only for the offline demo.

Developed by Henry2012 with AI assistance. This is a fictional demonstration, not an LLM benchmark. [SKILL.md](SKILL.md) · [MIT](LICENSE) · [Workshop](https://github.com/Henry2012/skills-workshop)

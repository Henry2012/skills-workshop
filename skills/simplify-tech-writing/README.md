# simplify-tech-writing

[简体中文](README.zh-CN.md) · [日本語](README.ja.md)

Rewrite Chinese or English technical text so it is easier to follow without losing information.

**Input** — Supply the source text, necessary context, intended reader and requested format. Ask for a rewrite or an ambiguity review.

**Output** — Return clearer text with the same meaning. For reviews, identify concrete ambiguities and corrections. Ask only when missing context would change the meaning or result.

## Working rules

Keep conditions, negation, actors, sequence, numbers, units, identifiers and uncertainty. Do not turn HTTP 200 into recovery, automatic behavior into manual instructions, or an unknown actor into an invented one. Editing a command does not authorize running it.

## Minimal example

Install for Codex from your project (Node.js 22.20+):

```sh
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill simplify-tech-writing -a codex -y --copy
```

> Use simplify-tech-writing to clarify: “The export request failed at 10:00. One retry returned HTTP 200 at 10:02; the final export status was not checked.” Preserve every fact and return only the rewrite.

[11 original cases](references/examples.md) · [Methods](references/methods.md) · [Sources](references/sources.md)

## Dependencies and limits

No PDF, network, account or other skill is required for normal editing. This is a heuristic writing method inspired by ASD-STE100, not a compliance checker. The standard and dictionary are not bundled. Exact standard queries need an authorized source; Japanese rewriting has not been evaluated.

Developed by Henry2012 with AI assistance. This is a fictional demonstration, not an LLM benchmark. [SKILL.md](SKILL.md) · [MIT](LICENSE) · [Workshop](https://github.com/Henry2012/skills-workshop)

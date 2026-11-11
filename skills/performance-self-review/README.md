# performance-self-review

[简体中文](README.zh-CN.md) · [日本語](README.ja.md)

Turn authorized work records into a personal self-review with a traceable evidence ledger.

**Input** — Supply the assessment period, your role, the projects in scope, the required format, and records you are allowed to use. Existing records are enough; extra retrieval needs its own access and authorization.

**Output** — Return the review text, a ledger linking claims to sources, and a coverage note. Track discovered records, retrieved bodies and material actually read separately.

## Working rules

Keep personal actions separate from team outcomes, targets from achieved results, and reported measurements from verified results. Preserve dates, denominators and partial states. Follow the requested length and sections; do not add an action plan unless requested.

## Minimal example

Install for Codex from your project (Node.js 22.20+):

```sh
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill performance-self-review -a codex -y --copy
```

> Use performance-self-review with the fictional input linked below. Write the requested results and reflection paragraphs, plus a separate evidence ledger. Use only the supplied material.

[Input](https://github.com/Henry2012/skills-workshop/blob/main/examples/self-review/input.md) · [Output](https://github.com/Henry2012/skills-workshop/blob/main/examples/self-review/output.md) · [Local reference](references/example.md)

## Dependencies and limits

Local or pasted documents are sufficient. No company connector is required. Reading permission does not authorize publishing, messaging, or updating an employer's system. Keep real source records and outputs outside this public repository.

Developed by Henry2012 with AI assistance. This is a fictional demonstration, not an LLM benchmark. [SKILL.md](SKILL.md) · [MIT](LICENSE) · [Workshop](https://github.com/Henry2012/skills-workshop)

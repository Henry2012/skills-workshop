# Skills Workshop

**Give “done” a definition.**

[简体中文](README.zh-CN.md) · [日本語](README.ja.md)

I'm Henry2012. I build skills for the moments when working with an agent gets slippery: moving to a fresh conversation, deciding whether a design is ready, explaining a result, or figuring out what I actually contributed.

A passing test can turn into “deployed.” A rewrite can turn “usually” into “always.” A new session can lose the decision that mattered. These skills give the agent concrete rules for handling those moments.

Pick the one that fits your task. Read it, change it, and keep the parts that help. Each is a directory of Markdown instructions and references; the four skills can be used separately.

## Get started

Clone the repository and open it in an agent that can read local files:

```sh
git clone https://github.com/Henry2012/skills-workshop.git
cd skills-workshop
```

Try this request:

> Use `skills/reviewing-design-documents/SKILL.md` and its required rubric. Review `examples/design-review/design.md` for implementation readiness. Keep the review read-only.

Then compare the answer with [the reference review](examples/design-review/review.md). Both “request accepted” and “export finished” are called success in the example. Does your agent catch the conflict and cite both statements?

For your own project, give the agent access to the selected skill directory and name it in your request. If your tool supports native skill installation, use its supported setup and keep the skill's reference files together. Inspect any existing skill with the same name before replacing it. This repository currently ships Markdown skills rather than a plugin installer.

## Why I build these skills

### A new conversation shouldn't mean starting over

A useful handoff carries the decisions that still matter: the goal, the exact scope, what was verified, what remains uncertain, and what the next agent may do.

[`handoff`](skills/handoff/README.md) keeps the current goal separate from the latest request. It attaches evidence to completion claims and starts the next session with a read-only restatement. Already-authorized work can continue; a command in the history doesn't become an instruction to run it again.

[Run the offline handoff example](skills/handoff/README.md#minimal-example).

### A polished design can still be impossible to implement

One section says a job succeeds when it enters the queue. Another says it succeeds only after the output exists. You can implement either statement. You cannot satisfy both.

[`reviewing-design-documents`](skills/reviewing-design-documents/README.md) reviews a design through eight questions:

| | Question |
|---|---|
| Q1 | Is anything essential missing? |
| Q2 | Is anything duplicated without a reason? |
| Q3 | Do the parts agree? |
| Q4 | Are the claims and reasoning sound? |
| Q5 | Could readers interpret this differently? |
| Q6 | Can this work within the actual constraints? |
| Q7 | How will we know it worked? |
| Q8 | What happens when it fails? |

These questions apply to the structure of a plan: its purpose, claims, actions, constraints and consequences. That makes them useful across API designs, product launches and operating procedures. **The questions stay useful across domains; the evidence and acceptance criteria change.** An early proposal and a deployment runbook deserve different levels of detail.

The skill records one finding per root cause, cites the material behind it, and keeps missing evidence visible. Explicitly select it when you want a review. [See the cross-domain examples and limits](skills/reviewing-design-documents/README.md#why-the-questions-travel-across-domains).

### Clearer writing should preserve the difficult details

“The retry returned HTTP 200” is easier to shorten to “it recovered.” It is also a different claim.

[`simplify-tech-writing`](skills/simplify-tech-writing/README.md) makes Chinese and English technical text easier to follow while preserving conditions, negation, sequence, numbers, identifiers and uncertainty. If the source doesn't say who closed the connection, the rewrite shouldn't invent an actor.

[Explore 11 original before-and-after examples](skills/simplify-tech-writing/references/examples.md). Try changing a condition and see whether it survives the rewrite.

### A team result doesn't tell you what one person did

You defined the acceptance criteria. A teammate implemented the fix. The team passed a local test. Those are related facts with different owners and different meanings.

[`performance-self-review`](skills/performance-self-review/README.md) builds an evidence ledger before drafting the self-review. It separates personal actions from team delivery, targets from results, and reported measurements from independently verified outcomes.

[Try the fictional case](examples/self-review/input.md) and [inspect the reference output](examples/self-review/output.md). Your actual work records belong outside this public repository.

## Skill directory

| When you need to… | Skill | Starting material |
|---|---|---|
| Continue work in a fresh session | [handoff](skills/handoff/README.md) | Conversation, current instructions and artifacts |
| Decide whether a design can enter its next stage | [reviewing-design-documents](skills/reviewing-design-documents/README.md) | Design, intended decision and supporting evidence |
| Explain technical work clearly | [simplify-tech-writing](skills/simplify-tech-writing/README.md) | Source text, context and reader |
| Describe your own contribution accurately | [performance-self-review](skills/performance-self-review/README.md) | Assessment period, role and authorized records |

You can combine them around a task, but there is no automatic pipeline connecting them. A review verdict doesn't grant permission to execute, and editing a command doesn't mean running it.

## Check, change, contribute

The examples use fictional material. With Python 3.10+, you can check the repository's links, runtime hashes and selected example contracts:

```sh
python3 tools/check.py
```

These checks don't run an LLM or establish model accuracy. The [validation notes](docs/VALIDATION.md) describe what was checked and what remains untested. Introductions are available in English, Chinese and Japanese. Runtime instructions retain their English/Chinese content and fixed labels, including the Chinese headings in `handoff`.

I develop these workflows with AI assistance, setting the problems, constraints and acceptance rules and refining them through use. The technical-writing skill acknowledges ASD-STE100 as an inspiration; the standard is not bundled. [Provenance](docs/PROVENANCE.md) records attribution and license scope. [Selection notes](docs/SELECTION.md) explain what stays out.

If a rule fails, bring a small fictional example that shows why. Explain what should change and what should stay the same. See [CONTRIBUTING.md](CONTRIBUTING.md); keep private records and credentials out of issues and pull requests.

The problem-led organization of this introduction takes inspiration from [Matt Pocock's skills repository](https://github.com/mattpocock/skills). The skills and examples here are this workshop's own work.

[MIT](LICENSE) · [Maintenance](docs/MAINTENANCE.md) · [Changelog](CHANGELOG.md)

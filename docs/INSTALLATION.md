# Installation verification

Use the existing [Vercel skills CLI](https://github.com/vercel-labs/skills). This repository needs no custom installer or plugin manifest: the CLI discovers the four SKILL.md entrypoints under skills/.

## Tested commands

Node.js 22.20+ is required by skills@1.7.6. The observed test environment used Node.js 25.4.0, npm 11.7.0 and skills 1.7.6 on macOS. Run commands in the project that should receive the files.

```sh
# All skills, Codex
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill '*' -a codex -y --copy

# One skill, Codex
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill reviewing-design-documents -a codex -y --copy

# All skills, Claude Code
npx --yes skills@1.7.6 add Henry2012/skills-workshop --skill '*' -a claude-code -y --copy
```

The quotes preserve the literal wildcard. The first --yes allows npx to fetch the CLI; the final -y skips the CLI's confirmation. The explicit --copy makes the placement method independent of interactive defaults. The commands use project scope, not -g. Inspect existing same-named skills before running them: installation may replace local customizations.

## Verification scope

Verified on 2026-11-11 (Asia/Shanghai) against [source commit 3556210](https://github.com/Henry2012/skills-workshop/commit/35562102f975585fc8a42b8a31b934b83067a1cd), using the GitHub commands above in empty project directories:

| Command target | Installed skills | Files matched byte for byte | Exit code | References, license and lock |
|---|---:|---:|---:|---|
| Codex, all | 4 | 27 | 0 | PASS |
| Codex, reviewing-design-documents only | 1 | 7 | 0 | PASS |
| Claude Code, all | 4 | 27 | 0 | PASS |

Tests use separate empty project directories, an isolated npm cache and XDG_STATE_HOME, and DISABLE_TELEMETRY=1. The existing user-level skill installation is not used as a test target. The telemetry setting also disables the CLI's remote security-audit requests; no third-party security score is claimed.

For each tested installation, inspect actual files, compare every installed file's bytes with its source, check relative resource links, and inspect skills-lock.json. With --copy, Codex receives files in .agents/skills/ and Claude Code receives files in .claude/skills/. Selected installation must contain only the requested skill. Each skill includes its own MIT license; reader-guide links to repository-wide examples use public URLs.

Candidate packages are checked from a local path before publication; the documented GitHub commands are then checked against the published files. Successful placement and matching bytes do not prove that a running Agent has refreshed its catalog or will follow every instruction. Agent invocation and model behavior remain separate checks. No Windows/Linux, global-installation or other-agent result is claimed.

Re-running an add command retrieves the then-current repository content. The CLI version is pinned, but the repository's main branch can change. Keep your project lock file and review updates. See the upstream [command reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) for other supported options.

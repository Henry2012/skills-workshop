# Maintaining a small public edition

Keep the public repository independent. Never mirror all files or history from a development workspace.

For each proposed update:

1. Identify the skill and exact source revision. Keep private source locations in a private maintenance record.
2. Compare against the previous imported source hash. Inspect additions, removals, dependencies, attachments and behavior changes.
3. Select only authorized, redistributable files. Preserve attribution and permission boundaries. Do not copy local settings, reports or historical data.
4. Update the public example when the intended behavior changes. Record what changed and why in the changelog; synchronize the three introductions.
5. Regenerate the published-content manifest with `python3 tools/check.py --write-manifest`, then run `python3 tools/check.py`. Review the manifest diff instead of treating a newly generated hash as proof of safety.
6. Review the staged files and author/committer metadata. Use the maintainer's GitHub noreply identity. Push only the reviewed public branch.

The manifest covers eleven runtime files and four per-skill licenses. The original six runtime files are preserved imports; five belong to the separately prepared technical-writing edition. Source maps and confidential audit notes remain outside this repository. Documentation, examples and tooling are reviewed through Git and the local checker. For simplify-tech-writing, update the public adaptation deliberately; never recopy its full development directory or reintroduce the standard attachment and mappings.

After changing installable files, follow [installation verification](INSTALLATION.md). Check that a skill works as a standalone directory: runtime references must stay inside it, while links to repository-wide examples use public URLs. Preserve the bundled license. The CLI version and the source revision are separate versions.

A later skill is eligible only if its existing original or substantive adaptation work is identifiable, its required resources are portable, its rights are clear, and it has an honest demonstration. A name change or translated README does not meet that threshold.

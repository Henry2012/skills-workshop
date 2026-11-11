# Validation coverage

Release candidate 0.1.0, checked on 2026-11-11 UTC.

## What was exercised

| Check | Evidence and boundary |
|---|---|
| Offline status-helper demo | `python3 tools/demo_handoff.py` runs three real unit tests, records source hashes, and generates a handoff with local absolute paths. It tests the fictional helper and example generator, not an LLM's handoff behavior. |
| Handoff artifact | The checker verifies the 13 fixed headings, current test receipt, matching source hashes, and verification-boundary markers when the demo has run. Generated artifacts stay in ignored `build/`. |
| Design-review reference | The walkthrough identifies the explicit completion contradiction, cites both statements, keeps one root-cause finding, and retains Q5/Q7 as affected questions. Three negative controls check that missing headings, a false READY verdict, and a lost secondary effect are rejected by the local checker. |
| Self-review reference | Selected facts and coverage limits are checked against the invented input. The source reference also retains its explicit fictional-data statement. Meaning and attribution were reviewed while authoring the example. |
| Packaging | Relative Markdown file links, three-language introductions, the selected skill set and six runtime-file hashes are checked. |
| Publication hygiene | The candidate contains text files only. The checker flags common secret prefixes, private-key blocks, personal home paths, internal hosts and unexpected email addresses. The final Git tree and metadata receive a separate release review. |

Run the examples and checks from the repository root:

```sh
python3 tools/demo_handoff.py
python3 tools/check.py
```

The demo performs a local test run once per invocation. Do not interpret the historical command inside a generated handoff as an instruction to run it again.

## What this does not establish

No independent or cross-model LLM evaluation was performed. The reference outputs are authored examples, not recordings of separate model experiments. Formatting and selected-fact checks do not prove complete semantic correctness, usefulness in every domain, or protection against all secret leakage.

No business records, production systems, private chat services, deployment paths or employer performance systems were used in the examples. Translations were reviewed for consistency during preparation; they have not had independent native-speaker review. The runtime contracts retain their original English/Chinese instructions and fixed labels.

For behavior evaluation, run the documented prompt in a fresh agent context, retain the model/tool versions and response, and compare it with the input and skill rules. Change one meaningful fact and check whether the conclusion changes appropriately. Report failures with fictional inputs through the [contribution process](../CONTRIBUTING.md).

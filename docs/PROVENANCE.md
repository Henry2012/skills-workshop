# Provenance and license scope

The owner confirmed on 2026-11-11 that `handoff`, `reviewing-design-documents` (now `review-plans`), and `performance-self-review` were developed with AI assistance and may be released under MIT.

The owner also confirmed authorship of `simplify-tech-writing` and requested its inclusion in this MIT-licensed collection, retaining original methods and examples while excluding the standard PDF. Its public edition was prepared on the same date.

These are locally developed workflows, not copies presented as third-party inventions of the maintainer. This statement concerns the published expression and implementation of the workflows. It does not claim that concepts such as evidence ledgers, design reviews, or handoffs were invented here.

| Component | Origin | Public edition |
|---|---|---|
| handoff | Maintainer's AI-assisted workflow, source version 0.4.1 | Runtime rules preserved; multilingual introduction and fictional walkthrough added. |
| review-plans | Maintainer's AI-assisted design, rubric and subsequent refinements | Explicit invocation gate, verdict logic and references preserved; multilingual introduction and fictional review added. |
| performance-self-review | Maintainer's AI-assisted evidence and attribution workflow | Rules and explicitly fictional reference preserved; multilingual introduction and portable demonstration added. |
| simplify-tech-writing | Maintainer's AI-assisted technical-writing methods and original examples; inspired by ASD-STE100 | Retains original methods and 11 examples; excludes the standard PDF, dictionary and systematic rule/entry mappings. See [specific source and license boundaries](../skills/simplify-tech-writing/references/sources.md). |
| Repository guides, examples and local checker | Prepared for this public edition with AI assistance | MIT. Examples are invented and are not customer or employee records. |

All files shipped in this edition are covered by the root [MIT license](../LICENSE). No third-party code, standard, book, PDF, model weights or external service is bundled. External sources such as ASD-STE100 retain their own rights and are outside this MIT grant. Mentioned product names belong to their respective owners and do not imply endorsement.

The repository starts with a fresh history. Public per-file content hashes are recorded in [provenance.json](../provenance.json); a private source mapping is maintained separately and is not shipped. Review material changes and license scope again for later additions. This record is not a legal opinion or a guarantee that an automated scan detects all confidential information.

The [handoff comparison](HANDOFF-COMPARISON.md) records shared purpose and metadata as well as substantial behavioral differences from Matt Pocock's workflow; similarity review alone does not establish independent authorship. Reader guides use a concise task/input/output/constraints structure inspired by the referenced entrypoint. Installation uses the external Vercel skills CLI without bundling its implementation. Each installed skill carries a copy of this repository's MIT license.

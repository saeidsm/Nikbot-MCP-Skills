# Public skill release workflow

Apply when the owner explicitly requests publication of a new or customized skill. A general product delivery task does not authorize publishing its business context.

1. Inventory owned instructions, references, helper code and assets. Record provenance and license per upstream component; a user's copy is not evidence of redistribution rights.
2. Stage a clean public edition separately. Never push a private checkout, history, logs, captures, generated customer artifacts, credentials, bearer links or account configuration. Generalize names, hostnames, absolute private paths, emails, phone numbers, identifiers, backend architecture and incident details.
3. Retain useful behavior. Replace deployment-specific integrations with explicit capability discovery and placeholders. Document missing runtime pieces. Do not present a text-only adaptation as including tools/fonts it intentionally omits.
4. Use one named branch per skill in the owner's designated public repository. Check remote refs first; avoid active executor branches and shared worktrees. Never overwrite or force-push someone else's branch. Do not merge without the applicable authorization and review.
5. Include SKILL.md, portable setup, usage, dependencies/limitations, provenance and applicable license notices. Do not silently choose a license for content you do not own or lack authority to license.
6. Validate frontmatter, local links, installation structure and examples. Scan every intended file for secrets and private data; have an independent reviewer inspect the exact staged bytes. Recheck any revisions before upload. Exclude unclear assets rather than publish first and clean later.
7. Push the reviewed exact tree, verify remote commit and file contents, and provide full copyable branch/download URLs. Distinguish publication from successful installation or execution in another agent.
8. Keep a private source-to-public mapping and withheld-items list. For future updates repeat the same review; do not automatically sync raw personal skills into a public repo.

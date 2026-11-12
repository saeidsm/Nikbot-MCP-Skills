---
name: persian-writing
description: Write and edit natural Persian and mixed-language documents with preservation, orthography, RTL layout and rendered-output checks.
---

# Persian writing and RTL review

This portable instruction-only edition is an editorial and layout-review layer. It does not install fonts, normalize originals, run document repair scripts or replace a document/PDF/presentation workflow.

## Establish intent
Identify audience, purpose, artifact, register and edit scope. An informal request for an official letter still calls for professional prose. Extract supplied facts and use the existing approved template. Ask only about a missing consequential fact; mark other unknowns rather than inventing them.

## Preserve meaning
- Keep direct quotations, transcribed evidence and legal clauses intact unless explicitly asked to edit them. Label edited versions. Editorial work is not legal verification.
- Preserve names, identifiers, code, URLs, paths, API fields, placeholders, formulas, versions and machine-readable data exactly.
- Preserve numeric value, sign, precision, unit, date/calendar and currency. Never silently turn rial into toman, change a calendar or infer a missing monetary unit. Persian display digits are not a reason to change underlying spreadsheet types.
- Do not normalize Arabic passages as Persian. Protect proper names and source spelling when uncertain.

## Draft and edit
Use natural Persian, specific verbs, coherent terminology and the register appropriate to the recipient. Avoid literal English phrasing and redundant honorifics. In newly written editable Persian prose, use Persian ی and ک and contextual نیم‌فاصله. Do not apply blanket character replacement to technical strings, quotations or names. Check compounds, suffixes, ezafe and punctuation in context rather than assuming one regex is correct everywhere.
For UI copy, prefer short action labels, actionable validation and consistent concepts; preserve localization placeholders and pluralization semantics. Orthography-only work must not turn into an unrequested substantive rewrite.

## RTL artifacts
Use genuine RTL paragraph direction, not reversed text or spaces. Use isolated LTR spans for technical text. A right-aligned paragraph is not automatically RTL, and an RTL paragraph does not prove a table's logical direction. Inspect table direction, column order, cell alignment, native numbering, headers, footers and complete multilevel heading labels.
Use an available licensed shaping-capable font selected by the user/template. Vazir and Vazirmatn are different families. This package includes neither. Confirm actual rendered font, fallback, glyph joining and portable export behavior. Do not overwrite system fonts just to satisfy a document.

## QA and delivery
Keep the original; edit a new copy when repairing an existing document. Use the host's trusted document tooling. Inspect every rendered page or slide for clipping, mixed-language punctuation, heading hierarchy, table breaks, footnotes and unintended fallback. Compare the final artifact with the source, not only with the previous draft. Verify files are nonempty and retrievable. Report what was rendered and what remains unverified. No upstream checker or successful regex proves semantic or visual correctness.

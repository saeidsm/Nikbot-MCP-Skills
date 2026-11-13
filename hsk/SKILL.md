---
name: hsk
description: "Hasan Kachal / حسن کچل: plan comprehensively, then deliver a safe, polished, usable product in visible phases with efficient time and token use. Use for HSK, HSK کن, حسن کچل کن, autonomous execution briefs for sam/Claude/Codex, or resuming authorized product delivery. Not a mandate to build an MVP, invent scope, or bypass permissions."
---

# HSK — حسن کچل

**Optimize for the fastest trustworthy working product, not the most code, tests, agents or reports.** Plan the complete agreed outcome and its connections before implementation; execute in visible, usable phases. The goal is a ready-to-use, safe, efficient product with clean UI/UX, not a throwaway MVP or a demo with fake integrations. Early phases are delivery checkpoints, not permission to abandon the full scope.

## Choose the mode

- **Brief:** Prepare a self-contained execution handoff using [execution brief](references/execution-brief.md). Do not start a competing implementation or send it to an external agent without authorization.
- **Execute:** Carry authorized work through implementation, proportionate verification, release and real acceptance.
- **Resume:** Recover the current executor, state and evidence; continue missing work rather than repeating discovery.
- A request to update this skill authorizes that update, not unrelated product work. Resolve ambiguous mode from the conversation; ask only if the distinction blocks a consequential action.

## 1. Plan the whole product, once

Inspect the existing source, deployed baseline, project instructions, active workers and prior decisions. Check critical prerequisites early: data and original attachments, credentials presence without exposing secrets, provider availability/budget, supported APIs, deployment access and migration compatibility. Do not design around an unverified integration.

Create one compact delivery contract:
1. Target users, their real journeys, required outputs and supported devices.
2. Agreed features and explicit exclusions; no agent-invented features.
3. A small architecture diagram and connection map: UI → API → storage/jobs → providers → returned result. Include identity, permission decisions, async work, errors and recovery where relevant.
4. Data lifecycle: ownership, access separation, durable saves, interruption/retry behavior, retention and recovery.
5. Deployment topology, dependencies, compatibility constraints and operational ownership.
6. Capacity assumptions: registered versus active/concurrent users, representative workload, latency and resource limits. Design for the requested capacity, including hundreds of users when required, without equating that with hundreds of simultaneous expensive jobs.
7. Ordered phases with visible outputs, acceptance checks, dependencies and the next release target.
8. Time/token/spend limits and the few risks that could actually prevent safe delivery.

Cover relevant corners and integration boundaries, not every imaginable scenario. Reuse proven open-source components and existing project tools after checking fit, license, maintenance and real interfaces. Prefer a thin integration over rebuilding queues, permission bridges or UI foundations. Avoid adding a framework merely to avoid a small adapter.

Make ordinary reversible choices and proceed. Ask only for an essential unresolved fact, an owner-reserved tradeoff or required approval. This skill grants no extra authority: respect tool denials, native safety checks, secrets, data sharing and budgets. Continue independent work while a genuinely blocked action waits.

## 2. Execute in visible phases

Keep one accountable lead and one owner for shared migrations/releases. Reuse active workers and worktrees; never start duplicate jobs because a report is missing. Delegate only independent bounded work whose benefit exceeds coordination cost. Respect requested models and verify actual routing.

First prove the most important end-to-end journey on the real stack. Then complete the agreed features in dependency order. Every phase must produce something observable: a working screen, integration, output or deployed behavior, not only another specification. Show the user the current result early, with unfinished behavior clearly labeled.

Freeze each phase's scope. Put optional ideas in a future-work backlog, not in the release path. Incorporate explicit user changes and their impact; do not silently shrink the final contract. A blocked dependency is not a reason to rebuild unrelated modules or leave independently deliverable work unfinished.

## 3. Spend tokens on decisions and delivery

Use a concise current-state handoff: source version, completed behavior, evidence, next action and real blocker. Read relevant files/diffs and bounded logs; retrieve more only when needed. Do not repeatedly ingest full repositories, histories or verbose test output. Preserve full logs as artifacts and summarize the actionable lines.

Use the selected capable lead for architecture and consequential integration decisions; use permitted less expensive models for bounded implementation where appropriate. Avoid repeated multi-agent reviews and speculative variants. Track actual usage when available; never equate subscription percentage with an API invoice.

Reassess at each phase if planning, review or tests are consuming the delivery budget without producing a working increment. Narrow the next action, reuse existing evidence and solve the concrete blocker. Do not repeat an unchanged expensive test suite or failed experiment without a reason and a changed hypothesis.

## 4. Verify proportionately, not exhaustively

Select a short acceptance matrix from [delivery acceptance](references/delivery-acceptance.md) before implementation. While iterating, run checks for changed paths and likely regressions. Before release, run the necessary integration/regression checks for the frozen candidate; use a full suite when project rules or broad impact justify it, not as an automatic ritual.

A first release does not require thousands of newly invented tests, every hypothetical fault, or proof of zero errors. Existing mandatory CI still applies. Never disable a required check, weaken assertions or hide failures to ship faster.

Prioritize:
- The main real user journey from original input to saved/reopened output.
- Authentication/access separation and protection of data and credentials.
- The relevant interruption/retry path, avoiding lost progress and duplicate effects.
- Migration/recovery safety when state changes are involved.
- A bounded representative performance check at the declared concurrency and workload, plus resource observations. Record measured capacity separately from the design target; do not claim hundreds of users were proven by a health check.

Use synthetic/non-sensitive data where possible and authorized real integration probes when needed. Mocks are not provider or deployment acceptance. Fix release-blocking defects; log low-impact imperfections with an owner and follow-up rather than seeking impossible perfection. Use independent review for consequential changes, not endless review of the same frozen bytes.

## 5. Make UI/UX part of functionality

Reuse the project's design system and appropriate UI/UX, RTL and Persian element skills. Build a coherent primary flow with clear hierarchy, readable typography, responsive layouts, obvious actions, accessible controls and useful empty/loading/error states. Preserve user progress across navigation and unreliable networks when the task requires it.

Inspect the rendered product on relevant desktop/mobile sizes and walk through the actual workflow. A screenshot alone is not interaction testing; passing backend tests is not acceptable UX. Avoid exposing internal processing and developer controls in the user's main path. Never call an unchanged legacy screen a delivered redesign.

## 6. Release a usable product and prove it

Use the existing supported release process and exact tested source. Take appropriate backups, check migration compatibility and recovery proportional to risk, and preserve rollback or forward-repair options. Do not blindly restore a live database or revert to an incompatible API. Do not deploy unrelated changes.

Verify running version, health and the representative user journey after release. Check required workers, persistence and restart behavior when applicable. Deliver a usable link or artifact and a short demonstration of what works. Unavailable features must not masquerade as active controls.

Report separately: **implemented / tested / pushed / merged / deployed / enabled / accepted**. Never turn test counts or source commits into claims of a usable product. State known limitations and real blockers, not guessed completion percentages. Finish only when the agreed product is usable or a specific blocker prevents further authorized progress.

## 7. Preserve continuity without bureaucracy

Use the existing private task registry and handoff, not a second tracker. Record current phase/evidence, executor, next action, blocker/owner, review date or event trigger and definition of done. Keep a concise chronological summary so another agent can resume without rereading every log. Do not abandon open work when attention shifts.

Use a supported schedule only when follow-up is needed and authorized; verify it exists before promising to monitor. Keep generic reusable skills separate from business context. For authorized public publication, follow [public skill release](references/public-skill-release.md), with a dedicated skill branch and a sanitized portable edition. Never publish secrets, private infrastructure details, customer data or token-bearing links.

---
name: hsk
description: "Hasan Kachal / حسن کچل: turn an ambitious task into a comprehensive, bounded execution brief and drive authorized work to a verified usable product. Use for HSK, HSK کن, حسن کچل کن, or requests to package a task for autonomous execution by an external executor and subagents. Distinguish prompt preparation from permission to execute."
---

# HSK — حسن کچل

HSK means **own the outcome, not an endless plan**. Convert a rough goal into a precise assignment that a capable lead and its workers can finish without asking the owner to manage every step. Deliver a usable vertical slice early, then complete the remaining agreed scope. A large test count, a polished report, or source pushed to a branch is not delivery.

## Choose the requested mode

- **Execution brief:** When asked to “HSK this for my coding agent”, produce a self-contained execution prompt and handoff. Do not start a competing implementation. Read [the brief template](references/execution-brief.md). Preparing a handoff does not itself authorize sending instructions to an external agent; deliver it to the user unless sending is authorized.
- **Execute:** When asked to do the work autonomously, use the brief as the working contract and continue through authorized implementation, tests, review and delivery.
- **Resume:** Find the existing task and executor, reconcile what actually happened, then continue missing work. Do not restart from discovery or spawn duplicates merely because context changed.
- If the user only asks to create this skill, create the skill; do not execute an unrelated product task.

For an unspecified “HSK کن”, retain the context: if the conversation is preparing a prompt for another agent, prepare that prompt; if it asks to build an outcome, execute within its authorization. Ask only when this consequential distinction cannot be resolved.

## 1. Establish the delivery contract

Inspect the current project, instructions, artifacts, live baseline and active executors. Reuse the existing repository, architecture, approved design and worktrees. Do not invent unavailable APIs or assume a configured model is working.

Write a short contract containing:
- User outcome and target users, surfaces and environment.
- A smallest **usable** release, explicit acceptance examples, and later agreed phases.
- Scope exclusions: enhancements are backlog, not new prerequisites.
- Existing evidence versus claims not yet verified.
- Dependencies, authority, data-sharing boundaries, spending cap and rollback constraints.
- Where work, state, results and next action will be retained.

Make reversible product choices yourself. Ask only for a missing fact that blocks a specific step after checking available sources, a material tradeoff reserved for the owner, or an action requiring confirmation. Routine discovery, tests and ordinary implementation should not become repeated approval requests. This skill is not permission to bypass a denied tool, hook, sandbox, budget, authentication or native safety mechanism; use the supported approval path and continue independent work.

## 2. Orchestrate without interference

Keep one accountable lead. Delegate independent implementation or review with a precise outcome, allowed files, dependencies, acceptance checks and return format. Limit parallelism to the available compute, context and conflict risk; more workers is not inherently faster.

- Inspect active sessions before starting workers. Assign ownership of shared files, migrations and releases.
- Use isolated worktrees when needed; reuse existing ones and avoid duplicate clones or indexes.
- Integrate completed work before launching redundant variants. A review finds actionable defects, not a mandate to redesign everything.
- Respect the user's chosen models. Use the chosen lead for important design/integration decisions and appropriately capable workers for bounded implementation, tests and review when that routing is available. Verify actual routing; do not silently substitute models or spend on a new provider. Track meaningful model/token/time spend when available, but never convert subscription quota percentages into API cost without supported rates and usage data.
- Send changes in user direction to existing workers. Follow up idle workers; do not leave work abandoned when a new request arrives.

## 3. Deliver in bounded slices

Start with one representative end-to-end user flow and real inputs. Keep data durable across interruptions where the task depends on it. Fix correctness blockers and ship the slice before growing dashboards, adapters, inventories or abstractions.

A later explicit user reprioritization can change the release contract: incorporate it, explain the delivery impact, and refreeze. The feature-freeze rule prevents agent-invented scope creep, not the owner changing direction.

If a blocked dependency prevents full delivery, release an independently useful, authorized slice only when it is safe and does not misleadingly present unavailable functions as working; record the remaining outcome as open.

At each milestone: compare against the contract, freeze feature growth for that release, integrate, test, review, then deliver. Preserve all remaining agreed features in the backlog. Do not reduce scope silently or call an interim slice the finished product.

For user-facing products, reuse the existing design system and suitable design/RTL skills; aim for clear, polished, accessible interaction rather than treating passing tests as sufficient UX.

Use targeted tests while iterating and a full appropriate regression on the final frozen candidate. Repeat a full run when the candidate changes materially, not after every documentation edit. Preserve failed acceptance evidence; fix the cause rather than changing thresholds, skipping tests or rerunning until green.

## 4. Prove usefulness, not just code correctness

Use the relevant acceptance checklist in [delivery acceptance](references/delivery-acceptance.md).

- Prove the whole path with real authentication and representative data when permitted. Mocks and synthetic fixtures establish limited facts only.
- Check prerequisites early: original attachments, account access, provider entitlement/credit, configuration, model support and deployment capability. A UI without its source data or an unaffordable provider is not the intended working feature.
- Verify output files are actually retrievable and correct. Include only explicitly intended outputs; never export arbitrary untracked files or secrets.
- Distinguish code written, tests passed, source pushed, merged, deployed, enabled and user-accepted. Give no guessed percent complete.

## 5. Release and finish

Follow the project's release rules. Bind reviewed/tested source to the exact release. Back up relevant data, verify recovery proportional to risk, retain rollback artifacts, check concurrent work, and use a reversible rollout. Do not deploy unrelated pending changes blindly or label a destructive migration reversible without evidence.

After release, check actual user flow, health, access isolation and output delivery. If a gate stays off, say what users can and cannot do. If blocked, deliver useful independent results plus the exact missing requirement; do not fabricate completion or silently replay uncertain jobs.

End with a concise result: usable link/artifact, demonstrated behavior, stage evidence, outstanding items with owner/trigger, and rollback or known limitations that affect use. In private owner delivery, existing authorized expiring report links may be printed as full copyable SUMMARY_URL, REPORT_URL and ZIP_URL and returned in structured MCP fields; keep credentials out of public repositories and permanent logs.

## 6. Preserve continuity

Use the project's existing task registry and handoff, not a second competing tracker. Keep reusable skills/code separate from private business context; use the owner-designated private tracker.

Every unfinished task records: current stage/evidence, executor, next action, blocker and responsible party, review date or event trigger, and definition of done. Update after meaningful changes. If a future check is needed, use an actual supported schedule/notification and verify it exists before promising to watch. Notes alone do not wake an agent.

Do not claim that this skill permanently monitors work or grants tools. A later agent must revalidate state, permissions and active ownership before resuming.

## Publishing reusable skills

When public skill publication is explicitly authorized, follow [the public release workflow](references/public-skill-release.md). Publish a sanitized portable edition, not a private environment snapshot. Keep one skill per dedicated branch and obtain an independent review of the exact bytes before public upload.

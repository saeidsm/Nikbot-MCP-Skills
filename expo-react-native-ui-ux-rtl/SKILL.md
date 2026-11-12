---
name: expo-react-native-ui-ux-rtl
description: Design and implement accessible Expo/React Native UX with multilingual RTL, durable user flows and existing-project conventions.
---

# Expo / React Native UX and RTL engineering

This is a project-neutral edition. No particular SDK, folder layout, design system, localization library or private application architecture is assumed.

## Inspect before implementing
Read repository guidance, package manifest and lockfile, nearby screens, navigation, providers, API/auth boundaries and current tests. Record supported platforms/locales and actual native direction behavior. Reuse existing components, tokens and patterns rather than adding a second navigation, state or styling framework. Verify commands before running them.

## Define a usable experience
For each feature specify user job, primary action, success state, next natural action and acceptance examples. Cover loading, empty, offline, reconnect, permission denial, error/retry, pending background work, cancellation and success. Preserve drafts and progress across navigation, interruption and process restarts where the workflow requires it. Show cost and consequences before committing, not after.
Use progressive disclosure and brief in-context help with skip/reopen paths. Experienced users should retain a fast route. Avoid shame, false urgency, forced loops and surprise billing. For family products, provide appropriate adult controls and avoid child-directed purchases; do not make therapeutic claims without evidence.

## Implementation contract
Produce complete typed components with stable keys, cleanup, bounded effects, cancellation and duplicate-submission protection. Respect auth and route guards. Handle keyboard, safe areas, reduced motion, accessibility roles/labels/states, focus and screen-reader reading order. Prefer semantic color tokens and verify contrast for actual rendered themes. Do not rebuild existing controls without a demonstrated gap.
Localize every user-visible string, validation message and accessibility label. Check placeholder parity across supported locales. Avoid hardcoded text and fake completed translations.

## RTL and language switching
Use logical spacing and positioning where supported. Test effective native direction instead of assuming CSS-style start/end support. Do not double-reverse an already mirrored row. Mirror directional arrows, gestures and transition semantics; do not mirror logos, photos or media symbols. Keep numerals, technical strings and mixed-script labels readable.
If direction changes require a native reload, preserve navigation intent, auth, unsaved drafts and resumable operations. Test same-direction switches separately from RTL-to-LTR switches. Font choice must cover actual scripts and font scaling; missing font files cannot be solved by merely naming a family.

## Acceptance
Run applicable types, lint and tests, then exercise representative screens on actual platform builds or clearly label simulator/browser-only evidence. Test screen readers, font scaling, keyboard, small screens, touch targets, language switches, lost connectivity and resume. Capture visual evidence at supported themes/locales. Passing unit tests alone is not visual validation.
Release only within authorization, with rollback proportional to change risk. Separate implementation, tests, merge, deployment and actual feature availability. Use first-party Expo, React Native, Apple HIG, Material and WCAG documentation as version-specific references, not unexamined instructions.

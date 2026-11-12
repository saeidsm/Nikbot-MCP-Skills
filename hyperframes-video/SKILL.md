---
name: hyperframes-video
description: Build, edit, preview, and render HTML motion videos with HyperFrames. Use for HyperFrames projects, vertical Reels, photo before-and-after comparisons, social promos, and architectural motion graphics when a deterministic HTML timeline fits.
---

# HyperFrames Video

Use the project's existing version when present. For a new project, select an explicit CLI version from the upstream package and verify the available commands with its help. Run it in the project directory. Read the relevant [official guides](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes) for format, motion, vertical video, media, or rendering.

## Build

1. Map the brief to a timeline with shot purpose, approximate beats, on-screen text, source assets, and output ratio. Preserve supplied footage and project facts. For before-and-after imagery, use common corners, horizons, or edges as anchors. Use an intentional cut or wipe and preserve the original camera perspective.
2. For a new project use `npx hyperframes init <dir> --skip-skills`. Create a root HTML composition and put separate scenes, source media, and locally scoped fonts in project directories. Keep user-editable text, colors, and media as explicit variables where appropriate.
3. Declare timed clips with `class="clip"`, `data-start`, and `data-duration`. Use stable IDs, a paused GSAP timeline per composition, and register it in `window.__timelines` under its composition ID. Drive visuals by timeline position. Keep timeline seeking independent of randomness, wall clock, and network calls. Use CSS stacking for paint order.
4. Animate the before-and-after boundary across aligned frames. Keep critical text away from platform controls and inspect the actual center profile crop. For Persian, use a shaping-capable font, RTL text direction, and isolated Latin labels.
5. Use only music permitted for the requested use and include any required credit. Time accents and transitions to the chosen audio. Keep output settings appropriate for the destination, including portrait 1080 × 1920 when the brief calls for a vertical Reel.

## Preview and render

- Use `npx hyperframes preview` to inspect motion in the browser when available. Run `npx hyperframes check --json` and review start, transition, ending, and cover frames. Confirm the current version's snapshot and render flags with `--help`.
- Export the requested deliverable with the CLI, or use an available renderer if the target environment cannot run the HyperFrames render path. Verify codec, aspect ratio, duration, frame rate, and audio on the actual output. State which renderer produced the deliverable when you switch.
- Keep upload and publishing separate from rendering. Use the requested account, destination and local timezone and verify the status reported by the publishing service.

Source selection: [Awesome Claude Video Skills](https://github.com/zhuyansen/awesome-claude-video-skills). Workflow reference: [HeyGen HyperFrames](https://github.com/heygen-com/hyperframes), Apache-2.0.

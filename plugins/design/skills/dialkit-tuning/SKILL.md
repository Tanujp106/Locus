---
name: dialkit-tuning
description: Use when adding or using DialKit to tune interface parameters, motion, layout, color, or animation locally without shipping the tuning surface as product UI.
---

# DialKit Tuning

Use DialKit as a local development instrument, not as a second design system. The README is the API reference; this skill contains the preferences and judgment rules for using it.

## Preferences

- Keep DialKit development-only by default; never enable `productionEnabled` unless explicitly requested.
- Preserve the existing visual direction, copy, spacing, interaction behavior, tokens, and component boundaries.
- Use DialKit’s standard/default surface. Do not custom-design, restyle, rename, or replace the panel.
- Mount one `DialRoot` and register meaningful, separate `useDialKit` panels for distinct subjects.
- Expose existing source-of-truth variables/configuration; do not create a parallel animation, layout, or theme system.
- Expose the important controls needed for the requested behavior, but do not expose arbitrary implementation details.
- Treat exact user-provided values, selectors, dimensions, colors, and wording as literal constraints.
- Verify the panel is actually mounted, visible, and changing the intended UI; installation alone is not success.

DialKit already hides its root and timeline UI in production by default. Keep that safety behavior and add a framework-appropriate development guard when useful.

## Authoring rules

- Wire returned values into the existing CSS-variable, typed-config, Motion, or component-prop pipeline.
- Use `satisfies DialConfig` for mutable config tuples; avoid `as const` when it creates readonly-tuple errors.
- Use stable panel IDs when a logical panel must reconnect across remounts or pages.
- Use persistence only for intentional local iteration, with an explicit namespaced key; never make local tuning state shared product state.
- Use presets or JSON Copy to capture candidate values, then move accepted values into source/CSS or the real animation system.
- Use `useDialKitController` only when programmatic reset, local presets, URL synchronization, or updates are genuinely needed.
- Use `useDialTimeline`/`DialTimeline` for scrubbing, clip timing, spring/easing comparison, replay, looping, or event-driven playback—not for ordinary live dials.
- For timeline authoring: tune through `clip.current`, copy the result, move it into the real Motion/CSS animation, and remove the timeline authoring path when it is no longer needed.
- Hiding `<DialTimeline />` is not enough if the component still reads `clip.current`; DialKit is still driving the rendering.

## Diagnose before changing source

- Package or stylesheet missing: check the manifest and install before rewriting imports.
- Panel invisible: verify `DialRoot`, hook wiring, and the inspected route.
- Deleted modules still appear: clear only the relevant stale build cache and restart the existing process.
- Readonly tuple error: replace frozen tuples with `satisfies DialConfig` or another mutable compatible type.
- Values disappear: connect controls to the real source of truth and use intentional local persistence if needed.
- Browser shows old behavior: use a fresh tab or hard reload before changing working code.

Do not redesign the panel, add a second animation system, or broaden the refactor before checking dependency presence, mounted paths, active processes, and stale output.

## Minimum verification

- Run focused tests for DialKit wiring and exposed controls.
- Run the project’s normal diff and type/build checks.
- Use browser verification only when visibility, live tuning, layout, or runtime behavior cannot be proven in code.
- When browser testing is needed, use the already-running development port; never silently create a fallback port.
- Confirm the local panel changes the intended UI and production rendering does not show it.
- Report unavailable browser evidence honestly; a successful install, HTTP 200, or build is not visual proof.

## Definition of done

The standard DialKit integration is visible locally, controls map to existing source-of-truth values, accepted exploratory values have been transferred into the real implementation, production behavior remains unchanged, and focused verification passes.

## Reference

Consult the [DialKit README](https://github.com/joshpuckett/dialkit) for current API details instead of duplicating them here.

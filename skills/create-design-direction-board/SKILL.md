---
name: create-design-direction-board
description: Use when a designer wants researched design directions turned into an interactive, shareable HTML artifact with multiple selectable high-fidelity interfaces, reasoning, tradeoffs, and source links, or wants a selected direction refined without relying on Figma.
---

# Design Direction Board

You are a product designer and front-end prototyper. Convert researched direction briefs into one interactive, original, high-fidelity HTML artifact that helps a designer compare and select a direction.

Use with `find-design-references` and either `find-divergent-design-references` for exploration or `find-convergent-design-references` for refinement. Let those skills own evidence and design judgment; this skill owns interface execution and presentation.

## Input Contract

Use the supplied project brief, constraints, requested direction count, and structured direction briefs. Each brief should identify its core idea, changed assumptions, layout, hierarchy, visual system, data representation, interaction, tradeoff, and inspected canonical sources.

If direction briefs are missing, complete the relevant reference workflow before building. Never invent source products, links, observed patterns, or unsupported rationale.

## Artifact Contract

Create one self-contained HTML file with embedded CSS and minimal vanilla JavaScript. It must open directly without a build step, framework, Figma, server, or external runtime dependency.

Include:

- a floating or sticky sidebar with one descriptively named option per direction
- one direction visible at a time, with clear selected state
- previous and next controls
- keyboard-accessible native controls and logical focus order
- URL hashes such as `#direction-4` that restore and share the selected direction
- responsive comparison chrome while preserving the intended product viewport
- concise reasoning, tradeoff, and canonical source links for every direction

Use the requested direction count; default to 10 when unspecified. Generate direction names from the research rather than a fixed list.

## High-Fidelity Standard

Every direction must be an original, complete product interface—not a moodboard, screenshot, wireframe, schematic, or rough reconstruction.

Resolve all relevant:

- layout, hierarchy, grid, spacing, typography, colour, and elevation
- navigation, controls, icons, cards, tables, charts, and data states
- realistic domain content, labels, values, units, timestamps, and statuses
- empty, loading, error, selection, or comparison states when material to the concept
- responsive behaviour, contrast, legibility, and interaction feedback

Do not use placeholder boxes, lorem ipsum, decorative charts without meaning, fake controls, clipped content, or unfinished sections. Use inline SVG for charts and simple icons when assets are not supplied.

## Preserve Useful Comparability

Keep the product objective, audience, core information, and non-negotiable constraints consistent across directions. Vary the solution meaningfully through structure, hierarchy, disclosure, navigation, density, representation, interaction, or visual expression.

Do not present colour swaps or cosmetic reskins as separate directions. Each direction must embody a distinct researched strategy and remain feasible enough to inform a real design decision.

## Page Structure

1. **Direction navigation:** names and current selection.
2. **High-fidelity interface:** the dominant area; show one complete direction.
3. **Reasoning:** core idea, defining decisions, project fit, and key tradeoff.
4. **Evidence:** canonical links that informed the direction and the specific principle transferred.

Keep explanations secondary to the interface. Do not add scoring, filters, dashboards about the research, or controls the user did not request.

## Implementation Rules

- Use semantic HTML, scoped CSS, and small readable JavaScript.
- Store selection in the URL hash; handle initial load, clicks, browser history, and invalid hashes.
- Use buttons for direction controls and expose selection with `aria-current` or `aria-selected`.
- Keep each direction's markup and styling capable of meaningful structural variation.
- Avoid external libraries unless the requested design cannot be achieved reasonably without one.
- When publishing is requested, preserve the standalone artifact and use the available hosting workflow.

## Convergent Updates

When refining a selected direction, change only that direction and shared infrastructure required by it. Preserve other directions, source traceability, navigation, and shareable hashes unless the user asks to remove them.

## Final Check

- Research was completed and inspected before creation.
- Every direction is original, high fidelity, distinct, and project-relevant.
- Realistic content and meaningful data visualisation are present.
- Sidebar, keyboard controls, previous/next, and URL hashes work.
- The first render is complete and no content clips at supported widths.
- Reasoning and canonical sources match each direction.
- The file opens independently and requires no Figma or build process.

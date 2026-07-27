# Locus agent instructions

Locus is a portable collection of reusable agent skills.

## Browser testing

Use the browser when the task changes browser-visible UI or interaction behavior, the user asks for visual verification, code-level checks are inconclusive, the change is cross-cutting or high-risk, or the issue reproduces only in the browser.

Prefer focused code inspection, tests, type checks, linting, and existing runtime checks when browser verification is not needed.

When browser testing is needed, use the already-running app port. Create or start a port only if no app is running. Keep browser testing focused on the affected route and behavior.

## Skill use

Use the smallest relevant skill. Preserve explicit user scope, verify the requested end state, and report environment or authentication boundaries honestly.

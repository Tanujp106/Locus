# Mobbin Research Playbook

Read this file only when Mobbin is useful or explicitly requested.

## Route the Request

| Artifact | Mobbin action | Parameters |
|---|---|---|
| App screen, mobile component, web app UI, bottom sheet, card, or navigation | `mobbin_search_screens` | Set `platform` to `ios` or `web`. Use `deep` for nuanced discovery and `standard` for quick literal lookup. |
| Multi-step journey such as onboarding, checkout, transfer, or account setup | `mobbin_search_flows` | Search one journey at a time. Set `platform` to `ios` or `web`. |
| Marketing-site section such as hero, pricing, navbar, or footer | `mobbin_search_sections` | Search one website section at a time. Do not use for in-product mobile components. |

## Write Effective Queries

- Describe one screen, journey, or section in natural language.
- State visible elements and how they relate; avoid vague style words.
- Do not combine intents, use negations, pass keyword lists, or repeat the platform in the query.
- Name an app only when filtering to that product.

Example: `dashboard overview with a primary balance, comparison data, and compact financial insight cards`.

## Search in Passes

1. Search mature category leaders by product and target artifact.
2. Search the task or pattern without an app name to discover alternatives.
3. Search meaningful surrounding states or journey variants separately.
4. Add smaller or adjacent products only when they contribute a distinct solution.

Start with 4–8 results. Paginate or exclude seen screen IDs only when more coverage could add a new pattern.

## Evidence Rules

- Inspect returned images before describing them; metadata is not visual evidence.
- Preserve each canonical `mobbin_url` and identifier.
- Link every mentioned screen, flow, or section to its Mobbin URL.
- Do not infer unseen interactions, states, or rationale.
- If Mobbin was explicitly requested but unavailable, state the gap and provide exact queries. Do not silently substitute another source.

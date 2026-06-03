# Newsletter UI Kit · The Civic Node

A high-fidelity recreation of the publication as it appears to a reader on Substack.

> The brand has one product: a weekly Substack newsletter at `drinkyouroj.substack.com`. There is no app, no dashboard, no marketing site. This kit recreates the **reader-facing surfaces** only.

## Files
- `index.html` — homepage / archive: masthead + issue list + sidebar
- `issue.html` — reading view of a single dispatch (clickable from the homepage)
- `cover.html` — share-card / banner template (1500×500, Bluesky proportions)
- `components/Masthead.jsx` — logo + nav + tagline
- `components/IssueRow.jsx` — single archive row
- `components/Dispatch.jsx` — full reading view body
- `components/Disclosure.jsx` — standard disclosure block

## What is interactive
- Click an issue row on the home page → opens the reading view.
- Subscribe field accepts an email and shows a confirmation state.
- The "Read more" arrow on the issue row reveals the lede inline.

## What is not implemented (intentionally)
- Real comments, restacks, hearts (these belong to the Substack platform — we don't reskin them).
- Search.
- Settings / account.

If you need any of the above, ask before adding — they are not in the brand's source material.

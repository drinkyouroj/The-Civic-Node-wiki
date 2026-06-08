# workspace/engagement/

Runtime output of the `tcn-substack-engagement` skill. One file per day:
`YYYY-MM-DD-worksheet.md`. Each worksheet is **paste-ready** — the user opens each permalink, pastes,
and clicks. The skill never writes to Substack; everything here is executed by hand.

Each dated worksheet also doubles as a **local dedup ledger**: the next day's run reads recent
worksheets to supplement the live Likes & Replies / own-Notes dedup read (the live read stays the source
of truth).

## Worksheet template

```markdown
# Engagement Worksheet — YYYY-MM-DD

**Built from:** workspace/notes/YYYY-MM-DD-<weekday>-options.md
**Account verified:** @drinkyouroj
**Dedup summary:** <one line — what was already-spent and skipped, incl. any angle dropped for echoing the day's own Notes>

## Comments
- [ ] **<Author> (@handle)** · <permalink>
  - *Their note:* <1-line gist>
  - *Paste:* <the comment text, voice-checked>
  - *Why:* <which plan angle; why unspent>

## Restacks
- [ ] **<Author>** · <permalink>
  - *Their note:* <1-line gist>
  - *Paste (restack note):* <one sentence of added analysis>

## Follows
- [ ] **<Account>** · <profile link>
  - *Why:* <one line — how this trains the audience-aligned algorithm>
```

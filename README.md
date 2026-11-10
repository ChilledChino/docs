# ChilledChino public docs

Source for ChilledChino's public documentation.

```
public-docs/
├── navigation.json   sidebar tree (page / folder nodes, each page -> a content file by url)
├── content/          markdown, one file per page
│   ├── index.md            -> /docs
│   ├── getting-started.md  -> /docs/getting-started
│   ├── ai/
│   │   ├── overview.md     -> /docs/ai/overview
│   │   └── limits.md       -> /docs/ai/limits
│   └── privacy/
│       └── overview.md     -> /docs/privacy/overview
└── images/           assets referenced from markdown
```

## navigation.json

Maps the sidebar. A `page` node has a `name` and a `url`; a `folder` node has a `name` and `children`. A page's `url` maps to a content file: `/docs` → `content/index.md`, `/docs/<path>` → `content/<path>.md`.

It can be edited by hand, or regenerated from the files in `content/` by the GitHub Action in `.github/workflows/`. The generator keeps the existing order and names where a page already appears, and appends any new content files it finds. Run it locally with:

```
python scripts/gen_nav.py
```

## Writing

- Straight to the point. State the fact, not the journey to it.
- Prefer tables and short lists over long prose.
- Ground every claim in the running system. The source of truth for AI behavior is `ChilledChino/AI_RULES.md` in the bot repo.

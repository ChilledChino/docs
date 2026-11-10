#!/usr/bin/env python3
"""Regenerate navigation.json from the markdown files in content/.

A page's url maps to a content file:
    /docs            -> content/index.md
    /docs/<path>     -> content/<path>.md

The generator preserves the order, names and folder grouping already in
navigation.json, and appends any content file that has no node yet. New pages
get a title from the file's first H1, falling back to the file name.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
NAV = ROOT / "navigation.json"
SITE_NAME = "ChilledChino Documentation"


def url_for(md: Path) -> str:
    rel = md.relative_to(CONTENT).with_suffix("")
    if rel.name == "index" and rel.parent == Path("."):
        return "/docs"
    return "/docs/" + rel.as_posix()


def title_for(md: Path) -> str:
    for line in md.read_text(encoding="utf-8").splitlines():
        m = re.match(r"#\s+(.+)", line.strip())
        if m:
            return m.group(1).strip()
    return md.stem.replace("-", " ").title()


def existing_urls(node: dict) -> set[str]:
    urls: set[str] = set()
    for child in node.get("children", []):
        if child.get("type") == "page":
            urls.add(child["url"])
        elif child.get("type") == "folder":
            urls |= existing_urls(child)
    return urls


def folder_for(url: str) -> str | None:
    # /docs/ai/overview -> "ai"; /docs/getting-started -> None
    parts = url.removeprefix("/docs").strip("/").split("/")
    return parts[0] if len(parts) > 1 else None


def main() -> None:
    if NAV.exists():
        nav = json.loads(NAV.read_text(encoding="utf-8"))
    else:
        nav = {"name": SITE_NAME, "children": []}

    have = existing_urls(nav)
    pages = sorted(CONTENT.rglob("*.md"), key=lambda p: url_for(p))

    for md in pages:
        url = url_for(md)
        if url in have:
            continue
        page = {"type": "page", "name": title_for(md), "url": url}
        folder = folder_for(url)
        if folder is None:
            nav["children"].append(page)
        else:
            node = next(
                (c for c in nav["children"]
                 if c.get("type") == "folder" and c.get("name", "").lower() == folder.lower()),
                None,
            )
            if node is None:
                node = {"type": "folder", "name": folder.title(), "children": []}
                nav["children"].append(node)
            node["children"].append(page)

    NAV.write_text(json.dumps(nav, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"navigation.json: {len(pages)} page(s) on disk")


if __name__ == "__main__":
    main()

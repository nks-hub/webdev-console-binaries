#!/usr/bin/env python3
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from typing import Dict, List


START_MARKER = "<!-- RELEASE_TABLE_START -->"
END_MARKER = "<!-- RELEASE_TABLE_END -->"


def gh_api(url: str, token: str) -> Dict:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_releases(repo: str, token: str) -> List[Dict]:
    releases: List[Dict] = []
    page = 1
    while True:
        params = urllib.parse.urlencode({"per_page": 100, "page": page})
        url = f"https://api.github.com/repos/{repo}/releases?{params}"
        chunk = gh_api(url, token)
        if not chunk:
            break
        releases.extend(r for r in chunk if not r.get("draft"))
        if len(chunk) < 100:
            break
        page += 1
    releases.sort(key=lambda r: r.get("published_at") or "", reverse=True)
    return releases


def first_nonempty_line(text: str) -> str:
    for raw in (text or "").splitlines():
        line = raw.strip()
        if line:
            return line
    return "-"


def md_escape(text: str, limit: int = 140) -> str:
    out = (text or "-").replace("\r", " ").replace("\n", " ").strip()
    out = re.sub(r"\s+", " ", out)
    out = out.replace("|", r"\|")
    if len(out) > limit:
        out = out[: limit - 3].rstrip() + "..."
    return out


def build_table(repo: str, releases: List[Dict]) -> str:
    lines = [
        START_MARKER,
        "| Tag | Name | Published | Assets | Description |",
        "| --- | --- | --- | ---: | --- |",
    ]
    for rel in releases:
        tag = rel.get("tag_name", "-")
        name = md_escape(rel.get("name") or "-")
        published = (rel.get("published_at") or "-")[:10]
        assets = len(rel.get("assets") or [])
        desc = md_escape(first_nonempty_line(rel.get("body") or ""))
        tag_url = rel.get("html_url") or f"https://github.com/{repo}/releases/tag/{tag}"
        lines.append(f"| [{md_escape(tag)}]({tag_url}) | {name} | {published} | {assets} | {desc} |")
    lines.append(END_MARKER)
    return "\n".join(lines) + "\n"


def update_readme(path: str, block: str) -> bool:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL)
    if pattern.search(content):
        updated = pattern.sub(block.strip(), content)
    else:
        section = "\n## Release Catalog\n\n" + block
        updated = content.rstrip() + "\n" + section
    if updated == content:
        return False
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(updated)
    return True


def main() -> int:
    readme_path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    repo = os.environ.get("GITHUB_REPOSITORY", "nks-hub/webdev-console-binaries")
    token = os.environ.get("GITHUB_TOKEN", "")
    releases = fetch_releases(repo, token)
    table_block = build_table(repo, releases)
    changed = update_readme(readme_path, table_block)
    print(f"Updated: {changed}; releases: {len(releases)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

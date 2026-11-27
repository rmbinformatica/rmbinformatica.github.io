#!/usr/bin/env python3
"""Validate the redirect manifest and export a Cloudflare Bulk Redirect CSV."""
import argparse
import csv
import json
import re
from pathlib import Path

ORIGIN = "https://rmbinformatica.com"

def load_redirects(path):
    # JSON subset of YAML keeps Python tooling dependency-free.
    content = "\n".join(line for line in path.read_text(encoding="utf-8").splitlines()
                        if not line.lstrip().startswith("#"))
    data = json.loads(content)
    if not isinstance(data, dict) or set(data) != {"redirects"} or not isinstance(data["redirects"], list):
        raise ValueError("Expected a redirects list")
    result = {}
    for rule in data["redirects"]:
        if not isinstance(rule, dict) or set(rule) != {"from", "to", "status"} or rule["status"] != 301:
            raise ValueError("Expected from, to and status 301")
        source, dest = rule["from"], rule["to"]
        for p in (source, dest):
            if not isinstance(p, str) or not re.fullmatch(r"/[A-Za-z0-9._~/%-]*", p) or "//" in p or "%" in p or any(s in (".", "..") for s in p.split("/")):
                raise ValueError(f"Invalid local path: {p!r}")
        if source == dest or source in result:
            raise ValueError(f"Self redirect or duplicate: {source}")
        if source in ("/", "/sitemap.xml", "/feed.xml", "/robots.txt"):
            raise ValueError(f"Protected route: {source}")
        result[source] = dest
    for source, dest in result.items():
        if dest in result:
            raise ValueError(f"Redirect chain or cycle: {source} -> {dest}")
    return {ORIGIN + k: ORIGIN + v for k,v in result.items()}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=Path("_data/redirects.yml"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    redirects = load_redirects(args.manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for source, dest in sorted(redirects.items()):
            # status, preserve query string, include subdomains, subpath matching, preserve path suffix
            writer.writerow([source, dest, 301, "TRUE", "FALSE", "FALSE", "FALSE"])
    print(f"Exported {len(redirects)} redirect rules to {args.output}")

if __name__ == "__main__":
    main()

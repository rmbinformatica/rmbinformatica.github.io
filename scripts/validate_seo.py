#!/usr/bin/env python3
"""Validate production SEO artifacts without network or third-party dependencies."""
import argparse
from pathlib import Path
from urllib.parse import urlsplit, unquote
from xml.etree import ElementTree as ET
from html.parser import HTMLParser

ORIGIN = "https://rmbinformatica.com"
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
ATOM = "{http://www.w3.org/2005/Atom}"
errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

def sitemap(root):
    tree = ET.parse(root / "sitemap.xml").getroot()
    if tree.tag != NS + "urlset":
        raise ValueError("Expected a sitemap urlset")
    urls = [n.text.strip() for n in tree.findall(NS+"url/"+NS+"loc") if n.text]
    check(bool(urls), "Empty sitemap")
    check(len(urls) == len(set(urls)), "Duplicate sitemap URLs")
    return set(urls)

def target(root, url):
    u = urlsplit(url)
    if u.scheme != "https" or u.netloc != "rmbinformatica.com" or u.query or u.fragment:
        return None
    path = unquote(u.path).lstrip("/")
    if ".." in Path(path).parts:
        return None
    p = root / path
    for candidate in (p, p/"index.html", Path(str(p)+".html")):
        if candidate.is_file() and candidate.resolve().is_relative_to(root.resolve()):
            return candidate
    return None

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonicals = []
        self.alternates = {}
    def handle_starttag(self, tag, attrs):
        if tag != "link":
            return
        a = dict(attrs)
        rel = (a.get("rel") or "").lower().split()
        if "canonical" in rel:
            self.canonicals.append(a.get("href"))
        if "alternate" in rel and a.get("hreflang"):
            lang = a["hreflang"].lower()
            check(lang not in self.alternates, "Duplicate hreflang: " + lang)
            self.alternates[lang] = a.get("href")

def links(path):
    parser = Links()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site", type=Path)
    ap.add_argument("--baseline", type=Path)
    args = ap.parse_args()
    root = args.site
    for name in ("sitemap.xml", "feed.xml", "robots.txt"):
        check((root/name).is_file(), "Missing " + name)
    if errors:
        raise SystemExit("\n".join(errors))
    urls = sitemap(root)
    feed = ET.parse(root/"feed.xml").getroot()
    check(feed.tag == ATOM+"feed", "Invalid Atom feed")
    robots = (root/"robots.txt").read_text().splitlines()
    check("Sitemap: "+ORIGIN+"/sitemap.xml" in robots, "Incorrect robots sitemap")
    check(not any(line.strip().lower() == "disallow: /" for line in robots), "Production robots blocks entire site")
    baseline = sitemap(args.baseline) if args.baseline else set()
    for url in sorted(baseline - urls):
        # Documentation is intentionally removed; all other historical destinations must survive.
        if urlsplit(url).path.lower() not in ("/readme", "/readme.html", "/readme.md"):
            check(target(root,url) is not None, "Historical route missing: "+url)
    parsed = {}
    for url in sorted(urls):
        p = target(root,url)
        check(p is not None, "Invalid or missing sitemap target: "+url)
        if p and p.suffix.lower() == ".html":
            parsed[url] = links(p)
            c = parsed[url].canonicals
            # Legacy HTML may lack canonical; new indexable HTML must provide one.
            if url in baseline and not c:
                print("Legacy canonical missing (review before release):", url)
            else:
                check(len(c)==1 and c[0]==url, "Canonical mismatch: "+url+" "+str(c))
    for url, meta in parsed.items():
        for lang, href in meta.alternates.items():
            other = parsed.get(href)
            check(other is not None, "Hreflang target missing: "+url+" "+str(href))
            if other:
                check(url in other.alternates.values(), "Hreflang not reciprocal: "+url+" "+str(href))
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"SEO checks passed for {len(urls)} sitemap URLs; {len(baseline)} historical URLs compared.")

if __name__ == "__main__":
    main()

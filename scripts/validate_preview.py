#!/usr/bin/env python3
"""Check generated preview pages independently of production sitemap checks."""
from pathlib import Path
from html.parser import HTMLParser
from xml.etree import ElementTree as ET
import sys

LANGS = {"pt-BR", "en", "es", "it", "fr", "de"}
ROUTES = {lang: "/preview-v2/" + (lang + "/" if lang != "pt-BR" else "") for lang in LANGS}

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = None
        self.noindex = False
        self.hreflang = {}
        self.alternates = []
        self.analytics = False
        self.categories = set()
        self.category_tones = {}
        self.flags = 0
        self.globe_images = set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("data-category"):
            self.categories.add(a["data-category"])
            self.category_tones[a["data-category"]] = a.get("data-tone")
        if tag == "svg" and "rmb-flag" in (a.get("class") or "").split():
            self.flags += 1
        if tag == "img" and (a.get("class") or "").startswith("rmb-globe-"):
            self.globe_images.add(a.get("src"))
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "meta" and a.get("name") == "robots":
            self.noindex = "noindex" in (a.get("content") or "").lower()
        if tag == "a" and a.get("hreflang"):
            self.hreflang[a["hreflang"]] = a.get("href")
        if tag == "link" and a.get("hreflang"):
            self.alternates.append(a.get("href"))
        if tag == "script" and "googletagmanager.com" in (a.get("src") or ""):
            self.analytics = True

def main():
    root = Path(sys.argv[1])
    sitemap = ET.parse(root / "sitemap.xml")
    urls = [n.text or "" for n in sitemap.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    assert not any("/preview-v2/" in u for u in urls), "Preview leaked into sitemap"
    for lang, route in ROUTES.items():
        path = root / route.lstrip("/") / "index.html"
        page = Page()
        html = path.read_text(encoding="utf-8")
        page.feed(html)
        assert "05.930.393/0001-56" in html and "© 2003–" in html, route
        if lang == "pt-BR":
            assert "RMB Informática | Infraestrutura, Suporte de TI e Software em Natal/RN" in html, route
            assert "1998" in html and "Desde 2003" in html, route
            assert html.count(">Saiba mais</a>") == 6, "Missing home solution link"
            assert 'href="/servicos/hospedagem-e-nuvem/"' in html and 'href="/servicos/consultoria-de-ti-natal"' in html, route
            assert 'id="rmb-chat-load"' in html and 'src="/assets/js/online-chat.js"' in html, route
            assert 'src="https://www.intergram.xyz/js/widget.js"' not in html, "Chat loaded without user action"
            assert 'application/ld+json' in html, route
            assert 'id="rmb-featured-title"' in html and html.count('class="rmb-feature-card') == 6, "Missing featured services"
            assert 'href="/servicos/monitoramento-de-disponibilidade"' in html, route
            assert 'class="rmb-hero-network"' in html, route
            for tone in ('msp','cloud','security','automation','diagnostic','monitor','ai'):
                assert f'data-tone="{tone}"' in html, tone
            assert html.count('data-tone=') == 28, route
            assert page.category_tones == {"infra":"msp","msp":"msp","servers":"msp","cloud":"cloud","security":"security","backup":"security","mail":"cloud","software":"automation","devops":"cloud","automation":"automation","data":"diagnostic","finance":"automation","open":"cloud","web":"automation","consulting":"diagnostic","ai":"ai"}, "Incorrect category palette"
            assert '/assets/css/rmb.css?v=' in html, route
        assert page.lang == lang, f"{route}: wrong HTML language"
        assert page.noindex, f"{route}: missing noindex"
        assert not page.alternates, f"{route}: unexpected SEO alternate"
        assert not page.analytics, f"{route}: analytics enabled"
        expected = {k:v for k,v in ROUTES.items() if k != lang}
        assert len(page.categories) == 16, f"{route}: missing categories"
        assert page.flags == 6, f"{route}: missing flags"
        assert page.globe_images == {'/assets/brand/globe-light.svg', '/assets/brand/globe-dark.svg'}, f"{route}: wrong globe assets"
        assert page.hreflang == expected, f"{route}: incorrect language selector {page.hreflang}"
    for asset in ("assets/css/rmb.css", "assets/js/theme.js", "assets/brand/globe-light.svg", "assets/brand/globe-dark.svg"):
        assert (root / asset).is_file(), f"Missing asset {asset}"
    blog = (root / "blog/index.html").read_text(encoding="utf-8")
    assert "rmb-blog-grid" in blog and "assets/css/rmb.css" in blog, "Blog not using redesign"
    print("All six preview pages passed language, navigation, noindex and asset checks.")

if __name__ == "__main__":
    main()

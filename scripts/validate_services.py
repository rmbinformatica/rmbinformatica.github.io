from pathlib import Path
from xml.etree import ElementTree as ET
import sys
root=Path(sys.argv[1])
slugs=["hospedagem-de-sites","hospedagem-email","hospedagem-de-sistemas","gerenciamento-cpanel","consultoria-cloudflare"]
urls={n.text for n in ET.parse(root/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
for slug in slugs:
    route='/servicos/'+slug
    candidates=[root/(route.lstrip('/')+'.html'), root/route.lstrip('/')/'index.html',root/route.lstrip('/')]
    page=next((p for p in candidates if p.is_file()),None)
    assert page is not None, route
    html=page.read_text(encoding='utf-8')
    assert 'rmb-service-grid' in html and 'Solicitar proposta comercial' in html, route
    assert 'https://rmbinformatica.com'+route in urls, route
category=(root/'servicos/hospedagem-e-nuvem/index.html').read_text(encoding='utf-8')
for slug in slugs:
    assert 'href="/servicos/'+slug+'"' in category, slug
print('Five service pages and category validated')

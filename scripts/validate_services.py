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

# Exercise actual HTTP requests with the same local preview server distributed in ZIP.
from threading import Thread
from urllib.request import urlopen
from preview_server import make_server
server=make_server(root, port=0)
thread=Thread(target=server.serve_forever, daemon=True)
thread.start()
try:
    for route in ['/preview-v2/', '/servicos/hospedagem-e-nuvem/'] + ['/servicos/'+s for s in slugs]:
        with urlopen(f'http://127.0.0.1:{server.server_port}{route}', timeout=10) as response:
            assert response.status == 200, route
            assert 'text/html' in response.headers.get('Content-Type',''), route
            if route in ['/servicos/'+s for s in slugs]:
                assert b'rmb-proposal-form' in response.read(), route
finally:
    server.shutdown()
    server.server_close()
    thread.join()
print('HTTP smoke test passed for seven routes')

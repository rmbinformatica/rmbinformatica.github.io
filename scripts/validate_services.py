from pathlib import Path
from xml.etree import ElementTree as ET
import sys
root=Path(sys.argv[1])
slugs=["hospedagem-de-sites","hospedagem-email","hospedagem-de-sistemas","gerenciamento-cpanel","consultoria-cloudflare","assessoria-registro-de-dominios"]
cloud_slugs=slugs.copy()
msp_slugs=["gerenciamento-de-redes","suporte-de-ti-para-empresas","suporte-n2-terceirizado","monitoramento-de-infraestrutura","dba-remoto","gerenciamento-de-servidores","virtualizacao-de-servidores","consultoria-docker","implantacao-service-desk"]
server_slugs=["servidores-em-natal","windows-server","servidores-linux"]
infra_slugs=["redes-corporativas-natal","cabeamento-estruturado-natal","wifi-corporativo-natal"]
security_slugs=["firewall-corporativo","vpn-empresarial","redundancia-de-internet-natal"]
backup_slugs=["backup-corporativo"]
slugs+=msp_slugs+server_slugs+infra_slugs+security_slugs+backup_slugs
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
for slug in cloud_slugs:
    assert 'href="/servicos/'+slug+'"' in category, slug
msp=(root/'servicos/servicos-gerenciados-ti/index.html').read_text(encoding='utf-8')
for slug in msp_slugs:
    assert 'href="/servicos/'+slug+'"' in msp, slug
for category_slug, category_slugs in [('sistemas-e-servidores', ["servidores-em-natal","windows-server","servidores-linux","virtualizacao-de-servidores","dba-remoto","gerenciamento-de-servidores"]), ('infraestrutura-empresarial', ["redes-corporativas-natal","cabeamento-estruturado-natal","wifi-corporativo-natal"])]:
    category_html=(root/'servicos'/category_slug/'index.html').read_text(encoding='utf-8')
    for slug in category_slugs:
        assert 'href="/servicos/'+slug+'"' in category_html, slug
for category_slug, category_slugs in [('seguranca-e-conectividade', ["firewall-corporativo","vpn-empresarial","redundancia-de-internet-natal","suporte-de-ti-para-empresas"]), ('backup-e-continuidade', ["backup-corporativo"])]:
    category_html=(root/'servicos'/category_slug/'index.html').read_text(encoding='utf-8')
    for slug in category_slugs:
        assert 'href="/servicos/'+slug+'"' in category_html, slug
print('All service pages and categories validated')

# Exercise actual HTTP requests with the same local preview server distributed in ZIP.
from threading import Thread
from urllib.request import urlopen
from preview_server import make_server
server=make_server(root, port=0)
thread=Thread(target=server.serve_forever, daemon=True)
thread.start()
try:
    for route in ['/preview-v2/', '/servicos/hospedagem-e-nuvem/', '/servicos/servicos-gerenciados-ti/', '/servicos/sistemas-e-servidores/', '/servicos/infraestrutura-empresarial/', '/servicos/seguranca-e-conectividade/', '/servicos/backup-e-continuidade/'] + ['/servicos/'+s for s in slugs]:
        with urlopen(f'http://127.0.0.1:{server.server_port}{route}', timeout=10) as response:
            assert response.status == 200, route
            assert 'text/html' in response.headers.get('Content-Type',''), route
            if route in ['/servicos/'+s for s in slugs]:
                assert b'rmb-proposal-form' in response.read(), route
finally:
    server.shutdown()
    server.server_close()
    thread.join()
print('HTTP smoke test passed for all commercial routes')

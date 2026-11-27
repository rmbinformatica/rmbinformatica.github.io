# Arquitetura RMB v2.0
Status: direção aprovada; implementação incremental.
Jekyll + GitHub Pages; manter master em produção. Site estático com conteúdo Markdown, Liquid, HTML semântico, CSS próprio e JS vanilla.
## Navegação
Empresa (história, competências, atuação, cases autorizados); Serviços (16 categorias, páginas específicas); Parcerias B2B; Projetos; Recursos (blog, ferramentas e ajuda); Contato.
## Estrutura
_data/ para dados públicos; _servicos/ para páginas localizadas; _layouts/ e _includes/ compartilhados; assets/ para CSS, JS, imagens e fontes; _posts/ preservado; _docs/ excluído.
Português na raiz, demais idiomas em /en/, /es/, /it/, /fr/, /de/.
Inventário privado: 155 serviços, 16 categorias em 26/11/2026. Não equivale a 155 páginas. Exportar apenas dados públicos autorizados; nunca copiar a planilha integral.
Preservar /servicos/hospedagem-email, /contato.html, /blog/, /about/ e URLs de posts existentes até inventário de rotas e decisão de redirecionamento. Manter formulário atual até validação do endpoint.
## Entrega
Build em branch de desenvolvimento, sem deployment automático; teste de rotas, metadados, acessibilidade, desempenho e exclusões. Merge apenas com aprovação.

## Páginas orientadas ao público e ao problema
Separar serviço comercial (ID estável) de landing page (ID próprio). Um serviço pode ter várias páginas por idioma, inclusive técnica, não técnica ou por problema/setor, quando a necessidade de compra justificar conteúdo distinto. Uma página pode representar vários serviços. Centralizar o cadastro público dos serviços; não duplicar o inventário. Navegação principal apresenta o catálogo sem multiplicar entradas; páginas especializadas são ligadas contextualmente.

## Migração de URLs
Cloudflare Bulk Redirects é a camada aprovada para HTTP 301; GitHub Pages permanece como origem. _data/redirects.yml é a fonte versionada de migrações aprovadas. CI valida mapa e exporta CSV como artefato; configuração da conta Cloudflare e ativação ficam sujeitas à aprovação e validação HTTP. Não criar mapeamentos fictícios antes dos destinos definitivos.

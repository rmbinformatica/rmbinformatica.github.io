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

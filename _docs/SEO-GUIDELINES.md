# SEO
Preservar rotas indexadas e registrar redirecionamentos antes de mudanças. Canonical absoluto próprio. Título, descrição, H1 e conteúdo específicos por página e idioma. Links internos reais, breadcrumbs, sitemap, hreflang recíproco e dados estruturados fiéis (Organization, Service, BreadcrumbList quando aplicável). Não inventar avaliações ou usar páginas duplicadas para variantes de palavras-chave.
Verificar Search Console, indexação, conversões e desempenho. Dados privados de pesquisa não devem ser publicados.

## Intenção de busca e variações por público
Pesquisar tanto termos especializados quanto perguntas e sintomas em linguagem cotidiana, por idioma. Criar páginas distintas apenas se intenção, público, conteúdo e proposta comercial forem materialmente diferentes; caso contrário, consolidar em uma página com explicações em camadas. Evitar doorway pages e canibalização; cada página independente tem canonical próprio, links contextuais e metadados únicos. Monitorar consultas, conversões e sobreposição antes de manter, fundir ou redirecionar variantes. Hreflang relaciona traduções da mesma landing page, não páginas de públicos diferentes.

## Critérios obrigatórios de aceitação
- Manter https://rmbinformatica.com/sitemap.xml e /feed.xml; validar XML, origem HTTPS e existência dos destinos do sitemap no build.
- robots.txt de produção deve anunciar o sitemap e não bloquear todo o site.
- URLs canônicas próprias e hreflang recíproco para traduções reais; x-default quando aplicável. Não relacionar variantes editoriais distintas.
- Comparar rotas históricas com a versão de referência; qualquer remoção exige redirecionamento explícito, aprovação e teste do status/destino na hospedagem real.
- Preservar verificações existentes do Search Console e Analytics; após publicação, conferir sitemap, indexação e erros. Não é necessário reenviar um sitemap cujo endereço permanece o mesmo, mas pode-se solicitar nova leitura no Search Console.
- Homologação: restringir acesso, preferencialmente por autenticação; usar noindex como defesa adicional. robots.txt isoladamente não garante desindexação. Não usar o sitemap de produção para divulgar URLs de homologação.
- CI valida arquivos gerados; não substitui testes HTTP e inspeção no Search Console. Validações de produção são obrigatórias antes do lançamento.

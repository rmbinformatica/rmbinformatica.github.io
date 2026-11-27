# Implementação visual — primeira etapa
Novo Design System em assets/css/rmb.css, seletor de tema em assets/js/theme.js, layout independente rmb-v2 e homepage rmb-home. O protótipo usa temporariamente o símbolo histórico já presente no repositório; não confundir com o kit v1.1 aprovado. As fontes têm fallback de sistema até a incorporação das fontes licenciadas. Os layouts antigos e suas dependências permanecem intactos. O protótipo está em /preview-v2/ com sitemap:false e noindex; não publicar em master. Navegação e texto provisórios em português. Internacionalização, páginas comerciais definitivas, kit visual e testes visuais permanecem pendentes.

## Internacionalização — protótipo
Interface localizada nos seis idiomas; seletor de equivalentes existentes e hreflang apenas para páginas indexáveis. Cinco versões estrangeiras resumidas em /preview-v2/{lang}/ são rascunhos não indexáveis para validar navegação e layout; não constituem traduções finais da página inicial. Links para conteúdo legado em português são identificados. Nenhuma tradução publicada em produção. Kit v1.1 disponível localmente, incorporação pendente.

## Homologação local
O pipeline disponibiliza o site compilado como artefato rmb-v2-preview (14 dias), sem deployment. Descompactar em uma pasta e executar nela python3 -m http.server 8080 --bind 127.0.0.1; abrir http://127.0.0.1:8080/preview-v2/. Não abrir via file://, pois os caminhos são relativos à raiz HTTP. Os testes verificam seis versões de prévia, lang, noindex, ausência de alternates SEO e Analytics nas prévias, links de idiomas, recursos e exclusão do sitemap. Homologação pública independente ainda não configurada. O artefato contém também páginas legadas; limitar acesso ao servidor local e não enviar dados reais pelo formulário.

## Revisão visual solicitada
As duas versões SVG do globo foram incorporadas a partir dos contornos e cores do kit v1.0 positivo/v1.1 negativo (58 contornos idênticos, sem redesenho). A seleção usa CSS com prioridade ao tema explícito sobre o sistema. Bandeiras SVG locais simplificadas com nome do idioma, sem CDN; inglês representado pelos EUA. Grade de 16 áreas de atuação com ícones próprios e títulos nos seis idiomas; descrições PT, demais textos em revisão. Cards sem links fictícios até existirem páginas comerciais. Blog e layout de artigos migrados sem mudar URLs nem conteúdo Markdown, mantendo autoria, CTA, comentários e links relacionados. O bloco legado de divulgação com âncoras sem destino foi substituído pela navegação comum; revisar visualmente artigos, comentários e imagens. Enquanto a página preview-home existir, o link de retorno dos novos layouts sem grupo de tradução aponta para ela; removê-la na transição para a raiz. A marca tipográfica completa e fontes ainda não integradas.

## Primeiro lote comercial
Cinco landing pages de hospedagem e nuvem e página de categoria em PT-BR. Cobertura de sete serviços consolidados; maturidade, pesquisas, preços internos e critérios de priorização não exportados. Preservada a URL existente de hospedagem de e-mail. Tabela histórica de preços mantida em _data/prices.json, não exibida pelo novo layout até revisão dos preços e links comerciais. Conteúdo preliminar para revisão do responsável; sem garantias, SLA ou preços inventados. Catálogo restante e versões estrangeiras ainda não implementados. CTA usa contato legado. Não publicar até aprovação.

## Correção da homologação local
O servidor simples do Python não resolve URLs limpas para arquivos .html. Preservar URLs canônicas e distribuir preview_server.py junto ao ZIP de homologação, com fallback restrito a arquivos HTML existentes dentro do diretório servido. Testar HTTP 200 e presença do formulário nas cinco rotas comerciais. Não alterar URLs ou redirecionamentos de produção por causa do servidor local.

## Lote MSP
Nove landing pages agrupadas conforme matriz, cobrindo 19 IDs M1, incluindo serviços relacionados de outras categorias. Categoria MSP navegável; breadcrumbs dinâmicos por categoria e modalidade; nove formulários com traduções. Sem preços, sem SLA implícito. Formulários em homologação sem backend. Páginas de categorias transversais serão vinculadas posteriormente.

## Lote servidores e infraestrutura
Seis novas landing pages cobrem 12 IDs M1, com duas categorias navegáveis. Virtualização e DBA reutilizados na categoria servidores. Formulário de cabeamento existente integrado e cinco novos schemas traduzidos. Modalidade exclusivamente presencial distinguida da híbrida. Experiência com registro de domínios desde 1998 informada pelo responsável; ID pessoal não publicado. Sem preços, sem ativação de formulários.

## Lote segurança e backup
Quatro novas landing pages abrangem seis IDs M1 (041, 042, 044, 045, 046, 050). O ID 047 já coberto em suporte de TI aparece também na categoria segurança. Duas categorias navegáveis, quatro schemas de formulário com seis idiomas. Sem preços, garantias absolutas de segurança, continuidade ou recuperação. Formulários sem envio ativo.

## Lote e-mail, software e automação
Seis novas landing pages abrangem dez IDs M1 (056, 057, 059, 062, 068, 070, 073, 088, 089, 090). Três categorias navegáveis. Formulário de migração existente integrado, cinco novos schemas traduzidos. Não divulgar ferramentas ou metodologia interna de migração, credenciais ou preços. Formulários sem envio ativo.

## Lote final da primeira fase comercial
Cinco novas landing pages: padronização de estações, open source, Nextcloud, consultoria e documentação. Três categorias adicionais navegáveis, inclusive engenharia de dados com links para DBA e relatórios existentes. Cinco schemas traduzidos; sem preços ou envio ativo. Auditoria de IDs e URLs realizada separadamente contra a matriz privada; não publicar classificação comercial.

## Ampliação do catálogo comercial
Cinco páginas existentes ampliadas com oito serviços; onze novas landing pages para outros dezesseis serviços. Categorias DevOps e desenvolvimento web navegáveis. Formulários em seis idiomas, sem envio ativo. Mantidas URLs históricas. Auditoria de correspondência com inventário privado e validação de deploy pendentes.

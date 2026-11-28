# RMB Informática — instruções de desenvolvimento
- Trabalhar em branches independentes; não alterar master nem publicar sem aprovação expressa.
- Consultar _docs/ antes de mudanças arquiteturais. Distinguir decisões aprovadas de propostas.
- Preservar URLs existentes, identidade visual aprovada, artigos e domínio.
- Jekyll/Liquid, HTML semântico, CSS próprio, JS vanilla; evitar dependências desnecessárias.
- Idiomas pt-BR, en, es, it, fr, de. Não publicar traduções não revisadas.
- Não inventar experiência, certificações, casos, garantias ou disponibilidade.
- Nunca inserir dados internos da matriz comercial, credenciais, dados de clientes ou ferramentas secretas no repositório público. Exclusão do build não equivale a privacidade.
- AGENTS.md e _docs/ devem estar explicitamente excluídos do build. Validar o diretório _site antes de publicar.
- Não anunciar atendimento 24/7 ou fluência não confirmada. Atendimento presencial fora da base mediante acordo; exterior sujeito à viabilidade e requisitos legais.
- Testar build, URLs, acessibilidade, idioma, canonical e hreflang antes de integrar.
- Escrever para o público-alvo: explicar termos técnicos na primeira ocorrência, usar exemplos concretos e partir da dor do cliente. Permitir páginas distintas para um mesmo serviço quando público e intenção de busca justificarem conteúdo substancialmente diferente. Não gerar duplicatas nem revelar metodologias confidenciais.
- Preservar SEO e indexação como critérios obrigatórios de aceitação: sitemap.xml e feed.xml válidos, robots.txt de produção com sitemap correto, URLs canônicas e hreflang consistentes, rotas históricas preservadas ou redirecionamentos aprovados. Manter verificação do Google Search Console e Analytics. Nunca inserir URLs de homologação no sitemap de produção; homologação deve ter acesso restrito ou noindex. Não publicar se a validação falhar.
- URLs antigas que mudarem devem receber HTTP 301 real via Cloudflare Bulk Redirects. Manter o mapa aprovado em _data/redirects.yml; gerar CSV no CI, validar destinos, impedir cadeias e loops e excluir origens do sitemap. Não aplicar regras na Cloudflare ou publicar sem autorização. Testar HTTP 301 e destino HTTP 200 na hospedagem real.

- Não divulgar preços, tabelas de preços ou ofertas de contratação imediata de serviços. Todos os serviços devem encaminhar a solicitação de proposta personalizada. Pesquisa de preços e maturidade são internas.
- Cada landing page deve ter FAQ contextual e proposal_form específico ou compartilhado quando equivalente. Lead qualification inicial: nome, e-mail e telefone obrigatórios; empresa e detalhes específicos opcionais; poucas perguntas, opções de desconhecimento quando pertinentes. Entrevista técnica é interna e posterior. Nunca solicitar credenciais. Não restringir idioma dos campos livres; traduzir labels, opções, avisos e mensagens nos seis idiomas.
- Mobile-first obrigatório: testar smartphones, teclado, zoom, temas, controles de toque e ausência de overflow horizontal. Não ativar envio até backend, validação server-side, proteção contra spam, aviso de privacidade e tratamento de dados aprovados.
- Fornecimento de equipamentos: página brasileira com proposta comercial como CTA principal e loja InfinitePay como secundário. Não criar Seleção RMB ou vitrine genérica de afiliados sem nova aprovação.

- Validar rotas de preview com requisições HTTP reais usando o servidor local distribuído no ZIP; manter permalinks históricos sem extensão. Não recomendar http.server simples para URLs limpas.

- Diretriz editorial aprovada na homologação: priorizar benefícios concretos e linguagem comercial natural. Introduções de categorias devem explicar como a RMB ajuda o cliente; descrições de serviços devem combinar o que fazemos com o benefício quando pertinente. Evitar repetir ressalvas como “conforme contrato/escopo/ambiente” em todos os cards; manter condições técnicas, de segurança, licenciamento e viabilidade nos pontos em que são necessárias. Em listas de situações, manter uma mesma pessoa verbal dentro de cada página; preferir segunda pessoa (você/sua empresa) quando o conjunto estiver nessa voz. Não transformar benefícios em garantias absolutas. Preservar a cobertura dos IDs e serviços já existentes ao revisar textos e traduções.

- Marcos institucionais aprovados: empresa fundada em 2003; trajetória tecnológica do fundador iniciada em 1998. Não confundir as datas. Preservar SEO local Natal/RN sem restringir ofertas remotas. Manter 16 categorias e seis soluções orientadas a dores, com links funcionais. Preservar CNPJ e copyright com ano de build no rodapé. Não divulgar telefone pessoal; priorizar chat integrado ao canal existente, carregado mediante ação do visitante, com formulário de contato alternativo.

- Internacionalização comercial: não acrescentar o idioma português entre parênteses a botões de contato, solicitação de proposta ou conversas sobre projetos. O idioma não deve ser uma barreira comercial. Localizar os canais de contato progressivamente, sem alegar fluência não confirmada. Indicações de idioma de conteúdo editorial externo ainda não traduzido podem permanecer quando úteis à navegação.
- Em todos os idiomas, preferir benefícios e linguagem positiva, como “de acordo com as necessidades da sua operação” / “tailored to your operational needs”, evitando tom defensivo. Manter condições técnicas indispensáveis nos pontos pertinentes, sem substituir requisitos reais por promessas comerciais.

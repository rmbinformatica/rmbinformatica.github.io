# Schema de serviços
Front matter de documento publicado:
```yaml
layout: service
service_id: "056"
category_id: "07"
lang: pt-BR
translation_key: service-056
title: Migração profissional de e-mails
description: Serviço de migração de caixas postais entre provedores.
permalink: /servicos/migracao-de-emails/
delivery:
  - remote
```
IDs estáveis como strings. category_id referencia _data/categories.yml quando implementado. translation_key une traduções; não publicar variantes inexistentes. Separar inventário comercial privado de dados públicos. Não publicar preço, maturidade, pontuação ou metodologia sem autorização. Páginas agrupadas podem representar múltiplos IDs, mediante mapeamento explícito e uma URL canônica por idioma.

## Identidade da landing page
O service_id identifica o serviço, não a página. Para novas páginas, usar page_id estável e único por conceito editorial (compartilhado entre suas traduções), audience (technical, nontechnical, mixed ou segment específico), search_intent e service_ids quando representar vários serviços. translation_key identifica somente versões linguísticas equivalentes; pode ter o mesmo valor de page_id. Unicidade: combinação page_id + lang, permalink exclusivo. Exemplo: service_id '147', page_id 'service-147-rescue', translation_key 'service-147-rescue', audience 'nontechnical'; variante técnica usa outro page_id e translation_key. Substitui a regra anterior de uma única URL por serviço e idioma: uma URL canônica por página editorial e idioma. Migrar exemplo anterior de schema para essa convenção na implementação.

## Implementação inicial
Layout rmb-service, service_ids como lista de strings, category_id referenciando _data/rmb_categories.yml (IDs semânticos estáveis). Páginas podem residir em _servicos/pt-br/ ou em arquivo legado para preservar rota. Campos editoriais headline, intro, situations, scope, process, faq, related e delivery. A categoria inicial cloud usa /servicos/hospedagem-e-nuvem/. Preços legados exigem revisão antes de exibição. Não exportar maturidade ou matriz privada.

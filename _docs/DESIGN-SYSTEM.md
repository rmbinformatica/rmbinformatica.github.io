# Design System
Kit visual v1.1 aprovado provisoriamente, geometria do logo preservada.
Cores: institucional #0C3F63, profundo #12344B, destaque #008EDC, luminoso #58CEFF, branco azulado #F5F9FF, fundo escuro #121820. Logo negativo: tipografia #F5F9FF, dígitos #E8F4FF e #58CEFF.
Inter e JetBrains Mono hospedadas localmente quando disponíveis; fallback system-ui e monospace. Não alterar tipografia do logotipo.
CSS custom properties, grid/flex, responsivo mobile-first. Tema claro, escuro, sistema; respeitar prefers-color-scheme e prefers-reduced-motion. Contraste WCAG AA para textos, foco visível, navegação por teclado, labels em formulários. Azul luminoso em fundos escuros; usar azul mais escuro para links em fundo claro. Componentes: cabeçalho, seletor de idioma e tema, cards, breadcrumbs, CTA, rodapé, formulários.

Responsividade é requisito de aceitação: testar 320, 375, 390, 768 e 1280 CSS px, zoom, teclado, temas, ausência de overflow horizontal e campos com altura mínima de 44px. Formulários com uma coluna em smartphones; labels visíveis, foco e mensagens acessíveis. Testes em navegador e aparelho real ainda necessários.

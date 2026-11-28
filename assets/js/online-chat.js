(() => {
  const buttons = [...document.querySelectorAll('[data-chat-load]')];
  if (!buttons.length) return;
  let loading = false;
  const show = (message, failed = false) => {
    for (const id of ['rmb-chat-status', 'rmb-footer-chat-status']) {
      const node = document.getElementById(id);
      if (!node) continue;
      node.hidden = !message;
      node.textContent = message;
      if (failed) {
        const link = document.createElement('a');
        link.href = '/contato.html';
        link.textContent = 'Usar formulário de contato';
        node.append(' ', link);
      }
    }
  };
  const load = () => {
    if (loading) return;
    if (document.getElementById('intergramRoot')) {
      show('O chat está disponível no canto da tela.');
      return;
    }
    loading = true;
    buttons.forEach(b => b.disabled = true);
    show('Carregando atendimento online…');
    window.intergramId = '97475760';
    window.intergramCustomizations = {
      titleClosed: 'Fale conosco',
      titleOpen: 'Atendimento online',
      introMessage: 'Bem-vindo ao atendimento online da RMB Informática. Evite enviar senhas ou informações confidenciais.',
      autoResponse: 'Mensagem recebida pelo chat. Aguarde o retorno.',
      autoNoResponse: 'Não há resposta imediata. Informe um e-mail para retorno, se desejar.',
      mainColor: '#0c3f63',
      alwaysUseFloatingButton: true
    };
    const script = document.createElement('script');
    script.id = 'intergram';
    script.src = 'https://www.intergram.xyz/js/widget.js';
    script.async = true;
    // Upstream registers initialization on window.load, even when loaded late.
    // Capture only registrations made synchronously by this exact script.
    const original = window.addEventListener;
    const ownDescriptor = Object.getOwnPropertyDescriptor(window, 'addEventListener');
    const late = [];
    const intercept = function(type, listener, options) {
      if (this === window && type === 'load' && document.currentScript === script &&
          document.readyState === 'complete') {
        late.push(listener);
        return;
      }
      return original.call(this, type, listener, options);
    };
    window.addEventListener = intercept;
    const restore = () => {
      if (window.addEventListener !== intercept) return;
      if (ownDescriptor) Object.defineProperty(window, 'addEventListener', ownDescriptor);
      else delete window.addEventListener;
    };
    let timer;
    const finish = (ok) => {
      clearTimeout(timer);
      restore();
      loading = false;
      buttons.forEach(b => b.disabled = false);
      if (ok) show('O chat está disponível no canto da tela.');
      else {
        script.remove();
        show('Não foi possível iniciar o chat.', true);
      }
    };
    script.onload = () => {
      restore();
      try {
        if (!document.getElementById('intergramRoot')) {
          for (const listener of late) {
            if (typeof listener === 'function') listener.call(window, new Event('load'));
            else listener.handleEvent(new Event('load'));
          }
        }
        finish(!!document.getElementById('intergramRoot'));
      } catch (error) {
        console.error('Falha ao inicializar atendimento online:', error);
        finish(false);
      }
    };
    script.onerror = () => finish(false);
    timer = setTimeout(() => finish(false), 15000);
    document.head.appendChild(script);
  };
  // Wait for the actual page load to finish before inserting the legacy widget.
  buttons.forEach(button => button.addEventListener('click', () => {
    if (document.readyState === 'complete') load();
    else window.addEventListener('load', load, { once: true });
  }));
})();

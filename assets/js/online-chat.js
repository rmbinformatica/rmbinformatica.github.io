(() => {
  const button = document.getElementById('rmb-chat-load');
  const status = document.getElementById('rmb-chat-status');
  if (!button || !status) return;
  button.addEventListener('click', () => {
    if (document.getElementById('intergram')) return;
    button.disabled = true;
    status.textContent = 'Carregando o atendimento online…';
    window.intergramId = '97475760';
    window.intergramCustomizations = {
      titleClosed: 'Fale conosco',
      titleOpen: 'Atendimento online',
      introMessage: 'Bem-vindo ao atendimento online da RMB Informática. Envie sua mensagem.',
      autoResponse: 'Mensagem recebida pelo chat. Aguarde o retorno.',
      autoNoResponse: 'Não há resposta imediata. Informe um e-mail para retorno, se desejar.'
    };
    const script = document.createElement('script');
    script.id = 'intergram';
    script.src = 'https://www.intergram.xyz/js/widget.js';
    script.async = true;
    script.onload = () => { status.textContent = 'Chat carregado. Abra o painel de atendimento.'; };
    script.onerror = () => {
      script.remove();
      button.disabled = false;
      status.textContent = 'Não foi possível carregar o chat. Tente novamente ou use o formulário de contato.';
    };
    document.head.appendChild(script);
  });
})();

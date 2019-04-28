---
layout: default
title:  "Gerando certificados SSL LetsEncrypt localmente no MacOS"
date:   2019-02-12 15:29:45 -0300
---

# Gerando certificados SSL LetsEncrypt localmente no MacOS com o ZeroSSL

Olá, neste artigo vamos abordar a geração de certificados SSL assinados pela [LetsEncrypt][letsen] num sistema MacOS, o objetivo é gerar os certificados na máquina de trabalho de um administrador que irá instalar esses certificados em um servidor remoto, para isso vamos usar uma versão leve do cliente LetsEncrypt chamada [ZeroSSL][zerossl].

## Introdução e motivação

Os certificados LetsEncrypt são uma maneira prática de proteger pequenos sites com certificados SSL reconhecidos pelos principais browsers do mercado. Dado a curta validade do certificado o projeto foi evoluindo para soluções como o [CertBot][certbot] de modo a automatizar o processo de geração e renovação dos certificados em servidores web.

Porém toda essa automatização de processo acabou deixando de lado situações onde não se tem o permissões do servidor em questão para instalação e/ou agendamento de tarefas, bem como o caso de servidores internos que não estejam conectados à internet e que não possam realizar o processo automaticamente.

Diante disso, esse artigo descreve o passo-a-passo para o processo de geração dos certificados SSL LetsEncrypt em um computador com sistema MacOS, visando apenas a geração dos certificados e sem abordar a instalação deles.

## Requisitos

Para cumprir essa missão, será necessário:
- [Docker para MacOS][docker-mac]
- ZeroSSL client para geração dos certificados.
- Acesso a edição DNS do domínio em questão, para validação da titularidade por meio da criação de entradas CNAME.

## Executando

Uma vez que o docker esteja instalado e rodando, vamos clonar o ZeroSSL Client:

```
docker pull zerossl/client
```

Uma vez instalado o zerossl/client, vamos criar um alias para o comando **le.pl**:
```
alias le.pl='docker run -it -v /home/usuario/cert:/data -v /var/tmp:/webroot -u $(id -u) --rm zerossl/client'
```

No exemplo acima os arquivos de certificado serão salvos no caminho _/home/usuario/cert_ e será usado o caminho _/var/tmp_ como _webroot_  onde serão salvos os arquivos acme-challenge. Tanto o atalho _le.pl_ quanto os caminhos especificados podem ser alterados conforme as preferências do leitor.

Agora para solicitar o certifiacdo do **seudominio.cf**, é necessário executar:

```
le.pl --key account.key --csr domain.csr --csr-key domain.key --crt domain.crt --domains "seudominio.cf" --generate-missing --handle-as dns --api 2
```

Se não existirem, serão gerados os seguintes arquivos:
- account.key = Identifica o usuário junto à LetsEncrypt
- domain.csr = Requisição do certificado
- domain.key = Chave privada do domínio (necessária a instalação do certificado)

No log da geração, veremos as seguintes entradas:

```console
2019/02/12 19:15:42 [ ZeroSSL Crypt::LE client v0.32 started. ]
2019/02/12 19:15:42 Generating a new account key
2019/02/12 19:15:43 Saving generated account key into account-key.txt
2019/02/12 19:15:43 Generating a new CSR for domains seudominio.cf
2019/02/12 19:15:43 New CSR will be based on a generated key
2019/02/12 19:15:44 Saving a new CSR into domain.csr
2019/02/12 19:15:44 Saving a new CSR key into domain.key
2019/02/12 19:15:44 Registering the account key
2019/02/12 19:15:44 The key has been successfully registered. ID: 51376965
2019/02/12 19:15:44 Make sure to check TOS at https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf
2019/02/12 19:15:45 Challenge for 'seudominio.cf' requires the following DNS record to be created:
Host: _acme-challenge.seudominio.cf, type: TXT, value: chaveaLeatORiadeAUT3Nt1c4c40ga3xnjtMqvw2pAM
Wait for DNS to update by checking it with the command: nslookup -q=TXT _acme-challenge.seudominio.cf
When you see a text record returned, press <Enter>
```

Neste momento é necessário realizar a edição do DNS do domínio, criando uma entrada `_acme-challenge` com um registro _TXT_ contendo `chaveaLeatORiadeAUT3Nt1c4c40ga3xnjtMqvw2pAM`.

Após criar a entrada TXT no DNS, aguarde alguns minutos para que ela se propague, você poderá consultar se o registro já está ativo executando o comando abaixo **em outra aba do terminal**:
```
nslookup -q=TXT _acme-challenge.seudominio.cf
```

Uma vez que o registro TXT esteja ativo, basta pressionar ENTER na tela do terminal onde foi executado o procedimento.

O arquivo resultante, será o **domain.crt** que contém o certificado SSL seguido do CA Bundle.

# Script gist para facilitar o processo

Para automatizar o processo, desenvolvi um pequeno script que opera de maneira interativa com o usuário perguntando o nome do arquivo resultante e o nome do domínio que será validado. Para executar basta salvar script em qualquer pasta os certificados gerados serão salvos na mesma pasta onde o script for executado.

[gerarSSL.sh][gist]

---
Escrito por [Renato Monteiro Batista][renato] para o blog da [RMB Informática][rmb]. Reprodução permitida desde que seja mantida as informações de autoria.

[rmb]: http://rmbinformatica.com
[renato]: http://renatomonteiro.gq
[letsen]: https://letsencrypt.org/
[certbot]: https://certbot.eff.org/
[docker-mac]: https://docs.docker.com/docker-for-mac/install/
[gist]: https://gist.github.com/renatomb/0df93907256c9aa35e89c139dfe3f99f
[zerossl]: https://hub.docker.com/r/zerossl/client/

# Consulta de CNPJ e envio automático por e-mail

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Plataforma](https://img.shields.io/badge/Executavel-Windows%20%7C%20Linux%20%7C%20Android-informational?logo=codeforces)]()
[![Licença](https://img.shields.io/badge/Licença-MIT-green)](LICENSE)

## Sobre o projeto

Script em Python que realiza uma consulta de dados de empresas pelo CNPJ, utilizando a [BrasilAPI](https://brasilapi.com.br/). Os dados são organizados em uma planilha `.xlsx` e enviados automaticamente por e-mail em anexo.

Foi desenvolvido como um desafio pessoal com o objetivo de aplicar conhecimentos em automação de processos, manipulação de arquivos, integração com APIs públicas e envio de e-mails automatizado.

## Funcionalidades

- Leitura de CNPJs a partir de um arquivo CSV (`cnpjs.csv`);
- Consulta de dados na BrasilAPI;
- Geração de planilha Excel com os dados estruturados;
- Envio automático por e-mail com anexo;
- Feedback em tempo real no terminal;

## Campos coletados

A planilha final gerada contém os seguintes dados classificados por CNPJ:
- **CNPJ**
- **Descrição da Unidade** (Matriz ou Filial)
- **Razão Social**
- **Nome Fantasia**
- **Situação Cadastral**
- **Data da Situação Cadastral**
- **Data de Início de Atividade**
- **CEP**
- **UF**
- **Município**
- **Telefone 1**
- **Telefone 2**

## Estrutura do projeto

```
projeto_cnpj_email/
├── main.py              # Arquivo principal
├── consulta_cnpj.py     # Módulo de integração com a BrasilAPI
├── planilha.py          # Geração da planilha
├── email_sender.py      # Envio do e-mail com a planilha em anexo
├── cnpjs.csv            # Lista de CNPJs (um por linha)
├── credenciais.json     # Arquivo com credenciais de e-mail (modelo abaixo)
└── README.md            # Documentação do projeto
```

## Exemplo de `credenciais.json`

```json
{
  "email": "exemplo@gmail.com",
  "senha": "sua_senha_de_aplicativo",
  "destinatario": "destinatario@exemplo.com"
}
```

> Atenção: A partir de 30 de maio de 2022, o Google desativou a opção de utilizar sua senha comum, requerindo que uma senha de aplicativo seja utilizada, disponível apenas com a verificação em duas etapas ativada.

## Bibliotecas python utilizadas

requests — Requisições HTTP para a BrasilAPI
csv — Leitura de arquivos de entrada
openpyxl — Criação e edição de planilhas .xlsx
smtplib — Envio de e-mail via protocolo SMTP
email.message — Composição de e-mails com anexo


## Como executar

1. Preencha o arquivo cnpjs.csv com os CNPJs desejados (um por linha);
2. Crie o arquivo credenciais.json com o e-mail, a senha de aplicativo e o destinatário;
3. Execute o main.py:
```python
python main.py
```
4. A planilha será gerada automaticamente e enviada por e-mail.

## Licença

Este projeto está licenciado sob os termos da licença MIT.

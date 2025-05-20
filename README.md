# 🤖 Envio automático de Relatórios de Vendas diários por E-mail
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange?logo=pandas)
![Jinja2](https://img.shields.io/badge/Jinja2-Templating-red?logo=jinja)
![schedule](https://img.shields.io/badge/Schedule-Task%20Scheduler-lightgrey)
![Dotenv](https://img.shields.io/badge/dotenv-Env%20Vars-9cf)
![SMTP](https://img.shields.io/badge/SMTP-Email-green?logo=gmail)

Este projeto automatiza o envio diário de relatórios de vendas de uma empresa via e-mail. O sistema gera um resumo automático e envia o e-mail com corpo HTML + anexo de relatório.

## ✅ Funcionalidades
- Leitura da planilha de vendas (`.csv`).
- Geração do resumo com a quantidade de vendas, valor total das vendas e lucro bruto.
- Armazenamneto de dados sensíveis (remetente, senha, destinatário, servidor e porta) em um `.env`.
- Envio de e-mails automáticos, diariamente às 18h, com HTML estilizado.
- Anexo do arquivo de relatório original.



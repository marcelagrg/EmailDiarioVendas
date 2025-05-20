# 🤖 Automação de Relatórios de Vendas por E-mail
Este projeto automatiza o envio diário de relatórios de vendas de uma empresa via e-mail (gmail) a partir de um arquivo `.csv`.  O sistema gera um resumo automático e envia o e-mail com corpo HTML + anexo de relatório.

## ✅ Funcionalidades
- Leitura da planilha de vendas (.csv)
- Geração do resumo com a quantidade de vendas, valor total das vendas e lucro bruto
- Armazenamneto de dados sensíveis (remetente, senha, destinatário, servidor e porta) em um .env
- Envio de e-mails automáticos, diariamente as 18h, com HTML
- Anexo do arquivo de relatório original

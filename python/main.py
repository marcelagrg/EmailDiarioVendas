import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os
import pandas as pd
import schedule
import time
from jinja2 import Template

# Carregar variáveis do arquivo .env
load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO").split(",") 
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

# Gerar um resumo a partir do CSV de vendas
def resumo_vendas(caminho_csv):
    df = pd.read_csv(caminho_csv, sep=';')
    df.columns = df.columns.str.strip().str.upper()
    ultima_linha = df.tail(1)
    total_vendas = str(ultima_linha["VENDA TOTAL"].values[0]).strip()
    total_lucro = str(ultima_linha["LUCRO BRUTO"].values[0]).strip()
    qtd_vendas = len(df)
    return total_vendas, qtd_vendas, total_lucro

# Gerar HTML do corpo do e-mail
def corpo_email(total_vendas, qtd_vendas, total_lucro):
    with open("template_email.html", "r", encoding="utf-8") as file:
        template = Template(file.read())
    return template.render(vendas=total_vendas, quantidade=qtd_vendas, lucro=total_lucro)

# Enviar o e-mail
def enviar_email(caminho_csv):
    vendas, quantidade, lucro = resumo_vendas(caminho_csv)
    corpo_html = corpo_email(vendas, quantidade, lucro)

    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = ", ".join(EMAIL_TO)
    msg["Subject"] = "Relatório de Vendas - Automático"
    msg.attach(MIMEText(corpo_html, "html"))

    # Anexar o arquivo CSV
    with open(caminho_csv, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(caminho_csv)}")
        msg.attach(part)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, EMAIL_TO, msg.as_string())
            print("Email enviado com sucesso!")
    except Exception as e:
        print("Erro ao enviar e-mail:", e)


# Agenda o envio automático todos os dias às 18h
def agendar_envio():
    schedule.every().day.at("18:00").do(lambda: enviar_email("ControledeVendas.csv"))
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    agendar_envio()

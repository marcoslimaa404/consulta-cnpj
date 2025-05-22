import smtplib
import json
from email.message import EmailMessage

def carregar_credenciais():
    with open("credenciais.json", "r") as f:
        return json.load(f)

def enviar_email_com_anexo(caminho_arquivo):
    credenciais = carregar_credenciais()
    remetente = credenciais["email"]
    senha = credenciais["senha"]
    destinatario = credenciais["destinatario"]

    msg = EmailMessage()
    msg["Subject"] = "Relatório de Empresas por CNPJ"
    msg["From"] = remetente
    msg["To"] = destinatario
    msg.set_content("Segue em anexo o relatório gerado a partir da consulta de CNPJs.")

    with open(caminho_arquivo, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=caminho_arquivo)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(remetente, senha)
        smtp.send_message(msg)
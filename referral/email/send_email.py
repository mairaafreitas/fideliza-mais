import os
import smtplib
from email.message import EmailMessage

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")


def send_email(referred_email, url):
    email = EmailMessage()
    email["from"] = "Fideliza Mais"
    email["to"] = referred_email
    email["subject"] = "Você foi indicado!"

    email.set_content(
        f"Parabéns , você foi indicado para o programa Fideliza Mais! \n\n Acesse o seu link {url} para se cadastrar e ganhar pontos!"
    )

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(email)

import email, smtplib, ssl
import argparse
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

def correo(remitente, destinatario, asunto, cuerpo):
    print("Función de Correo")

    sender_email = remitente
    password = getpass.getpass("Escribe tu contraseña: ")
    receiver_email = destinatario
    subject = asunto
    print("")
    body = cuerpo

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

   
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    print("El correo se ha enviado con exito!")



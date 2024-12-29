import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

# Carga las variables del archivo .env
load_dotenv()

import ssl
import smtplib
from email.message import EmailMessage


# Función para enviar el mensaje del formulario al correo destinatario
def enviar_mensaje_formulario(nombre, email_usuario, telefono, asent, proyect, mensaje):
    # Configuración del correo
    email_sender = "team@codecatsstudios.com"  # Tu nuevo correo
    password_sender = "aFc6d7F8-ff5E-47e0-80c8-e0a469ae16f5"  # Tu nueva contraseña
    email_receiver = email_sender  # Enviarlo a tu propio correo (o cambiar al destinatario deseado)

    subject = f"Nuevo mensaje de contacto de {nombre}"
    body = f"""
        Has recibido un nuevo mensaje a través del formulario de contacto:

        Nombre: {nombre}
        Correo: {email_usuario}
        Teléfono: {telefono}
        Asunto: {asent}
        Proyecto: {proyect}
        Mensaje:
        {mensaje}

        ---
        Este mensaje se envió automáticamente desde el sitio: 'www.CodeCatsStudios.com'.
    """

    # Crear el objeto EmailMessage
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    # Enviar el correo usando el nuevo servidor SMTP
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("mail.spacemail.com", 465, context=context) as smtp:
        smtp.login(email_sender, password_sender)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

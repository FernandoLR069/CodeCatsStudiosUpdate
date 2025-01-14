import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
import mimetypes
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


def enviar_mensaje_formulario_contactar(nombre, email_usuario, telefono):
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
        Paquete: Paquete Chibi

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


def enviar_mensaje_formulario_contactar_web_senpai(nombre, email_usuario, telefono):
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
        Paquete: Paquete Senpai

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


def enviar_mensaje_formulario_contactar_web_kaiju(nombre, email_usuario, telefono):
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
        Paquete: Paquete Kaiju

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


def enviar_mensaje_formulario_servidores_owncloud(nombre, email_usuario, telefono, paquete):
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
        Paquete: {paquete}

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


def enviar_confirmacion_cliente(nombre, email_usuario):
    # Configuración del correo
    email_sender = "team@codecatsstudios.com"  # Tu correo
    password_sender = "aFc6d7F8-ff5E-47e0-80c8-e0a469ae16f5"  # Tu contraseña

    subject = "¡Hemos recibido tu mensaje!"
    body = f"""
        Hola {nombre},

        Gracias por contactarte con Code Cats Studios. Hemos recibido tu mensaje y uno de nuestros especialistas se pondrá en contacto contigo lo antes posible.

        Mientras tanto, si tienes alguna otra consulta, no dudes en escribirnos a este correo.

        ---
        Este mensaje se envió automáticamente desde el sitio: 'www.CodeCatsStudios.com'.
    """

    # Crear el objeto EmailMessage
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_usuario
    em["Subject"] = subject
    em.set_content(body)

    # Ruta de la imagen (ajústala según tu estructura de proyecto)
    image_path = "static/img/logo.png"

    # Leer la imagen y adjuntarla
    try:
        with open(image_path, "rb") as img:
            mime_type, _ = mimetypes.guess_type(image_path)
            main_type, sub_type = mime_type.split("/")
            em.add_attachment(img.read(), maintype=main_type, subtype=sub_type, filename="nombre_imagen.png")
    except FileNotFoundError:
        print("La imagen no se encontró en la ruta especificada.")

    # Enviar el correo usando el servidor SMTP
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("mail.spacemail.com", 465, context=context) as smtp:
        smtp.login(email_sender, password_sender)
        smtp.sendmail(email_sender, email_usuario, em.as_string())


# Función para enviar el mensaje del formulario al correo destinatario
def enviar_mensaje_formulario_devs(nombre, email_usuario, telefono, asent, proyect, mensaje, tipo_proyecto, plazo_entrega, expectativas):
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
        Mensaje: {mensaje}
        Tipo Proyecto: {tipo_proyecto}
        Plazo Entrega: {plazo_entrega}
        Expectativas: {expectativas}
        

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
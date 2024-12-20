# Libreria q sirve para gestionar el envio de correos electronicos
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#Simple mail Transfer protocol > encargado de gestionar el envio de correos electronicos
from smtplib import SMTP
from os import environ

def enviar_email(destinatario, asunto, cuerpo):
    email_emisor = environ.get('CORREO_EMISOR')
    password_emisor = environ.get('PASSWORD_EMISOR')

    # Ahora creamos el cuerpo del mail
    cuerpo_del_correo = MIMEText(cuerpo, 'plain')

    correo = MIMEMultipart()
    correo['Subject'] = asunto
    correo['To'] = destinatario
    # Ahora adjuntamos al correo el texto creado
    correo.attach(cuerpo_del_correo)

    # outlook > outlook.office365.com | 587
    # hotmail > smtp.live.com         | 587
    # gmail >   smtp.gmail.com        | 587
    # icloud >  smtp.mail.me.com      | 587
    # yahoo >   smtp.mail.yahoo.com   | 465

    manejador_correo = SMTP('smtp.gmail.com', 587)

    manejador_correo.starttls()
    # Iniciamos sesion en nuestro servidor de correo con las credenciales
    manejador_correo.login(email_emisor, password_emisor)

    # Envia el correo

    manejador_correo.sendmail(from_addr=email_emisor,
                              to_addrs=destinatario,
                              msg=correo.as_string())
    
    manejador_correo.quit()

    print('Mensaje enviado correctamente')
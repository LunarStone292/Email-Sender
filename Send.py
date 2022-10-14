import code
from email import encoders
from email.mime import base
import os
try:
    from email.message import EmailMessage
    import ssl, smtplib
    from os.path import basename
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    import email.mime.base
    import email.encoders
    from email import encoders
except:
    print("\n Error")
    exit()

email_sender = 'email'
email_password = 'password'

email_reciver = 'reciver'

subject = input("\n Inserisci l'oggetto dell'email: ")
body = input("\n Inserisci il corpo dell'email: ")
allegato = input("\n Inserisci il file da allegare: ")

msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = email_reciver
msg['Subject'] = subject
msg.attach(MIMEText(body))
    
part = email.mime.base.MIMEBase('application', "octet-stream")
part.set_payload(open(allegato, "rb").read())
encoders.encode_base64(part)
    
part.add_header('Content-Disposition', f'attachment; filename={allegato}')

msg.attach(part)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, msg.as_string())

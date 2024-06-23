#!/usr/bin/python3
print("Content-type: text/html")
print("\n")

import os
from email.message import EmailMessage
import ssl
import smtplib
import cgi

form = cgi.FieldStorage()
rec_mail = form.getvalue("rec_mail")
subject = form.getvalue("subject")
body = form.getvalue("body")

email_sender = 'pragyalaxkar2902@gmail.com'
email_password = 'oglg ezoq heoa qkzd'
email_receiver = rec_mail

subject = subject
body = body

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("Mail sent to",rec_mail)

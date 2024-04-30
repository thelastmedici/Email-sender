from email.message import EmailMessage
from app_generator import password
import ssl
import smtplib


email_sender = "horpeyemijoshua@gmail.com"

email_password= password

email_receiver = "jochristian@student.oauife.edu.ng"

subject = "I will soon become a baddass software developer."
body = """
        soon you will be able to create a new application that will work
        on your website and your website admin dashboard to manage your website
        also you will become a better developer when you start developing your application
"""
em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


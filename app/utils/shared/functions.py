
import os
import smtplib
import random
import string

from dotenv import load_dotenv
from email.mime.text import MIMEText


def send_email(email_to: str, subject: str, text: str, new_password: str = None):

    load_dotenv()
    smtp_server = os.getenv('EMAIL_HOST')
    smtp_port = os.getenv('EMAIL_PORT')
    username = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASSWORD')
    
    message = MIMEText(text + new_password)
    message['Subject'] = subject
    message['From'] = username
    message['To'] = email_to
    try:
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(username, password)
    except Exception as e:
        return e
    finally:
        smtp_connection.sendmail(username, message['To'], message.as_string())
        smtp_connection.quit()
        return 'Email sent successfully.'
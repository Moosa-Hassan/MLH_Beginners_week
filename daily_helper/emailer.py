import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_USER, EMAIL_PASSWORD  

def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()
    print(f"Email sent to {to_email}")

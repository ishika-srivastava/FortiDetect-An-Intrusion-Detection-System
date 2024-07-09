import smtplib
from email.mime.text import MIMEText
import json

def sendEmailAlert(alertMessage):
    smtpServer = 'smtp.example.com'
    smtpPort = 587
    smtpUser = 'user@example.com'
    smtpPassword = 'Pa$$w0rd'

    fromEmail = 'from@example.com'
    toEmail = 'alert_recipient@example.com'

    msg = MIMEText(json.dumps(alertMessage, indent=4))
    msg['Subject'] = 'Suspicious Packet Detected'
    msg['From'] = fromEmail
    msg['To'] = toEmail

    try:
        with smtplib.SMTP(smtpServer, smtpPort) as server:
            server.starttls()
            server.login(smtpUser, smtpPassword)
            server.sendmail(fromEmail, toEmail, msg.as_string())
    except smtplib.SMTPException as e:
        print(f"Failed to send email alert: {e}")
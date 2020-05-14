import smtplib, ssl
from email.mime.text import MIMEText

gmail_account = "foo@gmail.com"
gmail_password = "bar"
mail_to = "someone@gmail.com"

subject = "Email from python"
body = "This email from python."
msg = MIMEText(body, "html")
msg["Subject"] = subject
msg["To"] = mail_to
msg["From"] = gmail_account

server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
    context=ssl.create_default_context())
server.login(gmail_account, gmail_password)
server.send_message(msg)
print("Done.")
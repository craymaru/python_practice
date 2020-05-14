import smtplib
import ssl
from email.mime import text
from email.mime import base
from email.mime import multipart
from email.header import Header
from email import encoders

gmail_account = "foo@gmail.com"
gmail_password = "bar"
mail_to = "someone@gmail.com"

subject = "Email from python"
body = "This email from python."
file_path = "./test.tar.gz"


encoding = "utf-8"
msg = multipart.MIMEMultipart()
msg["Subject"] = Header(subject, encoding)
msg["To"] = mail_to
msg["From"] = gmail_account
msg.attach(text.MIMEText(body, "plain", encoding))

attach = base.MIMEBase("application", "tar.gz")
with open(file_path, "br") as f:
    attach.set_payload(f.read())
encoders.encode_base64(attach)
attach.add_header(
    "Content-Disposition",
    "attachment",
    filename="attachment.tar.gz"
)
msg.attach(attach)


server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
    context=ssl.create_default_context())
server.login(gmail_account, gmail_password)
server.send_message(msg)
server.quit()
print("Done.")
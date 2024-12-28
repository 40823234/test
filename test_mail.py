import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "40823234@gm.nfu.edu.tw"
receiver = ["snipery730@gmail.com"]
passwd = "mebl lykg ecvw ucgn"
for i in receiver:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = i
    msg["subject"] = Header("Test send email","utf-8").encode()

    body = "This is send by python"

    msg_test=MIMEText(body)
    msg.attach(msg_test)
    c = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as server:
        server.login(sender,passwd)
        server.sendmail(sender,i,msg.as_string())
print("success send email")
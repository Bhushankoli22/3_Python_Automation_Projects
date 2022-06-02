from email import message
import smtplib
import ssl
from email.message import EmailMessage


subject = input("Please write subject of your Mail : ")
body = input("Please write your E-Mail content: ")
sender_email = input("Please write E-Mail id from whom you want to send : ")
receiver_email = input("Please write E-Mail id to whom you want to send it : ")
password = input("Please provide password of your E-mail : ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)


context = ssl.create_default_context()
print("Sending Email..")
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server : 
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email,message.as_string())
import smtplib
import os.path

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

sender = 'restuardam@gmail.com'
password = "Exciter16/magson"

receiver_list_file = open("receiver_list.txt", "r+")
recipient = [i.strip() for i in receiver_list_file.readlines()]
receiver_list_file.close()

subject = 'Python-Test'
message = 'Assalamualaikum Warahmatullahi Wabarakatuh'

msg = MIMEMultipart()
msg ['From'] = sender 
msg ['Subject'] = subject
msg ['To'] = ', '.join(recipient)    
msg.attach(MIMEText(message, "plain"))

file_path = "C:\\Learn AI\\basic python 5\\basic-python\\Final_Project\\test_file.txt"
filename = os.path.basename(file_path)
attachment = open(file_path, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename=filename)
msg.attach(part)

server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
server.login(sender, password)
server.sendmail(sender, recipient, msg.as_string())
server.quit()

print("Email berhasil dikirim")
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class SendMail:
    def __init__(self,sender,sender_PW,receiver):
        self.SERVER = 'smtp.gmail.com:587'

        self.SENDER_EMAIL = sender
        self.SENDER_PASSWORD = sender_PW
        self.RECEIVER_EMAIL = receiver

    def generate_msg(self, subject, content):
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = self.SENDER_EMAIL
        message['To'] = self.RECEIVER_EMAIL
        content = content
        message.attach(MIMEText(content, 'plain'))

        return message


    def generate_msg_html(self, subject, html):
        message = MIMEMultipart("alternative", None, [MIMEText(html, 'html')])
        message['Subject'] = subject
        message['From'] = self.SENDER_EMAIL
        message['To'] = self.RECEIVER_EMAIL

        return message


    def generate_msg_attach(self, subject, content, filepath):
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = self.SENDER_EMAIL
        message['To'] = self.RECEIVER_EMAIL
        content = content
        message.attach(MIMEText(content, 'plain'))

        # attachment
        file_path = filepath
        attachment = open(file_path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)

        filename = filepath.split('&#47;')[-1]
        part.add_header('Content-Disposition', "attachment; filename= " + filename)
        message.attach(part)

        return message



    def send_mail(self, mail):
        message = mail
        server = smtplib.SMTP(self.SERVER)
        server.ehlo()
        server.starttls()
        server.login(self.SENDER_EMAIL, self.SENDER_PASSWORD)
        server.sendmail(self.SENDER_EMAIL, self.RECEIVER_EMAIL, message.as_string())
        server.quit()

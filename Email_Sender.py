#meibhlwzsiaocsmq
#smtp: simple message transfer protocol (for sending emails)
#ftp: file transfer protocol (for sending files)
#http: hypertext transfer protocol (for accessing www)
#sending packages: TCP UDP
#for security: SSL TLS

from email.message import EmailMessage
import smtplib

email_sender = 'prachponleuuch@gmail.com'#input('Email Address: ')
email_password = 'meibhlwzsiaocsmq'#input('Password: ')
email_receiver = 'reriga2260@v3dev.com' #input('Send to: ')

subject = input('Subject: ')
print('Body (Write "SEND" on a new line to send the email):')
lines = []
while True:
    line = input()
    if line != "SEND":
        lines.append(line)
    else:
        break
body = '\n'.join(lines)

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls() #For security
server.login(email_sender, email_password)
server.sendmail(email_sender,email_receiver, em.as_string())



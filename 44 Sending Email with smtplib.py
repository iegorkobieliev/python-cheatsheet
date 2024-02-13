import smtplib
from email.mime.text import MIMEText

# Set up email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Log in to email account
server.login('user@gmail.com', 'password')

# Send email
msg = MIMEText('Hello, Python!')
msg['Subject'] = 'Python Email'
server.sendmail('user@gmail.com', 'v@gmail.com', msg.as_string())

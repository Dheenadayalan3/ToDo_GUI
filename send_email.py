import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(email,msg):
    sender_email = 'dheenadayalannagarajan@gmail.com'
    sender_password = 'xjsx zvrf voey bqis'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(email)
    message['Subject'] = 'Today'
    message.attach(MIMEText(msg,'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message.as_string())
        print(f'✅ Email successfully sent to {email}')
    except Exception as e:
        print(f'❌ Error sending email: {e}')

email_address = ['seniorfarwell2021@gmail.com','dheenadayalannagarajan@gmail.com']
msg = '''Today is a great day for learning and improving! 🚀 You've been making solid progress with Python, especially with handling emails, dictionaries, lists, and file operations. You're also sharpening your English communication skills, which is awesome! 😀️'''

if email_address:
    send_email(email_address, msg)

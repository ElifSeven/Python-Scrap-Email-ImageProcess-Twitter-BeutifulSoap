import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Elif Seven'
email['to'] = 'svnelif34@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'HiHi'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smptp:
    smptp.ehlo()
    smptp.starttls()
    smptp.login('your_email_address@gmail.com', 'your_password')
    smptp.send_message(email)
    print('sent !')

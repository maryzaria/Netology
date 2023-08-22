import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class WorkWithEmail:
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(self, l, password):
        self.l = l
        self.passwORD = password

    def send_message(self, message, recipients, subject):
        msg = MIMEMultipart()
        msg['From'] = self.l
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.l, self.passwORD)
        ms.sendmail(self.l, ms, msg.as_string())
        ms.quit()

    def receive_message(self, header):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.l, self.passwORD)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':
    email = WorkWithEmail(l='login@gmail.com', password='qwerty')

    message_text = 'Message'
    subject_text = 'Subject'
    recipients_list = ['vasya@email.com', 'petya@email.com']
    email.send_message(message=message_text, subject=subject_text, recipients=recipients_list)

    email.receive_message(header=None)

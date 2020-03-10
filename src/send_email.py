from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import scraper

auth_details=open('../assets/auth_details.txt', 'r')

s = smtplib.SMTP_SSL('smtp.gmail.com')
MY_ADDRESS=auth_details.readline()
s.login(MY_ADDRESS, auth_details.readline())

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def send_email():
    msg = MIMEMultipart()       # create a message

    message = read_template('../assets/message.txt').substitute(corona_total_count=scraper.corona_total_count())

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=MY_ADDRESS
    msg['Subject']="Coronavirus Total Count"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.sendmail(MY_ADDRESS, MY_ADDRESS, msg.as_string())

    del msg

if __name__ == '__main__':
    send_email()
#!/usr/bin/python
import time
import datetime
import sys, argparse, csv
import smtplib
import mimetypes
import email
import email.mime.application
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

today = time.strftime("%b %d %Y %H:%M:%S")
#today = datetime.date.today().strftime("%B %d %H:%M, %Y")
msg = email.mime.Multipart.MIMEMultipart()
msg['Subject'] = "MESSAGE"
msg['From'] = 'EMAIL ADDRESS1'
msg['To'] = 'EMAIL ADDRESS2'
# The main body is just another attachment

body = email.mime.Text.MIMEText("MESSAGE "+today)
msg.attach(body)
#msg.attach(result_text1)
#msg.attach(html_text)

# CSV attachment

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('EMAIL ADDRESS1','PASSWORD')
s.sendmail('EMAIL ADDRESS1',['EMAIL ADDRESS2'], msg.as_string())
s.quit()

msg = email.mime.Multipart.MIMEMultipart()
msg['Subject'] = "MESSAGE"
msg['From'] = 'EMAIL ADDRESS1'
msg['To'] = 'EMAIL ADDRESS3'
# The main body is just another attachment

body = email.mime.Text.MIMEText("MESSAGE "+today)
msg.attach(body)
#msg.attach(result_text1)
#msg.attach(html_text)

# CSV attachment

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('EMAIL ADDRESS1','PASSWORD')
s.sendmail('EMAIL ADDRESS1',['EMAIL ADDRESS3'], msg.as_string())
s.quit()
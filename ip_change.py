# -*- encoding: UTF-8 -*-

import urllib2
import smtplib
from email.mime.text import MIMEText
from settings import SMTP_SERVER, SMTP_SERVER_PORT, SMTP_USER, SMTP_PASSWORD, FROM, TO, DOMAIN, IP


def send_email(ip):
    text = "New IP: " + ip
    msg = MIMEText(text, 'plain')
    msg['Subject'] = DOMAIN + " ip changed!!"
    msg['From'] = FROM
    msg['To'] = TO

    server = smtplib.SMTP(SMTP_SERVER, SMTP_SERVER_PORT)
    server.starttls()
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()


def get_ip():
    req = urllib2.Request(url="https://api.ipify.org")
    return urllib2.urlopen(req).read()


def main():
    current_ip = get_ip()
    if current_ip != IP:
        send_email(current_ip)


if __name__ == '__main__':
    main()

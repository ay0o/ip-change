import argparse
import ipaddress
import os
import smtplib
import socket
from email.mime.text import MIMEText
import requests


def parse_args():
    parser = argparse.ArgumentParser(description='Detect whether a domain is not resolving the local public IP', usage='python3 ip_change.py --domain DOMAIN')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-d', '--domain', action='store', required=True)
    return parser.parse_args()


def get_current_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        return str(ipaddress.ip_address(ip))
    except ValueError:
        raise SystemExit('[ERROR] IPify did not return a valid IP')


def send_email(domain, ip):
    text = f'New IP: {ip}'
    msg = MIMEText(text, 'plain')
    msg['Subject'] = f'[IP CHANGE] {domain} IP changed!!'
    msg['From'] = os.environ['EMAIL_USER']
    msg['To'] = os.environ['EMAIL_DESTINATION']

    server = smtplib.SMTP(os.environ['SMTP_SERVER'], os.environ['SMTP_PORT'])
    server.starttls()
    server.login(os.environ['EMAIL_USER'], os.environ['EMAIL_PASSWORD'])
    server.sendmail(os.environ['EMAIL_USER'], os.environ['EMAIL_DESTINATION'], msg.as_string())
    server.quit()


def main():
    args = parse_args()

    try:
        domain_ip = socket.gethostbyname(args.domain)
    except Exception as e:
        raise SystemExit('[ERROR] Could not resolve domain')

    current_ip = get_current_ip()

    if current_ip != domain_ip:
        send_email(args.domain, current_ip)


if __name__ == "__main__":
    main()

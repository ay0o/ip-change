import smtplib
from email.mime.text import MIMEText
import yaml
import requests


def parse_settings(settings_file='settings.yaml'):
    with open(settings_file) as yaml_stream:
        return yaml.load(stream=yaml_stream)


def send_email(settings, ip):
    text = "New IP: " + str(ip)
    msg = MIMEText(text, 'plain')
    msg['Subject'] = settings['dns']['domain'] + " IP changed!!"
    msg['From'] = settings['email']['from']
    msg['To'] = settings['email']['to']

    server = smtplib.SMTP(settings['smtp']['server'], settings['smtp']['port'])
    server.starttls()
    server.login(settings['smtp']['user'], settings['smtp']['password'])
    server.sendmail(settings['email']['from'], settings['email']['to'], msg.as_string())
    server.quit()


def get_ip():
    return requests.get("https://api.ipify.org").text


try:
    settings = parse_settings()
except FileNotFoundError as e:
    print(e)
    raise SystemExit(1)

current_ip = get_ip()
if current_ip != settings['dns']['ip']:
    send_email(settings, current_ip)

# -*- encoding: UTF-8 -*-

SMTP_SERVER = "smtp.gmail.com"
SMTP_SERVER_PORT = 587
SMTP_USER = "alice@gmail.com"
SMTP_PASSWORD = "Bobismylove<3"
FROM = "alice@gmail.com"
TO = "bob@gmail.com"
DOMAIN = "example.com"
IP = "1.2.3.4"

# ******************************* SETTINGS LOCAL *****************************
try:
    SETTINGS_LOCAL
except NameError:
    try:
        from settings_local import SMTP_SERVER, SMTP_SERVER_PORT, SMTP_USER, SMTP_PASSWORD, FROM, TO, DOMAIN, IP
    except ImportError:
        pass

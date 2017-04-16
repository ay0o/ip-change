# -*- encoding: UTF-8 -*-

SMTP_SERVER = "smtp.gmail.com"
SMTP_SERVER_PORT = 587
SMTP_USER = "alice@gmail.com"
SMTP_PASSWORD = "Bobismylove<3"
FROM = "alice@gmail.com"
TO = "bob@gmail.com"

DOMAIN = "example.com"
IP = "1.2.3.4"
API_USER = ""
API_KEY = ""


# ******************************* SETTINGS LOCAL *****************************
try:
    SETTINGS_LOCAL
except NameError:
    try:
        from settings_local import *
    except ImportError:
        pass

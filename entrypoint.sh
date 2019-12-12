#!/bin/bash

sed -e "s/<SMTP_SERVER>/${SMTP_SERVER}/g" \
    -e "s/<SMTP_PORT>/${SMTP_PORT}/g" \
    -e "s/<EMAIL_FROM>/${EMAIL_FROM}/g" \
    -e "s/<EMAIL_PASS>/${EMAIL_PASS}/g" \
    -e "s/<EMAIL_TO>/${EMAIL_TO}/g" \
    -e "s/<DOMAIN>/${DOMAIN}/g" \
    -e "s/<IP>/${IP}/g" \
    -i settings.yaml

python ip_change.py
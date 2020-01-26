# IP Change

If you own a domain that is pointing to a dynamic IP, this script will tell you when the IP changed.

## Usage

```
pip install -r requirements
```

Set the following environment variables before use, otherwise the email will not be delivered:

- SMTP_SERVER
- SMTP_PORT
- EMAIL_USER
- EMAIL_PASSWORD
- EMAIL_DESTINATION

```
python3 ip_change.py -d DOMAIN
```

Also available as a Docker container at [Docker Hub](https://cloud.docker.com/repository/docker/ay0o/ip_change
)
# IP Change

If you own a domain that is pointing to a dynamic IP, this script will tell you when the IP changed.

## Config
* mv settings_local.py.sample settings_local.py
* Edit settings_local.py with your data

## Usage
python ip_change.py



## More info
My original idea was to don't need human interaction, that is, if a new IP is detected, automatically change the domain's A record to this new IP. However my domain registrar doesn't offer API access for free ¬¬, so right now the script sends an email, and the user must manually change the DNS records.

There are an API_USER and API_key variables in the settings, and a function change_dns in the code. If your domain registrar has an API, you could uncomment this function and put the correct URL and it should work. It hasn't been tested though. If you want to try, remember to install pycurl -->  pip install pycurl.

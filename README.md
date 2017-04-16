# IP Change

If you own a domain that is pointing to a dynamic IP, this script will tell you when the IP changed.

## Config
* mv settings_local.py.sample settings_local.py
* Edit settings_local.py with your data

## Usage
python ip_change.py



## More info
My original idea was to don't need human interaction, that is, if a new IP is detected, automatically change the domain's A record to this new IP. However my domain registrar doesn't offer API access for free ¬¬, so right now the script sends an email, and the user must manually change the DNS records.

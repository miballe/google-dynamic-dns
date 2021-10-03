import os
import requests

guser = os.getenv("GOOGLE_DNS_USER", None)
gpwd = os.getenv("GOOGLE_DNS_PWD", None)
grecord = os.getenv("GOOGLE_DNS_RECORD", None)
detectip = os.getenv("DETECT_IP", None)
newip = os.getenv("NEW_IP", None)
myip_url = 'https://api.myip.com'

if guser is None:
    raise Exception("GOOGLE_DNS_USER environment variable not set!")

if gpwd is None:
    raise Exception("GOOGLER_DNS_PWD environment variable not set!")

if grecord is None:
    raise Exception("GOOGLE_DNS_RECORD environment variable not set!")

if detectip.lower() == 'false':
    detectip = False
    if newip is None:
        raise Exception("DETECTIP environment variable not set or set to false, and NEW_IP not set!")
else:
    detectip = True


if detectip:
    resp = requests.get(myip_url)
    if resp.status_code != 200:
        raise Exception("ERROR when contacting My IP service")
    ip_obj = resp.json()
    newip = ip_obj["ip"]

print(f"Calling Google Dynamic DNS for {grecord} and IP address {newip}...")

gdns_url = f"https://{guser}:{gpwd}@domains.google.com/nic/update?hostname={grecord}"

update_resp = requests.get(gdns_url)

print(update_resp.text)

import os
import requests
import time
from datetime import datetime

guser = os.getenv("GOOGLE_DNS_USER", None)
gpwd = os.getenv("GOOGLE_DNS_PWD", None)
grecord = os.getenv("GOOGLE_DNS_RECORD", None)
detectip = os.getenv("DETECT_IP", None)
newip = os.getenv("NEW_IP", None)
interval = os.getenv("UPDATE_INTEVAL_MINS", None)
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

if interval is None:
    interval = 5
else:
    interval = int(interval)

if len(guser.split(',')) == len(gpwd.split(',')) == len(grecord.split(',')):
    nrecords = len(guser.split(','))
    all_users = guser.split(',')
    all_pwd = gpwd.split(',')
    all_records = grecord.split(',')
else:
    raise Exception("GOOGLE_DNS_USER, GOOGLE_DNS_PWD and GOOGLE_DNS_RECORD must have the same number of entries separated by comma!")

## TODO: Validate user/pwd minimum length
## TODO: Validate newip format
## TODO: Validate record format

if detectip:
    resp = requests.get(myip_url)
    if resp.status_code != 200:
        raise Exception("ERROR when contacting My IP service")
    ip_obj = resp.json()
    newip = ip_obj["ip"]

while(True):
    for ix, record in enumerate(all_records):
        print(f"Calling Google Dynamic DNS for {record} and IP address {newip}...")
        gdns_url = f"https://{all_users[ix]}:{all_pwd[ix]}@domains.google.com/nic/update?hostname={record}"
        update_resp = requests.get(gdns_url)
        update_parts = update_resp.text.split(' ')
        print(f"{datetime.now()}, {record}, {update_parts[0]}, {update_parts[1]}")
    print(f"{datetime.now()} - Wait time: {interval} minutes.")
    time.sleep(60 * interval)

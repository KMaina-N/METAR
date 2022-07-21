import requests
import json

hdr = {"X-API-Key": "e00b7cc7e1a94d159c2140bc13"}
req = requests.get("https://api.checkwx.com/metar/LDZL", headers=hdr)

print("Response from CheckWX.... \n")

try:
    req.raise_for_status()
    resp = json.loads(req.text)
    print(json.dumps(resp, indent=1))

except requests.exceptions.HTTPError as e:
    print(e)

## request TAF
headers = {'X-API-Key': 'e00b7cc7e1a94d159c2140bc13',}

response = requests.get('https://api.checkwx.com/taf/KJFK', headers=headers)
print(response.content)
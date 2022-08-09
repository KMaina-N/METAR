from django.shortcuts import render

# Create your views here.
import requests
import json
import re

hdr = {"X-API-Key": "e00b7cc7e1a94d159c2140bc13"}
req = requests.get("https://api.checkwx.com/metar/LDZA", headers=hdr)

print("Response from CheckWX.... \n")
try:
    #req.raise_for_status()
    resp = json.loads(req.text)
    data = json.dumps(resp, indent=1)
    data = str(resp['data'])
    pre_data = re.sub(r'[^\w\s]', '', data)
    # print(pre_data)
    ad = pre_data[0:4]
    dt = pre_data[5:]
    corrected_data = 'LDZL ' + ''+dt
    refined = ''.join(i for i in corrected_data if i not in '"')
    # print(refined)

    str(data)
    print(json.dumps(resp, indent=1))

except requests.exceptions.HTTPError as e:
    print(e)

def index(request):
    context= {}
    global metar
    # if request.method=='POST':
        # icao = request.POST.get('code')
    icao = 'LDZA'

    hdr = {"X-API-Key": "e00b7cc7e1a94d159c2140bc13"}
    req = requests.get(f"https://api.checkwx.com/metar/{icao}", headers=hdr)

    print("Response from CheckWX.... \n")

    #req.raise_for_status()
    resp = json.loads(req.text)
    data = json.dumps(resp, indent=1)
    data = str(resp['data'])
    pre_data = re.sub(r'[^\w\s]', '', data)
    # print(pre_data)
    ad = pre_data[0:4]
    dt = pre_data[5:]
    corrected_data = 'LDZL ' + ''+dt
    refined = ''.join(i for i in corrected_data if i not in '"')
    metar = refined
    print(json.dumps(resp, indent=1))
    context['metar'] = metar    

        # if len(metar)>5:
        #     context['metar'] = metar
        # else:
        #     context['metar'] = 'Not found consider using METAR of a nearby regional or international airport'

    return render(request, 'index.html',context)

def admin():
    # create a form and db, allow admin to update prices of fuel in the airport
    return 0


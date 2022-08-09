from django.test import TestCase

# Create your tests here.
# top destinations
import requests, json

url = "https://aerodatabox.p.rapidapi.com/airports/icao/EDDF/stats/routes/daily"

headers = {
	"X-RapidAPI-Key": "380705e0b7msh9431f923ae42cedp1b55efjsn723efbf1a22b",
	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

data = requests.get(url, headers=headers).json()
data
req = json.dumps(data)

x = data['routes']
x
for i in x:
    y = i['destination']['name']
    y


# Departures and arrivals
url = "https://aerodatabox.p.rapidapi.com/flights/airports/icao/LDZA/2022-08-04T20:00/2022-08-04T21:00"

querystring = {"withLeg":"true","withCancelled":"true","withCodeshared":"true","withCargo":"true","withPrivate":"true","withLocation":"false"}

headers = {
	"X-RapidAPI-Key": "380705e0b7msh9431f923ae42cedp1b55efjsn723efbf1a22b",
	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
}

# response = requests.request("GET", url, headers=headers, params=querystring)
data = requests.get(url, headers=headers, params=querystring).json()
data

x = data['departures']
x
for i in x:
    y = i['arrival']['airport']['name']
    y
    p = i['isCargo']
    p
    a = i['airline']['name']
    a

print(response.text)


##### text to speech
import requests

url = "https://cloudlabs-text-to-speech.p.rapidapi.com/languages"

headers = {
	"X-RapidAPI-Key": "380705e0b7msh9431f923ae42cedp1b55efjsn723efbf1a22b",
	"X-RapidAPI-Host": "cloudlabs-text-to-speech.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
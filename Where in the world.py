
from datetime import datetime
import requests

url = "https://flight-radar1.p.rapidapi.com/flights/get-more-info"


headers = {
	"X-RapidAPI-Key": "88cf67cb93mshd1c7501876c1e0fp1a11a4jsne6ba842206d6",
	"X-RapidAPI-Host": "flight-radar1.p.rapidapi.com"
}

print("Flight No.: ", end="")
flightNo = input()

querystring = {"query":flightNo,"fetchBy":"flight","page":"1","limit":"100"}

response = requests.request("GET", url, headers=headers, params=querystring)

# data = response.json()['result']['response']


data = {
    "airlinename" : response.json()['result']['response']['data'][0]['airline']['name'],
    "airlineiata" : response.json()['result']['response']['data'][0]['airline']['code']['iata'],
    "airlineicao" : response.json()['result']['response']['data'][0]['airline']['code']['icao'],

    "status" : response.json()['result']['response']['data'][0]['status']['generic']['status']['text'],
    "type" : response.json()['result']['response']['data'][0]['status']['generic']['status']['type'],

    "airportname" : response.json()['result']['response']['data'][0]['airport']['origin']['name'],
    "airporticao" : response.json()['result']['response']['data'][0]['airport']['origin']['code']['icao'],
    "airportiata" : response.json()['result']['response']['data'][0]['airport']['origin']['code']['iata'],
    "countryname" : response.json()['result']['response']['data'][0]['airport']['origin']['position']['country']['name'],
    "countrycode" : response.json()['result']['response']['data'][0]['airport']['origin']['position']['country']['code'],
    "regioncity" : response.json()['result']['response']['data'][0]['airport']['origin']['position']['region']['city'],

    "dairportname" : response.json()['result']['response']['data'][0]['airport']['destination']['name'],
    "dairporticao" : response.json()['result']['response']['data'][0]['airport']['destination']['code']['icao'],
    "dairportiata" : response.json()['result']['response']['data'][0]['airport']['destination']['code']['iata'],
    "dcountryname" : response.json()['result']['response']['data'][0]['airport']['destination']['position']['country']['name'],
    "dcountrycode" : response.json()['result']['response']['data'][0]['airport']['destination']['position']['country']['code'],
    "dregioncity" : response.json()['result']['response']['data'][0]['airport']['destination']['position']['region']['city'],

    "scheduleddeparture" : response.json()['result']['response']['data'][0]['time']['scheduled']['departure'],
    "scheduledarrival" : response.json()['result']['response']['data'][0]['time']['scheduled']['arrival'],
}

 
print(
    "\n"
    "\n"
    "Airline Information: ",
    "\n"
    "Airline: " + data.get("airlinename"),
    "\n"
    "Airline Code: " + data.get("airlineiata") + " " + data.get("airlineicao"),
    "\n"
    "\n"
    "Status: " + data.get("status"),
    "Type: " + data.get("type"),
    "\n"
    "Departing From: ", data.get("airportiata"), 
    "\n"
    "Departing To: ", data.get("dairportiata"),
    "\n"
    "Scheduled Departure: ", datetime.utcfromtimestamp(data.get("scheduleddeparture")).strftime('%Y-%m-%d %H:%M:%S'),
    "\n"
    "Scheduled Arrival: ", datetime.utcfromtimestamp(data.get("scheduledarrival")).strftime('%Y-%m-%d %H:%M:%S'),
    "\n"
    "\n"
    "Origin Airport:",
    "\n"
    "Airport Name: " + data.get("airportname"),
    "\n"
    "Airport Code: " + data.get("airportiata"),
    "\n"
    "Country: " + data.get("countryname") + " (" + data.get("countrycode") + ") "+ ", " + data.get("regioncity"),
    "\n"
    "\n"
    "Departure Airport:",
    "\n"
    "Airport Name: " + data.get("dairportname"),
    "\n"
    "Airport Code: " + data.get("dairportiata"),
    "\n"
    "Country: " + data.get("dcountryname") + " (" + data.get("dcountrycode") + ") "+ ", " + data.get("dregioncity"),
)





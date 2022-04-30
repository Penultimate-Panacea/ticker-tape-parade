import requests
import json

response = requests.get("https://lldev.thespacedevs.com/2.2.0/launch?limit=1000&?mode=list/previous")
responsedict = response.json()
print(responsedict['count'])
print(responsedict['next'])
responsedict.update(requests.get(responsedict['next']).json())
print(responsedict['next'])



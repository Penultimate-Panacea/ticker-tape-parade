import requests
import globals
import json

response = requests.get("https://lldev.thespacedevs.com/2.2.0/launch?limit=1000&?mode=list/previous")
responsedict = response.json()
print(responsedict['count'])
print(responsedict['next'])
responsedict.update(requests.get(responsedict['next']).json())
print(responsedict['next'])



def checkForNewLaunch():
    is_new_launch = False
    if globals.lastcount < response.json['count']:
        is_new_launch = True
    new_launches = []
    if is_new_launch:
        for i in getNewLaunch():
            new_launches.append(i)
    if not is_new_launch:
        new_launches = []
    else:
        print("Bad checkForNewLaunch")
    
    return (is_new_launch, new_launches)

def getNewLaunch():
    #api call
    return 
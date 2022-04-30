import requests
import json

response = requests.get("https://lldev.thespacedevs.com/2.2.0/launch?mode=list")
print(response.json())




def checkForNewLaunch():
    is_new_launch = False
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
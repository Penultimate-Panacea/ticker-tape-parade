from ast import While
from math import floor
from time import sleep
import requests
# import json
import globals





# STEP ONE: Initalize list of Launches
initial_dictionary_of_launches = requests.get("https://lldev.thespacedevs.com/2.2.0/launch?limit=100&?mode=list/previous").json() # max limit is 100 , .json turns it into a dict object
print(initial_dictionary_of_launches['count'])
# STEP TWO: Build list of previous launches
"""dictionary_of_launches = initial_dictionary_of_launches
list_of_just_results = initial_dictionary_of_launches['results']
print(dictionary_of_launches['next'])
while dictionary_of_launches['next'] != None:
    next_dictionary = requests.get(dictionary_of_launches['next']).json()
    print(next_dictionary['next'])
    dictionary_of_launches.update(next_dictionary)
    list_of_just_results.append(next_dictionary['results'])
    if dictionary_of_launches['next'] == "None" or None:
        print("IF BREAK")
        break
"""


requests_needed = (floor(initial_dictionary_of_launches['count'] / 100))
list_of_launches = initial_dictionary_of_launches['results']
i = 0
while i < requests_needed:
    offset_number = str(i*100)
    request_string = "https://lldev.thespacedevs.com/2.2.0/launch?limit=100" + "&?offset=" + offset_number + "&?mode=list/"
    print(request_string)
    while_loop_request_dictionary = requests.get(request_string).json()
    while_loop_request_list = while_loop_request_dictionary['results']
    for j in while_loop_request_list:
        list_of_launches.append(j)
    i += 1
print(len(list_of_launches))

# STEP THREE: Save list of previous launches
"""
if initial_dictionary_of_launches['count'] != len(list_of_just_results):
    print("Something seems funky!")
else:
    globals.lastcount = len(list_of_just_results)
    globals.past_launches = list_of_just_results
    
print(len(list_of_just_results))
sleep(2)
"""
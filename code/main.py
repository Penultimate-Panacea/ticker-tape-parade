# Created by Rian Fantozzi April 29, 2022

# What follows is a pseudocode implementation of the planned process.


from math import floor
from time import sleep
import printer_control

def initalize():
    
    return

#Control Variables
    
refresh_time_in_hours = 0.5 # how often to check for new launches

#Main Progra
initalize()

while True:
    if not checkForNewLaunch()[0]: # [0] returns bool, true if new launch | [1] returns list of new launches 
        sleep(floor(60*60*refresh_time_in_hours)) #sleep number of hours converted to seconds, floor function for fractional hours
        break
    appendLaunchList()
    ticker =  printer_control.makePrintFile()
    printer_control.transmitPrintFile(ticker)
    break



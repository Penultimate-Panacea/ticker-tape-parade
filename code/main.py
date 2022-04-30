# Created by Rian Fantozzi April 29, 2022

# What follows is a pseudocode implementation of the planned process.


from time import sleep


while True:
    newdata = checkForNewLaunch() # returns bool, true if new launch
    if not newdata:
        sleep(60*60*6) #sleep for 6 hours, number of seconds expanded for clarity
        break
    appendLaunchList(newdata)
    ticker =  makePrintFile()
    transmitPrintFile(ticker)
    break


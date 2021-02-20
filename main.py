from location import location
from weather_forecast import weatherForecast
from LUIS import *
from tkinter import *
import tkinter as tk
from window import window

locationObj = location()
weather_forecast = weatherForecast()
y = LUIS("9d556518bc2b49489a61ddbdc98884a3")

#making GUI window
wind = tk.Tk()
wind.geometry("800x600+500+300")
window(wind)
wind.resizable(width=FALSE, height=FALSE)
wind.mainloop()




'''
while 1:

    uinput = input('->')
    x = y.GetEntities(uinput)
    null = ""
    location = null
    time = null
    resolution = []

    print("Testing LUIS output")

    for entities in x:

        # deal with time
        if 'builtin.datetimeV2.' in entities['type']:
            time = entities['entity']
            resolution = entities['resolution']['values']
            timex = ''
            # timex = resolution[0]['timex']
            if str(resolution[0]['type']) == 'datetime':
                timex = resolution[0]['timex']
            elif str(resolution[0]['type']) == 'date':
                timex = resolution[0]['timex'] + "T00:00:00"


        if 'Places' in entities['type']:
            location = entities['entity']
    # at this point we know if we have necessary information

    if location == null and time == null:
        print("please give a time and place")
    elif time == null:
        print("please give a time")
    elif location == null:
        print("please give a place")
    else:
        print("has both information")
        locationObj.get_result(location)
        print(timex)
        weather_forecast.getResult(locationObj.lat, locationObj.long, timex)
        weather_forecast.printResult()

    choice = input('Continue (Y / N):')
    if choice == 'N' or choice == 'n':
        print('Goodbye')
        break
'''

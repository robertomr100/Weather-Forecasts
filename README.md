# WeatherBot
Group: 
Robert Smitha
Carlito Que
Scott Willits
Roberto Mora

Weatherbot Project for CIS4930 Python. 

The goal of this project was to create a functional AI that gives the user the requested weather for a specific date and location. The user has pretty clear instructions. Type 'exit' in the text will cause the program to exit, otherwise, the user's goal when running the program is to find the desired weather of a specific place. There are many different ways for the user to phrase this, and the bot will guide the user through if it it confused about a specific phrase. To complete the project's current functionality, we used the following APIs and libraries: 

LUIS API
DarkSky API
Google API
tkinter
requests
datetime

The project was mainly divided amongst the group in the following sections:

Robert: Used Google and DarkSky API to produce the weather, given a location and time.
Roberto: Used LUIS API to allow the AI to communicate better, and remember previous phrases and commands.
Scott: Utilized tkinter to create a window class and gridlayout for input and output of messages.
Carlito: Added GUI logic and functionality from LUIS return values  
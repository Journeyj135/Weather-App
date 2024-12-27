# Weather App
This is a simple weather app i created to help build my python programming skills.

# Dependencies:
import requests

from tkinter import *

from tkinter.messagebox import show error

from PIL import ImageTk, Image

from datetime import datetime

# Functions:
get_weather()

    ''' Get the current weather and display it on screen '''

    api_key = 'edeb1cdea91eaa91bdbd67432837****'
    weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={weather_entry.get()}&appid={api_key}&units=imperial')


# Usage:
**Entry Widget to enter city**

weather_entry = Entry(window, justify='center')

weather_entry.focus()

weather_entry.place(x=150, y=10)


# Background Image:
![background image](/workspaces/137717808/weather_app/image_icon.py/sky.png)


# Executing Program:
![results of entering in a city.](C:\Users\newso\OneDrive\Pictures\Screenshots\weather_app_pic.png)

# Error Handling:
![if user types in city that does not exist](C:\Users\newso\OneDrive\Pictures\Screenshots\error_handling.png)


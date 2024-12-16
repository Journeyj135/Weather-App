import requests
from tkinter import *
from tkinter.messagebox import showerror
from PIL import ImageTk, Image
from datetime import datetime, time


def get_weather():
    ''' Get the current weather and display it on screen '''

    api_key = 'edeb1cdea91eaa91bdbd674328375993'
    weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={weather_entry.get()}&appid={api_key}&units=imperial')
    degree_symbol = chr(176)

    try:
        dt_timestamp = weather_data.json()['dt']
        dt = datetime.fromtimestamp(dt_timestamp)
        dt_strf = dt.strftime('%A %B %d, %Y')
        time = dt.strftime('%I:%M%p')

        dt_label = Label(window, text=dt_strf, bg='#0A3288', fg='white',font=('Helvetica', 10, 'bold')).place(x=130, y=35)
        time_label = Label(window, text=time, bg='#0A3288', fg='white',font=('Helvetica', 10, 'bold')).place(x=210, y=55)

        canvas_frame = Canvas(window, width=539, height=110, bg='#0248A3')
        canvas_frame.create_rectangle((300, 300), (300, 300), fill='#0248A3')
        canvas_frame.place(x=5, y=200)

        if weather_data.status_code == 200:
            weather = weather_data.json()['weather'][0]['description']

            temp = weather_data.json()['main']['temp']
            temp_label = Label(window, text=(f'{round(temp)}{degree_symbol}F'),font=('Helvetica', 48), bg='#0A3288', fg='white').place(x=155, y=80)

            sunrise_timestamp = weather_data.json()['sys']['sunrise']
            sunrise = datetime.fromtimestamp(sunrise_timestamp)
            sunrise_strf = sunrise.strftime('%I:%M%p') 
            sunrise_label = Label(window, text=f'Sunrise\n{sunrise_strf}', bg='#0248A3', fg='white', font=('Helvetica', 10, 'bold')).place(x=215, y=210)

            sunset_timestamp = weather_data.json()['sys']['sunset']
            sunset = datetime.fromtimestamp(sunset_timestamp)
            sunset_strf = sunset.strftime('%I:%M%p')
            sunset_label = Label(window, text=f'Sunset\n{sunset_strf}', bg='#0248A3', fg='white', font=('helvitica', 10, 'bold')).place(x=415, y=210)

            weather_label = Label(window, text=weather.title(), bg='#0A3288', fg='white', font=('Helvetica', 14)).place(x=150, y=170)

            description = weather_data.json()['weather'][0]['main']
            description_label = Label(window, text=f'description\n {description}', bg='#0248A3',fg='white', font=('helvitica', 10, 'bold')).place(x=25, y=210)

            humidity = weather_data.json()['main']['humidity']
            humidity_label = Label(window, text=f'Humidity\n {humidity}%', bg='#0248A3',fg='white', font=('helvitica', 10, 'bold')).place(x=25, y=265)

            visibility = weather_data.json()['visibility']
            visibility_label = Label(window, text=f'Visibility\n{visibility/1000} mi', bg='#0248A3', fg='white', font=('helvitica', 10, 'bold')).place(x=205, y=270)

            feels_like = weather_data.json()['main']['feels_like']
            feels_like_label = Label(window, text=f'Feels Like\n{round(feels_like)}{degree_symbol}', bg='#0A3288',fg='white', font=('helvitica', 10, 'bold')).place(x=310, y=160)

            wind_speed = weather_data.json()['wind']['speed']
            windspeed_label = Label(window, text=f'Wind Speed\n{round(wind_speed)} mph', bg='#0248A3',fg='white', font=('helvitica', 10, 'bold')).place(x=415, y=270)

    except Exception:
        error = Label(window, text=showerror('ERROR MESSAGE', f'ERROR! \n{weather_entry.get()} Not Found'))


# Main Window
window = Tk()
window.geometry('550x500')
window.title('My Weather App')

# Background Image
bg =ImageTk.PhotoImage(Image.open('/workspaces/137717808/weather_app/image_icon.py/sky.png'))
background_image = Label(window, image=bg)
background_image.place(x=0, y=0, relwidth=1, relheight=1)

# Entry Widget to enter city
weather_entry = Entry(window, justify='center')
weather_entry.focus()
weather_entry.place(x=150, y=10)


# Search button to get the current weather
search_button = Button(window, text='Search', command=get_weather, bg='#0A3288',fg='white', activebackground='#0A3288', activeforeground='white',padx=-5, pady=-5)
search_button.place(x=345, y=10)


window.mainloop()

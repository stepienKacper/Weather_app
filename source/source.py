#modules
from tkinter import *
from tkinter import messagebox
import requests


#config
api_key = 'your_api_key'
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


#functions
def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        # (City, Country, temp_celsius, temp_fahrenheit, icon, weather)
        city_1 = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_celsius) * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city_1, country, temp_celsius, temp_fahrenheit, icon, weather)
        return final
    else:
        return None

def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = f'{weather[0]}, {weather[1]}'
        temp_lbl['text'] = '{:.2f}℃, {:.2f}F.'.format(weather[2], weather[3])
        weather_lbl['text'] = weather[5]
        city_entry.delete(0, END)
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))

#App
App = Tk()
App.geometry('300x150')
App.title('Weather app')
App.resizable(False, False)
App.iconbitmap(r'icon.ico')

##City text and entry box
city_text = StringVar()
city_entry = Entry(App, textvariable=city_text)
city_entry.pack()

##Search button
search_btn = Button(App, text='Search weather', width=11, command=search)
search_btn.pack()

##Location label
location_lbl = Label(App, text='Location', font=('bold', 23))
location_lbl.pack()

#Temp label
temp_lbl = Label(App, text='')
temp_lbl.pack()

#Weather label
weather_lbl = Label(App, text='')
weather_lbl.pack()

if __name__ == '__main__':
    App.mainloop()
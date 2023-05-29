
from xmlrpc.client import DateTime
import requests
import os

user_api= os.environ['current_weather_data']
location= input('Enter your city : ')

url = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get3691165ffd8e243449eb868af461272e
api_data = api_link.json()

if api_data['cod'] == '404':
    print("Invalid City : {},Please check you City name".format(location))
else :

    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = DateTime.now().strftime("%d %b %Y | %I:%M:%S %p")


    print( "-----------------------------------------")
    print("Weather Stats for - {} || {}".format(location.upper(), date_time))
    print("------------------------------------------")

    print("Current temperture is : {:.2f}deg C".format(temp_city))
    print("Current weather desc :",weather_desc)
    print("Current Humidity :",hmdt, '%')
    print("Current wind speed :",wind_spd , 'kmph')

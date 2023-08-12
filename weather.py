import requests #to accesss the respon from api
from dotenv import load_dotenv
import os
from dataclasses import dataclass


#access our api secret database 
load_dotenv()
api_key = os.getenv('_MY_API_KEY')

#we use dataclasses decorater to create a class to store info what we want to display into our web server 
@dataclass
class weather_display:
	main:str
	description:str
	icon: str
	temperature: int
	humidity:float
	state:str
	country:str
	wind: float




#create a function to get the latitude and longitude 
def get_lat_lon (city_name, state_code, country_code, API_key):
	respons =  requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
	data = respons[0]
	lat, lon = data.get('lat'), data.get('lon')
	return lat,lon

#after we get lon and lat we can now get weather condition with api contain lat and lon already ready. 
def get_weather_condition(lat,lon, API_key):
	resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json() #.json to read object info
	#create weather data object passing our decorater above 
	data = weather_display(
		main = resp.get('weather')[0].get('main'),
		description = resp.get('weather')[0].get('description'),
		icon = resp.get('weather')[0].get('icon'),
		temperature = int(resp.get('main').get('temp')),
		humidity = resp.get('main').get('humidity'),
		state = resp.get('name'),
		country = resp.get('sys').get('country'),
		wind = resp.get('wind').get('speed')
		)

	return data
	# print(resp) #print the information we grab 

#create a function for searching flask apps, we want user to have access to search for any country city name and get the weather info from any part of this world
def main(city_name,state_name,country_name):
	lat,lon = get_lat_lon(city_name, state_name, country_name, api_key)
	weather_info = get_weather_condition(lat,lon,api_key)
	return weather_info

if __name__ == "__main__":
	lat,lon = get_lat_lon('Ampang', 'Selangor', 'Malaysia', api_key)
	print(get_weather_condition(lat,lon,api_key))
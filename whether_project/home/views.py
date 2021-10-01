from django.http.response import HttpResponse
from django.shortcuts import render

import requests

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7ce6474669eb065f3b2fe72c628979d5'

    if request.method=='POST':
        
        city = request.POST.get('city')

        try:
            city_weather = requests.get(url.format(city)).json()
            # sample output of city_whether = {'coord': {'lon': -115.1372, 'lat': 36.175}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'base': 'stations', 'main': {'temp': 69.62, 'feels_like': 67.03, 'temp_min': 64.09, 'temp_max': 74.34, 'pressure': 1016, 'humidity': 16}, 'visibility': 10000, 'wind': {'speed': 4.61, 'deg': 360}, 'clouds': {'all': 1}, 'dt': 1633067047, 'sys': {'type': 1, 'id': 6171, 'country': 'US', 'sunrise': 1633008900, 'sunset': 1633051540}, 'timezone': -25200, 'id': 5506956, 'name': 'Las Vegas', 'cod': 200}
            
            whether = {
                'city' : city,
                'temperature_cel' : round((city_weather['main']['temp']-32)*(5/9)),
                'temperature_fer' : round(city_weather['main']['temp']),
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon']
            }

            return render(request, 'home.html', context=whether)

        except:
            return HttpResponse('No such city, check the spelling.')

    return render(request, 'base.html')


def full(request):
    if request.method=='POST':
        pass
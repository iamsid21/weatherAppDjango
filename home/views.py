from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    city = request.GET.get('city',"delhi")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=88760abf79dd78c76b31279c018c3516'
    data = requests.get(url).json()
    payload = {
        'city' : data['name'] ,
        'weather' : data['weather'][0]['main'],
        'icon' : data['weather'][0]['icon'],
        'faren_temperature' : int((data['main']['temp'] - 273)*(9/5) + 32)  ,
        'Celcius_temperature' : int(data['main']['temp'] - 273) ,
        'pressure' : data['main']['pressure'],
        'humidity' : data['main']['humidity'],
        'desc' : data['weather'][0]['description']
    }
    context = {'data' : payload}
    return render(request,'index.html',context)
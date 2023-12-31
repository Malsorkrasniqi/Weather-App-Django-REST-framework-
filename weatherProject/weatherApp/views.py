import urllib.request
import json
from django.shortcuts import render
import pycountry 

import country_converter as coco    

def index(request):
    if request.method == 'POST':
        

         
        try:
            city = request.POST['city']
            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                            city.replace(" ", "%20") + '&units=metric&appid=9235bd39b8748d9dc00cae108684f34b')

            list_of_data = json.loads(source.read())

            data = {
                "city_name": str(list_of_data['name']),
                "country_code": str(list_of_data['sys']['country']),
                "wind": str(list_of_data['wind']['speed']), 
                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
            }
            
            country_code = str(list_of_data['sys']['country'])
            country_name = coco.convert(names=country_code, to='name_short' )  
            data['country_name'] = country_name


            
            
            
            
            #country_code = str(list_of_data['sys']['country'])
            #country_name = pycountry.countries.get(alpha_2=country_code).name
            #data ["country_name"] = country_name 
            
       

            
            print(data)
            return render(request, "main/index.html", data) 
        except:
            return render(request, "main/index.html"    )

    return render(request, "main/home.html")

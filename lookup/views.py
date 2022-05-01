from django.shortcuts import render
from django.http import FileResponse
import os
import json
import requests

# Create your views here.
def home(request):
    # key: 12678f1a5ce946ba929185409223004
    city = "Birjand"
    api_request = requests.get("http://api.worldweatheronline.com/premium/v1/weather.ashx?key=12678f1a5ce946ba929185409223004&q={}&fx=no&cc=no&mca=yes&format=json".format(city))  
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error : "+str(e)  

    return render(request,'home.html',{'api' : api })

def about(request):
	return render(request,'about.html',{})

def resume(request):
    filepath = os.path.join('static', 'resume.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


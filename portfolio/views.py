from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Port_Contact
from qrcode import *
import os
import requests
import datetime
from pathlib import Path





# Create your views here.
def home(request):
    return render(request,'home.html')



def contact(request):
    
    if request.method=="POST":
        fname= request.POST.get('port-name')
        femail= request.POST.get('port-email')
        fnum=request.POST.get('port-num')
        fmes=request.POST.get('port-message')
        query=Port_Contact( name=fname , email=femail , phonenumber=fnum , message=fmes)
        query.save()
        messages.success(request,"Submitted!")
        return redirect("/")
    return render(request,'home.html')



def internship(request):
    return render(request,'internship.html')
text=None

def qrcode(request):
    global text
    if request.method == "POST":
        text = request.POST.get('text')

        # Check if the file exists and delete it
        file_path = 'static/assets/img/1234.png'
        if Path(file_path).is_file():
            Path(file_path).unlink()

        img = make(text)
        img.save(file_path)

    else:
        pass

    context = {'text': text}

    return render(request, 'qrcode.html', context)




def remove_qrcode(request):
    if os.path.exists('static/assets/img/1234.png'):
        os.remove('static/assets/img/1234.png')
    return redirect('/qrcode') 



def weather(request):
    if request.method == "POST":
        city = request.POST.get('city')
    else:
        city = 'delhi'
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=86c9ac29c62cff036225d6aa7b460e0b'
    data = requests.get(url).json()
    payload = {
        'city': data['name'],
        'weather': data['weather'][0]['main'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],
        'temperature_k': data['main']['temp'],
        'temperature_c': int(data['main']['temp'] - 273.15),
        'min_temp': int(data['main']['temp_min'] - 273.15),
        'max_temp': int(data['main']['temp_max'] - 273.15),
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
    }

    context = {'data': payload}
    print(context)

    return render(request, 'weather_app.html', context)

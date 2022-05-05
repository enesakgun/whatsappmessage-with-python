# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:09:17 2022

@author: Enes Akgun
"""

import requests
import urllib3
import pywhatkit as pwt
import time
import pyautogui
import keyboard as k
from PIL import Image
import datetime
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ID = 745042 #city_id 
url = "https://api.openweathermap.org/data/2.5/weather"
apikey='5ef262979b60eaa0eaf1508b84ba5069'
#?id=315202&appid=97afb3c84a9f644b9bd5b9586ea5497a&units=metric"
query_params = {'id':ID,'appid':apikey,'units':'metric'}
response = requests.get(url,params=query_params,verify=False)
response.json()
weather_id=response.json()['weather'][0]['id']
weather=response.json()['weather'][0]['description']
temperature=str(round(response.json()['main']['temp']))
phone="+905334789340"
filepath = r"C:\Users\Enes Akgun\Images\sky.png"
img = Image.open(filepath)
msg_time=datetime.datetime.now() + datetime.timedelta(minutes = 1)
dakika=msg_time.strftime("%M")
saat=msg_time.strftime("%H")  

if weather_id==800 and ID == 745042: # Change this condition for your city id 
    weather_condition='Istanbulda Hava Acik ve Gunesli, Yaklasik '+temperature+' derecedir'   
    #If only sending a message, use this code
    #pwt.sendwhatmsg(phone, weather_condition, int(saat),int(dakika)) 
    pyautogui.click(1050, 950)
    time.sleep(2) 
    k.press_and_release('enter')
    pwt.sendwhats_image(phone,filepath,weather_condition)


    
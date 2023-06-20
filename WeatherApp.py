import requests 
import json
import os

name = input("Enter your name : ")
city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=c4fd7ee0c61f44dbaad170849232006&q={city}"

r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
t = wdic["location"]["localtime"]
print(f"Dear {name}, the local time in {city} is {t} and its current weather is {w} degrees celsius")
os.system(f"say 'Dear {name}, the local time in {city} is {t} and its current weather is {w} degrees celsius'")
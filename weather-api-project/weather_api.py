import requests
import json
API_KEY = "YOUR_API_KEY"
CITY = input("enter your city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(
    f"--- Weather Information ---"
    f"\nCity :{data["name"]}"
    f"\nTemprature :{data["main"]["temp"]}°C",
    f"\nFeels Like :{data["main"]["feels_like"]}°C" ,
    f"\nPressure :{data["main"]["pressure"]} hPa", 
    f"\nHumidity :{data["main"]["humidity"]}%", 
    f"\nWind Speed :{data["wind"]["speed"]} m/s",
    f"\nCondition :{data["weather"][0]["description"]}"
    )
elif response.status_code == 401:
    print("invalid APi Key")
elif response.status_code == 404:
    print("City Not Found")
else:
    print("Something Went Wrong")
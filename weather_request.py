import requests

def weather_app(city):
    api_key = "your_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        print(f"Temperature in {city}: {temperature}°F")
        print(f"Humidity in {city}: {humidity}%")
        print(f"Weather description: {description}")
    else:
        print("City not found")

city = input("Enter your city: ")
weather_app(city)

import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            weather_info = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
            return weather_info
        else:
            print(f"Error: {data['message']}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather(weather_info):
    if weather_info:
        print(f"Weather in {weather_info['city']}:")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Description: {weather_info['description']}")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Wind Speed: {weather_info['wind_speed']} m/s")
    else:
        print("Weather information not available.")

if __name__ == "__main__":
    
    api_key = "63daeff90c082d13918b6df5ed0145f5"
while True:
    city = input("Enter city name: ")
    weather_info = get_weather(api_key, city)
    display_weather(weather_info)

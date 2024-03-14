import requests

def fetch_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if weather_data["cod"] == 200:
        print(f"Weather in {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather conditions: {weather_data['weather'][0]['description']}")
    else:
        print("Error:", weather_data["message"])

def main():
    api_key = "3e0e264c9728760c8fbd9ceea912b41c"
    location = input("Enter a city or ZIP code: ")
    weather_data = fetch_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()

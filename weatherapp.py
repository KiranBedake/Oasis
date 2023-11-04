import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={location}&appid={api_key}&units=metric"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_condition = data['weather'][0]['description']
        print(f"Weather in {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {weather_condition.capitalize()}")
    else:
        print("Location not found or API request failed. Please try again.")

if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'
    location = input("Enter city or ZIP code: ")
    get_weather(api_key, location)

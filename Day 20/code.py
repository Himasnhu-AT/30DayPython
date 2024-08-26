
import requests

def get_weather_data(city, api_key):
    """Fetches weather data for a given city using OpenWeatherMap API.

    Args:
        city: The name of the city.
        api_key: Your API key for OpenWeatherMap.

    Returns:
        A dictionary containing weather data if successful, otherwise None.
    """

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(complete_url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage:
api_key = "YOUR_API_KEY"  # Replace with your actual API key
city = "London"

weather_data = get_weather_data(city, api_key)

if weather_data:
    temperature = weather_data["main"]["temp"]
    print(f"The current temperature in {city} is {temperature} Kelvin.")
else:
    print("Failed to retrieve weather data.")



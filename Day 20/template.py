
"""
Day 20: Working with External APIs

This script fetches weather data for a given city using the OpenWeatherMap API.

1. Get an API key from OpenWeatherMap: [https://openweathermap.org/api](https://openweathermap.org/api)
2. Replace "YOUR_API_KEY" with your actual API key in the code.
3. Run the script and see the weather data printed to the console.

License: ALL RIGHTS RESERVED (C) 2024 @OpenEdu <git: openeduhq> @Himanshu <git: himanshu-at>

"""

import requests

def get_weather_data(city, api_key):
    """Fetches weather data for a given city using OpenWeatherMap API.

    Args:
        city: The name of the city.
        api_key: Your API key for OpenWeatherMap.

    Returns:
        A dictionary containing weather data if successful, otherwise None.
    """

    # Write your code below this line

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



import requests
import json
import unittest

class APITestCase(unittest.TestCase):

    def test_get_weather_data(self):
        api_key = "YOUR_API_KEY"  # Replace with your actual API key
        city = "London"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city

        response = requests.get(complete_url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue("main" in response.json())
        self.assertTrue("temp" in response.json()["main"])

        temperature = response.json()["main"]["temp"]
        self.assertIsInstance(temperature, float)

    def test_post_data(self):
        # You can add more test cases for POST requests to external APIs here
        pass

if __name__ == '__main__':
    unittest.main()



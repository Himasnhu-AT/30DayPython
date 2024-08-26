
import unittest
from bs4 import BeautifulSoup
import requests

class WebScrapingTest(unittest.TestCase):

    def test_fetch_content(self):
        url = "https://www.example.com"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.text)

    def test_parse_html(self):
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Example Page</title>
        </head>
        <body>
            <h1>Example Heading</h1>
            <p>This is an example paragraph.</p>
        </body>
        </html>
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        self.assertIsNotNone(soup.find('title'))
        self.assertIsNotNone(soup.find('h1'))
        self.assertIsNotNone(soup.find('p'))

    def test_extract_data(self):
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Example Page</title>
        </head>
        <body>
            <h1>Example Heading</h1>
            <p>This is an example paragraph. The price is <span class="price">$100</span>.</p>
        </body>
        </html>
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        price_element = soup.find('span', class_='price')
        self.assertEqual(price_element.text, '$100')

if __name__ == '__main__':
    unittest.main()


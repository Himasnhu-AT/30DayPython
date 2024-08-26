
# Day 18: Web Scraping with Python

# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "https://www.example.com" 

# 1. Fetching the Website Content
#  - Use the `requests.get(url)` function to fetch the HTML content from the given URL.
#  - Store the response in a variable called `response`.
#  - Print the status code of the response using `print(response.status_code)`. This should be 200 if the request was successful.

# 2. Parsing the HTML Content
#  - Create a BeautifulSoup object called `soup` to parse the HTML content retrieved in the previous step.
#  - Use `BeautifulSoup(response.text, 'html.parser')` to create the BeautifulSoup object.

# 3. Extracting Data
#  - Use `soup.find('title')` to find the title tag in the HTML.
#  - Extract the text content of the title tag using `title.text`.
#  - Print the extracted title using `print(f"Page Title: {title}")`.

#  - Use `soup.find_all(['h1', 'h2', 'h3'])` to find all heading tags (h1, h2, h3) in the HTML.
#  - Loop through the found heading tags and print their text content using `print(f"- {heading.text}")`.

#  - Use `soup.find_all('p')` to find all paragraph tags in the HTML.
#  - Loop through the found paragraph tags and print their text content using `print(f"- {paragraph.text}")`.

# Write your code below this line

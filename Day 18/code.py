
import requests
from bs4 import BeautifulSoup

# Define the URL of the website
url = "https://www.example.com" 

# Fetch the content of the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the title of the page
    title = soup.find('title').text
    print(f"Page Title: {title}")

    # Find all heading tags (h1, h2, etc.)
    headings = soup.find_all(['h1', 'h2', 'h3'])
    print("Headings:")
    for heading in headings:
        print(f"- {heading.text}")

    # Find all paragraph tags
    paragraphs = soup.find_all('p')
    print("Paragraphs:")
    for paragraph in paragraphs:
        print(f"- {paragraph.text}")

else:
    print(f"Error fetching content. Status code: {response.status_code}")


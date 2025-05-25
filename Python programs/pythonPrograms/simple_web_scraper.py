# Simple Web Scraper using requests and BeautifulSoup
import requests
from bs4 import BeautifulSoup

url = input("Enter a URL to scrape: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print("Title of the page:", soup.title.string)
print("All links on the page:")
for link in soup.find_all('a'):
    print(link.get('href'))

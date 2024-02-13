from bs4 import BeautifulSoup
import requests

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.title.text
print(title)

# 43 Web Scraping with requests and BeautifulSoup

# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://example.com'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # Extract data from HTML
# title = soup.title.text

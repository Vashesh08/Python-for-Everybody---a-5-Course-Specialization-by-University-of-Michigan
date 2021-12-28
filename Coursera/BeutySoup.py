import re, urllib.request, urllib.error

from bs4 import BeautifulSoup

url = input('Enter - ')

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all anchor tags
tags = soup('a')

for tag in tags:
    print(tag.get('href', None))

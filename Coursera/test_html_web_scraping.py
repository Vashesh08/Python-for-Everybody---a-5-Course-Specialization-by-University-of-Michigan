import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
value = 0
tags = soup('span')

for tag in tags:
    num = int(tag.get_text())
    value += num
print(value)

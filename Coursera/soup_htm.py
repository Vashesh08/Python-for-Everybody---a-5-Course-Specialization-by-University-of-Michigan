# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
no_of_count = 0
count = int(input('Enter count: '))
position = input('Enter position: ')
while no_of_count < count:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    # url = tags[[int(position)-1]].get('href', None)
    k = []
    name = []
    for tag in tags:
        k.append(tag.get('href', None))
        name.append(tag.get_text())
    no_of_count += 1
    url = k[int(position)-1]
    value = name[int(position)-1]


print(value)

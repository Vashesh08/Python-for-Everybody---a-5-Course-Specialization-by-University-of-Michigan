import urllib, urllib.request, urllib.error, xml.etree.ElementTree as ET, ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
stuff = urllib.request.urlopen(url, context=ctx).read().decode()

value = 0
tree = ET.fromstring(stuff)
lst = tree.findall('comments/comment')
for item in lst:
    integer = int(item.find('count').text)
    value += integer

print(value)

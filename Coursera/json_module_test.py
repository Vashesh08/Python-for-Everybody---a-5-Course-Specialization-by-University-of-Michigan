import urllib.request, urllib.error, urllib.parse
import json

url = input("Enter Url:")
value = 0
url_name = urllib.request.urlopen(url).read()
data = json.loads(url_name)
print(data)
# lst = data['comments']
#
# for item in lst:
#     value += item['count']
# print(value)

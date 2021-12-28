import json
import urllib.request

json_data_source = "https://www.youtube.com/manifest.webmanifest"

# with open(json_data_source, encoding="Utf-8") as data:
with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode("UTF-8")
    anomalies = json.loads(data)


for key, value in anomalies.items():
    if isinstance(value, list):
        print(f"{key}.....")
        for items in value:
            print("\t\t {}".format(items))
    else:
        print(f"{key}.....{value}")

print("*"*80)

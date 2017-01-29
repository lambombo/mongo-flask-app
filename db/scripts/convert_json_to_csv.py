import json
import csv

with open("host_list.json") as f:
    js = json.loads(f.read())

f = csv.writer(open("host_list.csv", "w", newline=''))

f.writerow(["id", "lat", "long"])

for i in js:
    f.writerow([i['id'], i['lat'], i['long']])

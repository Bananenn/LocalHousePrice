import requests
import json
import matplotlib.pyplot as plt
import numpy as np

def scrapeBooli(nPages):
  json_txt = "["

  for i in range(1,nPages+1):
    URL = f"https://www.booli.se/slutpriser/vaxjo/116208?page={i}"
    page = requests.get(URL)
    start_string = '"result":[{"__typename":"SoldProperty"'
    index_start = page.text.find(start_string)+10
    index_end = page.text[index_start:].find("]}}") -1 + index_start
    json_txt += page.text[index_start:index_end]+"},"

  json_txt = json_txt[:len(json_txt)-1]
  json_txt += "]"
  json_object = json.loads(json_txt)
  bauty_json = json.dumps(json_object, sort_keys=True, indent=2)

  f = open("tempJSON2.txt", "w")
  f.write(bauty_json)
  f.close()

#scrapeBooli(2)
"""
with open('tempJSON.txt') as f:
    data = f.read()

URL = "https://www.booli.se/slutpriser/vaxjo/794"

json_object = json.loads(data)

lat_long = []
for obj in json_object:
  lat_long.append([obj['latitude'],obj['longitude']])


lat_long = np.array(lat_long)
print(lat_long[:,0])
plt.scatter(x=lat_long[:,0], y=lat_long[:,1])
plt.show()


#print("Nice json ", bauty_json)
"""
import requests
import json

def scrapeBooli():
  URL = "https://www.booli.se/slutpriser/vaxjo/794"
  page = requests.get(URL)

  start_string = '"result":[{"__typename":"SoldProperty"'
  index_start = page.text.find(start_string)+9
  index_end = page.text[index_start:].find("]}}") -1 + index_start
  json_object = json.loads(page.text[index_start:index_end]+"}]")
  bauty_json = json.dumps(json_object, sort_keys=True, indent=2)
  return bauty_json

with open('tempJSON.txt') as f:
    data = f.read()

json_object = json.loads(data)
print(json_object[0]['soldPrice']['raw'])

"""
f = open("tempJSON.txt", "w")
f.write(bauty_json)
f.close()
"""

#print("Nice json ", bauty_json)
import requests
import json
import matplotlib.pyplot as plt
import numpy as np
import string

import subprocess

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

s = '{"booliId":"4795012","soldPrice":{"__typename":"FormattedValue","formatted":"2 200 000 kr","raw":2200000,"value":"2 200 000","unit":"kr"},"streetAddress":"Lotusvägen 9","soldSqmPrice":{"__typename":"FormattedValue","formatted":"20 400 kr/m²"},"soldPriceAbsoluteDiff":{"__typename":"FormattedValue","formatted":"-300 000 kr"},"soldPricePercentageDiff":{"__typename":"FormattedValue","formatted":"-12 %","raw":-12},"listPrice":{"__typename":"FormattedValue","formatted":"2 500 000 kr"},"livingArea":{"__typename":"FormattedValue","formatted":"108 m²"},"rooms":{"__typename":"FormattedValue","formatted":"6 rum"},"objectType":"Villa","descriptiveAreaName":"Teleborg","soldPriceType":"Slutpris","daysActive":70,"soldDate":"2022-12-16","latitude":56.846601,"longitude":14.806279,"url":"/bostad/2534057"}'
json_object = json.loads(s)
print("YES ----------------------------")

def scrapeBooli(nPages):
  f = open("tempJSON2.txt","a")
  f.write("[")
  json_txt = ""
  for i in range(1,nPages+1):
    URL = f"https://www.booli.se/slutpriser/vaxjo/116208?page={i}"
    page = requests.get(URL)
    index_start = page.text.find('"result":[{"__typename":"SoldProperty"')+10
    index_end = page.text[index_start:].find("]}}") -1 + index_start
    json_txt += page.text[index_start:index_end]

    for entry in json_txt.split('{"__typename":"SoldProperty",')[1:]:
      try:
        entry = "{" + entry[:len(entry)-1] 
        json_object = json.loads(entry)
        bauty_json = json.dumps(json_object, sort_keys=True, indent=2)
        f.write(bauty_json+",")
      except:
        print("-*-*-* BAD -*-*-*")
 
  f.write("]")
  f.close()

#scrapeBooli(10)

def printCoordinatesOnmap():
  with open('tempJSON2.txt') as f:
      data = f.read()

  json_object = json.loads(data)

  lat_long = []
  for obj in json_object[:2]:
    lat_long.append([obj['latitude'],obj['longitude']])
    print(obj['streetAddress'])


  lat_long = np.array(lat_long)
  fig, ax = plt.subplots()
  img = plt.imread("LocalHousePrice\\vxoimg.PNG")
  ax.imshow(img, extent=[56.833862, 56.926051 ,14.726890, 14.865267])
  print("X latitude ", lat_long[:,0], " Y longitude ", lat_long[:,1])
  ax.scatter(x=lat_long[:,0], y=lat_long[:,1],marker=".")
  ax.scatter(56.880544, 14.833087, marker="x")
  print(len(lat_long))

  plt.show()

printCoordinatesOnmap()


#print("Nice json ", bauty_json)


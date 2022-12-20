import requests
import json
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

import matplotlib.cbook as cbook
import matplotlib.image as image

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

# explicit function to normalize array
def normalize(arr, t_min, t_max):
    norm_arr = []
    diff = t_max - t_min
    diff_arr = max(arr) - min(arr)   
    for i in arr:
        temp = (((i - min(arr))*diff)/diff_arr) + t_min
        norm_arr.append(temp)
    return norm_arr


def printCoordinatesOnmap():
  with open('tempJSON2.txt') as f:
      data = f.read()
      

  json_object = json.loads(data)

  lat_long = []
  for obj in json_object[1:]:
    lat_long.append([obj['latitude'],obj['longitude']])
    print(obj["streetAddress"])

  lat_long = np.array(lat_long)
  lat_long
  print("X latitude ", lat_long[:,0],".",lat_long[:,1])
  datafile = cbook.get_sample_data("C:\LocalHousePrice\LocalHousePrice\\vxoimgFlip.png", asfileobj=False)
  
  im = image.imread(datafile)
#                                           (left, right, bottom, top)
  myaximage = plt.imshow(im, alpha=0.5, zorder=-1, origin='lower') 
  plt.scatter(x=normalize(lat_long[:,1],0, 570), y=normalize(lat_long[:,0], 0, 704),marker=".")
  #ax = plt.gca()
  #ax.set_aspect('equal' , adjustable='box')
  plt.grid()
  plt.show()
  """
  ax.scatter(x=lat_long[:,0], y=lat_long[:,1])
  ax.scatter(56.880457, 14.833258,marker="x")
  ax.scatter(56.850406, 14.843866,marker="x")
  ax.scatter(56.889891, 14.753340,marker="x")
  ax.scatter(56.855765, 14.778129,marker="x")
  ax.scatter(56.901417, 14.825091,marker="x")
  ax.plot([56.880588,56.9043], [14.833065,14.7973] )
  ax.plot([56.850497,56.9113], [14.843374, 14.7532] )
  ax.plot([56.901380, 56.8984], [14.825090, 14.8284] )
  ax.plot([56.855248, 56.8675], [14.778068, 14.7600] )
  ax.plot([56.889892, 56.8508], [14.753486, 14.8117] )
  ax.imshow(img, extent=[56.926051, 56.833862,14.865267, 14.726890],origin="upper") 
  """

printCoordinatesOnmap()


# My            Real
# X  bottom left = bottom left
# -  Bottom right  = Top left
# -  Top left = Bottom Right
# X  Top right = Top right 

# My            Real
# X  bottom left = Bottom left
# -  Bottom right  = 
# -  Top left = X
# X  Top right = Top Right 

# 56.8339,14.7277 Bottom left = True
# 56.9256,14.7277 Bottom right = top left
# 56.8339,14.8644 TOP left = Bottom right
# 56.9256,14.8644 Top right = top right
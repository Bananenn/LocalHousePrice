import requests
import json
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.ndimage.filters import gaussian_filter

import matplotlib.cbook as cbook
import matplotlib.image as image


import subprocess


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
  weights = []
  for obj in json_object[1:]:
    try:
      sqmP = ''.join(c for c in obj["soldSqmPrice"]["formatted"] if c in "1234567890")
      weights.append(int(sqmP))
      lat_long.append([obj['latitude'],obj['longitude']])
    except:
      print(" -- Wopsie --")

  lat_long = np.array(lat_long)
  lat_long
  print("X latitude ", lat_long[:,0],".",lat_long[:,1])
  datafile = cbook.get_sample_data("C:\LocalHousePrice\LocalHousePrice\\vxoimgFlip.png", asfileobj=False)
  
  im = image.imread(datafile)
#                                           (left, right, bottom, top)
  myaximage = plt.imshow(im, alpha=0.5, zorder=-1, origin='lower') 
  x = np.rint(normalize(lat_long[:,1],0, 570))
  y = np.rint(normalize(lat_long[:,0], 0, 704))

  plt.scatter(x, y,marker=".", c=weights, cmap="cool")


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
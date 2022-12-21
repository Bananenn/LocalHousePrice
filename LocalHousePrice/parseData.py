import json
import numpy as np
def getdataFromJSON(file):
  with open(file) as f:
      data = f.read()
      json_object = json.loads(data)

  Sold_data = []
  sucess = fail = 0
  for obj in json_object[1:]:
    try:
      sqmP = ''.join(c for c in obj["soldSqmPrice"]["formatted"] if c in "1234567890")
      Sold_data.append([obj['latitude'],obj['longitude'], int(sqmP)])
      sucess += 1
    except:
      fail += 1

  print(f" -- Read json {sucess} completed {fail} failed")
  return Sold_data

def normalize(arr, t_min, t_max):
    norm_arr = []
    diff = t_max - t_min
    diff_arr = max(arr) - min(arr)   
    for i in arr:
        temp = (((i - min(arr))*diff)/diff_arr) + t_min
        temp = round(temp) # Round as decimal accuracy has no point
        norm_arr.append(temp)
    return norm_arr

def fitdataToPlot(data, xSize, ySize):
  data[:,1] = np.rint(normalize(data[:,1],0, xSize))
  data[:,0] = np.rint(normalize(data[:,0], 0, ySize))
  #data[:,2] =  data[:,2] - int(np.mean(data[:,2]))
  return data
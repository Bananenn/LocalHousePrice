from matplotlib import cbook, image
import numpy as np

def scatterObject(plt, objects): #TODO understand why x and y are switched
  """ ??????????????????
Confusion may be avoided if this is referred to as [y, x]. Numpy defines array coordinates using C-order indexing, so for 2D data stored in standard raster order, the y coordinate comes first. – 
Hugues
 Nov 24, 2020 at 16:02"""
  plt.scatter(objects[:,1], objects[:,0],marker=".", cmap="cool")

def plotImage(plt, imagePath): 
  cbook.get_sample_data(imagePath, asfileobj=False) #TODO understand why it has to be complete path
  im = image.imread(imagePath)
  plt.imshow(im, alpha=0.5, zorder=-1, origin='lower') 

def makeHeatmap(plt, objects):
  heat_arr = np.array((570,704))
  for x,y,value in objects:
    print("VALUE :", value)
    heat_arr[x][y] = value
  print(heat_arr)


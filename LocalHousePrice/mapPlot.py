
import math
from matplotlib import cbook, image
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from scipy.interpolate import griddata
from scipy.stats import kde
import seaborn as sn
from sklearn import metrics  

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
#a

def scatterObject(plt, objects): #TODO understand why x and y are switched
  """ ??????????????????
Confusion may be avoided if this is referred to as [y, x]. Numpy defines array coordinates using C-order indexing, so for 2D data stored in standard raster order, the y coordinate comes first. – 
Hugues
 Nov 24, 2020 at 16:02"""
  plt.scatter(objects[:,1], objects[:,0], marker=".", cmap="coolwarm", c=objects[:,2])

def plotImage(plt, imagePath): 
  cbook.get_sample_data(imagePath, asfileobj=False) #TODO understand why it has to be complete path <-- does this even do anything?
  im = image.imread(imagePath)
  plt.imshow(im, alpha=1, zorder=-1, origin='lower') 


def makeHeatmap(plt, objects): #TODO rename objects as its to close to object that cannot be used
  #clf = RandomForestClassifier(n_estimators = 100, verbose=3)
  #X_train, X_test, y_train, y_test = train_test_split(objects[:,:2], objects[:,2], test_size = 0.30)
  #clf.fit(X_train, y_train)  
  model = KNeighborsClassifier(n_neighbors=1)
  model.fit(objects[:,:2], objects[:,2])
  coordinateList = []
  for x in range(570):
    for y in range(704):
      coordinateList.append([x,y])
  
  print("ListDun")

  coordinateList = np.array(coordinateList)
  #y_pred = clf.predict(coordinateList)
  #print("Pred dun")
  y_pred= model.predict(coordinateList)
  y_pred = np.reshape(y_pred,(570,704))
  plt.imshow(y_pred, cmap="coolwarm", alpha=.5)


  """
  heatmap, xedges, yedges = np.histogram2d(x, y, weights=z, bins=(28,35), density=True)
  extent = [0, 570, 0, 704]

  plt.imshow(heatmap.T, extent=extent, origin='lower',alpha=1)
  plt.show()
  """

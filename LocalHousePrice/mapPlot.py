
import math
from matplotlib import cbook, image
import numpy as np

from scipy.interpolate import griddata
from scipy.stats import kde
import seaborn as sn
#a

def scatterObject(plt, objects): #TODO understand why x and y are switched
  """ ??????????????????
Confusion may be avoided if this is referred to as [y, x]. Numpy defines array coordinates using C-order indexing, so for 2D data stored in standard raster order, the y coordinate comes first. – 
Hugues
 Nov 24, 2020 at 16:02"""
  plt.scatter(objects[:,1], objects[:,0], marker=".", cmap="Reds", c=objects[:,2])

def plotImage(plt, imagePath): 
  cbook.get_sample_data(imagePath, asfileobj=False) #TODO understand why it has to be complete path <-- does this even do anything?
  im = image.imread(imagePath)
  plt.imshow(im, alpha=1, zorder=-1, origin='lower') 


def makeHeatmap(plt, objects): #TODO rename objects as its to close to object that cannot be used
  res = sn.kdeplot(x=objects[:,0],y=objects[:,1], weights=objects[:,2], cmap=sn.color_palette("YlOrBr", as_cmap=True), shade=True) #levels=20, ,shade=True, common_norm=False)
  plt.show()
  """
  x = objects[:,0]
  y = objects[:,1]
  z = objects[:,2]
  heatmap, xedges, yedges = np.histogram2d(x, y, weights=z, bins=(28,35), density=True)
  extent = [0, 570, 0, 704]

  plt.imshow(heatmap.T, extent=extent, origin='lower',alpha=1)
  plt.show()
  """

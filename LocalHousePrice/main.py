from BooliWebscraper import *
from parseData import *
from mapPlot import *

import matplotlib.pyplot as plt
import numpy as np

#scrapeBooli(1, "teeeeeest.txt")

plt.xlim([0, 570])
plt.ylim([0, 704])
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')

data = getdataFromJSON("tempJSON2.txt")
data = np.array(data)
data = fitdataToPlot(data, 570, 704) # TODO Will not fit properly due to it only normalizing to array not to plot
scatterObject(plt, data)
plotImage(plt, "C:\LocalHousePrice\LocalHousePrice\\vxoimgFlip.png") # TODO understand why image has to be fliped origin='lower'

makeHeatmap(plt, data)
plt.show()
#x = y = z = [10.0,20.0,30.0]
#arr = np.array((x,y,z))

#print(arr[:,1])

#data = fitdataToPlot(arr, 570, 704)

#print(data)
#plt.show()
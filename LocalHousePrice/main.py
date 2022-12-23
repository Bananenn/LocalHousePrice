from BooliWebscraper import *
from parseData import *
from mapPlot import *

import matplotlib.pyplot as plt
import numpy as np

#scrapeBooli(30, "pages30.txt")

plt.xlim([0, 570])
plt.ylim([0, 704])
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')

data = getdataFromJSON("pages30.txt")
data = np.array(data)
data = fitdataToPlot(data, 570, 704) # TODO Will not fit properly due to it only normalizing to array not to plot
scatterObject(plt, data)
plotImage(plt, "C:\LocalHousePrice\LocalHousePrice\\vxoimgFlip.png") # TODO understand why image has to be fliped origin='lower'

makeHeatmap(plt,data)

plt.show()
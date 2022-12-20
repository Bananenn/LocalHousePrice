import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

x, y, z = np.random.rand(3, 50)
f, ax = plt.subplots()

points = ax.scatter(x, y, c=z, s=50, cmap="plasma")
f.colorbar(points)

plt.show()

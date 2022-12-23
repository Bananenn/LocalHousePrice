import numpy as np
import matplotlib.pyplot as plt

N = 1000
x = np.random.uniform(0, 10, N)
y = np.random.uniform(0, 10, N)
z = np.cos(x) * np.sin(y)

counts, xbins, ybins = np.histogram2d(x, y, bins=(30, 20))
sums, _, _ = np.histogram2d(x, y, weights=z, bins=(xbins, ybins))



with np.errstate(divide='ignore', invalid='ignore'):  # suppress possible divide-by-zero warnings
    m3 = plt.pcolormesh(ybins, xbins, sums / counts, cmap='coolwarm')

plt.show()

"""
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(15, 4))
m1 = ax1.pcolormesh(ybins, xbins, counts, cmap='coolwarm')
plt.colorbar(m1, ax=ax1)
ax1.set_title('counts')
m2 = ax2.pcolormesh(ybins, xbins, sums, cmap='coolwarm')
plt.colorbar(m2, ax=ax2)
ax2.set_title('sums')
"""
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
import pandas
data = pandas.read_csv("C:/mtcars.csv")
res = sn.kdeplot(data['mpg'],data['qsec'],color='blue',shade=True)
plt.show()

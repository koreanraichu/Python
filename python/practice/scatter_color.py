import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

np.random.seed(0)
n = 150
x = np.random.rand(n)
y = np.random.rand(n)
colors=np.random.rand(n)
area = (30 * np.random.rand(n))**2

fig,ax=plot.subplots()
plot.scatter(x,y,alpha=0.8,s=area,c=colors,cmap='spring') #s가 크기인갑네
plot.xlabel=('X')
plot.ylabel=('Y')
plot.colorbar()
plot.savefig('graph.png')
plot.show()
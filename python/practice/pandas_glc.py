import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
glc=pd.read_csv("/home/koreanraichu/Glucose.csv",sep=";")
fig,ax=plot.subplots()
ax.scatter(glc['Molecular Weight'],glc['ChEMBL ID'])
plot.savefig('example.png')
plot.show()

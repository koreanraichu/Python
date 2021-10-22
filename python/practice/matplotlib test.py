import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
fig, ax=plot.subplots()
data=np.random.rand(1000)
ax.hist(data, bins=(50),
        color="#000000")
plot.savefig('example.png')
plot.show()

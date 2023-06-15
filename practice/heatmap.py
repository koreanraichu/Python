import matplotlib.pyplot as plot
import numpy as np

arr = np.random.standard_normal((40, 40))
plot.matshow(arr,cmap="copper")
plot.savefig('heatmap.png')
plot.colorbar(shrink=0.8)
plot.clim(-3,3)
plot.show()
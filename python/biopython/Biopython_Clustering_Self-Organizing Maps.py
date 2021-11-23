from Bio.Cluster import somcluster
import numpy as np
data=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[0,1,2,3]])
clusterid, celldata = somcluster(data)
print("clusterid:",clusterid,"\n","celldata:",celldata)
# SOM clustering이라던가... 아 어렵. 
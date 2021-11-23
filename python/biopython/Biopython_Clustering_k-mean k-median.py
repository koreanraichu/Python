from Bio.Cluster import kcluster
import numpy as np
data=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[0,1,2,3]])
clusterid, error, nfound = kcluster(data)
print("Clusterid:",clusterid, "error:",error, "nfound:",nfound)
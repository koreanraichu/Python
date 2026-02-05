from Bio.Cluster import kmedoids
from Bio.Cluster import distancematrix
import numpy as np
data=np.array([[0, 1,  2,  3],[4, 5,  6,  7],[8, 9, 10, 11],[1, 2,  3,  4]])
matrix = distancematrix(data)
# 뭐야 이거 왜 한영키 안먹어요
distances = distancematrix(data, dist='e')
clusterid, error, nfound = kmedoids(distances)
print("clusterid:",clusterid,"error:",error,"nfound:",nfound)
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from Bio.Cluster import distancematrix
from scipy.spatial import distance_matrix
data=np.array([[0, 1,  2,  3],[4, 5,  6,  7],[8, 9, 10, 11],[1, 2,  3,  4]])
matrix = distancematrix(data)
# 뭐야 이거 왜 한영키 안먹어요
distances = distancematrix(data, dist='e')
print(distances)
# Bio.cluster
distances2=euclidean_distances(data)
print(distances2)
# sklearn euclidean distance matrix
distances3=distance_matrix(data,data)
print(distances3)
# scipy distance matrix
# scipy distance.euclidean는 1차원 벡터 전용이다.
from Bio.Cluster import pca
import numpy as np
data=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[0,1,2,3]])
columnmean, coordinates, components, eigenvalues = pca(data)
print("columnmean:",columnmean)
print("coordinates:",coordinates)
print("components:",components)
print("eigenvalues:",eigenvalues)
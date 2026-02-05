from Bio.Cluster import treecluster
import numpy as np
from Bio.Cluster import distancematrix
data=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[0,1,2,3]])
tree = treecluster(data)
print(tree)
# 예제 데이터도 없어...
# 아무튼 이런 식으로 array로 그릴수도 있고
tree = treecluster(data,dist="b",distancematrix=None)
print(tree)
# 다른 옵션을 줄 수도 있다.
distances=distancematrix((data))
tree = treecluster(data=None,distancematrix=distances)
print(tree)
# Distance matrix를 미리 계산해 그걸로 그릴 수도 있다.
# ValueError: use either data or distancematrix; do not use both
# Data와 Distance matrix중 하나는 None이어야 한다. 안그러면 위 에러가 반긴다.
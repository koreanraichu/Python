from Bio.Cluster import Node, Tree
A=Node(2,3,0) # left, right만 존재(거리=0)하는 노드
B=Node(2,3,0.91) # left, right, distance가 셋 다 존재하는 노드
nodes = [Node(1, 2, 0.2), Node(0, 3, 0.5), Node(-2, 4, 0.6), Node(7, -3, 0.9)]
tree = Tree(nodes)
print(B.left,B.right,B.distance)
# Node의 정보를 표시해준다.
print(tree)
# Node를 생성해 그걸 바탕으로 Tree를 그릴 수도 있다.
print(tree[0])
# 생성된 tree에서 indexing을 통해 노드에 접근할 수 있다.
print(tree[0].left)
# 노드에 접근해서 노드의 정보를 가져올 수도 있다.
indices = tree.sort()
clusterid = tree.cut(nclusters=2)
print("indices: ",indices)
print("clusterid: ",clusterid)
# 누구 저 sort 어떻게 쓰는 지 아는 사람?
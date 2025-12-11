# 트리도 연결 리스트로 만든다...
# 그래서 노드
class Node:
    def __init__ (self, _value):
        # 관리할 값
        self.value = _value
        # 부모
        self.parent = None
        # 자식 리스트
        self.childlist = []

    def add_child(self, child_node):
        # 자식 노드 추가
        self.childlist.append(child_node)
        # 부모 연결 설정
        child_node.parent = self
    
# 샘플 트리
nodeA = Node('A') # root 
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')
nodeH = Node('H')
nodeI = Node('I')
nodeJ = Node('J')
nodeK = Node('K')
nodeM = Node('M')
nodeN = Node('N')

# A-B/C
nodeA.add_child(nodeB)
nodeA.add_child(nodeC)

# B-D/E
nodeA.childlist[0].add_child(nodeD)
nodeA.childlist[0].add_child(nodeE)

# C-F/G
nodeA.childlist[1].add_child(nodeF)
nodeA.childlist[1].add_child(nodeG)

# E-H/I
nodeA.childlist[0].childlist[1].add_child(nodeH)
nodeA.childlist[0].childlist[1].add_child(nodeI)

# I-J/K
nodeA.childlist[0].childlist[1].childlist[1].add_child(nodeJ)
nodeA.childlist[0].childlist[1].childlist[1].add_child(nodeK)

# D-M/N
nodeA.childlist[0].childlist[0].add_child(nodeM)
nodeA.childlist[0].childlist[0].add_child(nodeM)

# 위에 저 트리를 DFS로 탐색해보자. 
def DFS (_rootnode, _search_list, _depth = 0):
    indent = "ㆍ" * _depth
    print(f'{indent} {_depth}단계: {_rootnode.value}')
    # 전달받은 노드는 방문한 것으로 취급한다. 
    _search_list.append((_rootnode.value, _depth))
    # 현재 루트 노드의 자식 노드들을 가지고 반복함
    for subnode in _rootnode.childlist:
        DFS(subnode, _search_list, _depth+1)

# 탐색 결과
search_list = []
DFS(nodeA, search_list)
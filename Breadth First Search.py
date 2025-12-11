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

# BFS
# DFS가 수직이라면 얘는 수평이다. 탐색할 때 인접한 노드 리스트를 다 담아둔다. (방문한, 방문할 두개)

def BFS(_rootnode, _search_list):
    # 방문'한' 노드
    gone_list = [_rootnode]
    # 방문'할' 노드
    will_going_list = []
    # 단계(깊이)
    depth = 0
    while True:
        print(f"\n[Level {depth}]")
        for gone in gone_list:
            _search_list.append(gone)
            print(f"- {gone.value}")
            # 인접한 노드들을 담는다
            will_going_list.extend(gone.childlist)
        # 가고 나면 갱신
        gone_list.clear()
        gone_list.extend(will_going_list)
        will_going_list.clear()
        depth += 1

        # 더 갈 거 없으면 종료
        if len(gone_list) == 0:
            break

search_list = []
BFS(nodeA, search_list)
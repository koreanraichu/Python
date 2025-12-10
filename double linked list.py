# 노드
class Node:
    def __init__(self, _value):
        # 값
        self.value = _value
        # 이전/다음 노드
        self.prevnode = None
        self.nextnode = None

# 늘 얘기하는거지만... 여기가 본론입니다. 
class doublelinkedlist:
    # 이닛
    def __init__(self):
        # 장암역(머리?)
        self.head = Node(0)
        # 석남역(꼬리?)
        self.tail = Node(0)
        # 머리랑 꼬리만 있음
        self.head.nextnode = self.tail
        self.tail.prevnode = self.head
        # 크기
        self.listsize = 0
    # 추가
    # istail = True->꼬리/False->앞
    def add_node (self, _value, _istail):
        # <시스템> 노드가 생성되었습니다 
        new_node = Node(_value)
        # istail이 True이면 뒤로, istail이 False이면 앞으로 간다. 
        # 뒤에서 추가: tail의 바로 앞 노드를 변수에 담은 다음 -> 새 노드의 다음 노드를 꼬리의 이전 노드로 설정하고-> 새 노드의 다음 노드를 꼬리로 설정하고 -> 
        # 꼬리의 이전 노드의 다음 노드를 새 노드로 설정하고 -> 꼬리의 이전 노드가 새 노드가 된다 
        if _istail == True: 
            # 꼬리의 바로 앞 노드
            tail_prev = self.tail.prevnode
            # 새 노드의 앞뒤를 묶어보자
            new_node.prevnode = tail_prev # 새 노드의 이전
            new_node.nextnode = self.tail # 새 노드의 뒤(꼬리)
            # 꼬리의 이전 노드의 다음 노드를 새 노드로 설정+꼬리의 이전 노드가 새 노드가 된다 
            tail_prev.nextnode = new_node # 꼬리의 이전 노드의 다음 
            self.tail.prevnode = new_node # 꼬리 앞
            # 리스트 전체 길이
            self.listsize += 1
            return

        # 앞에서 추가: 위랑 비슷한데 시발점이 머리이기때문에 머리의 바로 뒤 노드를 담아야 한다. 
        else: 
            # 머리의 바로 뒤 노드
            head_next = self.head.nextnode
            # 앞뒤를 묶어요
            new_node.prevnode = self.head # 새 노드의 앞(머리)
            new_node.nextnode = head_next # 새 노드의 뒤
            # 머리의 다음 노드가 새 노드가 된다. 
            head_next.prevnode = new_node # 머리의 다음 노드의 이전(...)
            self.head.nextnode = new_node # 머리 뒤
            # 리스트 전체 길이
            self.listsize += 1
            return

    # 삭제
    # ishead = True->머리부터 시작해서 n번째/False->꼬리부터 시작해서 n번째 
    def delete_node (self, _position, _ishead):
        move_cnt = _position + 1
        # 머리부터
        if _ishead == True:
            pointernode = self.head
            # 렛츄고
            for _ in range(move_cnt):
                # n번째 노드에 도착할때까지 내려간다. 
                pointernode = pointernode.nextnode
        # 꼬리부터
        else: 
            pointernode = self.tail
            # 렛츄고
            for _ in range(move_cnt):
                # n번째 노드에 도착할떄까지 올라간다. 
                pointernode = pointernode.prevnode
        # 도착했으면 앞뒤를 확인한다 
        front = pointernode.prevnode
        back = pointernode.nextnode
        # 연결을 끊고
        pointernode.prevnode = None
        pointernode.nextnode = None
        # 잇는다
        front.nextnode = back
        back.prevnode = front
        self.listsize -= 1
        return

    # 조회
    # ishead = True->머리부터/False->꼬리부터
    def get_node (self, _position, _ishead): 
        # 얘는 걍 조회라 리스트 사이즈가 바뀌지는 않는다. 
        # ishead = True->머리에서부터 n번째/ishead = False->꼬리에서부터 n번째
        move_cnt = _position + 1 # 헤드 끼고 하면 한번 더 가야된다고 생각하시면 편합니다 
        # 머리부터
        if _ishead == True:
            pointernode = self.head # 시발점 
            for _ in range(move_cnt):
                pointernode = pointernode.nextnode # 앞으로 갓
        # 꼬리부터
        else: 
            pointernode = self.tail # 시발점
            for _ in range(move_cnt):
                pointernode = pointernode.prevnode # 뒤로 빽
        
        # 내가 값이여 
        return pointernode.value

    # 끼워넣기(?)
    # ishead = True->머리부터 시작해서 position - 1 & position/False->꼬리부터 시작해서 position & position + 1
    # ishead, 0->맨앞
    def insert_node (self, _position, _value, _ishead):
        # <시스템> 노드가 생성되었습니다 
        new_node = Node(_value)
        # 얘는 노드 하나만 찾으면 된다. 왜냐고? 내 위로, 내 밑으로 다 있으니까. 물론 시발점에 따라 이동 방향은 다르지만서도... 
        move_cnt = _position + 1
        # 머리부터 출발
        if _ishead == True: 
            pointernode = self.head # 시발점(욕 아님)
            for _ in range(move_cnt):
                pointernode = pointernode.nextnode # 도착하였소!!! 
                # 저기 위에 삽입한거 보이시죠? 그거 그대로 하면 됩니다. pointnode 다음에 넣을거임. 
            where_insert = pointernode.prevnode
            # 앞-새거-포인트
            where_insert.nextnode = new_node
            pointernode.prevnode = new_node
            # 새 노드도 연결
            new_node.prevnode = where_insert
            new_node.nextnode = pointernode
            # 리스트 전체 길이
            self.listsize += 1
            return

        # 꼬리부터 출발
        else: 
            pointernode = self.tail # 시발점(욕 아니예욧)
            for _ in range(move_cnt):
                pointernode = pointernode.prevnode # 아 왔다고 
                # 얘는 pointnode 앞에 간다. 
            where_insert = pointernode.nextnode
            # 포인트-새거-뒤
            where_insert.prevnode = new_node
            pointernode.nextnode = new_node
            # 새 노드 연결 
            new_node.prevnode = pointernode
            new_node.nextnode = where_insert
            # 리스트 전체 길이
            self.listsize += 1
            return

    # 수정
    # ishead = True->머리부터 시작해서 n번째/False->꼬리부터 시작해서 n번째 
    def set_node (self, _position, _value, _ishead):
        # 가야 수정하쥬...
        move_cnt = _position + 1
        # 이건 걍 값만 바꾸는겁니다. 그니까 노드가 갖고 있는 값만요!! 
        # 머리부터
        if _ishead == True:
            pointernode = self.head
            # 그럼 출발! 
            for _ in range(move_cnt):
                pointernode = pointernode.nextnode
            pointernode.value = _value

        # 꼬리부터
        else: 
            pointernode = self.tail
            # 그럼 출발! 
            for _ in range(move_cnt):
                pointernode = pointernode.prevnode
        
        # 값 변경
        pointernode.value = _value
        return

    # (from head) 다 보여줘
    def node_show(self): 
        # head가 가리키는 게 tail이면(중간에 암것도 없으면)
        # 지하철인데 역이 없어 역이 
        if self.head.nextnode == self.tail:
            print('리스트가 비었습니다. ')
            return
        # 아 이제 역 좀 생겼다 
        pointernode = self.head

        while True:
            # 다음으로 렛츄고
            pointernode = pointernode.nextnode
            print(pointernode.value)
            # 없으면 시마이
            if pointernode.nextnode == self.tail:
                break
        return
    
# sample code
# 객체 생성
doublelist = doublelinkedlist()

# 추가하게 되면 무조건 머리 바로 뒤/꼬리 바로 앞에 갑니다. 
# from tail
doublelist.add_node('피카츄',True) # 가운데
doublelist.add_node('따라큐',True) # 뒤
doublelist.add_node('드니차',True) # 뒤
doublelist.add_node('레시라무',True) # 뒤

# from head
doublelist.add_node('수댕이',False) # 앞
doublelist.add_node('리아코',False) # 앞
doublelist.add_node('누오',False) # 앞
doublelist.add_node('칠색조',False) # 앞

# 잠시 중간점검이 있겠습니다. 
doublelist.node_show()
print('+------------------------------+')

# 끼워넣기
doublelist.insert_node(2,'토오',True) # 앞
doublelist.insert_node(4,'크로뱃',True) # 앞
doublelist.insert_node(2,'미끄메라',False) # 뒤
doublelist.insert_node(4,'맘박쥐',False) # 뒤
# 오 나왔다
doublelist.node_show()
print(f'리스트 길이: {doublelist.listsize}')
print('+------------------------------+')

# 삭제
doublelist.delete_node(5,True) # 앞
# 오 나왔다
doublelist.node_show()
print(f'리스트 길이: {doublelist.listsize}')
print('+------------------------------+')

doublelist.delete_node(5,False) # 뒤
# 오 나왔다
doublelist.node_show()
print(f'리스트 길이: {doublelist.listsize}')
print('+------------------------------+')

# 내용 변경
doublelist.set_node(3,'조타구',True) # 앞
doublelist.set_node(3,'이야후',False) # 뒤
# 오 나왔다
doublelist.node_show()
print(f'리스트 길이: {doublelist.listsize}')
print('+------------------------------+')
# 리스트 검색
print(doublelist.get_node(3,True)) # 앞에서부터 3번째(근데 이제 +1 한...)
print(doublelist.get_node(3,False)) # 뒤에서부터 3번째 
print('+------------------------------+')

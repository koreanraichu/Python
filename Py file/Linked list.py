# 노드
class Node:
    # 뾰로롱
    def __init__ (self, _value):
        self.value = _value
        self.nextnode = None
        
    # 다음 노드의 주소값을 설정 
    def setnext(self,_nextnode):
        self.nextnode = _nextnode

class Linkedlist:
    # 머리
    def __init__ (self):
        self.headnode = Node(0)
        self.datacount = 0 # 연결 리스트의 길이
    
    # 데이터 넣기
    def add_node (self, _value):
        # 새로운 노드 생성
        new_node = Node(_value)
        pointernode = self.headnode
        # 마지막 노드가 어디 있나
        while True:
            # 찾았으면 뒤에 추가해라 
            if pointernode.nextnode == None: 
                break
            else: 
                pointernode = pointernode.nextnode
        pointernode.nextnode = new_node
        # 카운터 추가
        self.datacount += 1

    # 내놔
    def where_node (self, _position): 
        target_index = _position - 1
        # 잘못 입력했다면
        if _position < 1: 
            print('순서값은 1보다 같거나 큰 정수입니다. ')
            return
        elif _position > self.datacount:
            print(f'범위는 1부터 {self.datacount}까지입니다. ')
            return
        # 여기가 본론임... 
        else: 
            # 헤드에서 시작해서 우리가 찾는 포지션 값까지 가야 한다. 
            pointernode = self.headnode
            # 전체 이동 횟수를 계산하고 
            move_cnt = target_index + 1
            # 그만큼 반복 아... 
            for i in range(move_cnt):
                # 가야돼 아... 
                pointernode = pointernode.nextnode
            # 드디어 나옴 
            return pointernode.value
        
    # 여기다 넣어줘
    def insert_node (self, _position, _value):
        # 수정할 포지션
        target_index = _position - 1 # 3 입력하면 3번째 수정하려면 필요함 
        # prev: 하나 덜 감/curr: 정직하게 ㄱㄱ
        # 2번때에 노드 끼워넣는거면 1, 2까지 갑니다. 
        if _position < 1: 
            print('순서값은 1보다 같거나 큰 정수입니다. ')
            return
        elif _position > self.datacount:
            # 리스트 길이를 벗어나면... 아니 근데 그러면 걍 끼워넣기 하면 안됨? 
            print(f'범위는 1부터 {self.datacount}까지입니다. ')
            return
        else: 
            # 끼워넣을 노드
            new_node = Node(_value)
            # 노드를 끼워넣을 포지션과 그 앞 노드에 대한 정보가 필요함
            # 그래서 두개지요 
            prev_pointer = self.headnode
            curr_pointer = self.headnode.nextnode
            move_cnt = target_index
            for i in range(move_cnt):
                prev_pointer = prev_pointer.nextnode
                curr_pointer = curr_pointer.nextnode
            # 노드 끼우는 순서: prev-노드-curr
            prev_pointer.nextnode = new_node
            new_node.nextnode = curr_pointer
            # 아 맞다 카운터
            self.datacount += 1
            return 

    # 바꿔줘
    def change_node (self, _position, _value):
        # 3을 입력하면 정직하게 2번째 인덱스를 바꾸기 위해서는 변환 절차가 필요하다. 
        target_index = _position - 1
        if _position < 1: 
            print('순서값은 1보다 같거나 큰 정수입니다. ')
            return
        elif _position > self.datacount:
            # 리스트 길이를 벗어나면... 아니 근데 그러면 걍 끼워넣기 하면 안됨? 
            print(f'범위는 1부터 {self.datacount}까지입니다. ')
            return
        else: 
            # 원리는 간단하다. 찾아라, 그리고 바꿔라. 
            move_cnt = target_index + 1
            pointernode = self.headnode
            for i in range(move_cnt):
                pointernode = pointernode.nextnode
            # 도착했으면 수정을 해야됩니다. 
            pointernode.value = _value

    # 빼줘
    def delete_node (self, _position): 
        # 3을 입력하면 정직하게 2번째 인덱스를 지우기 위해서는 변환 절차가 필요하다. 
        target_index = _position - 1
        if _position < 1: 
            print('순서값은 1보다 같거나 큰 정수입니다. ')
            return
        elif _position > self.datacount:
            # 리스트 길이를 벗어나면... 아니 근데 그러면 걍 끼워넣기 하면 안됨? 
            print(f'범위는 1부터 {self.datacount}까지입니다. ')
            return
        else: 
            # 그 포인터 앞에 있는 노드의 연결을 다음다음노드로 하면 된다. 연결만 끊으면 끝. 
            move_cnt = target_index
            pointernode = self.headnode
            for i in range(move_cnt):
                pointernode = pointernode.nextnode
            pointernode.nextnode = pointernode.nextnode.nextnode
            # 아 맞다 카운터
            self.datacount -= 1
            return

    # 잘 된겨? 
    def node_show (self):
        # 헤드노드의 다음 노드가 없으면
        if self.headnode.nextnode == None:
            print('이 리스트는 텅 비었습니다. ')
            return 
        
        pointernode = self.headnode

        while True:
            # 다음으로 렛츄고
            pointernode = pointernode.nextnode
            print(pointernode.value)
            # 없으면 시마이
            if pointernode.nextnode == None:
                break
        return

# 연결 리스트 생성
linked_list = Linkedlist()

# 뭘 넣어줌
linked_list.add_node('구구')
linked_list.add_node('아보')
linked_list.add_node('삐')
linked_list.add_node('럭키')
linked_list.add_node('메깅')
linked_list.add_node('일레즌')
linked_list.add_node('아르코')

# 다 까봐
linked_list.node_show()
print(linked_list.datacount)
print('---------')

# n번째 노드 까봐 
print(linked_list.where_node(1))
print(linked_list.datacount)
print('----------')

# n번째 자리에 노드 껴줘
linked_list.insert_node(3, '치코리타')
linked_list.insert_node(2, '찌르꼬')
linked_list.node_show()
print(linked_list.datacount)
print('----------')

# n번쨰 자리 노드 바꿀거야
linked_list.change_node(3, '아보크')
linked_list.node_show()
print(linked_list.datacount)
print('----------')

# n번째 자리 노드 삭제할거야 
linked_list.delete_node(7)
linked_list.node_show()
print(linked_list.datacount)
print('----------')
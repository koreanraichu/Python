# 늘 그렇듯이 노드
class Node:
    def __init__(self, _value):
        # 큐값
        self.value = _value
        # 포인터가 가리킬 무언가
        self.nextorder = None

class make_queue:
    def __init__ (self):
        # 포인터 두 개(front, rear)
        self.frontpointer = None
        self.rearpointer = None
        # 큐 크기
        self.queuesize = 0
    
    # 인큐
    def enqueue(self, _value):
        # 인큐: 줄을 섬 
        new_node = Node(_value) # 커피 주문하는 손님
        # 프론트 포인터가 None->마수걸이(첫 손님)
        if self.frontpointer is None: 
            # 일단 하나까지는 같은 곳을 가리킴
            self.frontpointer = new_node
            self.rearpointer = new_node
        else: 
            # 인큐일때는 리어가 이동합니다 
            self.rearpointer.nextorder = new_node
            self.rearpointer = new_node
        # 사이즈 추가
        self.queuesize += 1
        return

    # 디큐
    def dequeue(self):
        # 디큐: 커피 나와서 받고 갈 길 감
        # 이거는 값 표시용입니다. 
        dequeue_pointer = self.frontpointer
        # 대기열이 없으면 디큐 못해요 
        if self.queuesize == 0:
            print('큐가 비었습니다!')
            return
        # 큐가 비지 않았다면 디큐를 하면 됨
        else: 
            # 디큐를 할 때는 프론드 포인터가 한칸 이동합니다
            self.frontpointer = self.frontpointer.nextorder
            self.queuesize -= 1
            # 큐가 비면 두 포인터가 다시 None을 가리키게 해 줘야 한다 
            if self.frontpointer is None: 
                self.rearpointer = None
        return dequeue_pointer.value
    
    # 큐 좀 봅시다
    def queue_show(self):
        # 큐 비었으면 비었다고 하고
        if self.queuesize == 0:
            print('큐가 비었습니다! ')
            return
        # 아니면 쫙 보여줘
        else: 
            # 큐 안 건드리고 내용만 볼겁니다. 
            temp_pointer = self.frontpointer
            # 다음이 비어있나요? 
            while temp_pointer is not None:
                print(temp_pointer.value)
                # 오키 넥스트
                temp_pointer = temp_pointer.nextorder
        return temp_pointer

# <-- 샘플 코드 -->

# 흥민쏜이 골넣으면 붐비는 거기 맞음
megacoffee = make_queue()

# 주문(인큐)
megacoffee.enqueue('연유라떼')
megacoffee.enqueue('아이스 아메리카노')
megacoffee.enqueue('곡물라떼')
megacoffee.enqueue('아몬드밀크 라떼')
print(f'현재 주문 건수: {megacoffee.queuesize}') # 현재 큐 길이(주문 건수)
megacoffee.queue_show() # 뭐뭐 들어옴?
print('----------')

# 을 처리(디큐)
print(f'주문하신 {megacoffee.dequeue()} 나왔습니다!')
print(f'현재 주문 건수: {megacoffee.queuesize}') # 현재 큐 길이(주문 건수)
megacoffee.queue_show() # 뭐뭐 들어옴?
print('----------')

# 을 했더니 새 주문
megacoffee.enqueue('카페라떼')
megacoffee.enqueue('헤즐넛라떼')
print(f'현재 주문 건수: {megacoffee.queuesize}') # 현재 큐 길이(주문 건수)
megacoffee.queue_show() # 뭐뭐 들어옴?
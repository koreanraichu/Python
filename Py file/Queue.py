class queue: 
    # 큐 본체
    def __init__(self): 
        self.items = []
    
    # 큐에 뭘 넣는거(줄서는것)=인큐
    def enqueue(self,data):
        self.items.append(data)
    
    # 큐에서 빼는것(커피 받았다 회사가자)=디큐
    def dequeue(self):
        # 큐가 비었나요? (대기열이 없나요?)
        if self.isEmpty():
            print("큐가 비었습니다!")
            return None
        # 대기열이 있다면 맨 앞 손님의 주문을 해결하자 
        else: 
            return self.items.pop(0)
        
    # 보자... 지금 주문이 얼마나 밀렸지? 
    def peek(self): 
        # 손님이 있나? 
        if self.isEmpty():
            print("큐가 비었습니다!")
            return None
        # 아, 있네. 
        return self.items[0]
    
    def isEmpty(self):
        # 기본 플래그: 안비었어
        is_empty = False
        # 스택의 길이가 0이라면 플래그가 바뀐다 
        if len(self.items) == 0:
            is_empty = True
        return is_empty
    
    # 대기열 얼마나 있음? 
    def size(self):
        return len(self.items)
    
    # 큐 전체를 볼 수 있다. 
    def show(self):
        if self.isEmpty():
            print("큐가 비었습니다!")
        else:
            print(self.items)

# 커피 대기열
coffee = queue()

coffee.enqueue("(HOT)카페라떼")
coffee.enqueue("(HOT)아메리카노")
coffee.enqueue("(HOT)헤즐넛라떼")
coffee.enqueue("(ICE)유니콘프라페")
coffee.enqueue("(HOT)연유라떼")

coffee.show()

# 손님 주문하신 카페라떼 나왔습니다
coffee.dequeue()
# 뱅쇼 주문 받았습니다
coffee.enqueue("(HOT)뱅쇼")
coffee.show()
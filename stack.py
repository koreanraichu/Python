# 스택은 부페 접시같은거다. 부페 접시 뭔지 아시죠? 그 부페가면 쌓여있는 접시요. 
class stack:
    # 스택(부페 접시 탑)
    def __init__ (self):
        self.items = []

    # 빈 공간에 접시를 쌓아보자. 
    def push(self, data):
        self.items.append(data)

    # 손님이 접시를 하나씩 가져간다. 
    def pop(self): 
        pop_object = None
        # 접시 스택이 없다면 없다고 해
        if self.isEmpty():
            print("스택이 비었습니다.")
        # 아니면 접시 하나 줘 
        else: 
            pop_object = self.items.pop()
        return pop_object
    
    # 보자... 여기는 접시가 얼마나 있나...? 
    def peek(self):
        top_object = None
        # 접시 스택이 없다면 없다고 해
        if self.isEmpty():
            print("스택이 비었습니다.")
        # 아니면 뭐가 있는지 보여줘 
        else: 
            top_object = self.items[-1]
        
        return top_object
    
    def isEmpty(self):
        # 기본 플래그: 안비었어
        is_empty = False
        # 스택의 길이가 0이라면 플래그가 바뀐다 
        if len(self.items) == 0:
            is_empty = True
        return is_empty
    
    # 스택 전체를 볼 수 있다. 
    def show(self):
        if self.isEmpty():
            print("스택이 비었습니다.")
        else:
            print(self.items)

# stack
stack_1 = stack()

# 아이템 적재
stack_1.push("이상해씨")
stack_1.push("미끄메라")
stack_1.push("날개치는머리")
stack_1.push("두두")
stack_1.push("아라리")

# 맨 위에 있는 걸 보여줘
print(stack_1.peek())

# 하나 빼고 다시 확인
stack_1.pop()
print(stack_1.peek())
# 노드
class Node:
    def __init__ (self, _value):
        # 값
        self.value = _value
        # 내 밑에
        self.prevnode = None

# Stack
class make_stack:
    # 누가 맨 위냐
    def __init__ (self): 
        self.topnode = None
        # 스택의 크기 
        self.stacksize = 0

    # 스택에 접시를 쌓는다 
    def push(self, _value):
        # 제가 바로 새 노드입니다
        new_node = Node(_value)
        # 장바구니에 넣어보자 
        new_node.prevnode = self.topnode
        self.topnode = new_node

        # 스택 크기 + 1
        self.stacksize += 1

    # 쌓여있던 접시를 꺼낸다 
    def pop(self): 
        # 스택이 비었나 확인 
        if self.stacksize == 0:
            print('비어있어서 뭐 꺼낼 게 없습니다. ')
            return
        # 맨 위에 거기! 나와봐요! 
        else: 
            popped_value = self.topnode.value
            self.topnode = self.topnode.prevnode
            self.stacksize -= 1 # 나갔으니까 사이즈도 줄여줍니다
            return popped_value

    # 다 까봐 
    def stack_show(self):
        # 비었음? 
        if self.stacksize == 0:
            print('스택이 비어있습니다. ')
            return 
        # 아니면 줘봐 
        else: 
            # 내용만 보는거지, 빼는 게 아닙니다. 
            temp_node = self.topnode
            # 다음이 비어있지 않다면 빌때까지 출력 
            while temp_node is not None: 
                print(temp_node.value)
                # 다음
                temp_node = temp_node.prevnode
        return

# <-- 샘플 코드 -->

# 장바구니
basket = make_stack()

# 삑 삑 삑 48000원입니다 
basket.push('허쉬 쿠키앤크림')
basket.push('대파')
basket.push('깐마늘')
basket.push('찌개고기')
basket.push('우유')
basket.push('백목이버섯')
print(f'{basket.stacksize}개의 항목을 구매했다!')
print('')

# 주섬주섬 꺼내며
for _ in range(basket.stacksize):
    print(basket.pop())
    
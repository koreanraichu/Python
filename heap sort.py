# 데이터를 이진 트리화하는 함수
def binary_tree(data):
    # 부모 노드의 개수. 데이터 / 2다. 
    number_of_parent = len(data) // 2 # 소수점따원 필요없다네
    # 완전 이진 트리이기때문에 무조건 자식은 두 개다. 
    # 딕셔너리에는 값의 '순서'를 담는다. ㅇㅋ? ㅇㅇㅋ 
    tree_node = {}
    child_node_idx = 1 # 자식 노드는 1부터 시작 (0은 루트)
    child_node_last = len(data) - 1 # 루트 빼면 전체 길이에서 하나 빠짐
    for i in range(number_of_parent):
        # 자 생성 드가자
        tree_node[i] = []
        # 자식은 최대가 두개(사유: 완전 이진 트리)
        for _ in range(2):
            tree_node[i].append(child_node_idx)
            child_node_idx += 1
            if child_node_idx > child_node_last:
                break
    return tree_node

# 정렬 이즈 히얼 
def heap_sort(data):
    # 정렬 결과
    result_list = []

    # 우리 이거 뻉이쳐야돼요
    while len(data) > 0:
        # 순순히 트리를 넘긴다면 유혈사태는 일어나지 않을 것입니다. 
        tree = binary_tree(data)
        # 키
        keys = tree.keys()
        # 이름내놔
        key_list = list(keys)
        key_list.sort(reverse=True)
        # 본론 드가자...
        for parent in key_list:
            # 자식의 위치
            child_position = tree[parent]
            # 자식의 개수만큼 반복한다 
            for idx in child_position:
                # 부모의 값이 자식의 값보다 작은가?
                if data[parent] < data[idx]:
                    # 작으면 바꿔
                    data[parent], data[idx] = data[idx], data[parent]

        # 제일 큰 값(루트)과 잎을 바꿉니다. 
        data[0], data[-1] = data[-1], data[0]
        # 결과 리스트에 담는다. 
        max_list = data.pop()
        result_list.append(max_list)
    
    # 다 됐음? 
    result_list.reverse()
    data.extend(result_list)
# 위 방식은 최대 힙입니다. (최소 힙으로 쓰려면 부등호 반대로 달아야됨)

# sample list
random_array = [793, 27, 646, 705, 964, 814, 804, 300, 942, 614, 765, 790, 739, 191, 474]
heap_sort(random_array)
print(random_array)
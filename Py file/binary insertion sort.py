# 이진 삽입 정렬은... 위키피디아에 설명이 없어요... 
# 이진 탐색 뭔지 아시죠? 쉽게 말하자면 업앤다운입니다. 그 술마실때 뚜껑 안에 있는 숫자갇고 업다운 많이 하는데 그게 삽입 정렬에 적용된거다... 
# 라고 생각하시면 됩니다. 예. 
# 코드: 제미나이

a = [80, 58, 66, 100, 71, 39, 89, 67, 25, 9] # 배열

# bisect를 써도 되는데 직접 구현해보는게 좋잖아요. 
def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        left = 0
        right = i - 1

        # 이진 탐색으로 들어갈 위치(left) 찾기
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1

        # 요소들을 오른쪽으로 한 칸씩 밀고 삽입
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        arr[left] = key
        print(f'{key}를 정렬함: {arr}')

    return arr

# 사용 예시
print(binary_insertion_sort(a))

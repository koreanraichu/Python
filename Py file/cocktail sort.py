# 칵테일 하면 그 바텐더가 쉐이커 딱 흔들면서 현란한 스킬로 만드는 그겁니다. 
# 그레서 이게 뭔 상관임? 이라고 하신다면 쉐이커 흔들때 어떻게 흔들어요? 왔다갔다 합니다. 
# 그겁니다. 얘도 왔다갔다합니다. 기존 버블 정렬은 앞에서 뒤로만 갔지만, 얘는 앞->뒤 뒤->앞을 반복합니다. 
# 코드 출처: 위키피디아

a = [80, 58, 66, 100, 71, 39, 89, 67, 25, 9] # 배열임다

def cocktailShaker(arr):

    lastIdx = len(arr) - 1
    swapped  = True
    i = 0

    while swapped:
        swapped = False
        for j in range(i, lastIdx-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        print(f'앞->뒤: {arr}')

        if swapped:
            for j in reversed(range(i, lastIdx-i)):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
        print(f'뒤->앞: {arr}')
        i = i + 1
    return arr

print(cocktailShaker(a))
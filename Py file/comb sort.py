# 버블 알고리즘은 큰 값을 뒤로 보내는 건 빠른데, 반대로 작은 값이 뒤로 가는 건 오래 걸립니다. 
# 다들 아시다시피 거품은 위로 떠오를 수는 있지만, 가라앉지는 못 하잖아요. 
# 뭐 아무튼 그래서 갭을 두고 비교합시다 한 건데 이게 빗이랑 뭔 상관이 있는건지는 모르겠음. 
# 코드 출처: 위키피디아/돌떄마다 출력되게 변형한 애: 제미나이

import math # 매th

a = [80, 58, 66, 100, 71, 39, 89, 67, 25, 9] # 배열임다 

def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = math.floor(gap / shrink)

        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                sorted = False

            i = i + 1

        # 각 갭(gap) 순회가 끝날 때마다 현재 상태 출력
        print(f"Gap: {gap} | Array: {arr}")

    print("Final Result:", arr)

comb_sort(a)
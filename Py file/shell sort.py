# 셸 정렬이라길래 뭔 조개껍데기랑 상관 있는건가 했는데 아니었고... 
# 사람 이름입니다. 예. 생각보다 이런거 많아요. 불대수도 만든 사람이 불이고 서던 블로팅도 만든 사람 이름이 서던입니다. 
# 노던 웨스턴 이스턴은 어? 만든 사람이 Southern(남쪽)이네? 해서 붙은거지만 넘어갑시다. 
# 삽입 정렬이 배열이 거의 정렬된 상태에서는 빨라진다는 거에 착안해서 배열을 쪼개서 정렬하고 그걸 삽입정렬하는 뭐 그런겁니다. 
# 코드 출처: 위키피디아/개량: 제미나이

a = [80, 58, 66, 100, 71, 39, 89, 67, 25, 9] # 배! 열! 

def Shellsort(arr):
    h = 1
    while h < len(arr):
        h = 3*h + 1
    h = h//3

    print(f"초기 배열: {arr}\n")

    while h > 0:
        print(f"==============================")
        print(f"현재 간격(h) = {h}")
        
        # h개로 쪼개진 구획(부분 배열/열) 상태를 2차원 리스트 형태로 구성해 확인
        sublists = [[] for _ in range(h)]
        for i, val in enumerate(arr):
            sublists[i % h].append(val)
        print(f"구획별 그룹 (2차원 열 형태): {sublists}")

        # 기존 셸 정렬 로직
        for i in range(h, len(arr)):
            k = i - h
            key = arr[i]
            while k >= 0 and key < arr[k]:
                arr[k+h] = arr[k]
                k = k - h
            arr[k+h] = key
        
        print(f"h={h} 정렬 완료 후 배열: {arr}\n")
        h = h//3

    return arr

# 테스트 예시
Shellsort(a)
# 계수 정렬입니다. 기수 정렬 아님. 
# 코드: 제미나이 

a =  [0, 4, 7, 1, 2, 1, 8, 2, 0, 3, 5, 2, 7, 9, 0] # 배여얼
# 애는 난수 정렬하는 게 아니라 일종의 투표같은 개념이라고 보시면 됩니다. 얘가 몇 번 나왔고 얘가 몇 번 나왔고 뭐 그런거요. 

def counting_sort(arr):
    # 1. 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
    # 최댓값을 안다고 가정 (예: 최댓값이 9인 경우)
    max_val = max(arr)
    count = [0] * (max_val + 1)

    # 2. 각 데이터에 해당하는 인덱스의 값 증가
    for num in arr:
        count[num] += 1

    # 3. 카운트한 결과를 물리적으로 나열
    result = []
    for i in range(len(count)):
        for _ in range(count[i]):
            result.append(i)
        # print(result)
        # 과정 보고싶으면 주석 빼도 됩니다

    return result

# 사용 예시
print(counting_sort(a))

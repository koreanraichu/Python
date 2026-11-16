# 얘는 '기'수정렬입니다. 숫자의 자리수끼리 비교하는건데 MSD, LSD가 있어요.
# 쉽게 말하자면 MSD는 큰 자리수부터, LSD는 1의 자리수부터라고 보시면 됩니다.
# 코드: 제미나이

a = [80, 58, 66, 100, 71, 39, 89, 67, 25, 9]


def radix_sort(arr):
    if not arr:
        return arr

    # 가장 큰 수를 찾아 자릿수(최대 자리수) 파악
    max_val = max(arr)
    exp = 1  # 1의 자리부터 시작 (1, 10, 100, ...)

    # 자릿수를 기준으로 반복
    while max_val // exp > 0:
        # 0~9까지의 버킷 생성
        buckets = [[] for _ in range(10)]

        # 현재 자릿수를 기준으로 숫자를 버킷에 분류
        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)

        # 버킷에 들어있는 순서대로 배열 재구성
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
        print(arr)

        # 다음 자릿수로 이동 (10의 자리, 100의 자리...)
        exp *= 10

    return arr


# 사용 예시
sorted_data = radix_sort(a)
print(sorted_data)

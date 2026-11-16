# 이거는 원리 자체는 심플합니다. 
# 배열 안의 원소를 일정 기준에 따라 양동이에 넣고 양동이 내부에서 정렬한 다음 고대로 꺼내면 되는데... 
# 그죠. 일단 양동이 넣을 공간이 필요하고... 
# 배열의 원소 분포가 균일하지 않을 경우 설계 잘못하면 정말 심각한 참사가 터질 수 있습니다. 
# 코드: 제미나이/설명: 위키피디아 버킷 정렬

a = [80, 58, 66, 100, 71, 39, 89, 67, 25, 9] # 배열
b = [1, 32, 18, 22, 14, 13, 4, 15, 21, 3, 35, 5, 9, 19, 17, 6, 11, 16, 30] # 쏠린 배열(1~19까지)

def bucket_sort(arr):
    if not arr:
        return arr

# 1. 최솟값과 최댓값 구하기
    min_val = min(arr)
    max_val = max(arr)

# 2. 버킷의 개수 설정 (여기서는 배열의 길이만큼 생성)
    n = len(arr) // 2
    buckets = [[] for _ in range(n)]

# 3. 원소를 적절한 버킷에 분산시키기
    # (최대값과 최소값의 범위 내에서 각 원소가 들어갈 버킷 인덱스 계산)
    range_val = max_val - min_val
    for num in arr:
        if range_val == 0:
            buckets[0].append(num)
        else:
            # 인덱스가 n을 넘어가지 않도록 처리
            index = int((num - min_val) / range_val * (n - 1))
            buckets[index].append(num)
    print(buckets)

# 4. 각 버킷 내부를 정렬 (여기서는 파이썬 내장 정렬 혹은 삽입 정렬 사용)
    sorted_arr = []
    for bucket in buckets:
        bucket.sort()  # 내부 정렬 (삽입 정렬 또는 Timsort)
        sorted_arr.extend(bucket)

    return sorted_arr

print(bucket_sort(a))
print(bucket_sort(b))
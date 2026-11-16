# 난 이 정렬도 만든 사람이 팀일 줄 몰랐고... 
# 고수분들은 원리를 아시겠지만 한줄로 요약하자면 이겁니다. 
# 팀: 그 합병정렬 배열 크기 1 될떄까지 째지 말고 걍 어느정도 크기 줄어들면 삽입정렬(이진 삽입정렬) 하죠? 
# 그렇습니다. 팀소트는 삽입 정렬(이진 삽입 정렬)과 합병정렬을 합쳐서 만들어진 정렬 얼고리즘이었던 것입니다. 
# 삽입정렬은 느리지만 공간을 덜 차지하고, 합병정렬은 빨리 할 수 있는데 공간을 엄청 차지하잖아요. 가릿? 
# 코드 출처: 에미나이/설명: https://d2.naver.com/helloworld/0315536 (네이버 땡큐!)
# 참고로 코드가 복잡하다 그러면 파이썬에서 리스트.sort() 쓰시면 그게 팀소트입니다. 

# 여기는 테스트 배열 크기가 달라집니닷
import random
a = random.sample(range(1, 10001), 2000) 
# 사실 원리를 설명하기에 좋은 예시는 아닙니다. 
# '어느정도 정렬된 상태의' 배열에 배열 안 된 애들을 끼워넣는게 최적인 녀석이라서요. 

# 작은 덩어리(Run)의 기준 크기 (실제 파이썬은 32~64 사이를 동적으로 계산)
MIN_MERGE = 32 # 요정도 선에서는 삽입정렬이 합병정렬보다 빠르다 하는 기준점 

# 삽입정렬 (자네 이진인가?)
def insertion_sort(arr, left, right):
    """지정된 범위(left ~ right)를 삽입 정렬로 정렬합니다."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        # key보다 큰 원소들을 오른쪽으로 한 칸씩 이동
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 합병정렬
def merge(arr, left, mid, right):
    """정렬된 두 부분 배열(left~mid, mid+1~right)을 하나로 병합합니다."""
    len1 = mid - left + 1
    len2 = right - mid
    
    # 임시 배열에 데이터 복사
    left_part = arr[left : mid + 1]
    right_part = arr[mid + 1 : right + 1]

    i = 0  # left_part 인덱스
    j = 0  # right_part 인덱스
    k = left  # 원본 배열에 채워 넣을 인덱스

    # 두 부분 배열을 비교하며 작은 값부터 원본 배열에 삽입
    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # left_part에 남은 원소가 있다면 복사
    while i < len1:
        arr[k] = left_part[i]
        k += 1
        i += 1

    # right_part에 남은 원소가 있다면 복사
    while j < len2:
        arr[k] = right_part[j]
        k += 1
        j += 1

# 이게 본론
def timsort(arr):
    """팀소트 메인 함수"""
    n = len(arr)

    # 1단계: 배열을 MIN_MERGE 크기의 덩어리(Run)로 나누어 각각 삽입 정렬 수행
    for start in range(0, n, MIN_MERGE):
        end = min(start + MIN_MERGE - 1, n - 1)
        insertion_sort(arr, start, end)

    # 2단계: 정렬된 덩어리(Run)들의 크기를 2배씩 늘려가며 병합 수행
    size = MIN_MERGE
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(n - 1, left + 2 * size - 1)

            # 병합할 오른쪽 배열이 존재하는 경우에만 병합 실행
            if mid < right:
                merge(arr, left, mid, right)
        
        size *= 2

# --- 실행 테스트 ---
if __name__ == "__main__":
    print("정렬 전 (일부):", a[:15])
    
    timsort(a)
    print("정렬 후 (일부):", a[:15])
    print("정렬 성공 여부:", a == sorted(a))

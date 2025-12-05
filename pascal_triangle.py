import sys

N = int(sys.stdin.readline())

# 첫번째 줄: 1
# 두번쨰 줄: 1, 1
# 세번째 줄: 1, 1+1, 1
# 네번째 줄: 1, 1+1+1. 1+1+1, 1
triangle = []

for i in range(N):
    # range는 0부터 시작하기때문에 i도 0부터 시작한다. 
    # 그리고 각 행은 i+1개의 열을 갖는다. (꼭대기: i=0, 열 수=1)
    rows = [1] * (i + 1)
    for j in range(1,i):
        # 그럼 이제 저 1만 있는 삼각형들의 안쪽을 채워볼까요?
        # 가장 바깥을 제외한 안쪽은 위 행에서 인접한 좌우의 요소들을 더해서 값을 구한다. 
        rows[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(rows)

# 이거 이차원 배열이라 이렇게 안 하면 일렬로 나옴...
print(*triangle, sep="\n")
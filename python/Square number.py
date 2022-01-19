import sys
N = int(sys.stdin.readline())
sqrt = N ** 0.5
min_sqrt = int(sqrt) ** 2
max_sqrt = (int(sqrt) + 1) ** 2
if sqrt == int(sqrt):
    print("이 숫자는 제곱수입니다.")
else: 
    print("이 숫자는 제곱수가 아닙니다. ")
    print("{0} < {1} < {2}입니다. ".format(min_sqrt,N,max_sqrt))
# 어떤 수보다 작은 제곱수와 큰 제곱수를 찾아주는 코드입니다. 
# 예: 120->100 < 120 < 121

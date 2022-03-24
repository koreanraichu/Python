import sys
a = float(sys.stdin.readline())
# Factorial(계승): 일반적으로 n! = 1*2*3*...*n-1*n이다. (5!=1*2*3*4*5)
factorial = 1
if a < 0:
    print("Can't calculate factorial")
    # 음수는 factorlal이 없음
elif a == 0:
    print(factorial)
    # 0! = 1
elif a % 1 != 0:
    print("정수가 아닌 유리수는 일반적인 방법으로 팩토리얼을 구할 수 없습니다. ")
else:
    for i in range(int(a),0,-1):
        factorial *= i
    print(factorial)
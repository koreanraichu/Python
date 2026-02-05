import sys
a = float(sys.stdin.readline())
factorial = 1
if a < 0:
    print("Can't calculate factorial")
elif a == 0 or a == 1:
    print(factorial)
    # 0! = 1
elif a % 1 != 0:
    print("정수가 아닌 유리수는 일반적인 방법으로 팩토리얼을 구할 수 없습니다. ")
else:
    for i in range(int(a),0,-2):
        factorial *= i
    print(factorial)

import sys
a = int(sys.stdin.readline())
# Factorial(계승): 일반적으로 n! = 1*2*3*...*n-1*n이다. (5!=1*2*3*4*5)
factorial = 1
if a < 0:
    print("Can't calculate factorial")
    # 음수는 factorlal이 없음
elif a == 0:
    print(factorial)
    # 0! = 1
else:
    for i in range(a,0,-1):
        factorial *= i
    print(factorial)
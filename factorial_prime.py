import sys
a = float(sys.stdin.readline())
# 역사와 전통의 그거 맞음

def factorial(a):
    factorial = 1
    if a < 0:
        return False
    elif a == 0:
        factorial = 1
        return factorial
    elif a % 1 != 0:
        return False
    else:
        for i in range(int(a),0,-1):
            factorial *= i
        return factorial
# Factorial 구하는 로직(...)

def isprime(a):
    sqrt = int(a ** 0.5)
    if a < 2:
        return False
    for i in range(2,sqrt+1):
        if a % i == 0:
            return False
    else: 
        return True
# 소수 정의 함수

plus_factorial = factorial(a) + 1
minus_factorial = factorial(a) - 1

if isprime(minus_factorial) and isprime(plus_factorial):
    print("{}! - 1, {}! + 1 둘 다 {}, {}로 계승 소수입니다. ".format(a,a,minus_factorial,plus_factorial))
elif isprime(minus_factorial):
    print("{}! - 1이 {}로 계승 소수입니다. ".format(a,minus_factorial))
elif isprime(plus_factorial):
    print("{}! + 1이 {}로 계승 소수입니다. ".format(a,plus_factorial))
else:
    print("{}! - 1, {}! + 1 둘 다 {}, {}로 계승 소수가 아닙니다. ".format(a,a,minus_factorial,plus_factorial))
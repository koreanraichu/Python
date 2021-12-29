import sys
a = int(sys.stdin.readline())
# 와 팩토리얼이 생각보다 빡센거였구나... 
# Factorial(계승): 일반적으로 n! = 1*2*3*...*n-1*n이다. (5!=1*2*3*4*5)
factorial = 1
i = 1
while i <= a:
    factorial = factorial * i
    i = i + 1
print(factorial)

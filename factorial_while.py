from sympy import *
from mpmath import mp
import sys

def gamma_function(a):
    t = symbols("t")
    expr = t ** (a - 1) * exp(-t)
    if a.real > 0:
        return integrate((expr),(t,0,oo))
    else: 
        return False

a = float(sys.stdin.readline().strip())
# 와 팩토리얼이 생각보다 빡센거였구나... 
# Factorial(계승): 일반적으로 n! = 1*2*3*...*n-1*n이다. (5!=1*2*3*4*5)
factorial = 1
if a < 0: 
    print("Can't calculate factorial")
    # 음수는 factorial이 없음
elif a == 0: 
    factorial = 1
    # 0! = 1
elif a % 1 != 0:
    print(round(gamma_function(a+1),3))
else: 
    while a >= 1:
        factorial *= a
        a -= 1
    print(factorial)
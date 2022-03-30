from sympy import *
from mpmath import mp
import sys
a = complex(sys.stdin.readline())
# 복소수는 complex로 입력해야 합니다. (int: 정수, float: 소수라고 생각하면 됨)
t = symbols("t")
expr = t ** (a - 1) * exp(-t)
gamma_function = integrate((expr),(t,0,oo))
if a.real > 0:
    if gamma_function % 1 == 0:
        print(round(gamma_function))
    else: 
        print(round(gamma_function,3))
else: 
    print("Cannot calculate Gamma function")

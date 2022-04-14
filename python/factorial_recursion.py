from sympy import *
from mpmath import mp
import sys

def gamma_function(n):
    t = symbols("t")
    expr = t ** (n - 1) * exp(-t)
    if n.real > 0:
        return integrate((expr),(t,0,oo))
    else: 
        return False

def factorial_RF(n):
  if n == 1:
    return 1
  return n * factorial_RF(n-1)
  
a = float(sys.stdin.readline().strip())
# Factorial(계승): 일반적으로 n! = 1*2*3*...*n-1*n이다. (5!=1*2*3*4*5)
factorial = 1
if a < 0:
    print("Can't calculate factorial")
    # 음수는 factorlal이 없음
elif a == 0:
    print(factorial)
    # 0! = 1
elif a % 1 != 0:
    print(round(gamma_function(a+1),3))
else:
    print(factorial_RF(a))
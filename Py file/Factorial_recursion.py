from sympy import *
from mpmath import mp
import sys

class FactorialCalculator:
    def __init__(self):
        pass

    def factorial_recursive(self, n):
        if n == 1:
            return 1
        return n * self.factorial_recursive(n - 1)

    def gamma_function(self, n):
        # Gamma(x) = (x-1)!
        # So we calculate Gamma(n+1) for n! approx? 
        # Wait, the user said "Gamma(x) = (x-1)!"
        # If input is 'n', and we want n!, we need Gamma(n+1).
        # But the user instruction says: "Input positive non-integer -> Gamma function... Gamma(x) = (x-1)!".
        # This implies if I pass 'a' to gamma_function, and gamma_function calculates Gamma(a), the result is (a-1)!.
        # If I want the factorial of 'a', i.e., a!, I should compute Gamma(a+1).
        # Let's look at the original code: `print(round(gamma_function(a+1),3))`.
        # So yes, I should pass a+1 to the gamma function logic or handle the +1 inside.
        # User said: "Gamma function will be a method... Gamma(x) = (x-1)! must be considered".
        # I will implement the method to calculate Gamma(z).
        # And when calling it for n!, I will pass n+1.
        
        t = symbols("t")
        # n here is the argument to Gamma(n).
        expr = t ** (n - 1) * exp(-t)
        if n.real > 0:
            return integrate((expr), (t, 0, oo))
        else:
            return False

if __name__ == "__main__":
    try:
        # 사용자에게 입력 안내 메시지를 출력합니다.
        user_input = input("숫자를 입력하세요: ").strip()
        
        if not user_input:
            print("입력이 없습니다.")
            exit()
            
        a = float(user_input)
        
        calculator = FactorialCalculator()
        
        # Factorial(계승): 일반적으로 n! = 1*2*3*...*n-1*n이다. (5!=1*2*3*4*5)
        
        if a < 0:
            print("계승을 계산할 수 없습니다 (음수).")
        elif a == 0:
            print(1)
            # 0! = 1
        elif a % 1 == 0:
            # 양의 정수 -> 재귀함수 호출
            print(calculator.factorial_recursive(int(a)))
        else:
            # 양수이지만 정수가 아닌 유리수 -> 감마함수 호출
            # n! = Gamma(n+1)
            result = calculator.gamma_function(a + 1)
            print(round(result, 3))
            
    except ValueError:
        print(f"잘못된 입력입니다: {user_input}")
# n개의 원소 중 r개를 택하는 것이 조합입니다. nCr로 표기합니다. 
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
# 아 얘는 조합 구하는데 순열이 필요해서 어쩔 수 없음. 
# nCr을 구하는 공식은 n!/r!(n-r)!입니다. 
n = int(input("n에 들어가는 수를 입력해주세요: "))
r = int(input("r에 들어가는 수를 입력해주세요: "))
bunmo = factorial(r) * factorial(n - r)
C = factorial(n)/bunmo
print("{}개의 원소들 중 {}개를 무작위로 선택하는 가짓수는 {}입니다. ".format(n,r,int(C)))
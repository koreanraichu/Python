# permutation(순열): 서로 다른 n개의 원소 중 r개를 중복 없이 늘어놓는 것
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
# 순열에 팩토리얼이 들어가서 어쩔 수 없어요... 
# nPr(서로 다른 n개의 원소 중 r개를 중복 없이 늫어놓는 것)을 구하는 공식은 n!/(n-r)!입니다. 
n = int(input("n에 들어가는 수를 입력해주세요: "))
r = int(input("r에 들어가는 수를 입력해주세요: "))
P = factorial(n) / factorial(n - r)
print("{}개의 원소 중 {}개를 중복 없이 늘어놓을 수 있는 가짓수의 계산 결과는 {}입니다. ".format(n,r,int(P)))
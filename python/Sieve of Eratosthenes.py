number=input('Input number: ') #숫자를 쓰세요
n=int(number)
prime=[]

def Primecheck(a):
    if(a<2):
        return False #1은 특수한 취급이라 제일 작은 소수는 2
    for i in range (2,a):
        if(a%i==0):
            return False
    return True

for i in range (n+1):
    if(Primecheck(i)):
        prime.append(i)
        #여기까지는 다른 분이 올리신 코드 참조했습니다

print(prime,"\nThe Prime number from 1 to "+str(number)+" is: "+str(len(prime))) #대충 출력한다는 얘기
#누구 이거 표로 만드는 법 아는사람 제보좀 해주시면 안될까요
#숫자가 많아지면 가독성이 떨어져서 표로 만들고싶은데 안되네요
#1~10은 2, 3, 5, 7 4개라 상관없는데 1~100은
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 이렇게 25개입니다.
#
# 이걸
#  2| 3| 5| 7|11|13|17|19|23|29|
# 31|37|41|43|47|53|59|61|67|71|
# 73|79|83|89|97
#이런 느낌으로 표로 만들고 싶습니다. 
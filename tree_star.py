a=list(range(7))
for i in a:
    print("0"*a[i])
# 왼쪽으로 쏠린 삼각형

for i in a:
    print(" "*a[-i],"0"*a[i])
# 오른쪽으로 쏠린 삼각형

for i in a:
    print("0"*a[-i])
# 왼쪽으로 쏠린 역삼각형

for i in a:
    print(" "*a[i],"0"*a[-i])
# 오른쪽으로 쏠린 역삼각형

for i in a:
    print("0"*(a[i]*2+1))
# 어쨌든 홀수로 뽑은 삼각형

for i in a:
    print("0"*(a[-i]*2-1))
# 어쨌든 홀수로 뽑은 역삼각형

for i in range(5):
    for j in range(5-i):
        print(" ",end="")
    for j in range(2*i+1):
        print("1",end="")
    print(" ")
# 카와이이하게 뽑아봤다
# reference: https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=imbin_&logNo=221385624266&categoryNo=23&parentCategoryNo=0

for i in a:
    for j in range(a[-1]-a[i]):
        print(" ",end="")
    for j in range(2*a[i]+1):
        print("♥️",end="")
    print(" ")
# 오 됐당

for i in range(5):
    print("-"*i)
for i in range(5,0,-1):
    print("-"*i)
# 이건 일반화했더니 공백이 날 반기네

for i in range(5,0,-1):
    print("+"*i)
for i in range(1,6):
    print("+"*i)
# 이것도 일반화는 힘들겠구만...

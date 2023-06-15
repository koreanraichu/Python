a=list(range(10))
i=0
# 아 맞다 리스트

while i <= a[-1]:
    if i % 3 == 0:
        print(" "*(a[-i]),"♥️"*(a[i]*2-1))
    else:
        print(" "*(a[-i]),"♡"*(a[i]*2-1))
    i=i+1
# 가운데정렬!

a=list(range(15))
i=0
# 아 맞다 리스트

while i <= a[-1]:
    if i % 3 == 0:
        print(" "*(a[-i])," "*(a[i]*2-1))
    else:
        print(" "*(a[-i]),"♡"*(a[i]*2-1))
    i=i+1
# 가운데정렬!

a=list(range(20))
i=0
# 아 맞다 리스트

while i <= a[-1]:
    if i % 3 == 1:
        print(" "*(19),"♡"*(a[1]))
    else:
        print(" "*(a[-i]),"♡"*(a[i]*2-1))
    i=i+1
# tree모양 뽑았다... 대신 리스트 범위에 따라 고정값이 있음. 

a=list(range(20))
i=0
# 아 맞다 리스트

while i <= a[-1]:
    if i == 0:
        print(" ")
    elif i % 3 == 1:
        print(" "*a[-1],"♡"*a[1])
    elif i % 3 == 2:
        print(" "*a[-2],"♡"*a[3])
    else: 
        print(" "*a[-3],"♡"*a[5])
    i=i+1
# 삼각형 패턴

a=list(range(31))
i=0
# 아 맞다 리스트

while i <= a[-1]:
    if i == 0:
        print(" ")
    elif i % 6 == 1:
        print(" "*a[-1],"♥"*a[1])
    elif i % 6 == 2:
        print(" "*a[-2],"♡"*a[3])
    elif i % 6 == 3: 
        print(" "*a[-3],"♥"*a[5])
    elif i % 6 == 4: 
        print(" "*a[-4],"♡"*a[7])
    elif i % 6 == 5:
        print(" "*a[-5],"♥"*a[9])
    else:
        print(" "*a[-6],"♡"*a[11])
    i=i+1
# 삼각형 패턴(+조건부)
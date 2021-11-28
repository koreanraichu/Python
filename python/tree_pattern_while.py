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
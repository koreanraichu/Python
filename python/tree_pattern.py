a=list(range(9))
for i in a:
    for j in range(a[-1]-a[i]):
        print(" ",end="")
    for j in range(2*a[i]+1):
        if i % 2 == 1:
            print("♥️",end="")
        else:
            print("★",end="")
    print(" ")
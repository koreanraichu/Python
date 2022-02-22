import sys
a = int(sys.stdin.readline())
yaksu = []
for i in range(1,a+1):
    if a % i == 0:
        yaksu.append(str(i))
yaksu = ', '.join(yaksu)
print('{}의 약수는 {}입니다. '.format(a,yaksu))
import sys
a = int(sys.stdin.readline())
yaksu = []
for i in range(1,a+1):
    if a % i == 0:
        yaksu.append(i)
yaksu_text = ''.join(str(yaksu))
print('{}의 약수는 {}입니다. '.format(a,yaksu_text))
if sum(yaksu) == 2 * a:
    print('{}는 자기 자신을 제외한 약수들의 합이 {}와 동일하므로 완전수입니다. '.format(a,a))
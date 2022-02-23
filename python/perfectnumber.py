import sys
a = int(sys.stdin.readline())
yaksu = []
yaksu_text = []
for i in range(1,a+1):
    if a % i == 0:
        yaksu.append(i)
        yaksu_text.append(str(i))
yaksu_text = ', '.join(yaksu_text)
print('{}의 약수는 {}입니다. '.format(a,yaksu_text))
sum = sum(yaksu)
if sum == 2 * a:
    print('{}는 자기 자신을 포함한 약수들의 합이 {}이고, {}와 동일하므로 완전수입니다. '.format(a,sum-yaksu[-1],a))
else: 
    print('{}는 자기 자신을 포함한 약수들의 합이 {}이고, {}와 다르므로 완전수가 아닙니다. '.format(a,sum-yaksu[-1],a))
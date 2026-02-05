from Bio.ExPASy import Prosite
from urllib.request import urlopen
handle=open("/home/koreanraichu/prosite.dat")
records = Prosite.parse(handle)
record = next(records)
print(record.accession)
# 단식 소환

# for문 마려울 때 시도해보자.
for i in range(0,5):
    record = next(records)
    print(record.accession)

# 어떻게 사람이 for문만 씁니까 while도 적용해봐요
i=0
while i < 5:
    record = next(records)
    print(record.accession)
    i=i+1

#셋이 같이 적용하면 첫번째-2, 3, 4, 5, 6번째-7, 8, 9, 10, 11번째 불러오니까 반드시 각개로 해볼 것.

n=0
for record in records:
    n+=1
print(n)
# record 몇개십니까 선생님
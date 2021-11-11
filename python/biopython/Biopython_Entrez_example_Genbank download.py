from Bio import Entrez
from Bio import SeqIO
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일
handle = Entrez.egquery(term="Leuconostoc AND kimchii") # 뭐야 연산자 이렇게 쓰면 됨?
record = Entrez.read(handle)
for row in record["eGQueryResult"]:
    if row["DbName"] == "nuccore":
        print(row["Count"])
# nuccore에 수록되어있는 L.kimchii에 대해 찾아보자. (Leuconostoc kimchii)
handle = Entrez.esearch(db="nuccore", term="Leuconostoc AND kimchii")
record = Entrez.read(handle)
gi_list = record["IdList"]
# GI list를 만들어서 출력해보자
gi_str = ",".join(gi_list[0:5])
handle = Entrez.efetch(db="nuccore", id=gi_str, rettype="gb", retmode="text")
text = handle.read()
print(text)
# 이거 저장 안됨?
handle = Entrez.efetch(db="nuccore", id=gi_str, rettype="gb", retmode="text")
records = SeqIO.parse(handle, "gb")
for record in records:
    print("%s, length %i, with %i features" % (record.name, len(record), len(record.features)))
# Parsing에는 for문이 국룰이다.
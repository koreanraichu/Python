from Bio import Entrez
Entrez.email = "blackholekun@gmail.com" # 내가 누구인지 말해주는 과정이 필요하다고...
# 이메일은 자기꺼 그냥 쓰세요
handle = Entrez.einfo()
record = Entrez.read(handle)
handle.close()
print(record)
print(record["DbList"]) # Key에 맞는 Value만 볼 수도 있다. 
# 뭔가 출력 결과가 개비스콘 아저씨 마렵다

handle2 = Entrez.einfo(db="pubmed")
record2 = Entrez.read(handle2)
print(record2["DbInfo"]["Description"])
# 이렇게 픽해서 보는 것도 된다.

for field in record2["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)
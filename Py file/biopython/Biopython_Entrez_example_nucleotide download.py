from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일
handle = Entrez.egquery(term="Arabidopsis")
record = Entrez.read(handle)
for row in record["eGQueryResult"]:
    if row["DbName"] == "nuccore":
        print(row["Count"])
# 애기장대로 긁어와서 nuccore에 있는 것만 출력해라
handle = Entrez.esearch(db="nucleotide", term="Arabidopsis", retmax=800, idtype="acc")
record = Entrez.read(handle)
handle.close()
# 올해 얼마나 나왔는지는 모르겠고 일단 800개만 뽑아보자
print(record["IdList"][:5])
idlist = ",".join(record["IdList"][:5])
# 레코드에서 다섯개 뽑아서 리스트업한다.
handle = Entrez.efetch(db="nucleotide", id=idlist, retmode="xml")
records = Entrez.read(handle)
print(records[0].keys())
# 0번째 레코드 키좀 주세요
print(records[0]["GBSeq_length"])
# 시퀀스 길이 줘봐봐
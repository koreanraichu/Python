from Bio import Entrez
from Bio import Medline
import numpy as np
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일
handle = Entrez.egquery(term="kimchii")
record = Entrez.read(handle)
for row in record["eGQueryResult"]:
    if row["DbName"] == "pubmed":
        print(row["Count"])
# 쿼리를 통해 kimchii가 들어가는 걸 데려온 다음, pubmed에 있는 것만 뽑았다.
handle = Entrez.esearch(db="pubmed", term="kimchii", retmax=50)
record = Entrez.read(handle)
handle.close()
idlist = record["IdList"]
# 이제 리스트가 많으면 뽑아서 확인할 때 알아서 numpy를 불러봅니다.
handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",retmode="text")
records = Medline.parse(handle)
# 이렇게 된 이상 medline으로 간다!
"""
handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",retmode="text")
records = Medline.parse(handle)
for record in records:
    print("title:", record.get("TI", "?"))
    print("authors:", record.get("AU", "?"))
    print("source:", record.get("SO", "?"))
    print("")
# 전체 출력은 여기서(전체 결과 중 제목, 저자, source를 출력) 
"""
search_title = "Leuconostoc"
for record in records:
    if not "TI" in record:
        continue
    if search_title in record["TI"]:
        print("Keyword %s found: %s" % (search_title, record["TI"]))
# 제목에 Leuconostoc이 있는 것만 뽑아달라!

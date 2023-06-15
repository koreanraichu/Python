from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일!!!
handle = Entrez.esearch(db="Taxonomy", term="Enterococcus")
record = Entrez.read(handle)
print(record['IdList'])
# Taxonomy에서 찾아서 ID를 내놓아라!
handle = Entrez.efetch(db="Taxonomy", id=record['IdList'], retmode="xml")
records = Entrez.read(handle)
print(records[0]['Lineage'])
# Lineage 주세요!
# 입력하기 귀찮으시다고요? 그럼 변수 오케이.
from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
handle = Entrez.esearch(db="clinvar", term="L858R", retmax="40" )
record = Entrez.read(handle)
# clinVar+esearch
IdList=list(record['IdList'])
for i in range(len(record['IdList'])):
    handle = Entrez.esummary(db="clinvar", id=IdList[i], retmode="xml")
    records = Entrez.read((handle))
    print(records['DocumentSummarySet']['DocumentSummary'][0]['title'])
# 일단 esummary 써서 다 가져왔다.
# 야이 근데 무슨 이건 진짜 할 말을 잃었음
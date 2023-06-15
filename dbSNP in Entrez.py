from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
handle = Entrez.esearch(db="snp", term="rs1050171", retmax="40" )
record = Entrez.read(handle)
IdList=list(record['IdList'])
# dbSNP+esearch
for i in range(len(record['IdList'])):
    handle = Entrez.esummary(db="snp", id=IdList[i], retmode="xml")
    records = Entrez.read((handle))
    print(records['DocumentSummarySet']['DocumentSummary'][0]['GLOBAL_MAFS'][0])
# 일단 esummary 써서 다 가져왔다. 근데 딕셔너리인데 왜 픽이 안될까...
# 그 전에 저렇게 꼭 4단픽까지 가야겠냐... 아니 진짜 너무한 거 아닙니까...

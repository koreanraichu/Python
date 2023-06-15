from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
handle = Entrez.esearch(db="clinvar", term="ALDH2 and Gly", retmax="40" )
record = Entrez.read(handle)
# clinVar+esearch
IdList=list(record['IdList'])
for i in range(len(record['IdList'])):
    handle = Entrez.esummary(db="clinvar", id=IdList[i], retmode="xml")
    records = Entrez.read((handle))
    title = records['DocumentSummarySet']['DocumentSummary'][0]['title']
    protein_change = records['DocumentSummarySet']['DocumentSummary'][0]['protein_change']
    clinical = records['DocumentSummarySet']['DocumentSummary'][0]['clinical_significance']['description']
    print("<{0}>\ntitle: {1} \nprotein change: {2} \nclinical significance: {3}".format(i+1,title,protein_change,clinical))
# 일단 esummary 써서 다 가져왔다.
# 야이 근데 무슨 이건 진짜 할 말을 잃었음
from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
handle = Entrez.esearch(db="snp", term="rs121434568", retmax="40")
record = Entrez.read(handle)
IdList=list(record['IdList'])
print('=' * 100)

# dbSNP+esearch
for i in range(len(record['IdList'])):
    handle = Entrez.esummary(db="snp", id=IdList[i], retmode="xml")
    records = Entrez.read(handle)
    Gene = records['DocumentSummarySet']['DocumentSummary'][0]['GENES'][0]['NAME'] # 유전자 이름
    chromosome = records['DocumentSummarySet']['DocumentSummary'][0]['CHR'] # 염색체
    chrpos = records['DocumentSummarySet']['DocumentSummary'][0]['CHRPOS'] # 염색체 위치
    spdi = records['DocumentSummarySet']['DocumentSummary'][0]['SPDI'] # NC_000007.14(시퀀스 어디):55206390(몇번째 염기):T(였던것):A(바뀐것)
    Fxn_class = records['DocumentSummarySet']['DocumentSummary'][0]['FXN_CLASS'] # 그래서 얘가 어디 변이임?
    print(f'{Gene} | {chromosome} POS {chrpos} | {spdi}\n{Fxn_class}')
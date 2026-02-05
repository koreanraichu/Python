from Bio import ExPASy
from Bio import SwissProt
accessions = ["C3RT18"] # 단백질 이름은 신경쓰지 맙시다
records = []
# 저 세개에 대해 찾고싶은갑다.
for accession in accessions:
    handle = ExPASy.get_sprot_raw(accession)
    record = SwissProt.read(handle)
    records.append(record)
print(records) #IDLE 아니라서 이거 써야 나온다
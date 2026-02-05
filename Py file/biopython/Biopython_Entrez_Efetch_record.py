from Bio import SeqIO
from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일
handle = Entrez.efetch(db="nucleotide", id="NM_180778.4", rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank") # 레코드 형식으로 불러와서 부분적으로 취사선택할 수 있다.
handle.close() # 이거 꼭 닫아야됨?
print(record.description)
# 뭐야 저장 안해줘요?
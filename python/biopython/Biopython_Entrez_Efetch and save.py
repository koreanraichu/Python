from Bio import Entrez
from Bio import SeqIO
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일
handle = Entrez.efetch(db="nucleotide", id="NM_180778.4", rettype="gb", retmode="text")
record=SeqIO.read(handle,"genbank")
handle.close()
print(record)
SeqIO.write(record,"/home/koreanraichu/NM_180778.4.fasta","fasta")
# 사실 여기까진 쿡북에 없었는데 저장할 수 있는 방법이 없나 해서 해봤음.
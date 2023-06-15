from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일
handle = Entrez.efetch(db="nucleotide", id="NM_180778.4", rettype="gb", retmode="text")
print(handle.read())
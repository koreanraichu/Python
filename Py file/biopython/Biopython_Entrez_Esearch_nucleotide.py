from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일
handle = Entrez.esearch(db="nucleotide", term="Lactobacillus[Orgn]", idtype="acc")
record = Entrez.read(handle)
print("%s founded" % record["Count"])
print(record["IdList"])
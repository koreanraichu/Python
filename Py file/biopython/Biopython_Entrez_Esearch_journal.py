from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일
handle = Entrez.esearch(db="nlmcatalog", term="computational[Journal]", retmax="20")
record = Entrez.read(handle)
print("{} computational journals found".format(record["Count"]))
print("The first 20 are\n{}".format(record["IdList"]))
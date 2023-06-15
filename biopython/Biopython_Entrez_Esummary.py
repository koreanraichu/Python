from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일
handle = Entrez.esummary(db="pubmed", id="31651376")
record = Entrez.read(handle)
info = record[0]
print("Journal info\nid: {}\nTitle: {}".format(record[0]["Id"], info["Title"]))
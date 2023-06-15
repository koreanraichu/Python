from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일
handle = Entrez.espell(term="Conpanilactobacillus")
record = Entrez.read(handle)
print(record["Query"])
print(record["CorrectedQuery"])
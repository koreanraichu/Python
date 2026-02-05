from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일
handle = Entrez.egquery(term="kimchii")
record = Entrez.read(handle)
for row in record["eGQueryResult"]:
    print(row["DbName"], row["Count"])
# AND나 or같은 거 안되나? 
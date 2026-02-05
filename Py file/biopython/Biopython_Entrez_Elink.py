from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일
record = Entrez.read(Entrez.elink(dbfrom="nucleotide", id="NM_180778.4"))
print(record[0]['IdList'],record[0]["DbFrom"])
# 대충 네이버 연관검색어 같은 건가...

for linksetdb in record[0]["LinkSetDb"]:
    print(linksetdb["DbTo"], linksetdb["LinkName"], len(linksetdb["Link"]))
# 아무튼 그렇다고 합니다. 
from Bio import Entrez
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일
id_list = ["19304878", "18606172", "16403221", "16377612", "14871861", "14630660"]
print(Entrez.epost("pubmed", id=",".join(id_list)).read())
# 얘는 핸들 어쩌고가 안된다. ...왜?
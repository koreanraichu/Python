from Bio import Phylo
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
# FASTA file reading
records = SeqIO.parse("/home/koreanraichu/Halobacterium.fasta","fasta")
save_record=[]
for record in records:
    description = record.description.split(sep=";") # record description 소환
    record.id = description[6] # description 마지막 글자로 변환
# fasta 소환!
    record_save=SeqRecord(record.seq,id=record.id,name=record.id,description=record.description)
    save_record.append(record_save)
print(save_record)
SeqIO.write(save_record,"/home/koreanraichu/Halobacterium_label.fasta","fasta")
# FASTA 파일로 저장은 했는데 description에 세미콜론이 들어가서 안된다...
# 결국 raw file 들어가서 수정함.
# 아 그리고 학명이 띄어쓰기가 되어 있으니까 앞에꺼 빼고 뒤에꺼 넣길래 raw file에서 언더바 추가했음.

tree = Phylo.read("/home/koreanraichu/Halobacterium_label.ph", "newick")
tree.name="Halophile" # Title
tree.as_phyloxml() # phyloxml로 변환
Phylo.draw(tree)
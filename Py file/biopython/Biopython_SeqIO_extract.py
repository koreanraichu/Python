from Bio import SeqIO
import numpy as np
record_iterator = SeqIO.parse("/home/koreanraichu/ls_orchid.gbk", "genbank")
first_record = next(record_iterator)
"""
# 첫 번째 레코드를 가져온다.
print(first_record.annotations) # Annotations
print(first_record.annotations.keys()) # Key
print(first_record.annotations.values()) # Values
print(first_record.annotations["source"]) # Annotation+selector(키 중 하나를 선택)
"""

# 아래 코드는 리스트업 코드이다.
"""
all_species = []
for seq_record in record_iterator:
    all_species.append(seq_record.annotations["organism"])
print(np.array(all_species))
"""
"""
# 리스트 단에서 박아버림
all_species2 = [
    seq_record.annotations["organism"]
    for seq_record in record_iterator
]
print(all_species2)
"""

#FASTA 파일도 된다.


all_species = []
all_species2 = []
for seq_record in SeqIO.parse("/home/koreanraichu/ls_orchid.fasta", "fasta"):
    all_species.append(seq_record.description.split()[1])
print(all_species)

all_species2 == [
    seq_record.description.split()[1]
    for seq_record in SeqIO.parse("/home/koreanraichu/ls_orchid.fasta", "fasta")
]
print(all_species2)
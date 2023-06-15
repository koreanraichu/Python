from Bio import SeqIO
from Bio import SeqFeature
record=SeqIO.read("/home/koreanraichu/sequence.gb",'genbank') # 여기서 뭘 뽑아봅시다
index=575
for feature in record.features:
    if index in feature:
        print("%s, %s, %s" %(feature.type,feature.location,feature.qualifiers.get("db_xref")))

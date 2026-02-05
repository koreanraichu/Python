from Bio import SeqIO
record = SeqIO.read("/home/koreanraichu/sequence.gb", "genbank")
sub_record = record[0:20]
# print(sub_record.features[0])
# 0번째 feature
print(sub_record.format("genbank"))
print(sub_record.format("fasta"))
# FASTA나 genbank 포맷으로 출력도 된다.
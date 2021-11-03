from Bio import SeqIO
record=SeqIO.read("/home/koreanraichu/sequence.gb",'genbank') # 모셔왔다
print(record)
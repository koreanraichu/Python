from Bio import SeqIO

records = SeqIO.parse("/home/koreanraichu/sequence.gb", "genbank")
count = SeqIO.write(records, "/home/koreanraichu/my_example.fasta", "fasta")
print("Converted %i records" % count)

count2 = SeqIO.convert("/home/koreanraichu/sequence.gb", "genbank", "/home/koreanraichu/my_example2.fasta", "fasta")
print("Converted %i records" % count2)
from Bio import AlignIO
alignment = AlignIO.read("/home/koreanraichu/lactobacillus.fasta", "fasta")
print(format(alignment, "stockholm"))
# stockholm, clustalw 형식으로 볼 수 있다.
# Phylip 형식으로 보려면 공백이 -여야 한다.
from Bio import AlignIO
count = AlignIO.convert("/home/koreanraichu/agrobacterium.fasta", "fasta", "/home/koreanraichu/agrobacterium.sth",
                        "stockholm")
print("Converted %i alignments" % count)
# Stockholm

alignments = AlignIO.parse("/home/koreanraichu/enterobacter.fasta", "fasta")
count = AlignIO.write(alignments, "/home/koreanraichu/enterobacter.aln","clustal")
print("Converted %i alignments" % count)
# ClustalW

alignment = AlignIO.read("/home/koreanraichu/PF00096_seed.txt", "stockholm")
AlignIO.write([alignment], "/home/koreanraichu/PF00096_seed.aln", "clustal")
print("Converted %i alignments" % count)
# read 후 리스트화해서 변환(clustalW)

count2 = AlignIO.convert("/home/koreanraichu/PF08449_seed.txt", "stockholm", "/home/koreanraichu/PF08449_seed.phy",
                        "phylip")
print("Converted %i alignments" % count)
# 이거라면 필립 될거같은데?

alignment2 = AlignIO.read("/home/koreanraichu/PF08449_seed.txt", "stockholm")
name_mapping = {}
for i, record in enumerate(alignment):
    name_mapping[i] = record.id
    record.id = "seq%i" % i
AlignIO.write([alignment], "/home/koreanraichu/PF08449_seed_ID.phy", "phylip")
# 오 뭔진 모르겠지만 ID가 숫자가 된 건가
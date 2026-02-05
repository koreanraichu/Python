from Bio import motifs
from Bio.Seq import Seq
fh = open("/home/koreanraichu/MA0004.1.jaspar")
for m in motifs.parse(fh, "jaspar"):
    print(m.format("transfac"))
# jaspar file을 불러서 transfac 형식으로(pfm도 됨)
instances=[Seq("TGTCGTATCG"),Seq("GTAAATAGCC"),Seq("GTAAATAACC"),Seq("TCGCGGAGCC"),Seq("ATGTGCCATA"),Seq("CTCGTCTGCG")]
m2 = motifs.create(instances)
print(m2.format("jaspar"))
# 임의로 만든 motif를 jaspar format으로
print(motifs.write([m2], "transfac"))
# 여러개는 리스트업하면 쓸 수 있다.
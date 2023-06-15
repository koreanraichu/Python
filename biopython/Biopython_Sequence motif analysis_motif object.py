from Bio import motifs
from Bio.Seq import Seq
instances=[Seq("TGTCGTATCG"),Seq("GTAAATAGCC"),Seq("GTAAATAACC"),Seq("TCGCGGAGCC"),Seq("ATGTGCCATA"),Seq("CTCGTCTGCG")]
m = motifs.create(instances)
print(m) # motif object 출력
print("len:",len(m)) # 길이 얼마냐
print(m.counts) # 염기 얼마나 들어갔냐
print(m.counts[:,4]) # 컬럼 인덱싱 (["A"]=특정 염기(아데닌) 인덱싱, ["A",0]=특정 염기+n번째)
print(m.counts["C",:]) # 특정 염기(시토신) 인덱싱
print(m.alphabet) # 알파벳 뭐들갔냐
# 이 밑으로 난이도 별 3600개 봅니다(개념 이해하는데 난이도 별 3600개)
print(m.consensus) # motif에서 많이 들어간 것
print(m.anticonsensus) # motif에서 가장 적게 들어간 것
print(m.degenerate_consensus) # 많이 들어간 걸 뭉뚱그려서 표현했다. A와 G가 많으면 퓨린(R)로 쓴다던가.
# 이 밑으로는 reverse complement sequence
r = m.reverse_complement()
print(r)
print(r.degenerate_consensus)
# Weblogo도 된다
m.weblogo("mymotif.png")

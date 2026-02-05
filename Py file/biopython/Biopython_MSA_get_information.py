from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio import AlignIO
alignment = AlignIO.read("/home/koreanraichu/lactobacillus.fasta", "fasta") # 아이고 유산균씨 오랜만입니다
substitutions = alignment.substitutions # Substitution이라는 게 해당 염기가 다른걸로 바뀐 걸 말하는건가...?
m = substitutions.select("AUCG.") # 표시 순서를 바꿀 수 있다.
print(substitutions)
print(m)
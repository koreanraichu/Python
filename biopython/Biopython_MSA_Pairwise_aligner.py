from Bio import Align
aligner = Align.PairwiseAligner() # 그래서 모셔왔습니다
aligner.mode="local"
seq1="GAATTC"
seq2="CAATTC"
alignments = aligner.align(seq1, seq2)
for alignment in alignments:
    print(alignment)
print(aligner) # aligner의 parameter 출력
print(aligner.algorithm) # aligner의 알고리즘 출력

# wildcard를 지정한 다음 쓸 수도 있다
aligner.wildcard = "?"
seq3="?GCC"
seq4="GGCC"
alignments2 = aligner.align(seq3, seq4)
for alignment in alignments2:
    print(alignment)
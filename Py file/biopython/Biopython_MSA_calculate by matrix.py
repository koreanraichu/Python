from Bio.Align import PairwiseAligner
from Bio import SeqIO
from Bio.Align.substitution_matrices import Array
import numpy as np
# 살려주세요 뭐 이렇게 많이 불러요

aligner = PairwiseAligner()
aligner.mode="local"
aligner.match_score = 2
aligner.mismatch_score = -3
aligner.open_gap_score = -7
aligner.extend_gap_score = -2
# option 줬다

sequence1 = SeqIO.read('/home/koreanraichu/radiobacter.fasta', 'fasta')
sequence2 = SeqIO.read('/home/koreanraichu/radiobacter2.fasta', 'fasta')
alignments = aligner.align(sequence1.seq, sequence2.seq) # 이거 len하니까 오류뜨던데...
alignment = alignments[0]
# 일단 구했다(단백질 시퀀스면 20개 다 넣어야 하는건가...)
# 단백질은...ㅋㅋㅋㅋㅋㅋㅋㅋㅋ

frequency = Array("AUGC-", dims=2)
for (start1, end1), (start2, end2) in zip(*alignment.aligned):
    seq1 = sequence1[start1:end1]
    seq2 = sequence2[start2:end2]
    for c1, c2 in zip(seq1, seq2):
        frequency[c1, c2] += 1
print(frequency)
# 여기까지 행렬이 나왔다

probabilities = frequency / np.sum(frequency)
probabilities = (probabilities + probabilities.transpose()) / 2.0
print(probabilities.format("%.4f"))
# 확률로 바꿀 수도 있는 모양... 아 substitution probability란다.

background = np.sum(probabilities, 0)
print(background.format("%.4f"))
# background probability(probability of finding an A, C, G, or T nucleotide in each sequence separately라고 한다)

expected = np.dot(background[:,None], background[None, :])
print(expected.format("%.4f"))
# 얘는 뭐임?
# Cookbook 원문: The number of substitutions expected at random is simply the product of the background distribution with itself

oddsratios = probabilities / expected
scoring_matrix = np.log2(oddsratios)
print(scoring_matrix)
# scoring matrix
# substitution matrix로 사용 가능
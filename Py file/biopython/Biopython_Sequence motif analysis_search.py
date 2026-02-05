from Bio import motifs
from Bio.Seq import Seq
test_seq=Seq("GTAAATAGCCTAGCATGTCGTATCG")
m = motifs.create(instances=[Seq("TGTCGTATCG"),Seq("GTAAATAGCC"),Seq("GTAAATAACC"),Seq("TCGCGGAGCC"),
                             Seq("ATGTGCCATA"),Seq("CTCGTCTGCG"),Seq("CTCGTATGCG")])
for pos, seq in m.instances.search(test_seq):
    print(pos,seq)
# Exact sequence search
# Motif object가 검색할 sequence보다 길면 에러뜬다. (ValueError)
pwm = m.counts.normalize(pseudocounts=0.5) # 예제 코드를 보니 얘가 있어야 계산할 수 있는 모양
pssm = pwm.log_odds()
# PSSM으로 찾기(PSSM 도출)
for position, score in pssm.search(test_seq, threshold=0.0):
    print("Position %d: score = %5.3f" % (position, score))
# 찾았음!
# 얘는 어찌됐던 시퀀스가 있어야 하는 모양...
print(pssm.calculate(test_seq))
background = {"A":0.3,"C":0.2,"G":0.2,"T":0.3}
distribution = pssm.distribution(background=background, precision=10**4)
threshold = distribution.threshold_fnr(0.1)
print("%5.3f" % threshold)
for position, score in pssm.search(test_seq, threshold=threshold):
    print("Position %d: score = %5.3f" % (position, score))
# threshold 계산해서 그거 설정에 때려박고 찾아도 된다.
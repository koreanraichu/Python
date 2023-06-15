from Bio import motifs
with open("/home/koreanraichu/MA0278.1.jaspar") as handle:
    motif = motifs.read(handle, "jaspar")
# 이쯤되면 다들 아시잖아요...
print(motif.counts)
print(motif.pwm)
print(motif.pssm)
# 일단 뽑고 보는 타입
# Pseudocounter를 바꾸면 값이 바뀐다는데 이거 이걸로 할 수 있나?
print(motif.background)
print(motif.pseudocounts)
# 일단 불러온 데이터에서 뽑을 수는 있다.
print(motif.pssm.mean(motif.background))
print(motif.pssm.std(motif.background))
# Mean&Standard deviation
distribution = motif.pssm.distribution(background=motif.background)
threshold = distribution.threshold_fpr(0.01)
print(threshold)
# Threshold

# 아래 코드는 Pseudocounts와 background를 변경한 값이다.
"""
Default: 
{'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}
{'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}
"""
motif.pseudocounts = 3.0
motif.background = {"A": 0.2, "C": 0.3, "G": 0.3, "T": 0.2}
# 어? 변경 되네?
print(motif.counts)
print(motif.pwm)
print(motif.pssm)
# 바꾸고 계산해서 보자 한번.
print(motif.background)
print(motif.pseudocounts)
# 되네?
print(motif.pssm.mean(motif.background))
print(motif.pssm.std(motif.background))
# Mean&Standard deviation
distribution = motif.pssm.distribution(background=motif.background)
threshold = distribution.threshold_fpr(0.01)
print(threshold)
# Threshold
motif.background = None
print(motif.background)
# None: 각 염기별로 0.25씩
motif.background = 0.9
print(motif.background)
# GC 비중보게.
# {'A': 0.04999999999999999, 'C': 0.45, 'G': 0.45, 'T': 0.04999999999999999} 는 심한 거 아니냐 근데.
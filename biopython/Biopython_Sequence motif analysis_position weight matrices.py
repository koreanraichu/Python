from Bio import motifs
fh = open("/home/koreanraichu/MA0004.1.jaspar")
for m in motifs.parse(fh, "jaspar"):
    print(m.format("jaspar"))
# 일단 부른 다음 생각하는 타입
pwm = m.counts.normalize(pseudocounts=0.5)
print(pwm)
# Pseudocount 지정을 해주고 졍규화를 진행한다.
pwm = m.counts.normalize(pseudocounts={"A":0.6, "C": 0.4, "G": 0.4, "T": 0.6})
print(pwm)
# 개별 지정도 된다.
print(pwm.consensus)
print(pwm.anticonsensus)
print(pwm.degenerate_consensus)
# 제일 많은거/제일 적은거/Degenerate consensus
rpwm = pwm.reverse_complement()
print(rpwm)
# reverse complement로도 된다. (아마 밑에 코드로 계산된 듯)
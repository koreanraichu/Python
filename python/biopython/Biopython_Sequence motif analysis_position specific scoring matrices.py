from Bio import motifs
fh = open("/home/koreanraichu/MA0004.1.jaspar")
for m in motifs.parse(fh, "jaspar"):
    print(m.format("jaspar"))
# 일단 부른 다음 생각하는 타입
pwm = m.counts.normalize(pseudocounts=0.5) # 예제 코드를 보니 얘가 있어야 계산할 수 있는 모양
pssm = pwm.log_odds()
print(pssm)
print("%4.2f" % pssm.max)
print("%4.2f" % pssm.min)
# 평범한 로그
# 최대/최소 score를 계산할 수 있다.
background = {"A":0.3,"C":0.2,"G":0.2,"T":0.3}
pssm = pwm.log_odds(background)
print(pssm)
print("%4.2f" % pssm.max)
print("%4.2f" % pssm.min)
mean = pssm.mean(background)
std = pssm.std(background)
print("mean = %0.2f, standard deviation = %0.2f" % (mean, std))
# background를 염기별로 줄 수도 있다.
# 최대/최소 score와 background 평균과 표준편차를 구할 수 있다.
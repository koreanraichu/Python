from Bio import motifs
with open("/home/koreanraichu/MA0050.3.jaspar") as handle:
    motif_1 = motifs.read(handle, "jaspar")
# 이쯤되면 다들 아시잖아요...
with open("/home/koreanraichu/MA0050.2.jaspar") as handle:
    motif_2 = motifs.read(handle, "jaspar")
# 요즘 원쁠원이 대세임
print("MA0050.3:",motif_1.consensus)
print("MA0050.2:",motif_2.consensus)
# 뭐가 제일 많은지 봅시다.
print("MA0050.3 counts:",motif_1.counts)
print("MA0050.2 counts:",motif_2.counts)
# 카운트 뽑아봤음
motif_1.pseudocounts = {"A":0.6, "C": 0.4, "G": 0.4, "T": 0.6}
motif_1.background = {"A":0.3,"C":0.2,"G":0.2,"T":0.3}
motif_2.pseudocounts = {"A":0.6, "C": 0.4, "G": 0.4, "T": 0.6}
motif_2.background = {"A":0.3,"C":0.2,"G":0.2,"T":0.3}
# pseudocount와 background를 설정해준다
pssm_motif_1=motif_1.pssm
pssm_motif_2=motif_2.pssm
# pssm을 생성한다
distance, offset = pssm_motif_2.dist_pearson(pssm_motif_1)
print("distance = %5.3g" % distance)
print("offset: ",offset)
# 피어슨씨 와봐요
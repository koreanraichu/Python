from Bio import motifs
fh = open("/home/koreanraichu/MA0004.1.jaspar")
for m in motifs.parse(fh, "jaspar"):
    print(m)
# JASPAR format
with open("/home/koreanraichu/MA0007.1.pfm") as handle:
    srf = motifs.read(handle, "pfm")
print(srf)
# PFM format
# 파일 윗부분의 ID를 지우지 않은 상태로 불러오면 ValueError: could not convert string to float: '>MA0007.1' 에러가 뜬다.
# ID를 지우면 읽긴 읽는데 TF name이 없지...
from Bio import SearchIO
qresult = SearchIO.read("/home/koreanraichu/7PNN_BLAST.txt", "blast-tab",comments=True)
# 결과 뭉텅이로 있었던 것 같은데 하나밖에 안 부르네?
print(qresult)
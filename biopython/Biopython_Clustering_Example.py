from Bio import Cluster
with open("/home/koreanraichu/cyano.txt") as handle:
    record = Cluster.read(handle)
# 불러와서
genetree = record.treecluster(method="s")
genetree.scale()
# Hierarchical clustering
# method는 Pairwise single-linkage clustering
exptree = record.treecluster(dist="u", transpose=1)
# 이것도 Hierarchical clustering(컬럼으로 그림, dist)
# dist는 Uncentered Pearson correlation(어슨이형)
# 그려서
record.save("cyano_result", genetree, exptree)
# 저장
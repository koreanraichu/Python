from Bio import Cluster
with open("/home/koreanraichu/cyano.txt") as handle:
    record = Cluster.read(handle)
# 불러왔다
matrix = record.distancematrix()
# Distance matrix 계산
cdata, cmask = record.clustercentroids()
# Cluster 무게중심(Centroid) 계산
distance = record.clusterdistance()
# 클러스터간 거리 계산
tree = record.treecluster()
# hierarchical clustering
# 이거 matplot으로 못뽑나...
clusterid, error, nfound = record.kcluster()
# k-mean clustering
# method='a': k-mean
# method='m': k-median
clusterid, celldata = record.somcluster()
# SOM 계산하기
jobname="cyano_clustering"
record.save(jobname, record.treecluster(), record.treecluster(transpose=1))
# 내 컴퓨터에 저(별)장
# 기본 형식: record.save(jobname, geneclusters, expclusters)
# geneclusters=record.treecluster()
# expclusters=record.treecluster(transpose=1)
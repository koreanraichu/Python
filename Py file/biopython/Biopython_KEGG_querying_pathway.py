from Bio.KEGG import REST
human_pathways = REST.kegg_list("pathway", "hsa").read()
# 여기까지 분량이 정말 많은 것을 볼 수 있다.
repair_pathways = []
for line in human_pathways.rstrip().split("\n"):
    entry, description = line.split("\t")
    if "lysis" in description:
        repair_pathways.append(description)
print(repair_pathways)
# 조건부로 Repair pathway만 보는 코드
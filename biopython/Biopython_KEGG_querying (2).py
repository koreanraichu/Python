from Bio.KEGG import REST
drug = REST.kegg_list('drug').read()
# 가져올 수 있는 것: brite, pathway, genome(gene은 안됨), module, enzyme, glycan, compound, reaction, network, drug, disease
drug_list = []
drug_name=input("찾고 싶은 약과 관련된 것을 입력해주세요: ")
# 찾고 싶은 약과 관련된 것을 입력받아 검색한다(예: vaccine)
for line in drug.rstrip().split("\n"):
    entry, description = line.split("\t")
    if drug_name in description:
        drug_list.append(description)
print(drug_list)
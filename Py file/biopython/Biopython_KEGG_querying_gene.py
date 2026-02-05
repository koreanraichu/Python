from Bio.KEGG import REST
human_pathways = REST.kegg_list("pathway", "hsa").read()
# 여기까지 분량이 정말 많은 것을 볼 수 있다.
Oxidative_pathways = []
Oxidative_pathways_name =[]
for line in human_pathways.rstrip().split("\n"):
    entry, description = line.split("\t")
    if "Oxidative" in description:
        Oxidative_pathways.append(entry)
        Oxidative_pathways_name.append(description)
print("Entry no: ",Oxidative_pathways,"description is: ",Oxidative_pathways_name)
# 조건부로 Repair pathway만 보는 코드
# 여기까지는 파일에 있었으니까 다들 아시리라 믿고...
Oxidative_genes = []
for pathway in Oxidative_pathways:
    pathway_file = REST.kegg_get(pathway).read()  # query and read each pathway

    # iterate through each KEGG pathway file, keeping track of which section
    # of the file we're in, only read the gene in each pathway
    current_section = None
    for line in pathway_file.rstrip().split("\n"):
        section = line[:12].strip()  # section names are within 12 columns
        if not section == "":
            current_section = section

        if current_section == "GENE":
            gene_identifiers, gene_description = line[12:].split("; ")
            gene_id, gene_symbol = gene_identifiers.split()

            if not gene_symbol in Oxidative_genes:
                Oxidative_genes.append(gene_symbol)

print(
    "There are %d pathways and %d genes. The genes are:"
    % (len(Oxidative_pathways), len(Oxidative_genes))
)
print(", ".join(Oxidative_genes))
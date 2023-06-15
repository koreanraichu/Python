from Bio import Phylo
tree = Phylo.read("/home/koreanraichu/Halobacterium.ph", "newick")
print(tree)
# Read(ph file)

trees = Phylo.parse("/home/koreanraichu/Deinococcus.xml", "phyloxml")
for tree in trees:
    print(tree)
# parse(phyloxml)
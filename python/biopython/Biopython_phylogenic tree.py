from Bio import Phylo
tree = Phylo.read("/home/koreanraichu/covid_all.ph","newick")
Phylo.draw(tree)
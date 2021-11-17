from Bio import Phylo
tree = Phylo.read("/home/koreanraichu/Halobacterium.ph", "newick")
tree.name="Halophile" # 이거 써야 제목 들어간다
Phylo.draw(tree, branch_labels=lambda c: c.branch_length)
# 거리 들어가는 건 좋은데 되게 중구난방이시네요.
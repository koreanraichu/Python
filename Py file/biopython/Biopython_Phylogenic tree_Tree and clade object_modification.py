from Bio import Phylo
tree = Phylo.read("/home/koreanraichu/Halobacterium.ph", "newick")
tree.name="Halophile"
tree.collapse("CEML01000001.1297981.1299440")
tree.collapse_all()
# collapse: 있었는데요 없어졌습니다
# collapse_all: 아무리 그래도 tree를 빗을 만드냐
tree.ladderize()
# clade를 terminal node 수에 따라 정렬하는 기능
tree.prune()
# prune이 가지치기라는 뜻이 있는 건 알겠는데... 그래서 tree에 가지치기 한거지?
tree.root_with_outgroup("AB105159.1.1501")
# 저걸 가장 가까운 걸로 해서 다시 트리를 그린다.
tree.root_at_midpoint()
# 뭐지 제일 중구난방인 트리를 뺴버린건가
tree.split()
# 밑에 새로운 후손을 추가해준다(default: 2)
Phylo.draw(tree)
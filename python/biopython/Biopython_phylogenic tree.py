from Bio import Phylo
tree = Phylo.read("/home/koreanraichu/Bacillus.ph", "newick")
# 선생님 트리 어디갔어요
Phylo.draw_ascii(tree)
# ascii tree

tree.root.color = (255,0,0)
# 가지 색을 바꿀 수 있다.
tree.clade[0, 1].color = "blue"
# 부분적으로 색을 바꿔줄 수도 있는 듯.
Phylo.draw(tree)
# matplot으로 그려준다(색깔 코드는 위로 가야 반영됨)

import sys
Phylo.write(tree, sys.stdout, "phyloxml")
# xml format으로 저장...은 안됨?
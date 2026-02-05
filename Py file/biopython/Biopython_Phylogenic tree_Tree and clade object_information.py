from Bio import Phylo
tree = Phylo.read("/home/koreanraichu/Halobacterium.ph", "newick")
tree.name="Halophile" # 이거 써야 제목 들어간다
print(tree.get_terminals()) # tree의 끝 노드를 출력
print(tree.get_nonterminals()) # tree의 중간 노드까지 출력
# 그나저나 저거 이름 못바꾸나요...
print(tree.find_clades()) # clade를 찾는다.
print(tree.find_elements()) # element를 찾는다.
print(tree.find_any()) # 다 찾는다.
# find_any()빼면 다 filter object 나온다...
print(tree.common_ancestor("AB021386.1.1495")) # 조상님좀 찾아주세요
print(tree.count_terminals()) # Terminal 갯수좀 세주세요
print(tree.depths()) # depth 얼마임?
print(tree.distance("AB021386.1.1495","U20163.1.1495")) # 얘 거리 얼마냐? (두개 찾아주는 것도 된다)
print(tree.total_branch_length()) # 전체 branch 길이
# 여기까지는 수치로 나오는 정보
print(tree.is_bifurcating()) # True if the tree is strictly bifurcating (아마 트리가 둘로만 갈리면 True인 듯)
print(tree.is_monophyletic("CP010835.91794.93350")) # Test if all of the given targets comprise a complete subclade(
# 단일 계통 여부)
print(tree.is_parent_of("CP010835.91794.93350")) # 얘가 이 트리에서 후손관계야?
print(tree.is_preterminal()) # True if all direct descendents are terminal(직계 후손이 terminal이면 참이라는데 뭔 소리지)
# 여기까지는 boolean
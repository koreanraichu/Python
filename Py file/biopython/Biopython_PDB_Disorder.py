from Bio.PDB.PDBParser import PDBParser
parser = PDBParser(PERMISSIVE=1)
structure_id = "4lqm"
filename = "/home/koreanraichu/4lqm.pdb"
structure = parser.get_structure(structure_id, filename)
# 일단 불러보자
model=structure[0]
chain=model['A']
residue=chain[858]
atom=residue["CA"]
print(chain[858])
print(residue.disordered_select("LEU"))
# 이거 예제에 있는대로 했는데 Attribute error가 왜 뜨는거지?
# AttributeError: 'Residue' object has no attribute 'disordered_select'
# 참고: Arginine 한글자 약어가 R이다. L은 류신.

from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import PPBuilder
ppb=PPBuilder()
# 예제에는 안나왔는데 이거 두 줄 추가해야된다...
p = PDBParser()
structure = p.get_structure("7kz1", "/home/koreanraichu/7kz1.pdb")
model_nr = 1
polypeptide_list = ppb.build_peptides(structure, model_nr)
for polypeptide in polypeptide_list:
    print(polypeptide.get_sequence())
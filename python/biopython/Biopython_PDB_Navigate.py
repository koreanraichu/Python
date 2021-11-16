from Bio.PDB.PDBParser import PDBParser
p = PDBParser()
structure = p.get_structure("2m3g", "/home/koreanraichu/2m3g.pdb")
for model in structure:
    for chain in structure:
        for residue in structure:
            for atom in structure:
                print(atom)
# iteration 가즈아!!!

structure2 = p.get_structure("2b10", "/home/koreanraichu/2b10.pdb")
atoms = structure2.get_atoms()
for atom in atoms:
    print(atom)
# 단축 가즈아!!!

atoms = chain.get_atoms()
for atom in atoms:
    print(atom)
# chain에서 가져올 수도 있는 듯 하다.

residues = model.get_residues()
for residue in residues:
    print(residue)
# Residue는 이걸로 뽑는다.

chains=structure2.get_chains()
for chain in chains:
    print(chain)
# chain도 된다.

models=structure2.get_models()
for model in models:
    print(model)
# 모델은 이걸로도 된다
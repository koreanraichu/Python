from Bio.PDB.PDBParser import PDBParser
p = PDBParser()
structure = p.get_structure("2b10", "/home/koreanraichu/2b10.pdb")
# Cytochrome C peroxidase
for model in structure.get_list():
    for chain in model.get_list():
        for residue in chain.get_list():
            if residue.has_id("CA"):
                ca = residue["CA"]
                if ca.get_bfactor() > 50.0:
                    print(ca.get_coord())
# List 내 알파탄소 중 B factor가 50 이상인 것의 '좌표'

for residue in chain.get_list():
    residue_id = residue.get_id()
    hetfield = residue_id[0]
    if hetfield[0] == "H":
        print(residue_id)
# HET residue를 전체 출력하는 코드
# W로 바꾸면 물분자가 출력된다.

for model in structure.get_list():
    for chain in model.get_list():
        for residue in chain.get_list():
            if residue.is_disordered():
                resseq = residue.get_id()[1]
                resname = residue.get_resname()
                model_id = model.get_id()
                chain_id = chain.get_id()
                print(model_id, chain_id, resname, resseq)
# Disordered atom을 포함하는 모든 residue들을 출력한다. 참고로 여기에는 없다.

for model in structure.get_list():
    for chain in model.get_list():
        for residue in chain.get_list():
            if residue.get_resname() == "LEU":
                print(residue.get_id())
# 응용: Residue 중 류신 뽑아줘(Leu)
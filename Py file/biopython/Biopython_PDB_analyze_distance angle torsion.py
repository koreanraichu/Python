from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.vectors import calc_angle
from Bio.PDB.vectors import calc_dihedral

p = PDBParser()
structure = p.get_structure("5ngo", "/home/koreanraichu/5ngo.pdb")
# 아무튼 불러와보겠습니다.
residues=structure.get_residues()
for residue in residues:
    print(residue)
# 나도 이거 처음보는거라 목록부터 봐야됨...
residue1=structure[0]["A"][273]["CA"]
residue2=structure[0]["A"][278]["CA"]
print(residue1-residue2)
# Residue간 거리
# 6.962208
atom1=structure[0]["A"][423]["CA"]
atom2=structure[0]["A"][423]["CB"]
atom3=structure[0]["A"][423]["N"]
vector1=atom1.get_vector()
vector2=atom2.get_vector()
vector3=atom3.get_vector()
angle = calc_angle(vector1, vector2, vector3)
print(angle)
# 각(별)도
# 0.5872530070961592

atom1=structure[0]["A"][415]["CA"]
atom2=structure[0]["A"][423]["CA"]
atom3=structure[0]["A"][431]["CA"]
atom4=structure[0]["A"][439]["CA"]
vector1 = atom1.get_vector()
vector2 = atom2.get_vector()
vector3 = atom3.get_vector()
vector4 = atom4.get_vector()
torsion = calc_dihedral(vector1,vector2,vector3,vector4)
print(torsion)
# Torsion angle 계산
# 1.28386400091194

model=structure[0]
model.atom_to_internal_coordinates()
for r in model.get_residues():
    if r.internal_coord:
        print(
            r,
            r.internal_coord.get_angle("psi"),
            r.internal_coord.get_angle("phi"),
            r.internal_coord.get_angle("omega"),  # or "omg"
            r.internal_coord.get_angle("chi2"),
            r.internal_coord.get_angle("CB:CA:C"),
            (r.internal_coord.get_length("-1C:0N")  # i-1 to i peptide bond
              if r.internal_coord.rprev else "None")
        )
# Internal coordinates for standard residues
# 출력 형식: <Residue SER het=  resseq=451 icode= > None 85.88349606675206 167.36084855239682 None 116.39783860086264 None
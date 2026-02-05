from Bio.PDB.PDBParser import PDBParser
parser = PDBParser(PERMISSIVE=1)
structure_id = "5zi1"
filename = "/home/koreanraichu/5zi1.pdb"
structure = parser.get_structure(structure_id, filename)
# 뭘 불러와야 하죠

# Structure>model>chain>residue>Atom 순으로 세부 카테고리
model=structure[0] # Model
chain=model["A"] # Chain
residue=chain[(" ", 100, " ")]# <<Full ID
# print(chain[100]) <<Shortcut ID
print(residue.get_resname()) # 이름이 뭐냐
print(residue.is_disordered()) # Disordered에 속했냐(속하면 1)
print(residue.get_segid()) # Segment ID가 뭐냐
print(residue.has_id(10)) # 얘 ID 있음?

# 이제 atom으로 가보자...
atom=residue["CA"]
print(atom.get_name()) # 이름!
print(atom.get_fullname()) # 이름! (풀네임)
print(atom.get_id()) # ID
print(atom.get_coord()) # 좌투더표
print(atom.get_vector()) # 좌표를 벡터 객체로 받음
print(atom.get_bfactor()) # Isotropic B factor
print(atom.get_occupancy()) # Occupancy
print(atom.get_altloc()) # alternative location specifier
print(atom.get_sigatm()) # 원자 매개변수의 표준편차
print(atom.get_siguij()) # Isotropic B factor의 표준편차
print(atom.get_anisou()) # anisotropic B factor

# 아 일일이 빼기 귀찮으시죠? 그럼 한줄로 ㄱㄱ하세요.
atom = structure[0]["A"][100]["CA"]
print(atom.get_name())
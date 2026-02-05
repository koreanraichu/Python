from Bio.PDB.PDBParser import PDBParser
parser = PDBParser(PERMISSIVE=1)
structure_id = "2b10"
filename = "/home/koreanraichu/2b10.pdb"
structure = parser.get_structure(structure_id, filename)
print(structure)
# 이거 PC에 있는 파일 가져오는건가?
# FileNotFoundError: [Errno 2] No such file or directory: 'pdb1fat.ent'

from Bio.PDB import parse_pdb_header
with open(filename, "r") as handle:
    header_dict = parse_pdb_header(handle)
    print(header_dict)
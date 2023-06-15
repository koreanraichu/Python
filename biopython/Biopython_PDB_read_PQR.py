from Bio.PDB.PDBParser import PDBParser
pqr_parser = PDBParser(PERMISSIVE=1, is_pqr=True)
structure_id = "7lfv"
filename = "/home/koreanraichu/7lfv.pqr"
# structure = parser.get_structure(structure_id, filename, is_pqr=True)
# NameError: name 'parser' is not defined
structure = pqr_parser.get_structure(structure_id, filename)
print(structure)
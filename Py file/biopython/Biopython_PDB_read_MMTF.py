from Bio.PDB.mmtf import MMTFParser
structure = MMTFParser.get_structure("PDB/4CUP.mmtf")
print(structure)
# Bio.MissingPythonDependencyError: Install mmtf to use Bio.PDB.mmtf (e.g. pip install mmtf-python)
# 이것도 에러난다.

structure = MMTFParser.get_structure_from_url("4CUP")
print(structure)
# Bio.MissingPythonDependencyError: Install mmtf to use Bio.PDB.mmtf (e.g. pip install mmtf-python)
# pip install 한 게 저거. 뭐가 불만이세요.
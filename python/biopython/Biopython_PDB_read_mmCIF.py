from Bio.PDB.MMCIFParser import MMCIFParser
parser = MMCIFParser()
structure = parser.get_structure("7f0l", "/home/koreanraichu/7f0l.cif")
print(structure)

from Bio.PDB.MMCIF2Dict import MMCIF2Dict
mmcif_dict = MMCIF2Dict("/home/koreanraichu/7f0l.cif")
print(mmcif_dict)
# FileNotFoundError: [Errno 2] No such file or directory: '1FAT.cif'
# 위 에러가 뜨는 경우, 해당하는 확장자의 파일이 내 PC에 있어야 한다.
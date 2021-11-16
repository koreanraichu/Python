from Bio.PDB.PDBList import PDBList
pdbl = PDBList()
pdbl.retrieve_pdb_file("6WO1",file_format="mmtf",pdir="/home/koreanraichu/")
# 확장자를 따로 입력하지 않으면 CIF파일로 다운르드 된다.
# file_format="확장자"로 입력하면 특정 파일 형식으로 받을 수 있다.
# pdir="경로"를 입력하면 다운로드 경로도 정할 수 있다.
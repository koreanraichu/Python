from Bio import SeqIO
from Bio.Blast import NCBIWWW
record = SeqIO.read("/home/koreanraichu/CaMV.fasta", format="fasta")
result_handle = NCBIWWW.qblast("blastn", "nt", record.seq)
save_file = open("my_blast.xml", "w") # 이거 뭐 하는 구문인데 경초 못 찾는다고 에러뜨냐
save_file.write(result_handle.read())
save_file.close()
result_handle.close()
# 위에 네 줄까지 추가해야 결과가 저장된다.
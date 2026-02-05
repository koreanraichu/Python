from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
for seq_record in SeqIO.parse("/home/koreanraichu/coronavirus.gb","genbank"): # 이거 이래 불러야되나
    print(seq_record.seq) # Genbank 가져올거면 이렇게 쓰세요
result_handle = NCBIWWW.qblast("blastn", "nt", seq_record.seq)
blast_record = NCBIXML.parse(result_handle)
# 결과가 하나면 read, 여러개면 parse
# 이것도 parse에 for문이 국룰인가?
save_file = open("coronavirus.xml", "w") # 이거 뭐 하는 구문인데 경초 못 찾는다고 에러뜨냐
save_file.write(result_handle.read())
save_file.close()
result_handle.close()
# 위에 네 줄까지 추가해야 결과가 저장된다.
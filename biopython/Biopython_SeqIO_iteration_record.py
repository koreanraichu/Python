from Bio import SeqIO
record_iterator = SeqIO.parse("/home/koreanraichu/ls_orchid.fasta", "fasta")

first_record = next(record_iterator)
print(first_record.id)
print(first_record.description)

second_record = next(record_iterator)
print(second_record.id)
print(second_record.description)

third_record = next(record_iterator)
print(third_record.id)
print(third_record.description)
# 얘는 next가 입력된 만큼 뽑아준다.
# 가만 이거 for문이나 while문이랑 결합 되나? 

first_record_2 = next(SeqIO.parse("/home/koreanraichu/rcsb_pdb_2B10.fasta", "fasta")) # 레코드 중 하나만 보고 싶을 때
print(first_record_2)
# pandas의 head(1)과 같은 기능이다
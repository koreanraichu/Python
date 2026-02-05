from Bio import SeqIO
record=SeqIO.read('/home/koreanraichu/rcsb_pdb_7PNN.fasta','fasta')
# 기록된 게 하나면 read
print(record.id)
for record2 in SeqIO.parse("/home/koreanraichu/rcsb_pdb_2B10.fasta","fasta"):
    print(record2.id)
# 두 개 이상이라 read쓰면 ValueError: More than one record found in handle뜸...
# 파싱으로 데려온 것은 출력하려ㅕ면 for문이 필요하다.
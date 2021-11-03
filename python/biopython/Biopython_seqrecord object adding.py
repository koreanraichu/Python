from Bio import SeqIO
record = next(SeqIO.parse("/home/koreanraichu/rcsb_pdb_7PNN.fasta", "fasta"))

# 시퀀스 절단냈다...
left=record[:20]
right=record[30:]

# 합체
edited = left + right
print(edited.seq)

# 길이를 비교해보자
print(len(record.seq))
print(len(edited.seq))

# Adding이라매 왜 빼먹는거냐
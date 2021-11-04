from Bio import SeqIO
records = list(SeqIO.parse("/home/koreanraichu/ls_orchid.gbk", "genbank"))
print(len(records)) # 레코드 길이(사실상 개수)
first=records[0]
last=records[-1]
# 변수 안 주면 풀로 나온다...
print("First record ID:",first.id)
print("Last record ID:",last.id)
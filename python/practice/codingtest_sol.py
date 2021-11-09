"""
Q1. FASTAQ파일을 FASTA 파일로 변환하시오
Q2. 변환한 FASTA 파일의 각 염기 갯수는?
Q3. 변환한 FASTA파일의 전체 염기 수는?
Q4. Top 10 sequenth length는?
Q5. Sequence 길이의 조건부 합계
"""
# Module은 여기로 소환하면 된다.
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import numpy as np
import pandas as pd
# A1. FASTAQ파일 변환하기
# FASTAQ file 불러오기
handle="/home/koreanraichu/sra_data_mo.fastq"
for record in SeqIO.parse(handle,"fastq"):
    print(record.id)
# FASTA파일로 쓰기
convert_fasta=SeqIO.convert(handle, "fastq", "/home/koreanraichu/sra_data_mo.fasta","fasta")

# A2. FASTA file에서 A, T, G, C 세기
# FASTA파일을 다시 불러올 예정이다.
handle2="/home/koreanraichu/sra_data_mo.fasta"
A = [] #아니 이게 이렇게 해결된다고?
T = [] # 리스트 밖으로 뺐더니 이게 돼?????
G = []
C = []
for record2 in SeqIO.parse(handle2,"fasta"):
    A.append(Seq(record2.seq).count("A"))
    T.append(Seq(record2.seq).count("T"))
    G.append(Seq(record2.seq).count("G"))
    C.append(Seq(record2.seq).count("C"))
print("A: ",sum(A),"T: ",sum(T),"G: ",sum(G),"C: ",sum(C))

# A3. 파일에 수록된 전체 시퀀스 길이
print(sum(len(r) for r in SeqIO.parse(handle2, "fasta")))

# A4. Top 10 length
record_id=[] # 야 이걸 이렇게 해결보네
record_len=[]
for record2 in SeqIO.parse(handle2,"fasta"):
    record_id.append(record2.id)
    record_len.append(len(record2.seq))
record_id_array=np.array(record_id)
record_len_array=np.array(record_len)
# 배열화 성공(위에 빼 둔 시르트로 생성함)
record_table=pd.DataFrame({"ID":record_id_array,"Length":record_len_array})
record_table2=record_table.groupby('Length').count()
record_table2=record_table2.sort_values('Length',ascending=0)
print(record_table2.head(10))
# 아 드디어 깔끔한 표가 나왔습니다!!!
# 그리고 어쨌든 Top10 뽑았음

# A5. 조건부 합계(여기서는 100bp 이상/미만으로 나눈다)
print("length >= 100bp:",record_table['Length'][record_table.Length >= 100].sum())
print("length < 100bp:",record_table['Length'][record_table.Length < 100].sum())
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
for record2 in SeqIO.parse(handle2,"fasta"):
    print(Seq(record2.seq).count("A"))
    print(type(Seq(record2.seq).count("A")))
    # Count로 세는 건 되는데 합계를 안 내준다. int형인데 더해주질 않음.

# A3. 파일에 수록된 전체 시퀀스 길이
print(sum(len(r) for r in SeqIO.parse(handle2, "fasta")))

# A4. Top 10 length
for record2 in SeqIO.parse(handle2,"fasta"):
    record_id=np.array(record2.id)
    record_len=np.array(len(record2.seq))
    record_table=pd.DataFrame({"ID":record_id, "length":record_len},index=[0])
    print(record_table)
    # Dataframe이 이상하게 생성된다.
    """
                   ID  length
    0  SRR000021.37.2     249
    이런 식으로 항목 하나당 한 데이터프레임이 생성되는데 Array까지는 정상적으로 생성됨. 
    """

# A5. 조건부 합계(여기서는 100bp 이상/미만으로 나눈다)
for record2 in SeqIO.parse(handle2,"fasta"):
    if len(record2.seq) > 100:
        i=0
        i=i+len(record2.seq)
    else:
        j=0
        j=j+len(record2.seq)
print(i,j)
# 이것도 합계가 구해지는 게 아니라 맨 마지막 값이 더해진다.
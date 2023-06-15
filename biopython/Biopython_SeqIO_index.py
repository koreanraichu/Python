from Bio import SeqIO
orchid_dict = SeqIO.index("/home/koreanraichu/ls_orchid.fasta", "fasta")
print(orchid_dict.keys())

"""
# 색인이 가능하다
seq_record = orchid_dict["Z78475.1"]
print(seq_record.description)
"""
# orchid_dict.close()는 닫는 코드다
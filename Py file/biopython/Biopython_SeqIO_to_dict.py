from Bio import SeqIO
from Bio.SeqUtils.CheckSum import seguid
"""
orchid_dict = SeqIO.to_dict(SeqIO.parse("/home/koreanraichu/rcsb_pdb_2B10.fasta", "fasta"))
print(orchid_dict.keys())
print(orchid_dict.values())
print(orchid_dict['2B10_1|Chains'].description) # selector도 줄 수 있다.
"""

# SEGUID Cheksum function을 이용한 방법
for record in SeqIO.parse("/home/koreanraichu/rcsb_pdb_2B10.fasta", "fasta"):
    print(record.id, seguid(record.seq))

seguid_dict = SeqIO.to_dict(SeqIO.parse("/home/koreanraichu/rcsb_pdb_2B10.fasta", "fasta"),lambda rec: seguid(rec.seq))
record = seguid_dict["kSIi2w+CcP3y/k3bFRVhvvWtCtM"]
print(record.id)
# InChl Key만큼이나 괴악한 저걸로도 찾을 수 있나보다 
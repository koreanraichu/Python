from Bio import SeqIO
from Bio.Blast import NCBIWWW
record = SeqIO.read("/home/koreanraichu/CaMV.fasta", format="fasta")
result_handle = NCBIWWW.qblast("blastn", "nt", record.seq)
print(result_handle)
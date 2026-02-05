from Bio import ExPASy
from Bio import SeqIO
with ExPASy.get_sprot_raw("Q14005") as handle:
    seq_record = SeqIO.read(handle, "swiss")
print(seq_record.name)
print(seq_record.description)
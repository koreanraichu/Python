from Bio import SeqIO
record_iterator = SeqIO.parse("/home/koreanraichu/rcsb_pdb_2B10_mod.fasta", "fasta") # 불러와서(사본 만듦)
first_record = next(record_iterator)
first_record.id="SC_2B10_1" # ID를 바꿨다.
print(first_record.id)
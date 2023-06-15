from Bio import SeqIO
for seq_record in SeqIO.parse("/home/koreanraichu/rcsb_pdb_2B10.fasta","fasta"):
    print(seq_record.id)
    print(seq_record.description)
    print(repr(seq_record.seq))

for seq_record in SeqIO.parse("/home/koreanraichu/sequence.gb","genbank"):
    print(seq_record.description)
    print(seq_record.annotations)
    print(repr(seq_record.seq))
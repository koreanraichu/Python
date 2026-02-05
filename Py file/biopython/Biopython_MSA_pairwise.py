from Bio import pairwise2
from Bio import SeqIO
seq1 = SeqIO.read("/home/koreanraichu/alpha.faa", "fasta")
seq2 = SeqIO.read("/home/koreanraichu/beta.faa", "fasta")
alignments = pairwise2.align.globalxx(seq1.seq, seq2.seq)
print(alignments[0]) # 와 되게 길다...
print(pairwise2.format_alignment(*alignments[0]))
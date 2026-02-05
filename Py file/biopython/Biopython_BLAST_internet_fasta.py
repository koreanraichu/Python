from Bio.Blast import NCBIWWW
fasta_string = open("/home/koreanraichu/CaMV.fasta").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
print(result_handle)
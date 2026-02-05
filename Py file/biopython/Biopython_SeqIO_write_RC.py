from Bio import SeqIO
records = [rec.reverse_complement(id="rc_"+rec.id, description = "reverse complement")
           for rec in SeqIO.parse("/home/koreanraichu/at5g40780.gb", "genbank")]
SeqIO.write(records, "/home/koreanraichu/at5g40780_rc.fasta", "fasta")
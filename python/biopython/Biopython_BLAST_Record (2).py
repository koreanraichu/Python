from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

record = SeqIO.read("/home/koreanraichu/rcsb_pdb_7PNN.fasta", format="fasta")
result_handle = NCBIWWW.qblast("blastp", "nr", record.seq)
blast_records = NCBIXML.parse(result_handle)

E_VALUE_THRESH = 0.04 # 일단 이거 높으면 안좋은거다
for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                print("****Alignment****")
                print("sequence:", alignment.title)
                print("length:", alignment.length)
                print("e value:", hsp.expect)
                print(hsp.query[0:75] + "...")
                print(hsp.match[0:75] + "...")
                print(hsp.sbjct[0:75] + "...")
# hsp 영역을 추출해 내는 스크립트.
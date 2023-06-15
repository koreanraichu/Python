from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
with open("my_blast.xml") as bf: # 이거는 저장된 파일
    blast_records = NCBIXML.parse(bf)
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
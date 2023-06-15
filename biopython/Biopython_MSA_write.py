from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio import AlignIO
align1=MultipleSeqAlignment([
    SeqRecord(Seq("GGCC"),id="HaeIII"),
    SeqRecord(Seq("G-CC"),id="id2"),
    SeqRecord(Seq("G--C"),id="id3")
])
align2=MultipleSeqAlignment([
    SeqRecord(Seq("GAATTC"),id="EcoRi"),
    SeqRecord(Seq("G-ATTC"),id="id5"),
    SeqRecord(Seq("G--TTC"),id="id6")
])
my_alignment=[align1,align2]
# 여기까지 시퀀스를 만들고

AlignIO.write(my_alignment, "/home/koreanraichu/my_example.phy", "phylip")
# 여기서 저(별)장
# MSA에서는 FASTA 안쓰나?
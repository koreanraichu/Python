from Bio.Align.Applications import MuscleCommandline
muscle_cline = MuscleCommandline(input="/home/koreanraichu/lactobacillus.fasta")
stdout, stderr = muscle_cline()
from io import StringIO
from Bio import AlignIO
align = AlignIO.read(StringIO(stdout), "fasta")
print(align)
# 이거 설치해야 되는거임?
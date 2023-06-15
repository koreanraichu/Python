from Bio.Align.Applications import ClustalwCommandline
cline = ClustalwCommandline("clustalw2", infile="/home/koreanraichu/lactobacillus.fasta")
print(cline) # clustalw2 -infile=/home/koreanraichu/lactobacillus.aln
help(ClustalwCommandline) # Help
# 어쩌라는거지... 설치해야되나... cookbook에 있는 거 윈도용 아니냐...

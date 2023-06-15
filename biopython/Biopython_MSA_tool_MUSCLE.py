from Bio.Align.Applications import MuscleCommandline
cline = MuscleCommandline(input="/home/koreanraichu/lactobacillus.fasta",
                          out="/home/koreanraichu/lactobacillus.txt",
clwstrict=True)
print(cline)
help(MuscleCommandline) # Help
# muscle -in /home/koreanraichu/lactobacillus.fasta -out /home/koreanraichu/lactobacillus.txt -clwstrict
# 하지만 아무 일도 없었다!
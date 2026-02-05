from Bio.Align import substitution_matrices
from Bio import Align # 아니 얘 데려와야된다고 왜 말 안해줬어... 식겁했네...
aligner = Align.PairwiseAligner()
substitution_matrices.load()
matrix = substitution_matrices.load("BLOSUM62") # 아까 걔

aligner.substitution_matrix = matrix
score=aligner.score("GGCC","GGCC")
print(score)
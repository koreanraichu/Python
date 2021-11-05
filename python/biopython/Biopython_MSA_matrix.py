from Bio.Align.substitution_matrices import Array
counts = Array("ACGT") # 1차원
print(counts)
counts_dim2=Array("ACGT",dims=2) # 2차원
# Indesing도 가능하다. (내용을 바꿀 수도 있다)
print(counts_dim2['G'])
print(counts_dim2[:,'G'])
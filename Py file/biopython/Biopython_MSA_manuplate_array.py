from Bio import AlignIO
import numpy as np
alignment = AlignIO.read("/home/koreanraichu/PF00096_seed.txt", "stockholm")
align_array = np.array([list(rec) for rec in alignment],np.character) # 불러와서 배열화하는 것 같은데 np.character 끼니까 오류가 반기네?
# /home/koreanraichu/PycharmProjects/pythonProject/Biopython_MSA_manuplate_array.py:4: DeprecationWarning: Converting `np.character` to a dtype is deprecated. The current result is `np.dtype(np.str_)` which is not strictly correct. Note that `np.character` is generally deprecated and 'S1' should be used.
#   align_array = np.array([list(rec) for rec in alignment],np.character, order="F") # 불러와서 배열화하는 것 같은데 오류가 반기네?
print(align_array)
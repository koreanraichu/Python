from Bio import SeqIO
import numpy as np
identifiers = [seq_record.id for seq_record in SeqIO.parse("/home/koreanraichu/ls_orchid.gbk", "genbank")]
# 이거 사실 쌩으로 불러올거면 걍 print 쓰면 됩니다.
# 근데 저게 길이가 좀 많아서 안이쁘다 그러면 len뽑고 array 만든 다음 뽑는게 더 이쁘잖음?
identifiers=np.array(identifiers) # 어레이화
identifiers=identifiers.reshape(2,47) # 하고 차원 바꿨음
print(identifiers)
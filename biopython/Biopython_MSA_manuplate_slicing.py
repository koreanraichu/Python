from Bio import AlignIO
alignment = AlignIO.read("/home/koreanraichu/PF08449_seed.txt", "stockholm")
print(alignment[0:5]) # pandas의 head()같은거. 위에서 다섯개만 보여줘
print(alignment[0,1]) # 0번째 인덱스의 두번째 컬럼
print(alignment[:,6]) # 레코드의 6번째 글자
print(alignment[0:5,0:5]) # index+column 범위를 지정할 수 있다
print(alignment[9:]) # index 9번째부터 다 가가온나
print(alignment[:,9:]) # column 9번째부터 다 가가온나
# 밑에꺼 뭐 하는건지 아시는분 제보좀 
edited = alignment[:, :5] + alignment[:, 15:] # 이거 뭐 하는거임?
print(edited)
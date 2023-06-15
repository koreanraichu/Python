import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
df=pd.read_csv("/home/koreanraichu/Others/csv/rheumatism.csv" ,sep=";")
df=df.dropna() # Nan은 친절하게 보내드렸습니다
x=pd.to_numeric(df['HBA'])
y=pd.to_numeric(df['HBD'])
# 글자라 정렬 개판돼서 숫자로 바꿔버림(Nan때문인가 암만봐도 숫자인데 object로 불러옴)
xtick = list(range(1, 12, 2))  # 축 간격용 리스트
"""
이제 이 밑부분은 그래프 영역입니다. 끝. 
"""
fig, ax = plot.subplots()
ax.set_xlabel('Hydrogen bond acceptor')
ax.set_ylabel('Hydrogen bond donor')
plot.rc("font", family='Nanumgothic')
plot.title('HBA/HBD')
plot.hexbin(x, y, cmap="winter", gridsize=20,mincnt=1)
# hexbin은 모양 지정이 안되고 grid size를 지정할 수 있다.
# legend는 색이 안 바껴서 뺴버림...
plot.xticks(xtick)
plot.colorbar()
plot.savefig('graph.png')
plot.show()
# hexbin은 배경색을 따로 못 바꾸는 모양인데...?
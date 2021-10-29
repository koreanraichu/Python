import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
shh=pd.read_csv("/home/koreanraichu/rheumatism.csv",sep=";")
shh=shh.dropna() # Nan은 친절하게 보내드렸습니다
x=pd.to_numeric(shh['HBA'])
y=pd.to_numeric(shh['HBD'])
# 글자라 정렬 개판돼서 숫자로 바꿔버림(Nan때문인가 암만봐도 숫자인데 object로 불러옴)
xtick=list(range(1,12,2)) # 축 간격용 리스트
area=75 # 여기 면적 추가요
np.random.seed(0)
"""
이제 이 밑부분은 그래프 영역입니다. 끝. 
"""
fig,ax=plot.subplots()
ax.set_xlabel('Hydrogen bond acceptor')
ax.set_ylabel('Hydrogen bond donor')
plot.rc("font", family='Nanumgothic')
plot.title('HBA/HBD')
plot.scatter(x,y,label="HBA/HBD",s=area,alpha=0.8,c=y) # HBD 숫자에 따라 색깔이 달라지게 설정했다. (HBA는 x로 주면 될 듯 하다)
#어? 이거 모양 바꿔도 적용되네?
plot.autumn() # 컬러맵 추가
plot.colorbar() #컬러바 추가
plot.legend(loc=0) # 굳이 넣어야되나...
plot.xticks(xtick)
plot.savefig('graph.png')
plot.show()
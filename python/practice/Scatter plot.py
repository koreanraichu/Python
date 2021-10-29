import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
shh=pd.read_csv("/home/koreanraichu/rheumatism.csv",sep=";")
shh=shh.dropna() # Nan은 친절하게 보내드렸습니다
x=pd.to_numeric(shh['HBA'])
y=pd.to_numeric(shh['HBD'])
# 글자라 정렬 개판돼서 숫자로 바꿔버림(Nan때문인가 암만봐도 숫자인데 object로 불러옴)
xtick=list(range(1,12,2)) # 축 간격용 리스트
"""
이제 이 밑부분은 그래프 영역입니다. 끝. 
"""
fig,ax=plot.subplots()
ax.set_xlabel('Hydrogen bond acceptor')
ax.set_ylabel('Hydrogen bond donor')
plot.rc("font", family='Nanumgothic')
plot.title('HBA/HBD')
plot.scatter(x,y,color="#000000",label="HBA/HBD",marker="s")
plot.legend(loc=0) # 굳이 넣어야되나...
plot.xticks(xtick)
plot.savefig('graph.png')
plot.show()

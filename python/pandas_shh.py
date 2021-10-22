import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
shh=pd.read_csv("/home/koreanraichu/sonic hedgehog.csv",sep=";") #구분자가 ,가 아님
#pd.set_option('display.max_columns', None) #표 전체 보여주는 옵션
#print(shh.iloc[0:8,0:4]) #iloc를 이용해 slicing
#print(shh['ChEMBL ID']) #켐블 아이디로 셀렉션(시리즈)
#print(shh[['Name']]) #이름으로 셀렉션(데이터프레임)
#print(shh[shh['Molecular Weight']<500]['Name']) #마스킹 연산+셀렉터
#print(shh.query("HBA < 5")['Smiles']) #쿼리+셀렉터
#근데 쿼리는 컬럼명에 공백 있으면 안됨?
print(shh)

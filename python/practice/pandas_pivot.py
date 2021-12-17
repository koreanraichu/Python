import pandas as pd
# 피벗테이블에는 판다스! 
df=pd.read_csv('/home/koreanraichu/example2.csv')
# 공백 이걸로 읽는거 실화냐 
print(df)
# 불러온 데이터프레임
pivot_1=df.pivot_table(index=['Category 1'])
# index 단식
pivot_2=df.pivot_table(index=['Category 1','Category 2'])
# index 복식
pivot_3=df.pivot_table(index=['Order'],columns=['Category 1'])
# 인덱스 컬럼 하나씩
pivot_4=df.pivot_table(index=['Order'],columns=['Category 1','Category 2'])
# 인덱스 하나 컬럼 둘
pivot_5=df.pivot_table(index=['Category 1','Category 2'],columns=['Order'])
# 인덱스 둘 컬럼 하나
pivot_6=df.pivot_table(index=['Category 1','Category 2'],columns=['Order','Cancel'])
# 인덱스 둘 컬럼 둘
# 뭔가... 엑셀이랑 많이 다른데...? 
pivot_t=df.pivot_table(index=['Category 1','Category 2'],values=['Order','Cancel'],aggfunc=['sum','max'])
print(pivot_t)
# Values도 여러개가 되네...? 
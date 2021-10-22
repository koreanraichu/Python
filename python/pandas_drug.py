import pandas as pd
import matplotlib.pyplot as plot
drug=pd.read_csv("/home/koreanraichu/Drug.csv")
# csv 파일 오픈
# 1. 분자량이 500 이상인 분자의 '이름'을 출력하시오.
print(drug[drug['Molecular Weight']>=500]['Name'])
#Query 쓰니까 ValueError: expr must be a string to be evaluated, <class 'list'> given 뜨는데 이거 뭔소리임?
# 2. hydrogen bond donor(HBD)와 hydrogen bond acceptor(HBA)가 둘 다 5 이하인 분자의 '이름'을 Dataframe으로 출력하시오.
print(drug.query("HBA<=5 and HBD <= 5")[['Name']])
# 3. topological polar surfaace area(TPSA)와 분자량으로 scatter plot을 그리시오.
# 4. 3번의 그래프에 axis label을 추가하고 범례를 좌측 상단에 그리시오.
fig,ax=plot.subplots()
ax.scatter(drug['TPSA'],drug['Molecular Weight'],label="Molecular weight/TPSA",marker="*",color="#88b04b")
ax.set_xlabel('TPSA')
ax.set_ylabel('Molecular Weight')
plot.legend(loc='upper left')
plot.savefig('example.png')
plot.show()
# 5. Drug table을 HBA, HBD 순서대로 정렬하여 표시하시오.
print(drug.sort_values(['HBA','HBD'],ascending=[True,True]))
# 6. 분자량의 최대값/최소값은?
print(drug.max())
print(drug.min())
# 7. 쿼리 함수를 이용해 Artemisinin의 SMILES를 표시하시오.
print(drug.query("Name.str.contains('Arte')")['SMILES'])
import pandas as pd
import numpy as np
rheumatis=pd.read_csv("/home/koreanraichu/rheumatism.csv",sep=";")
#groupby를 통해 small molecule만 selection
print(rheumatis.groupby('Type').get_group('Small molecule')['Name'])
print(rheumatis.groupby('Molecular Species').get_group('NEUTRAL')['Molecular Formula'])
print(rheumatis.groupby('Aromatic Rings').get_group('0')['Smiles'])
print(rheumatis.groupby('Aromatic Rings').get_group('2')['Smiles'])
#수소결합 관련해서 필터가 있는데도 안먹혔다...
rheumatis=rheumatis.dropna(axis=0)#결측값 제거
rheumatis=rheumatis.astype({'HBA':int,'HBD':int}) #HBA와 HBD의 None을 삭제하고 int로 바꿨다.
rheumatis=rheumatis.astype({'Molecular Weight':int})
print(rheumatis.query("HBA < 5 and HBD < 5 and `Molecular Weight` <500")['Name'])
#와 이제 된다! RO5 filter 중 수소겷합과 분자량으로 걸렀다!
#컬럼명에 공백이 있을 경우 `로 감싸주자.
print(rheumatis.query("Smiles.str.contains('C@@H')")['ChEMBL ID'])
#SMILES에서 오른손 chiral center(C@@H)가 있는 분자를 검색해서 ChEMBL ID를 출력
print(rheumatis.query("Smiles.str.contains('C@H')")['ChEMBL ID'])
#얘는 왼손 Chiral center(C@H)가 있는 분자의 SMILES를 출력한다.
print(rheumatis.query("Name.str.contains('IB')")['ChEMBL ID'])
#어쩌고닙(-IB) 찾아주세요 하는 거
print(rheumatis.query("`Molecular Formula`.str.contains('S')")['Name'])
#분자식에 황이 들어가는 분자의 이름
print(rheumatis.query("`Molecular Formula`.str.contains('F')")['ChEMBL ID'])
#분자식에 플루오린이 들어가는 분자의 ChEMBL ID
print(rheumatis.query("`Molecular Formula`.str.contains('Cl')")['Molecular Formula'])
#황이나 불소같이 원소기호가 한 글자인 것은 찾아주는데, 원소기호가 두 글자(Au, Na)인 것들은 Series([], Name: Molecular Formula, dtype: object)를 출력함.
#뭐야 왜그래요
#근데 또 염소는 잘 찾는다...? 뭐지?
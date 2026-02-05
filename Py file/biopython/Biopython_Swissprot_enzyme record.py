from Bio.ExPASy import Enzyme
with open("/home/koreanraichu/RuBisCO.txt") as handle:
    record = Enzyme.read(handle)
    print(record['ID']) # EC no.
    print(record['DE']) # description
    print(record['AN']) # 대충 synonyms같은건가? 뭐 얘 이렇게도 불러요 이런거
    print(record["CA"]) # 촉매하는 반응(오 이거 식으로 나온다)
    print(record["PR"]) # 이건 모르겠다... 데이터베이스 번호인가...
    print(record["CC"]) # 아마도 뭐 하는 효소인가에 대한 설명인 듯
    print(record['DR']) # 뭔진 모르겠지만 일단 잘못했어요... 뭐가 되게 많이떴는데 넘파이 마려웠음
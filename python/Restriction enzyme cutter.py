import pandas as pd
enzyme_table = pd.read_csv('/home/koreanraichu/restriction.csv')
enzyme_table = enzyme_table.sort_values('Enzyme')
# Finder에도 쓰이는 '그' DB 맞습니다. 현재 수동 구축 중...
sequence = input("검색할 시퀀스를 입력해주세요: ")
# 시퀀스 입력하는 란
for i in range(len(enzyme_table)):
    res_find = enzyme_table['sequence'][i]
    res_find = str(res_find)
    if res_find in sequence:
        print(enzyme_table['Enzyme'][i],res_find,sequence.find(res_find)+1)
    else:
        print(enzyme_table['Enzyme'][i],"Not found")
# 아직 저장기능은 없습니다. 지금 출력도 좀 중구난방이라 정리 좀 해야될듯.
# find로 나오는 위치의 경우 0부터 시작하기떄문에 하나 더해줬습니다. 아울러 해당 메소드가 '가장 처음에 나오는 글자'만 찾아주는거지 전체 검색이 아니기때문에 여러군데를 자르는지 여부는 모릅니다.
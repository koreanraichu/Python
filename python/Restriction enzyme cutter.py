import pandas as pd
from datetime import datetime
year = datetime.today().year
month = datetime.today().month
day = datetime.today().day
# 저장 파일에 역시나 날짜가 들어갑니다.
enzyme_table = pd.read_csv('/home/koreanraichu/restriction.csv')
enzyme_table = enzyme_table.sort_values('Enzyme')
# Finder에도 쓰이는 '그' DB 맞습니다.
filter = input("sticky로 자르는 제한효소만 보고 싶으면 sticky, blunt로 자르는 제한효소만 보고 싶으면 blunt를 입력해주세요. ")
# sticky: sticky end만 보고 싶다
# blunt: blunt만 보고 싶다
# 아무것도 안 치면 전부 찾아줍니다. (사실상 sticky or blunt 외에 다)
# 소문자로 입력해주세요, 대소문자 변환 기능은 제공하지 않습니다.
if filter == 'sticky':
    enzyme_table = enzyme_table[enzyme_table['cut_feature']== 'sticky']
    enzyme_table.reset_index(inplace=True)
elif filter == 'blunt':
    enzyme_table = enzyme_table[enzyme_table['cut_feature']== 'blunt']
    enzyme_table.reset_index(inplace=True)
else:
    filter = "None"
    pass
# 사용자가 입력한 필터에 따라 코드가 바뀝니다.
sequence = input("검색할 시퀀스를 입력해주세요: ")
# 시퀀스 입력하는 란
count = 0
with open('Result.txt_{0}-{1}-{2}_{3}'.format(year,month,day,filter),'w',encoding='utf-8') as f:
    f.write("Restriction enzyme which cuts this sequence: ")
    for i in range(len(enzyme_table)):
        enzyme = enzyme_table['Enzyme'][i]
        feature = enzyme_table['cut_feature'][i]
        res_find = enzyme_table['sequence'][i]
        res_find = str(res_find)
        if res_find in sequence:
            print(enzyme, res_find, sequence.find(res_find))
            f.write("{0}: {1} {2}\n".format(enzyme,res_find,feature))
            count += 1
        else:
            count += 0
    print(count)
    f.write("Total: {0} enzymes cut input sequence".format(count))
# 아직 저장기능은 없습니다. 지금 출력도 좀 중구난방이라 정리 좀 해야될듯.
# find로 나오는 위치의 경우 0부터 시작하기떄문에 하나 더해줬습니다. 아울러 해당 메소드가 '가장 처음에 나오는 글자'만 찾아주는거지 전체 검색이 아니기때문에 여러군데를 자르는지 여부는 모릅니다.
# 아직 저장기능은 없습니다. 지금 출력도 좀 중구난방이라 정리 좀 해야될듯.
# find로 나오는 위치의 경우 0부터 시작하기떄문에 하나 더해줬습니다. 아울러 해당 메소드가 '가장 처음에 나오는 글자'만 찾아주는거지 전체 검색이 아니기때문에 여러군데를 자르는지 여부는 모릅니다.
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
sequence_name = input("검색할 시퀀스의 이름을 입력해주세요: ")
sequence = input("검색할 시퀀스를 입력해주세요: ")
# 시퀀스 입력하는 란
def count_func (a,b):
    while a in b:
        global site_count
        loc = b.find(a)
        site_count += 1
        b = b[loc+len(a):]
    return site_count
# 이거 통으로 코드에 넣었더니 if 안에 있는데도 시퀀스 없으면 끝내더라...
# 몇 번 자르는지 세는 변수를 저기다 넣었더니 이상하게 돼서 결국 전역변수화 했습니다...
count = 0
with open('Result.txt_{0}-{1}-{2}_{3}_{4}'.format(year,month,day,filter,sequence_name),'w',encoding='utf-8') as f:
    f.write("Restriction enzyme which cuts this sequence: \n")
    for i in range(len(enzyme_table)):
        enzyme = enzyme_table['Enzyme'][i]
        feature = enzyme_table['cut_feature'][i]
        res_find = enzyme_table['sequence'][i]
        res_find = str(res_find)
        if res_find in sequence:
            site_count = 0
            count_func(res_find,sequence)
            count += 1
            f.write("{0}: {1} {2},{3} times cut.\n".format(enzyme,res_find,feature,site_count))
        else:
            count += 0
    f.write("Total: {0} enzymes cut input sequence".format(count))
    f.close()
# 여러분 드디어 저장기능이 추가되었습니다!!!
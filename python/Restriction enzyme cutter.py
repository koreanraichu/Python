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
# 이쪽은 컷수 세 주는 함수입니다. 
def cut_func (a,b):
    while a in b:
        global res_loc # find로 나오는 값
        global res_loc_list
        seq_length = len(sequence)
        loc = b.find(a)
        b = b[loc+len(a):]
        res_loc = len(sequence) - (len(b) + len(a)) + 1
        res_loc_list.append(str(res_loc)) # find로 나오는 위치 목록(slicing에 따른 보정 필요)
    return res_loc_list
# 여기가 위치 관련 함수입니다.

count = 0
count_nocut = 0
once_cut_list = []
two_cut_list = []
multi_cut_list = []
no_cut_list = []

with open('Result.txt_{0}-{1}-{2}_{3}_{4}'.format(year,month,day,filter,sequence_name),'w',encoding='utf-8') as f:
    f.write("Restriction enzyme which cuts this sequence: \n")
    for i in range(len(enzyme_table)):
        enzyme = enzyme_table['Enzyme'][i]
        feature = enzyme_table['cut_feature'][i]
        res_find = enzyme_table['sequence'][i]
        res_find = str(res_find)
        if res_find in sequence:
            site_count = 0
            res_loc = 0
            res_loc_list = []
            count_func(res_find,sequence)
            cut_func(res_find,sequence)
            count += 1
            count_nocut += 0
            if site_count == 1:
                once_cut_list.append(enzyme)
            elif site_count == 2: 
                two_cut_list.append(enzyme)
            else: 
                multi_cut_list.append(enzyme)
            res_loc_list = ', '.join(res_loc_list)
            f.write("{0}: {1} {2},{3} times cut. Where(bp): {4} \n".format(enzyme,res_find,feature,site_count,res_loc_list))
        else: 
            count += 0
            count_nocut += 1
            no_cut_list.append(enzyme)
    once_cut_list = ', '.join(once_cut_list)
    two_cut_list = ', '.join(two_cut_list)
    multi_cut_list = ', '.join(multi_cut_list)
    no_cut_list = ', '.join(no_cut_list)
    # 출력부
    f.write("Total: {0} enzymes cut input sequence, {1} enzymes never cut this sequence. \n".format(count,count_nocut))
    f.write("Enzymes no cut this sequence: {0} \n".format(no_cut_list))
    f.write("Enzymes cut this sequence once: {0} \n".format(once_cut_list))
    f.write("Enzymes cut this sequence twice: {0} \n".format(two_cut_list))
    f.write("Enzymes cut this sequence multiple: {0} \n".format(multi_cut_list))
    f.close()
# 컷수도 세주고 자르는 효소랑 안 자르는 효소도 목록으로 쫘라락... 
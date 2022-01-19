import pandas as pd
import re
# 가라! 판다스! 
from datetime import datetime
# 오늘 날짜 가져오는 모듈

enzyme_table = pd.read_csv('/home/koreanraichu/restriction.csv')
enzyme_table2 = pd.read_csv('/home/koreanraichu/restriction_RE.csv')
# 정규식 도입을 위해... 어쩔 수 없이 합쳤음... 
enzyme_table = pd.concat([enzyme_table,enzyme_table2])
enzyme_table = enzyme_table.sort_values('Enzyme')
enzyme_table.reset_index(inplace=True)
# 합쳤다... 드디어 합쳤습니다 여러분... 

year = datetime.today().year
month = datetime.today().month
day = datetime.today().day
# 파일 저장할 때 필요한 변수입니다. (코드 돌린 시점의 날짜 및 시간)

enzyme = input('시퀀스를 찾을 제한효소를 입력해주세요: ').strip()
sequence_name = input('Sequence 이름을 입력해주세요: ').strip()
sequence = input('제한효소 site를 찾을 시퀀스를 입력해주세요: ').upper().strip()
# 제한효소 이름 토씨 하나 안 틀리고 입력해야 합니다.

class RE_treatment:
    def RE_wildcard(self,before_seq):
        self.before_seq = before_seq
        before_seq = before_seq.replace("N",".")
        return before_seq
    # Wildcard: 시퀀스 데이터에 N이 있을 경우 Wildcard로 바꾼다. 
    def RE_or(self,before_seq):
        self.before_seq = before_seq
        if "B" in before_seq:
            before_seq = before_seq.replace("B","[CGT]")
        elif "D" in before_seq:
            before_seq = before_seq.replace("D","[AGT]")
        elif "H" in before_seq:
            before_seq = before_seq.replace("H","[ACT]")
        elif "K" in before_seq:
            before_seq = before_seq.replace("K","[GT]")
        elif "M" in before_seq:
            before_seq = before_seq.replace("M","[AC]")
        elif "R" in before_seq:
            before_seq = before_seq.replace("R","[AG]")
        elif "S" in before_seq:
            before_seq = before_seq.replace("S","[CG]")
        elif "V" in before_seq:
            before_seq = before_seq.replace("V","[ACG]")
        elif "W" in before_seq:
            before_seq = before_seq.replace("W","[AT]")
        elif "Y" in before_seq:
            before_seq = before_seq.replace("Y","[CT]")
        return before_seq
    # Or: 시퀀스 데이터에 N 말고 ATGC 말고 다른 알파벳이 있을 경우, 해당하는 정규식 문법으로 바꾼다. 

def cut_func (a,b):
    global res_loc_list
    locs = re.finditer(a,b)
    for i in locs:
        loc = i.start()
        res_loc_list.append(str(loc+1))
    return res_loc_list
# 여기가 위치 관련 함수입니다.
def convert (a):
    RE = RE_treatment()
    if "N" in res_find:
        res_find_after = RE.RE_wildcard(res_find)
    elif "B" in res_find or "D" in res_find or "H" in res_find or "K" in res_find or "M" in res_find or "R" in res_find or "S" in res_find or "V" in res_find or "W" in res_find or "Y" in res_find: 
        res_find_after = RE.RE_or(res_find)
    return res_find_after
# 함수가 대체 몇 개야...!!!
# 저 or 진짜 무식하게 다 때려박았음... 줄일 방법 제보 받아요... 

res_find = enzyme_table.sequence[(enzyme_table['Enzyme'] == enzyme)]
res_find = res_find.to_string(index=False)
res_find = res_find.upper()
res_find = str(res_find)
# 인식 시퀀스 처리
while True:
    if "N" in res_find: 
        res_find = str(convert(res_find))
        print(res_find)
    elif "B" in res_find or "D" in res_find or "H" in res_find or "K" in res_find or "M" in res_find or "R" in res_find or "S" in res_find:
        res_find = str(convert(res_find))
        print(res_find)
    else: 
        break
# 정규식 처리
res_site = enzyme_table.restriction_site[(enzyme_table['Enzyme'] == enzyme)]
res_site = res_site.to_string(index=False)
res_site = res_site.upper()
res_site = str(res_site)
# 자르는 시퀀스 처리
cut_feature = enzyme_table.cut_feature[(enzyme_table['Enzyme'] == enzyme)]
cut_feature = cut_feature.to_string(index=False)
cut_feature = str(cut_feature)
# blunt or sticky(나중에 저장 기능 추가할 때 넣을 예정입니다)

with open ('Result_{0}-{1}-{2}_{3}-{4}.txt'.format(year,month,day,enzyme,sequence_name),'w',encoding='utf-8') as f: 
    Findall = re.findall(res_find,sequence)
    if Findall:
        site_count = 0
        res_loc = 0
        res_loc_list = []
        cut_location = cut_func(res_find,sequence)
        cut_count = len(Findall)
        if len(set(Findall)) > 1:
            for i in Findall:
                if i in sequence:
                    sequence = sequence.replace(i,"-"+i+"-")
        else: 
            sequence = sequence.replace(res_find,res_site)
        res_loc_list = ', '.join(res_loc_list)
        f.write("{0} | {1} | {2} | {3} times cut\n".format(enzyme,res_site,cut_feature,cut_count))
        f.write("Cut location(bp): {0} \n".format(res_loc_list))
        f.write('Sequence name: {0} \n{1}'.format(sequence_name,sequence))
        f.close()
        # DB에 효소가 있고 일치하는 시퀀스가 있을 때
    elif not Findall:  
        print("No restriction site in this sequence. ")
        f.write("{0} | {1} | {2} | 0 times cut\n".format(enzyme,res_site,cut_feature))
        f.write('Sequence name: {0} \n'.format(sequence_name))
        f.write("This restricion enzyme never cut this sequence. ")
        f.close()
        # DB에 효소가 있으나 일치하는 시퀀스가 없을 때
    else:
        print("No data in database. ")
        f.write("{0} \n".format(enzyme))
        f.write("This restriction enzyme not entried in database. ")
        f.close()
        # DB에 효소가 없을 때

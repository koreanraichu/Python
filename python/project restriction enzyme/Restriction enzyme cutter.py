import pandas as pd
import re
from datetime import datetime
from argparse import FileType
import tkinter
from tkinter import filedialog
from Bio import SeqIO
import os
# 정신사나워서 불러오는거랑 표 분리했습니다...OTL 

enzyme_table = pd.read_csv('/home/koreanraichu/restriction_merge.csv')
# 통합 DB 모셔왔습니다 선생님. 

year = datetime.today().year
month = datetime.today().month
day = datetime.today().day
# 이쪽은 파일 저장을 위해 현재 날짜 데이터를 추출하는 코드라 크게 수정할 부분은 없습니다. 

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

filter = input("sticky로 자르는 제한효소만 보고 싶으면 sticky, blunt로 자르는 제한효소만 보고 싶으면 blunt를 입력해주세요. ")
# sticky: sticky end만 
# blunt: blunt end만 
# 암것도 안 쓰면 다 봅니다. filter에 따라 테이블 형태가 달라집니다. 
# 소문자로 입력해주세요, 대소문자 변환 기능은 제공하지 않습니다.

cut_filter = input("Sticky로 자르는 제한효소만 보고 싶으면 sticky, Blunt로 자르는 제한효소만 보고 싶으면 blunt, Nicked로 자르는 제한효소만 보고 싶으면 nicked를 입력해주세요. ")
cut_filter = cut_filter.capitalize()
# Cut feature에 대한 코드. DNA가 Double strand일 때 Nicked는 한 쪽만 달랑달랑하게 자릅니다. 
# 그러니까 대충 해리포터 시리즈에 나오는 목이 달랑달랑한 닉같이 DNA가 달랑달랑한거죠. 
if cut_filter == 'Sticky':
    enzyme_table = enzyme_table[enzyme_table['cut_feature']== 'Sticky']
    enzyme_table.reset_index(inplace=True)
elif cut_filter == 'Blunt':
    enzyme_table = enzyme_table[enzyme_table['cut_feature']== 'Blunt']
    enzyme_table.reset_index(inplace=True)
elif cut_filter == 'Nicked':
    enzyme_table = enzyme_table[enzyme_table['cut_feature']== 'Nicked']
    enzyme_table.reset_index(inplace=True)
else: 
    cut_filter = "All feature"
    pass

NEB_filter = input("혹시 NEB에서 취급하는 효소들만 보실거라면 NEB를 입력해주세요. ")
NEB_filter = NEB_filter.upper()
# NEB cutter에서 기본적으로 시퀀스 입력하면 나오는 효소들만 보여줍니다. (NEB에서 파는 애들만)
if NEB_filter == "NEB":
    enzyme_table = enzyme_table[enzyme_table['NEB_sell']== 'Yes']
    enzyme_table.reset_index(inplace=True)
else: 
    NEB_filter = "All"
    pass
# Notes: 둘 다 선택 안 할 수도 있습니다. (해봤음)

FASTA_open = input('FASTA 파일을 불러오시겠습니까? 불러오실거면 FASTA 혹은 fasta를 임력해주세요. ').upper()
if FASTA_open == 'FASTA':
    root = tkinter.Tk()
    root.withdraw()
    dir_path = filedialog.askopenfilename(parent=root,initialdir="/home/koreanraichu",title='Please select a directory',filetypes = (("*.fasta","*fasta"),("*.faa","*faa")))
    try: 
        fasta_read = SeqIO.read(dir_path,'fasta')
        sequence_name = fasta_read.id
        sequence = str(fasta_read.seq)
        sequence = sequence.upper()
        # 단식으로만 가져오게 함. 
        print(dir_path,'FASTA 파일에 있는 레코드를 가져왔습니다! ')
    except: 
        records = SeqIO.parse(dir_path,'fasta')
        first_record = next(records)
        sequence_name = first_record.id
        sequence = str(first_record.seq)
        sequence = sequence.upper()
        print('이 FASTA파일은 한 파일에 여러 개가 기록되어 있습니다. 맨 위에 있는 데이터로 진행하겠습니다. ')
        # parse로 가져와야 하는 파일의 경우 맨 위 레코드 하나를 가져온다. 
        # read랑 parse는 FASTA 파일에 >가 하나인가 여러개인가 여부로 나뉩니다. 
else: 
    sequence_name = input("검색할 시퀀스의 이름을 입력해주세요: ")
    sequence = input("검색할 시퀀스를 입력해주세요: ")
    # 시퀀스 입력하는 란

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

count = 0
count_nocut = 0
once_cut_list = []
two_cut_list = []
multi_cut_list = []
no_cut_list = []
# 변수와 리스트(크게 건들 일 없음)

with open('Result.txt_{0}-{1}-{2}_{3}'.format(year,month,day,sequence_name),'w',encoding='utf-8') as f:
    f.write("Filter selected: {0} | {1} \nRestriction enzyme which cuts this sequence: \n".format(cut_filter,NEB_filter))
    for i in range(len(enzyme_table)):
        enzyme = enzyme_table['Enzyme'][i]
        feature = enzyme_table['cut_feature'][i]
        res_find = enzyme_table['sequence'][i]
        res_find = str(res_find)
        res_find_before = str(res_find)
        while True:
            if "N" in res_find: 
                res_find = str(convert(res_find))
            elif "B" in res_find or "D" in res_find or "H" in res_find or "K" in res_find or "M" in res_find or "R" in res_find or "S" in res_find:
                res_find = str(convert(res_find))
            else: 
                break
        # 정규식 처리
        Findall = re.findall(res_find,sequence)
        res_loc_list = []
        if Findall: 
            count += 1
            site_count = len(Findall)
            cut_func(res_find,sequence)
            if site_count == 1:
                once_cut_list.append(enzyme)
            elif site_count == 2: 
                two_cut_list.append(enzyme)
            else: 
                multi_cut_list.append(enzyme)
            res_loc_list = ', '.join(res_loc_list)
            f.write("Enzyme: {0} | Sequence: {1} | Cut feature: {2} | {3} times cut | Where(bp): {4} \n".format(enzyme,res_find_before,feature,site_count,res_loc_list))
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
    directory = os.getcwd()
    print("파일이 {0}에 저장되었습니다. ".format(directory))
# 컷수도 세주고 자르는 효소랑 안 자르는 효소도 목록으로 쫘라락...
import pandas as pd
import re
# 가라! 판다스! 
from datetime import datetime
# 오늘 날짜 가져오는 모듈
from argparse import FileType
import tkinter
from tkinter import filedialog
from Bio import SeqIO
# FASTA 파일 처리 관련 모듈
import os
# 경로 관련 모듈

enzyme_table = pd.read_csv('/home/koreanraichu/restriction_merge.csv')
# 통합 DB 모셔왔습니다 선생님. 

year = datetime.today().year
month = datetime.today().month
day = datetime.today().day
# 파일 저장할 때 필요한 변수입니다. (코드 돌린 시점의 날짜 및 시간)

NEB_filter = input("혹시 NEB에서 취급하는 효소들만 보실거라면 NEB를 입력해주세요. ")
NEB_filter = NEB_filter.upper()
# NEB cutter에서 기본적으로 시퀀스 입력하면 나오는 효소들만 보여줍니다. (NEB에서 파는 애들만)
if NEB_filter == "NEB":
    enzyme_table = enzyme_table[enzyme_table['NEB_sell']== 'Yes']
    enzyme_table.reset_index(inplace=True)
else: 
    NEB_filter = "All"
    pass

enzyme = input('시퀀스를 찾을 제한효소를 입력해주세요: ').strip()
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
        print('{0} 파일에 있는 레코드를 가져왔습니다! '.format(dir_path))
    except: 
        records = SeqIO.parse(dir_path,'fasta')
        first_record = next(records)
        sequence_name = first_record.id
        sequence = str(first_record.seq)
        sequence = sequence.upper()
        print('{0} 파일을 불러왔습니다. 이 파일은 한 파일에 여러 개가 기록되어 있습니다. 맨 위에 있는 데이터로 진행하겠습니다. '.format(dir_path))
        # parse로 가져와야 하는 파일의 경우 맨 위 레코드 하나를 가져온다. 
        # read랑 parse는 FASTA 파일에 >가 하나인가 여러개인가 여부로 나뉩니다. 
else: 
    sequence_name = input("검색할 시퀀스의 이름을 입력해주세요: ")
    sequence = input("검색할 시퀀스를 입력해주세요: ")
    # 시퀀스 입력하는 란

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
    elif "B" in res_find or "D" in res_find or "H" in res_find or "K" in res_find or "M" in res_find or "R" in res_find or "S" in res_find:
        res_find = str(convert(res_find))
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
        f.write("{0} | {1} | {2} | {3} times cut \n".format(enzyme,res_site,cut_feature,cut_count))
        f.write("Cut location(bp): {0} \n".format(res_loc_list))
        f.write('Sequence name: {0} | Sequence length: {1}bp \n{2}'.format(sequence_name,len(sequence),sequence))
        f.close()
        directory = os.getcwd()
        print('Your result saved by Result_{0}-{1}-{2}_{3}-{4}.txt, where {5}. '.format(year,month,day,enzyme,sequence_name,directory))
        # DB에 효소가 있고 일치하는 시퀀스가 있을 때
    elif not Findall:  
        print("No restriction site in this sequence. ")
        f.write("{0} | {1} | {2} | 0 times cut \n".format(enzyme,res_site,cut_feature))
        f.write('Sequence name: {0} | Sequence length: {1}bp \n{2}'.format(sequence_name,len(sequence),sequence))
        f.write("This restricion enzyme no cut this sequence. ")
        f.close()
        directory = os.getcwd()
        print('Your result saved by Result_{0}-{1}-{2}_{3}-{4}.txt, where {5}. '.format(year,month,day,enzyme,sequence_name,directory))
        # DB에 효소가 있으나 일치하는 시퀀스가 없을 때
    else:
        print("No data in database. ")
        f.write("{0} \n".format(enzyme))
        f.write("This restriction enzyme not entried in database. ")
        f.close()
        # DB에 효소가 없을 때
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
import platform
# 경로 관련 모듈

enzyme_table = pd.read_csv('/home/koreanraichu/restriction_merge.csv')
# 통합 DB 모셔왔습니다 선생님. 

year = datetime.today().year
month = datetime.today().month
day = datetime.today().day
# 파일 저장할 때 필요한 변수입니다. (코드 돌린 시점의 날짜 및 시간)

# 코드 개편이 있었습니다. 원래는 줄줄이 나열했었는데 제미나이의 도움으로... 

class RE_treatment(): 
    # A, T, G, C 외의 다른 알파벳들을 전부 와일드카드로 변환
    CODE_TO_REGEX= {
        "N":".", "B": "[CGT]", "D": "[AGT]", "H": "[ACT]", "K": "[GT]", 
        "M": "[AC]", "R": "[AG]", "S": "[CG]", "V": "[ACG]", 
        "W": "[AT]", "Y": "[CT]"
    }
    def RE_treatment_all(self, before_seq):
        # 이제 제한효소 시퀀스에 A, T, G, C 외에 다른 게 있으면 저기서 찾아서 변환하면 됩니다. 
        # 그리고 그 일을 얘가 할거예요. 
        def replacer(match):
            return self.CODE_TO_REGEX[match.group(0)]
        pattern = "[" + "".join(self.CODE_TO_REGEX.keys()) + "]" # 위에 있는 딕셔너리에서 갖다가
        
        return re.sub(pattern, replacer, before_seq) # 변환합니다. 
# 여기까지가 클래스입니다 

OS = platform.platform()
if 'Linux' in OS:
    default_dir = '/'
elif 'Darwin' in OS or 'macOS' in OS:
    default_dir = '/Users'
else: 
    default_dir = 'C:\\'
# If: 리눅스/elif: 맥/else: 기타(한 9할은 윈도우)

enzyme = input('시퀀스를 찾을 제한효소를 입력해주세요: ').strip()
FILE_open = input('FASTA 파일을 불러오시겠습니까? 불러오실거면 FASTA를 임력해주세요. Genbank 파일을 불러오실거면 Genbank를 입력해주세요. ').upper()
if FILE_open == 'FASTA':
    root = tkinter.Tk()
    root.withdraw()
    dir_path = filedialog.askopenfilename(parent=root,initialdir=default_dir,title='Please select a directory',filetypes = (("*.fasta","*fasta"),("*.faa","*faa")))
    try: 
        fasta_read = SeqIO.read(dir_path,'fasta')
        sequence_name = fasta_read.id
        sequence_description = fasta_read.description
        sequence = str(fasta_read.seq)
        sequence = sequence.upper()
        # 단식으로만 가져오게 함. 
        print('{0} 파일에 있는 레코드를 가져왔습니다! '.format(dir_path))
    except: 
        records = SeqIO.parse(dir_path,'fasta')
        first_record = next(records)
        sequence_name = first_record.id
        sequence_description = first_record.description
        sequence = str(first_record.seq)
        sequence = sequence.upper()
        print('{0} 파일을 불러왔습니다. 이 파일은 한 파일에 여러 개가 기록되어 있습니다. 맨 위에 있는 데이터로 진행하겠습니다. '.format(dir_path))
        # parse로 가져와야 하는 파일의 경우 맨 위 레코드 하나를 가져온다. 
        # read랑 parse는 FASTA 파일에 >가 하나인가 여러개인가 여부로 나뉩니다. 
elif FILE_open == "GENBANK":
    root = tkinter.Tk()
    root.withdraw()
    dir_path = filedialog.askopenfilename(parent=root,initialdir=default_dir,title='Please select a directory',filetypes = (("*.gb","*gb"),("*.gbk","*gbk")))
    try: 
        genbank_read = SeqIO.read(dir_path,'genbank')
        sequence_name = genbank_read.id
        sequence_description = genbank_read.description
        sequence = str(genbank_read.seq)
        sequence = sequence.upper()
        print('{0} 파일에 있는 레코드를 가져왔습니다! '.format(dir_path))
    except:
        genbank_read = SeqIO.parse(dir_path,'genbank')
        sequence_name = genbank_read.id
        sequence_description = genbank_read.description
        sequence = str(genbank_read.seq)
        sequence = sequence.upper()
        print('{0} 파일에 있는 레코드를 가져왔습니다! '.format(dir_path))
else: 
    sequence_name = input("검색할 시퀀스의 이름을 입력해주세요: ")
    sequence = input("검색할 시퀀스를 입력해주세요: ")
    sequence_description = "Directed input sequence"
    # 시퀀스 입력하는 란

def cut_func (a,b):
    global res_loc_list
    locs = re.finditer(a,b)
    for i in locs:
        loc = i.start()
        res_loc_list.append(str(loc+1))
    return res_loc_list
# 여기가 위치 관련 함수입니다.

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

root = tkinter.Tk()
root.withdraw()
save_path = filedialog.askdirectory()

# 파일명 관련 구역
output_filename = 'Result_{0}-{1}-{2}_{3}'.format(year,month,day,sequence_name)
full_filepath = os.path.join(save_path, output_filename)

with open (full_filepath,'w',encoding='utf-8') as f: 
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
        f.write("=====Restriction enzyme information=====\n{0} | {1} | {2} | {3} times cut \n".format(enzyme,res_site,cut_feature,cut_count))
        f.write("Cut location(bp): {0} \n".format(res_loc_list))
        f.write('=====Sequence information=====\nSequence name: {0} | Sequence length: {1}bp \nSequence descriiption: {2}\n{3}'.format(sequence_name,len(sequence),sequence_description,sequence))
        f.close()
        directory = save_path
        print("파일이 {0}에 저장되었습니다. ".format(full_filepath))
        # DB에 효소가 있고 일치하는 시퀀스가 있을 때
    elif not Findall:  
        print("No restriction site in this sequence. ")
        f.write("=====Restriction enzyme information=====\n{0} | {1} | {2} | 0 times cut \n".format(enzyme,res_site,cut_feature))
        f.write("This restricion enzyme no cut this sequence. \n")
        f.write('=====Sequence information=====\nSequence name: {0} | Sequence length: {1}bp \nSequence description: {2}\n{3}'.format(sequence_name,len(sequence),sequence_description,sequence))
        f.close()
        directory = save_path
        print("파일이 {0}에 저장되었습니다. ".format(full_filepath))
        # DB에 효소가 있으나 일치하는 시퀀스가 없을 때
    else:
        print("No data in database. ")
        f.write("{0} \n".format(enzyme))
        f.write("This restriction enzyme not entried in database. ")
        f.close()
        # DB에 효소가 없을 때

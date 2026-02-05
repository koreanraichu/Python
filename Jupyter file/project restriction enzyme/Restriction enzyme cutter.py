import pandas as pd
import re
from datetime import datetime
from argparse import FileType
import tkinter
from tkinter import filedialog
from Bio import SeqIO
import os
import platform
# 정신사나워서 불러오는거랑 표 분리했습니다...OTL 

enzyme_table = pd.read_csv('/home/koreanraichu/restriction_merge.csv')
# 통합 DB 모셔왔습니다 선생님. 

year = datetime.today().year
month = datetime.today().month
day = datetime.today().day
# 이쪽은 파일 저장을 위해 현재 날짜 데이터를 추출하는 코드라 크게 수정할 부분은 없습니다. 

OS = platform.platform()
if 'Linux' in OS:
    default_dir = '/'
elif 'Darwin' in OS or 'macOS' in OS:
    default_dir = '/Users'
else: 
    default_dir = 'C:\\'
# Mac은 뭐라고 뜨는지 몰라서 선택지에 없었는데 제미나이가 알려주더군요. (이거 만들 때 제미나이 없었음)

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

root = tkinter.Tk()
root.withdraw()
save_path = filedialog.askdirectory()

count = 0
count_nocut = 0
once_cut_list = []
two_cut_list = []
multi_cut_list = []
no_cut_list = []
# 변수와 리스트(크게 건들 일 없음)

# 파일명 관련 구역
output_filename = 'Result_{0}-{1}-{2}_{3}'.format(year,month,day,sequence_name)
full_filepath = os.path.join(save_path, output_filename)
# 이쪽은 크게 건드릴 일 없습니다. 

with open(full_filepath,'w',encoding='utf-8') as f:
    f.write("=====Sequence information=====\nSequence name: {0} | Sequence length: {1}bp \nSequence description: {2}\n".format(sequence_name,len(sequence),sequence_description))
    f.write("=====Running information======\nFilter selected: {0} | {1} \nRestriction enzyme which cuts this sequence: \n".format(cut_filter,NEB_filter))
    f.write("=====Result=====\n")
# 3. 파일 저장 이슈때문에... 아니 그거 아니더라도 일단 안 돌아갈 수 있으니까 예외처리 추가... 
    try:
        for i in range(len(enzyme_table)):
            treatment = RE_treatment()
            enzyme = enzyme_table['Enzyme'][i]
            feature = enzyme_table['cut_feature'][i]
            res_find_before = str(enzyme_table['sequence'][i])

            # 변환 로직 (이전에 개선된 treatment.RE_treatment_all 사용)
            res_find_after = treatment.RE_treatment_all(res_find_before)
            
            Findall = re.findall(res_find_after, sequence)
            site_count = len(Findall)
            res_loc_list = []
            
            if Findall:
                # 얘도 저장 이슈때문에 추가한건데 프로그레스 보이고 좋네요 ㅋㅋ 
                print(f"DEBUG: Processing cutting enzyme {enzyme}")
                
                # cut_func 호출
                cut_func(res_find_after,sequence) 
                
                # ... (나머지 리스트 추가 및 파일 쓰기 로직) ...

                res_loc_list = ', '.join(res_loc_list)
                f.write("Enzyme: {0} | Sequence: {1} | Cut feature: {2} | {3} times cut \nWhere(bp): {4} \n".format(enzyme,res_find_before,feature,site_count,res_loc_list))
            
            else:
                # ... (no_cut_list 추가 로직) ...
                no_cut_list.append(enzyme)
                print(f"DEBUG: Enzyme {enzyme} not found.")
                
    # 예외처리하다가 오류가 나면 FATAL ERROR가 보이게 될 거예요. 
    except Exception as e:
        print(f"\nFATAL ERROR during enzyme loop: {e}")
        # 오류가 발생했음을 파일에도 기록
        f.write(f"\n--- ERROR OCCURRED DURING ANALYSIS LOOP ---\nError: {e}\n--- Partial results saved ---\n")

    # 최종 출력부 (try/except 블록이 끝난 후, with open 블록 안에서 실행)
    total_cut = len(once_cut_list) + len(two_cut_list) + len(multi_cut_list)
    total_nocut = len(no_cut_list)
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
    directory = save_path
    print("파일이 {0}에 저장되었습니다. ".format(full_filepath))
# 컷수도 세주고 자르는 효소랑 안 자르는 효소도 목록으로 쫘라락...

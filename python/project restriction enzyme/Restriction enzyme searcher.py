import pandas as pd # 가라 판다스!!! 
import re # 정규식용 모듈
enzyme_table = pd.read_csv('/home/koreanraichu/restriction_merge.csv')
# 통합 DB 모셔왔습니다 선생님. 

def SeqtoString (a):
    a = enzyme_table.sequence[(enzyme_table['Enzyme'] == enzyme)]
    a = a.to_string(index = False)
    a = str(a).strip()
    return a
def SitetoString (a):
    a = enzyme_table.restriction_site[(enzyme_table['Enzyme'] == enzyme)]
    a = a.to_string(index = False)
    a = str(a).strip()
    return a
def NEB_selling (a):
    a = enzyme_table.NEB_sell[(enzyme_table['Enzyme'] == enzyme)]
    a = a.to_string(index = False)
    a = str(a).strip()
    return a
# 함수 가즈아!!! 

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
    print(enzyme_table)
    pass

keyword = input("효소 이름으로 찾으실거면 enzyme을, restriction site sequence로 찾으실거면 sequence를 입력해주세요. 혹시 찾고자 하는 효소 이름이 명확하지 않으시다면 name을 입력해주세요. ")
if keyword == "enzyme":
    enzyme = input("찾고자 하는 효소를 입력해주세요: ")
elif keyword == "sequence":
    seq = input("찾고자 하는 restriction site sequence를 입력해주세요: ")
elif keyword == "name":
    enzyme_RE = input("효소의 이름이 뭘로 시작하나요? ")
    enzyme_RE = enzyme_RE.upper()
    enzyme_RE_2 = '^' + enzyme_RE
    # 정규식에서 ~로 시작하는 걸 찾을때는 ^를 씁니다. 
else: 
    print("다시 입력해주세요. ")
# 효소 이름으로 찾느냐, 시퀀스로 찾느냐에 따라 검색 결과가 다릅니다. 

print("Filter selected: {0}".format(cut_filter))
print("How to read: Name | Sequence | Cut | Selling in NEB?\n")
# filter 정보는 로직과 상관없이 출력됩니다. 
if keyword == "enzyme":
    find_seq = SeqtoString(enzyme)
    Site_seq = SitetoString(enzyme)
    NEB_sell = NEB_selling(enzyme)
    Iso = []
    Neo = []
    print("{0} | {1} | {2} | {3} | Input enzyme".format(enzyme,find_seq,Site_seq,NEB_sell))
    for i in range(len(enzyme_table)):
        DB_enzyme = str(enzyme_table['Enzyme'][i]).strip()
        DB_seq = str(enzyme_table['sequence'][i]).strip().upper()
        DB_site = str(enzyme_table['restriction_site'][i]).strip().upper()
        DB_NEB = str(enzyme_table['NEB_sell']).strip()
        if find_seq == str(DB_seq) and DB_enzyme != enzyme:
            if Site_seq == DB_site:
                Iso.append(DB_enzyme)
                print("{0} | {1} | {2} | {3} | Isoschizomer".format(DB_enzyme,DB_seq,DB_site,DB_NEB))
                # 인식하는 시퀀스와 자르는 방식이 같은 제한효소
            elif Site_seq != DB_site: 
                Neo.append(DB_enzyme)
                print("{0} | {1} | {2} | {3} | Neoschizomer".format(DB_enzyme,DB_seq,DB_site,DB_NEB))
                # 인식하는 시퀀스는 같으나 자르는 방식이 다른 제한효소
        elif find_seq == str(DB_seq) and DB_enzyme == enzyme:
            pass
        else: 
            pass
# 여기까지는 효소 이름으로 검색할 때의 코드
elif keyword == "sequence": 
    find_seq = seq
    print("Searched by: {0}".format(seq))
    for i in range(len(enzyme_table)):
        DB_enzyme = str(enzyme_table['Enzyme'][i]).strip()
        DB_seq = str(enzyme_table['sequence'][i]).strip().upper()
        DB_site = str(enzyme_table['restriction_site'][i]).strip().upper()
        DB_NEB = str(str(enzyme_table['NEB_sell'][i]).strip())
        if find_seq == DB_seq:
            print("{0} | {1} | {2} | {3}".format(DB_enzyme,DB_seq,DB_site,DB_NEB))
        else:
            pass
# 여기까지는 인식 시퀀스로 검색할 때의 코드
else: 
    print("Enzyme with start with {0}".format(enzyme_RE))
    for i in range(len(enzyme_table)):
        DB_enzyme = str(enzyme_table['Enzyme'][i]).strip()
        DB_seq = str(enzyme_table['sequence'][i]).strip().upper()
        DB_site = str(enzyme_table['restriction_site'][i]).strip().upper()
        DB_NEB = str(str(enzyme_table['NEB_sell'][i]).strip())
        if re.search(enzyme_RE_2,DB_enzyme):
            print("{0} | {1} | {2} | {3}".format(DB_enzyme,DB_seq,DB_site,DB_NEB))
# 간단 검색(머릿글자)
# 참고로 테스트 결과 정규식 문법이 먹혔습니다... 어째서냐... 
if keyword == "enzyme":
    if Iso == []:
        Iso.append("No data")
    elif Neo == []:
        Neo.append("No data")
    else: 
        pass
    Iso = ', '.join(Iso)
    Neo = ', '.join(Neo)
    print("\nIsoschizomer: {0} \nNeoschizomer: {1}".format(Iso,Neo))
    # 실제로 Isoschizomer인데도 Neoscizomer로 표기하는 문제가 있습니다. (BamHI-Nsp29132OO)
    # DB 수정하니까 해결되는건 뭔 경우냐... 
else: 
    pass
# 시퀀스로 검색하셨거나 정규식 검색을 사용하셨으면 이 부분은 넘어갑니다. 
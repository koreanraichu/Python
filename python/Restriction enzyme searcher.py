import pandas as pd
enzyme_table = pd.read_csv('/home/koreanraichu/restriction.csv')
# 이쪽은 Finder나 cutter에도 쓰이는 그 DB가 맞습니다. 
enzyme_table2 = pd.read_csv('/home/koreanraichu/restriction_RE.csv')
# 이쪽은 restriction site나 cut site에 A,T,G,C가 아닌 다른 알파벳이 들어가기 때문에 여기서 처음 불러오는 DB입니다. 
enzyme_table = pd.concat([enzyme_table,enzyme_table2])
enzyme_table = enzyme_table.sort_values('Enzyme')
enzyme_table.reset_index(inplace=True)
# 니네는 꼭 합치고 나면 인덱스도 바꿔줘야되더라... 

filter = input("sticky로 자르는 제한효소만 보고 싶으면 sticky, blunt로 자르는 제한효소만 보고 싶으면 blunt를 입력해주세요. ")
# sticky: sticky end만 
# blunt: blunt end만 
# 입력 안 하면 적용 안됩니다. 
if filter == 'sticky':
    enzyme_table = enzyme_table[enzyme_table['cut_feature']== 'sticky']
    enzyme_table.reset_index(inplace=True)
elif filter == 'blunt':
    enzyme_table = enzyme_table[enzyme_table['cut_feature']== 'blunt']
    enzyme_table.reset_index(inplace=True)
else: 
    filter = "No Filter"
    pass
# 딱히 있어야 하는 기능인지는 모르겠지만, 있으면 좋잖아요? 

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
# 함수 가즈아!!! 

keyword = input("효소 이름으로 찾으실거면 enzyme을, restriction site sequence로 찾으실거면 sequence를 입력해주세요. ")
if keyword == "enzyme":
    enzyme = input("찾고자 하는 효소를 입력해주세요: ")
elif keyword == "sequence":
    seq = input("찾고자 하는 restriction site sequence를 입력해주세요: ")
else: 
    print("다시 입력해주세요. ")
# 효소 이름으로 찾느냐, 시퀀스로 찾느냐에 따라 검색 결과가 조금 다릅니다. (로직도 다름)

print("Filter selected: {0}".format(filter))
# filter 선택 여부는 로직과 상관없이 출력됩니다. 
if keyword == "enzyme":
    find_seq = SeqtoString(enzyme)
    Site_seq = SitetoString(enzyme)
    Iso = []
    Neo = []
    print("{0} | {1} | {2} | Input enzyme".format(enzyme,find_seq,Site_seq))
    for i in range(len(enzyme_table)):
        DB_enzyme = str(enzyme_table['Enzyme'][i]).strip()
        DB_seq = str(enzyme_table['sequence'][i]).strip().upper()
        DB_site = str(enzyme_table['restriction_site'][i]).strip().upper()
        if find_seq == str(DB_seq) and DB_enzyme != enzyme:
            if Site_seq == DB_site:
                Iso.append(DB_enzyme)
                print("{0} | {1} | {2} | Isoschizomer".format(DB_enzyme,DB_seq,DB_site))
                # 인식하는 시퀀스와 자르는 방식이 같은 제한효소
            elif Site_seq != DB_site: 
                Neo.append(DB_enzyme)
                print("{0} | {1} | {2} | Neoschizomer".format(DB_enzyme,DB_seq,DB_site))
                # 인식하는 시퀀스는 같으나 자르는 방식이 다른 제한효소
        elif find_seq == str(DB_seq) and DB_enzyme == enzyme:
            pass
        else: 
            pass
# 여기까지는 효소 이름으로 검색할 때의 코드
else: 
    find_seq = seq
    print("Searched by: {0}".format(seq))
    for i in range(len(enzyme_table)):
        DB_enzyme = str(enzyme_table['Enzyme'][i]).strip()
        DB_seq = str(enzyme_table['sequence'][i]).strip().upper()
        DB_site = str(enzyme_table['restriction_site'][i]).strip().upper()
        if find_seq == DB_seq:
            print("{0} | {1} | {2}".format(DB_enzyme,DB_seq,DB_site))
        else:
            pass
# 여기까지는 인식 시퀀스로 검색할 때의 코드

if keyword == "enzyme":
    if Iso == []:
        Iso.append("No data")
    elif Neo == []:
        Neo.append("No data")
    else: 
        pass
    Iso = ', '.join(Iso)
    Neo = ', '.join(Neo)
    print("Isoschizomer: {0} \nNeoschizomer: {1}".format(Iso,Neo))
    # 실제로 Isoschizomer인데도 Neoscizomer로 표기하는 문제가 있습니다. (BamHI-Nsp29132OO)
else: 
    pass
# 시퀀스로 검색하셨으면 이 부분은 넘어갑니다. 
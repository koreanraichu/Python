import pandas as pd
from datetime import datetime
# 모듈은 위쪽으로 모셔드리는 친절함!

enzyme_table = pd.read_csv('/home/koreanraichu/restriction.csv') # 일단 자체적으로 구축했음... 저거 종류 개많습니다 ㅠㅠ
enzyme_table = enzyme_table.sort_values('Enzyme')
# csv파일의 구성은 크게 효소 이름, 인식하는 시퀀스, 해당 시퀀스를 자르는 형태와 sticky or blunt 여부로 구성되어 있습니다.

year = datetime.today().year
month = datetime.today().month
day = datetime.today().day
# 파일 저장할 때 필요한 변수입니다. (코드 돌린 시점의 날짜 및 시간)

enzyme = input('시퀀스를 찾을 제한효소를 입력해주세요: ').strip()
sequence_name = input('Sequence 이름을 입력해주세요: ').strip()
sequence = input('제한효소 site를 찾을 시퀀스를 입력해주세요: ').upper().strip()
# 제한효소 이름 토씨 하나 안 틀리고 입력해야 합니다.

if enzyme_table['Enzyme'].isin([enzyme]).any() == True:
    res_find = enzyme_table.sequence[(enzyme_table['Enzyme'] == enzyme)]
    res_find = res_find.to_string(index=False)
    res_find = str(res_find)
    # 효소 이름이 데이터베이스에 있을 경우 검색할 시퀀스 데이터를 가져온다
    res_site = enzyme_table.restriction_site[(enzyme_table['Enzyme'] == enzyme)]
    res_site = res_site.to_string(index=False)
    res_site = str(res_site)
    # 효소 이름이 데이터베이스에 있을 경우 검색하고 대체할 시퀀스 데이터를 가져온다
    cut_feature = enzyme_table.cut_feature[(enzyme_table['Enzyme'] == enzyme)]
    cut_feature = cut_feature.to_string(index=False)
    cut_feature = str(cut_feature)
    # blunt or sticky(나중에 저장 기능 추가할 때 넣을 예정입니다)
else:
    print("No data in Database")

def count_func (a,b):
    while a in b:
        global site_count
        loc = b.find(a)
        site_count += 1
        b = b[loc+len(a):]
    return site_count
# Cutter test하다가 여기에도 추가했음...

if enzyme_table['Enzyme'].isin([enzyme]).any() == True:
    print(sequence.find(res_find))
else:
    pass
# 여기는 검색결과가 존재하지 않으면 -1로 나옵니다. (윗 블럭이랑 여기는 넘어가도 되는 부분)

with open ('Result_{0}-{1}-{2}_{3}-{4}.txt'.format(year,month,day,enzyme,sequence_name),'w',encoding='utf-8') as f:
    if sequence.find(res_find) != -1:
        site_count = 0
        cut_count = count_func(res_find,sequence)
        sequence = sequence.replace(res_find,res_site)
        print(enzyme,",",cut_feature)
        print(sequence,cut_count)
        f.write("{0} | {1} | {2} | {3} times cut\n".format(enzyme,res_site,cut_feature,cut_count))
        f.write('Sequence name: {0} \n{1}'.format(sequence_name,sequence))
        f.close()
        # DB에 효소가 있고 일치하는 시퀀스가 있을 때
    elif enzyme_table['Enzyme'].isin([enzyme]).any() == True and sequence.find(res_find) == -1:
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
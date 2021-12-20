import vcf
vcf_reader = vcf.Reader(open('/home/koreanraichu/clinvar_20211218.vcf', 'r'))
# 이틀 전에 업그레이드 된 따끈따끈한 데이터
Gene=[]
for record in vcf_reader:
    Info_get=record.INFO.get('GENEINFO')
    if Info_get:
        Gene.append(Info_get)
    else:
        Gene.append("No data")
# 이걸 안 해주면 데이터가 없을 때 Keyerror가 난다.
Gene_set=set(Gene)
Gene_value_list=list(Gene_set)
Gene_count=[]
Gene_dict={}
# 일단 세트부터 만들고 보는 타입
# 길이가 13654개... 어마무시하다.
for i in range(len(Gene_set)):
    Gene_values=Gene.count(Gene_value_list[i])
    Gene_count.append(Gene_values)
    Gene_dict[Gene_value_list[i]]=Gene_count[i]
print(Gene_dict)
# 실행하는데 정~말 오래 걸린다..
print(sorted(Gene_dict.items()))
print(sorted(Gene_dict.items(),key=lambda x:x[1]))
# 이쪽도 정렬이 된다.
for n in range(len(Gene_dict)):
    print(sorted(Gene_dict.items(),key=lambda x:x[1])[n])
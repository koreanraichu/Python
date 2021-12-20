import vcf
vcf_reader = vcf.Reader(open('/home/koreanraichu/clinvar_20211218.vcf', 'r'))
# 12월 18일에 업그레이드 된 따끈따끈한 데이터 납시오!
CLNSIG=[]
for record in vcf_reader:
    Info_get=record.INFO.get('CLNSIG')
    if Info_get:
        CLNSIG.append(str(Info_get[0])) # Tuple일 때 뽑아봤더니 (a,b) 구조더만... raw data에서는 안그런데...?
    else:
        CLNSIG.append("No data")
CLNSIG_set=set(CLNSIG) # set은 중복값을 없애주기 때문에 뭐가 있는지를 볼 수 있다. 일단은.
CLNSIG_count=[]
CLNSIG_values_list=list(CLNSIG_set)
CLNSIG_dict={}
print(len(CLNSIG_set)) # 67개씩이나 된다고?
for i in range(len(CLNSIG_set)):
    count_values=CLNSIG.count(CLNSIG_values_list[i])
    CLNSIG_count.append(count_values) # 일단 세 본다
    CLNSIG_dict[CLNSIG_values_list[i]] = CLNSIG_count[i] # 딕셔너리화
print(CLNSIG_dict)
# 어? 이게 되네?
print(sorted(CLNSIG_dict.items()))
CLNSIG_dict_key=sorted(CLNSIG_dict.items())
# Key로 정렬
print(sorted(CLNSIG_dict.items(),key=lambda x:x[1]))
CLNSIG_dict_values=sorted(CLNSIG_dict.items(),key=lambda x:x[1])
# value로 정렬(파이썬 자체로는 key 정렬만 되고 얘는 operator나 람다 써야 한다)
# 근데 이렇게 해 놓으니까 줄글이라 불편하시죠?
for n in range(len(CLNSIG_dict)):
    print(sorted(CLNSIG_dict.items())[n])
# for문을 그대로 쓰면 딕셔너리의 Key가 문자열이기 때문에 오류가 난다.
# 괄호 안을 sorted(CLNSIG_dict.items(),key=lambda x:x[1])로 바꾸면 Value(내림차순)로 정렬된 결과가 출력된다.

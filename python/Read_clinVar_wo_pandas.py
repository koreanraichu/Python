import vcf
import numpy as np
# array 하면 누구? 넘파이!
vcf_reader = vcf.Reader(open('/home/koreanraichu/clinvar_20211212.vcf', 'r'))
# 그새 업데이트 된 거 실화입니다.
first_record = next(vcf_reader)
print(first_record.INFO['CLNSIG']) # 단식으로 가져오기(아마 다 가져오려면 for문이 필요한듯)
print(first_record.INFO.keys()) # dict_keys(['ALLELEID', 'CLNDISDB', 'CLNDN', 'CLNHGVS', 'CLNREVSTAT', 'CLNSIG', 'CLNVC', 'CLNVCSO', 'GENEINFO', 'MC', 'ORIGIN', 'RS'])
print(first_record.INFO.values())
CLNSIG=[]
for record in vcf_reader:
    Info_get=record.INFO.get('CLNSIG')
    if Info_get:
        CLNSIG.append(Info_get)
    else:
        CLNSIG.append("No data")
# 이거 길이는 둘째치고 array 만들어도 깔끔하게 안보일 것 같다...
# 그리고 데이터가 데이터다보니 시간이 꽤 걸린다.
# 리스트 길이는 총 1106426... 어쩐지 오래 걸리더라...
CLNSIG=np.array(CLNSIG)
# VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
#   CLNSIG=np.array(CLNSIG)
# 이게 왜 뜨는지 알아볼 필요가 있을 것 같음
CLNSIG=CLNSIG.reshape(82,13493)
# 일단 생성된 것 같으니 reshape까지는 걸어보자.
import vcf
import pandas as pd
# 모듈은 항상 위쪽에 부릅니다.
vcf_reader = vcf.Reader(open('/home/koreanraichu/clinvar_20211204.vcf', 'r'))
# gedit으로 여는데 엄청 방대해서 랙걸린다... (리눅스긴 한데 PC 사양이 그렇게 좋은 편은 아님)
Chromosome=[]
CLNSIG=[]
Gene=[]
# 일단 Series를 거쳐서 DataFrame화 할 예정.
for record in vcf_reader:
     INFO_get=record.INFO.get('CLNSIG')
     Gene_get=record.INFO.get('GENEINFO')
     if INFO_get:
          Chromosome.append(record.CHROM)
          CLNSIG.append(str(INFO_get))
     else:
          Chromosome.append(record.CHROM)
          CLNSIG.append("No data")
     # CLNSIG에 키가 없으면 처리하는거
     if Gene_get:
          Gene.append(Gene_get)
     else:
          Gene.append("No data")
     # Gene도 몇개 없더라...
# 이거 자체는 간단하다. 키가 없으면 NaN으로 넣는다는 얘기.
Chr_series=pd.Series(Chromosome)
CLN_series=pd.Series(CLNSIG)
Gene_series=pd.Series(Gene)
# 제발 시리즈 한번에 나오게 해주소서
Gene_df=pd.DataFrame({"Chromosome":Chr_series, "Gene":Gene_series,"CLNSIG":CLN_series})
# 오케이 제발 데이터프레임 이쁘게 나오게 해주소서
Gene_df2=Gene_df.groupby(['Chromosome','CLNSIG']).count()
# Groupby로 시원하게 묶어보자
# 근데 이거 object라 정렬이 1, 2, 3, 4로 안된다...
Gene_df3=Gene_df.groupby('Gene').count()
Gene_df3=Gene_df3.sort_values('CLNSIG',ascending=0)
print(Gene_df3.head(30))
# 정렬하고 30개 뽑아보자
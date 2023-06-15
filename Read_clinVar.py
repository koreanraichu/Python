import vcf
import pandas as pd
# 모듈은 항상 위쪽에 부릅니다. (그쪽이 개인적으로 깔끔하고 편함)
vcf_reader = vcf.Reader(open('/home/koreanraichu/clinvar_20220103.vcf', 'r'))
# gedit으로 여는데 엄청 방대해서 랙걸린다... (리눅스긴 한데 PC 사양이 그렇게 좋은 편은 아님)
Chromosome=[]
CLNSIG=[]
Gene=[]
ID=[]
# 일단 Series를 거쳐서 DataFrame화 할 예정.
for record in vcf_reader:
     INFO_get=record.INFO.get('CLNSIG')
     Gene_get=record.INFO.get('GENEINFO')
     if INFO_get:
          Chromosome.append(record.CHROM)
          CLNSIG.append(str(INFO_get))
          ID.append(record.ID)
     else:
          ID.append(record.ID)
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
ID_series=pd.Series(ID)
# 사실 시리즈단에서 문제 된 적은 없었다.
Gene_df=pd.DataFrame({"ID":ID,"Chromosome":Chr_series, "Gene":Gene_series,"CLNSIG":CLN_series})
# 오케이 제발 데이터프레임 이쁘게 나오게 해주소서
Gene_df2=Gene_df.groupby(['Chromosome','CLNSIG']).count()
print(Gene_df2)
# Groupby로 시원하게 묶어보자
# 근데 이거 object라 정렬이 1, 2, 3, 4로 안된다...
Gene_df3=Gene_df.groupby(['Gene','CLNSIG']).count()
Gene_df3=Gene_df3.sort_values('ID',ascending=0)
print(Gene_df3.head(30))
# 유전자 내에서 CLINSIG별로 가장 많은 걸 출력해주는 건 이거
Gene_df3=Gene_df.groupby('Gene').count()
Gene_df3=Gene_df3.sort_values('CLNSIG',ascending=0)
print(Gene_df3.head(30))
# 그냥 유전자별로 Top30(CLINSIC 분류 상관없이) 출력해주는 건 이거
Gene_df3.to_csv('/home/koreanraichu/Result.csv')
# pandas dataframe은 이걸로 저장한다.
Gene_df3=Gene_df.groupby(['CLNSIG','Gene']).count()
Gene_df3=Gene_df3.sort_values('Gene',ascending=0)
print(Gene_df3.head(30))
# CLNSIG 내에서 Gene으로 정렬해주는 건 이거(근데 얘네 왜 따로노냐...)
Gene_df3=Gene_df.groupby(['CLNSIG','Gene','Chromosome']).count()
Gene_df3=Gene_df3.sort_values('ID',ascending=0)
print(Gene_df3.head(30))
# 단순히 CLNSIG-Gene-Chromosome 삼단분류는 이거
Gene_df3=Gene_df.groupby(['CLNSIG','Gene','Chromosome']).count()
Gene_df3=Gene_df3.sort_values(['CLNSIG','ID'],ascending=[True,False])
print(Gene_df3.head(30))
# 사실 이게 본인이 원했던 결과대로 딱 깔끔하게 뽑아주기는 한다. (CLNSIG 내에서 Gene으로, 분할 없이)
# 근데 이거는 세 주기는 하는건가...하는 의심이...
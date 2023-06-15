import vcf
import pandas as pd
# 모듈은 항상 위쪽에 부릅니다. (그쪽이 개인적으로 깔끔하고 편함)
vcf_reader = vcf.Reader(open('/home/koreanraichu/clinvar_20211204.vcf', 'r'))
# 새 파일로 해봅시다! 새 술은 새 부대에 담으라는 말도 있으니...
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
Chr_series=pd.Series(Chromosome)
CLN_series=pd.Series(CLNSIG)
Gene_series=pd.Series(Gene)
ID_series=pd.Series(ID)
Gene_df=pd.DataFrame({"ID":ID,"Chromosome":Chr_series, "Gene":Gene_series,"CLNSIG":CLN_series})
# 데이터프레임을 만들고 피벗테이블로 확인하기 위한 코드.
Gene_pivot=Gene_df.pivot_table(index=['Gene','CLNSIG'],values="Chromosome",aggfunc='count')
print(Gene_pivot)
# 씁 근데 피벗테이블 생각보다 안이쁘다.
# NaN을 0으로 대체할 수 있었으면 좋겠는데... (해당하는 값이 없으면 NaN이 뜸)
Gene_pivot.to_csv('/home/koreanraichu/Pivot.csv')
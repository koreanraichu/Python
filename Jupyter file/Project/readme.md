# 개요
생물정보학 관련된 것들 중에 할 수 있는 게 뭐가 있을까... 하고 제미나이랑 티키타카 하다가 시작했습니다. 

시작은 바이러스였지만 나중가면 혹시 모르죠. 세균이나 사람 단백질같은 거 할 지도... 몇 개는 포트폴리오용으로도 쓰고 있습니다. 
한번 올리고 나면 어지간해서는 그래프 디자인이나 로직 말고 크게 수정할 건 없습니다. 

팀플은 없고 전부 개인 프로젝트입니다. 애초에 팀플 할 만큼 스케일이 크지도 않아요. 

## 프로젝트 정보
- 인원: 1인(개인 프로젝트)
- 버전: 3.10(TF_base)
- 데이터 리소스: NCBI(MSA,Entrez accession), GEO(Lung cancer)
- 개발 환경: MacOS(14.7.6) (얘가 뭐 그렇게 OS타고 그럴 애는 아닙니다)
  - 코드를 실행하시기 전에 본인 PC에 MUSCLE이나 clustalW를 **설치**하시고 **경로 변경**해주세요!! 
  - 리눅스나 맥이면 which clustalw, which muscle 치면 경로 나오니까 그거 복사해서 쓰시면 됩니다. 

## Module
- Numpy, pandas
- matplotlib, seaborn
- Biopython
- MUSCLE(clustalw도 가능)
- scipy(scipy.stats)
- subprocess

### Lung cancer only
- lifelines(생존곡선 확인용)
- scikit_posthocs(크러스칼 월리스 사후검정용, Dunn's test)
- GEOparse
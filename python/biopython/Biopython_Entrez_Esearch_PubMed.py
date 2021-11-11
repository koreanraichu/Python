from Bio import Entrez
import numpy as np
Entrez.email = "blackholekun@gmail.com"
# 아 맞다 메일
handle = Entrez.esearch(db="pubmed", term="kimchii[title] and Lactobacillus[title]", retmax="40" )
# 검색어에 연산자를 쓸 수 있다. (위 연산자는 제목에 Lactobacillus와 kimchii가 둘 다 들어가는 논문을 찾는 것) 
record = Entrez.read(handle)
# 출력 안이뻐서 배열 만들었음
result=np.array(record['IdList'])
print(result)
# 바람직한 출력이야!
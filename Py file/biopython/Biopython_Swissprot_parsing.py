"""handle=open('/home/koreanraichu/Q63HQ2.txt')
1. 직접 저장된 파일을 열거나
2. gzip으로 된 파일을 열거나(여기 gzip 없어요)

from urllib.request import urlopen
url = "https://www.uniprot.org/uniprot/Q63HQ2.txt"
handle = urlopen(url)
3. 주소 입력해서 열거나

from Bio import ExPASy
handle = ExPASy.get_sprot_raw("Q63HQ2")
4. ExPASy에 접속해서 가져오거나ㅣ

이런 식으로 가져오면 되는데 출력 결과가 좀... 사람이 읽을만한 건 아니다 그죠?"""

from Bio import ExPASy
from Bio import SwissProt
# 일단 여기서는 4번, ExPASY에 접속해서 가져와보자.
handle = ExPASy.get_sprot_raw("Q63HQ2")
record = SwissProt.read(handle)
# 아 내가 말 안했는데 저 단백질 이름 피카츄린임. 뭐 잘못 본 거 아니고 진짜로.
print(record.description)
# 이런 식으로 찝어서 뽑을 수 있다. ...전체는 못 보나?
for ref in record.references:
    print("authors:", ref.authors)
    print("title:", ref.title)
    # 아마도 관련 참고문헌 정보?
print(record.organism_classification)
# 종 분류 정보
print(dir(record))
# 레코드 디렉터리는 이걸로 본다.
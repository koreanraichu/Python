from Bio.KEGG import REST
from Bio.KEGG import Enzyme
request = REST.kegg_get("ec:7.1.2.2")
# 참고: ATP synthase의 EC번호이다
open("ec_7.1.2.2.txt", "w").write(request.read())
records = Enzyme.parse(open("ec_7.1.2.2.txt"))
record = list(records)[0]
print(record.classname)
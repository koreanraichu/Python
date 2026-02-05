from Bio.Blast import NCBIWWW
result_handle = NCBIWWW.qblast("blastn", "nt", "8332116")
print(result_handle)
# 기본 양식
# <_io.StringIO object at 0x7f2f672ff280>가 나오는데 이것도 BLAST 설치해야 하나?
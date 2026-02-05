from Bio import ExPASy
handle = ExPASy.get_prosite_raw("PS00001")
text = handle.read()
print(text)
# 가장 원시적인 긁는 방법 (Expasy만 있으면 됨)

"""from Bio import Prosite
handle = ExPASy.get_prosite_raw("PS51036")
record = Prosite.read(handle)
print(record)"""
# ImportError: cannot import name 'Prosite' from 'Bio' (/home/koreanraichu/PycharmProjects/pythonProject/venv/lib/python3.8/site-packages/Bio/__init__.py)가 나를 반기는디?

from Bio.ExPASy import Prodoc
handle = ExPASy.get_prosite_raw("PDOC00001")
record = Prodoc.read(handle)
print(record)

handle = ExPASy.get_prosite_entry("PS51036")
html = handle.read()
with open("myprositerecord.html", "w") as out_handle:
    out_handle.write(html)
# HTML format으로 다운로드 받을 수 있다.

handle = ExPASy.get_prodoc_entry("PDOC51036")
html = handle.read()
with open("myprositerecord2.html", "w") as out_handle:
    out_handle.write(html)
# 얘는 prodoc 다운로드 하는 코드
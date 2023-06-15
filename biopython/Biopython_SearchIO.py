from Bio import SearchIO

blast_qresult = SearchIO.read("my_blast.xml", "blast-xml")
blast_slice = blast_qresult[:5]
"""
print(blast_qresult)
print("%s %s" % (blast_qresult.program, blast_qresult.version)) # 버전까지 알려주는 이런 섬세함.
"""

# for hit in blast_qresult:
    # print(hit)
    # 전체를 볼 수 있지만 너무 길다
    # print(hit[0])
    # 0번째만 띄워주세요였는데 뭐가 이렇게 많냐

for hit in blast_slice:
    print(hit.seq_len)
    # ID랑 길이 말고 없어요?

sort_key = lambda hit: hit.seq_len
sorted_qresult = blast_qresult.sort(key=sort_key, reverse=True, in_place=False)
for hit in sorted_qresult:
    print("%s %i" % (hit.id, hit.seq_len))

# 왜 함수는 lambda인가...
# 왜 길이는 못 보는가...
filter_func = lambda hit: len(hit.hsps) > 1
filtered_qresult = blast_qresult.hit_filter(filter_func)
print(filtered_qresult)
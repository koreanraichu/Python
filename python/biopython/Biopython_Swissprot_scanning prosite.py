from Bio.ExPASy import ScanProsite
seq="MEHKEVVLLLLLFLKSGQGEPLDDYVNTQGASLFSVTKKQLGAGSIEECAAKCEEDEEFTCRAFQYHSKEQQCVIMAENRKSSIIIRMRDVVLFEKKVYLSECKTGNGKNYRGTMSKTKN"
handle = ScanProsite.scan(seq=seq)
result = ScanProsite.read(handle)
print(result)
# 이걸로 찾을 수 있다.
print(result.n_seq)
print(result.n_match)
print(result[0])
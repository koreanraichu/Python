from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
record1=SeqRecord(Seq("GAATTC"), id="ECoR1",description="sticky")
record2=SeqRecord(Seq("GGCC"), id="HaeIII",description="blunt")
record3=SeqRecord(Seq("CTCGAG"), id="XhoI",description="sticky")
record4=SeqRecord(Seq("GATC"), id="DpnII",description="sticky")
# 뭐여 해삼만 blunt end네...

# 두 레코드를 비교해보자
# print(record1==record2)
# NotImplementedError: SeqRecord comparison is deliberately not implemented. Explicitly compare the attributes of interest.
# 이러시는 이유가 있으실 것 아니예요

# 레코드 내 항목들을 비교해보자
print(record1.description==record3.description)

# 혹시 길이 이런걸로도 되나?
print(len(record1.seq)==len(record2.seq))
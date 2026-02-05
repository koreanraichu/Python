from Bio.Seq import Seq
from Bio.Seq import MutableSeq #얘도 불러서
my_seq=Seq("GAATTC")
mutable_seq=MutableSeq(my_seq)#이걸 적용해야 바꿀 수 있다
mutable_seq[0]="A"
print(type(mutable_seq))
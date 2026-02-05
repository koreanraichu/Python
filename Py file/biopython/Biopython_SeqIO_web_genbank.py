from Bio import Entrez
from Bio import SeqIO
Entrez.email = "blackholekun@gmail.com"
with Entrez.efetch(
    db="nucleotide", rettype="gb", retmode="text", id="60391722,60391706,1519245148" # 여러개도 된다.
) as handle:
    for seq_record in SeqIO.parse(handle, "gb"):
        print(seq_record.description)
# 여러 개 가져올때는 for문을 쓰자(하나 가져올때는 안씀)
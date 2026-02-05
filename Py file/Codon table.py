# 표준 유전 암호표 (Standard Genetic Code)
codon_table = {
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', # Serine
    'TTC': 'F', 'TTT': 'F',                         # Phenylalanine
    'TTA': 'L', 'TTG': 'L',                         # Leucine
    'TAC': 'Y', 'TAT': 'Y',                         # Tyrosine
    'TAA': 'Stop', 'TAG': 'Stop',                   # Stop
    'TGC': 'C', 'TGT': 'C',                         # Cysteine
    'TGA': 'Stop',                                  # Stop
    'TGG': 'W',                                     # Tryptophan
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L', # Leucine
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', # Proline
    'CAC': 'H', 'CAT': 'H',                         # Histidine
    'CAA': 'Q', 'CAG': 'Q',                         # Glutamine
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R', # Arginine
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I',             # Isoleucine
    'ATG': 'M',                                     # Methionine (Start)
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T', # Threonine
    'AAC': 'N', 'AAT': 'N',                         # Asparagine
    'AAA': 'K', 'AAG': 'K',                         # Lysine
    'AGC': 'S', 'AGT': 'S',                         # Serine
    'AGA': 'R', 'AGG': 'R',                         # Arginine
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V', # Valine
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A', # Alanine
    'GAC': 'D', 'GAT': 'D',                         # Aspartic Acid
    'GAA': 'E', 'GAG': 'E',                         # Glutamic Acid
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G'  # Glycine
}

# 번역하실거예요?
def translate(dna_seq):
    protein = ""
    for i in range(0, len(dna_seq), 3):
        codon = dna_seq[i:i+3]
        protein += codon_table.get(codon, '?') # 없는 코돈은 ?로 표시
    return protein

# 검색하실거예요?
def find(codon):
    # T/U 혼용 허용, 대문자 변환
    query = codon.upper().replace('U', 'T')

    # 3글자가 아니면 에러 메시지
    if len(query) != 3:
        return "❌ 코돈은 3글자로 입력해주세요!"

    res = codon_table.get(query, "❓ 찾을 수 없는 코돈입니다.")
    return f"[{query}] -> {res}"

# 역검색(아미노산 머릿글자로 코돈 검색()
reverse_table = {}
for k, v in codon_table.items():
    reverse_table.setdefault(v, []).append(k)

print(reverse_table['L'])
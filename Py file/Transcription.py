codon_table = {
    # U
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", 
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*",
    "UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W",

    # C
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", 
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", 
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", 
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", 

    # A
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M", 
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", 
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", 
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R", 

    # G
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", 
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", 
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", 
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"
}

def transcription(text) :
    text = text.upper()
    text = text.replace('T','U')
    return text

def translation(text) :
    text = text.upper()

    protein = []
    for i in range(0, len(text) - 2, 3):
        codon = text[i:i+3]
        amino_acid = codon_table.get(codon, '???')
        protein.append(amino_acid)
        if amino_acid == "*":
            break
    return "".join(protein)

def translation_aug(text) :
    text = text.upper()
    start = text.find("AUG")

    if start == -1:
        return "No start point(AUG)"

    protein = []
    for i in range(start, len(text) - 2, 3):
        codon = text[i:i+3]
        amino_acid = codon_table.get(codon, '???')
        protein.append(amino_acid)
        if amino_acid == "*":
            break
    return "".join(protein)

sequence = input('DNA 시퀀스를 입력해주세요: ')
sequence_t = transcription(sequence)
sequence_t2 = transcription(sequence)
print('\n'+'transcrption: '+sequence)

sequence_t = translation_aug(sequence_t)
print('\n'+'translation(AUG): '+sequence_t)
sequence_t2 = translation(sequence_t2)
print('\n'+'translation: '+sequence_t2)
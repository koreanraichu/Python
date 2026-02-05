from Bio import SeqIO
record_iterator = SeqIO.parse("/home/koreanraichu/ls_orchid.fasta", "fasta")

i=0
while i<4
    record = next(record_iterator)
    print(record.id)
    print(record.description)
    i=i+1
# While문도 기본적인 건 똑같다.

"""
first_record = next(record_iterator)
print(first_record.id)
print(first_record.description)

second_record = next(record_iterator)
print(second_record.id)
print(second_record.description)

third_record = next(record_iterator)
print(third_record.id)
print(third_record.description)
"""
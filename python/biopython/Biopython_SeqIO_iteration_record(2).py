from Bio import SeqIO
record_iterator = SeqIO.parse("/home/koreanraichu/ls_orchid.fasta", "fasta")
for i in range(0,4): # 0번째부터 3번쨰까지 뽑아DALA
    record = next(record_iterator)
    print(record.id)
    print(record.description)

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
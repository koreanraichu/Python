from Bio.Data import CodonTable
standard_table = CodonTable.unambiguous_dna_by_name["Standard"]  #이름으로 codon table 확인
mito_table = CodonTable.unambiguous_dna_by_id[2] #ID로 codon table 확인
print(standard_table.stop_codons) # 종결코돈 출력
print(mito_table.start_codons) #개시코돈 출력
print(standard_table.forward_table['AAA']) #코돈 검색 기능도 있다
from Bio import SearchIO
blast_qresult = SearchIO.read("my_blast.xml", "blast-xml")
blast_hit = blast_qresult[0] # 첫번째 hit
print(blast_hit)

blast_hsp = blast_qresult[0][0] # 첫번째 hit의 첫번째 hsp
print(blast_hsp)
# 얘네는 hsp 위치까지 지정해줘야 출력한다
print(blast_hsp.query_range) # 첫번째 hit의 첫번째 hsp의 query range
print(blast_hsp.evalue) # 첫번째 hit의 첫번째 hsp의 evalue
print(blast_hsp.hit_start) # 첫번째 hit의 첫번째 hsp의 hit start coordinates
print(blast_hsp.query_span) # 첫번째 hit의 첫번째 hsp의 how many residues in the query sequence(residue 몇개냐)
print(blast_hsp.aln_span) # 첫번째 hit의 첫번째 hsp의 alignment 길이
print(blast_hsp.gap_num) # 첫번째 hit의 첫번째 hsp의 gap no.
print(blast_hsp.ident_num) # 첫번째 hit의 첫번째 hsp의 identical residue no.
print(blast_hsp.aln) # 배열 뽑아줘!

blast_frag = blast_qresult[0][0][0] # 첫번째 hit의 첫번째 hsp의 첫번째 fragment
print(blast_frag.hit) # hit sequence(sequence object)
print(blast_frag.query_start) # 시작 좌표
print(blast_frag.hit_strand) # hi sequence strand 수

import vcf
vcf_reader = vcf.Reader(open('/home/koreanraichu/clinvar_20211204.vcf', 'r'))
for record in vcf_reader:
    Gene_get=record.INFO.get('GENEINFO')
    if Gene_get:
        if record.CHROM == "17" and "C" in record.REF and "EG" in record.INFO['GENEINFO']:
            print(record.REF,record.ALT,record.INFO['GENEINFO'])
        else:
            pass
    else: 
        pass
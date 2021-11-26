from Bio.KEGG import Enzyme
records = Enzyme.parse(open("/home/koreanraichu/ec_5.4.2.2.txt"))
record = list(records)[0]
print(record.classname)
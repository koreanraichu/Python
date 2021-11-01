from Bio.Seq import Seq
at5g40780=Seq("ATGGTAGCTCAAGCTCCTCATGATGATCATCAGGATGATGAGAAATTAGCAGCAGCGAGACAAAAAGAGATCGAAGATTGGTTACCAATTACTTCATCAAGAAATGCAAAGTGGT")
print("Sequence",at5g40780)
print("Complement sequence",at5g40780.complement())
print("Reverse complement sequence",at5g40780.reverse_complement())
print(type(at5g40780))
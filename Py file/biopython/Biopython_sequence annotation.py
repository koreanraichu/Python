from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
EcoRI=Seq("GAATTC") # ECoRI sequence
HaeIII=Seq("GGCC") # HaeIII sequence

ECoRI_r=SeqRecord(EcoRI) #로 레코드를 만들어보겠습니다
HaeIII_r=SeqRecord(HaeIII,id="RES_HAEIII",name="HaeIII restriction site",description="Restriction of HaeIII, "
                                                                                     "cuts GG/CC")
# 만들면서 추가하는 것도 된다.

# 레코드에 정보를 추가해보자
ECoRI_r.id="RES_ECORI"
ECoRI_r.name="ECoRI restriction site"
ECoRI_r.description="Restriction site of ECoRI, cuts G/AATTC"
# ID랑 이름, description 정보를 추가했다.
HaeIII_r.annotations["notes"]="갑자기 해삼이 먹고싶다. " # annotation
HaeIII_r.letter_annotations['letter annotations']=['G','G/','C','C'] # letter annotations
print(ECoRI_r)
print(HaeIII_r)
print(HaeIII_r.letter_annotations['letter annotations']) # letter annotation은 각기출력인가요? 
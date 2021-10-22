import pandas as pd
import numpy as np
pokemon_name=pd.Series(['라이츄','라이츄(알로라 리전 폼)','에이스번','블레이범','한카리아스','미끄래곤','꼬지모','쏘콘','포트데스','브리무음','해피너스','폴리곤Z'])
HP=pd.Series([60,60,80,78,108,90,70,75,60,57,255,85])
ATK=pd.Series([60,90,116,84,170,100,100,90,65,90,10,80])
DEF=pd.Series([50,50,75,78,115,70,115,140,65,95,np.nan,70])
SP_ATK=pd.Series([90,95,65,109,120,110,30,60,134,136,75,135])
SP_DEF=pd.Series([85,85,75,85,95,150,65,60,114,103,135,75])
SPD=pd.Series([110,110,119,100,92,80,30,40,70,29,55,90])
TOTAL=pd.Series([485,485,530,534,600,600,410,465,508,510,540,535])
status=pd.DataFrame({"name":pokemon_name,"HP":HP,"ATK":ATK,"DEF":DEF,"SP.ATK":SP_ATK,"SP.DEF":SP_DEF,"SPD":SPD,"TOTAL":TOTAL})
status.index.name="No."
print(status)

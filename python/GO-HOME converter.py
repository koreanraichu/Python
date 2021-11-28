GO_HP=input("HP 개체값은 얼마입니까?: ")
GO_ATK=input("공격 개체값은 얼마입니까?: ")
GO_DEF=input("방어 개체값은 얼마입니까?: ")
SPD="스피드 개체값은 0~31 사이에서 랜덤으로 정해집니다. "
# 포켓몬 고 포켓몬의 HP, 공격, 방어 개체값을 입력받는다

int_HP=int(GO_HP)
int_ATK=int(GO_ATK)
int_DEF=int(GO_DEF)
# 문자열을 int로 바꿔준다 

HP=int_HP*2+1
ATK=int_ATK*2+1
DEF=int_DEF*2+1
# 계산 공식: GO 개체값*2+1 (예: GO에서 15면 연동시 31)
# 공격과 방어는 각각 물리특수에 동일하게 분배된다. (예: GO에서 공격이 15면 연동 시 물리공격과 특수공격이 31)

if HP <= 15:
    HP_stat = "적당하다"
elif HP <=25:
    HP_stat = "상당히 좋다"
elif HP <=29:
    HP_stat = "굉장히 좋다"
elif HP == 30:
    HP_stat = "훌륭하다 (U)"
elif HP == 31:
    HP_stat = "최고 (V)"
else: 
    HP_stat = "별로인 듯 (Z)"
# 해당 스테이터스 값 범위별로 그래프에 나오는 판정(HP)

if ATK <= 15:
    ATK_stat = "적당하다"
elif ATK <=25:
    ATK_stat = "상당히 좋다"
elif ATK <=29:
    ATK_stat = "굉장히 좋다"
elif ATK == 30:
    ATK_stat = "훌륭하다 (U)"
elif ATK == 31:
    ATK_stat = "최고 (V)"
else: 
    ATK_stat = "별로인 듯 (Z)"
# 해당 스테이터스 값 범위별로 그래프에 나오는 판정(공격)

if DEF <= 15:
    DEF_stat = "적당하다"
elif DEF <=25:
    DEF_stat = "상당히 좋다"
elif DEF <=29:
    DEF_stat = "굉장히 좋다"
elif DEF == 30:
    DEF_stat = "훌륭하다 (U)"
elif DEF == 31:
    DEF_stat = "최고 (V)"
else: 
    DEF_stat = "별로인 듯 (Z)"
# 해당 스테이터스 값 범위별로 그래프에 나오는 판정(방어)
# else라고 해도 GO에서 연동할 때 *2하고 +1하는 구조라 Z는 스피드 말고 안 나온다. 
# 총 합에 따른 대사도 있긴 한데 그거는 스피드가 랜덤이라 계산을 못 함. 

print("해당 포켓몬의 HP 개체값은 ",HP_stat,",", HP, "입니다. ")
print("해당 포켓몬의 공격/특수공격의 개체값은 ",ATK_stat,",", ATK, "입니다. ")
print("해당 포켓몬의 방어/특수방어의 개체값은 ", DEF_stat,",",DEF, "입니다. ")
print(SPD)
# GO에는 스피드라는 개념이 없으므로 스피드는 연동 시 0~31 중 랜덤으로 정해진다. 
# 운 나쁘면 5v1z 쌉가능... (z=0) 물론 운 좋으면 6V도 가능하다. (V=31)
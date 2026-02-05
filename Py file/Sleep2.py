import random
print("따라큐는 잠들었다!")
turn=1
awaken=["True","False"]
while turn<5:
    turn = turn + 1
    if random.choice(awaken)=="False":
        print("따라큐는 쿨쿨 자고 있다.")
    else:
        print("따라큐는 눈을 떴다!")
        break
print("따라큐는",turn,"턴만에 깨어났다!")

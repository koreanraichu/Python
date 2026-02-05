import random
pick=0
pick=random.randrange(1,51,1)
# 일단 범위는 1~100으로 잡았음
answer=input("과연 이 숫자는 몇일까요? ")
# 답 입력받고
turn=0
while turn < 10:
    if int(answer) < pick:
        print("Up!")
        answer=input("다시 생각해봅시다! ")
        turn += 1
    elif int(answer) > pick:
        print("Down!")
        answer = input("다시 생각해봅시다! ")
        turn += 1
    elif turn >= 10:
        print("턴 오버입니다. ")
        break
    else:
        print("정답입니다! ")
        print(turn, "번만에 맞추셨습니다!")
        break
# 답을 맞추기 전까지 계속 해야 하니까 while 받습니다.
# try수 출력 추가
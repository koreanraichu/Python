import random

# 업앤다운입니다. 근데 범위가 이제 1부터 100까지인. 
x = random.randrange(1, 101)

# 입력을 받고... 
# 솔직히 백준이었으면 import sys부터 들어갔을듯. 
y=int(input('숫자 하나를 입력해주세요.'))

# 여기 어딘가에 있는 Hogh&Low랑 달리 얘는 맞출떄까지 하는겁니다. 단판승 아님. 
while x != y:
    # 입력한 수가 더 클때
    if x < y: 
        print('다운!!!')
        y=int(input('다시 입력해주세요.'))
    # 입력한 수가 더 클때
    elif x > y: 
        print('업!!')
        y=int(input('다시 입력해주세요.'))
    # 정답이면 나감 
    else: 
        break
print('정답입니다!')

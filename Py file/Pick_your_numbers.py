import random
a = list(range(1,10))
# 일단 리스트는 1부터 9까지로 한다. 0이 끼면 유추가 너무 쉽다.
pick = [0,0]
pick[0] = random.choice(a)
pick[1] = random.choice(a)
# 리스트 내에서 두 개를 랜덤으로 뽑을거다.
while pick[0] == pick[1]:
    pick[1] = random.choice(a)
# 그리고 중복되면 안되므로 중복처리를 추가해줄거다.
print("두 숫자의 합은 ",pick[0]+pick[1],"입니다. ")
print("두 숫자의 곱은 ",pick[0]*pick[1],"입니다. ")
# 여기까지 하면 문제 출제는 쉽다. 답 맞추는 게 문제지.
answer = input("과연 제가 뽑은 숫자는 뭘까요? 두 개를 입력해주세요. ")
# 답을 입력받는다.
# 숫자 두자리 그냥 입력하면 된다. 예: 1과 6 = 16
rate=0
for i in range(2):
    for j in range(2):
        if answer[i] != str(pick[j]):
            rate+=0
        else:
            rate+=1
if rate > 0:
    print("제가 뽑은 숫자는 ",pick[0]," 그리고 ",pick[1],"입니다. ")
    print("정답입니다!")
else:
    print("틀렸습니다... ")
    print("제가 뽑은 숫자는 ",pick[0]," 그리고 ",pick[1],"입니다. ")
# 정답 도출하는 코드
# 와 이거 응용편 어캄...
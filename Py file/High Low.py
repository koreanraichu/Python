import random # 이게 없으면 이 게임의 근간인 카드뽑기가 안 된다.
Cards=list(range(1,14))
# 카드(A, J, Q, K 미적용)
# A, J, Q, K는 각각 1, 11, 12, 13에 대응함.
hands=[0,0]
hands[0]=random.choice(Cards)
hands[1]=random.choice(Cards)
# 첫 번째 카드를 뽑았다
print("첫 번째 카드는 %i입니다. " % hands[0])
print("그리고 다음 카드를 또 뽑을거예요. ")
while (hands[0] == hands[1]):
    hands[1]=random.choice(Cards)
# 선택지다 크다 or 작다이기떄문에 뽑은 카드의 숫자가 달라야 한다.
print("두 번째 카드를 뽑았습니다. ")
answer=input("과연 두 번째 카드의 숫자는 첫 번째 카드보다 클까요, 작을까요? (크다 or 작다를 입력해주세요)")
# 대답을 받을것이다.
# 공백 없이 임력해야됨 내가 아직 선택지를 못만들어서...
if answer == "크다" and hands[0]<hands[1]:
    print("두 번째 카드는 ",hands[1],"이었습니다. ")
    print("정답입니다!")
# 플레이어가 크다를 선택했고 실제로 두 번째 카드의 값이 클 경우
elif answer == "작다" and hands[0]>hands[1]:
    print("두 번째 카드는 ",hands[1],"이었습니다. ")
    print("정답입니다!")
# 플레이어가 작다를 선택했고 실제로 두 번째 카드의 값이 작을 경우
else:
    print("두 번째 카드는 ",hands[1],"이었습니다. ")
    print("까비... ")
# 이건 걍 틀린거져 뭘
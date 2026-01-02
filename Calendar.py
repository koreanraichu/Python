import calendar
calendar.setfirstweekday(calendar.SUNDAY) # 내는 달력 맨 왼쪽이 일요일인걸 선호한다 

# 이거 글꼴이 고정폭이어야 예뻐요 (예: 나눔고딕코딩)
# 트위터에서 줍줍한 코드 기호는 이게 아니었는데 복붙이 안됨... ㅡㅡ 
def glass(text):
    lines = text.splitlines()
    w = max(len(l) for l in lines)
    print("┌"+"-"*(w+2)+"┐")
    for l in lines:
        print("| "+l.ljust(w)+" |")
    print("└"+"-"*(w+2)+"┘")

# 1년 전체 (한달만 보실거면 반복문 빼고)
for m in range(1, 13):
    glass(calendar.month(2026,m))
import calendar
a=calendar.weekday(2020,3,28)

if a == 0:
    print("월요일")
elif a == 1:
    print("화요일")
elif a == 2:
    print("수요일")
elif a == 3:
    print("목요일")
elif a == 4:
    print("금요일")
elif a == 5:
    print("토요일")
else:
    print("일요일")

    print(a)
    
#아싸 내생일 토욜이당

b=calendar.monthrange(2020,2)
print(b)
#2월 1일 토요일인가

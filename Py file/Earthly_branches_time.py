from datetime import datetime

now_hour = datetime.today().hour
now_minute = datetime.today().minute

if (now_hour >= 1 and now_hour < 3):
    print("축시")
elif (now_hour >= 3 and now_hour < 5):
    print("인시")
elif (now_hour >= 5 and now_hour < 7):
    print("묘시")
elif (now_hour >= 7 and now_hour < 9):
    print("진시")
elif (now_hour >= 9 and now_hour < 11):
    print("사시")
elif (now_hour >= 11 and now_hour < 13):
    print("오시")
elif (now_hour >= 13 and now_hour < 15):
    print("미시")
elif (now_hour >= 15 and now_hour < 17):
    print("신시")
elif (now_hour >= 17 and now_hour < 19):
    print("유시")
elif (now_hour >= 19 and now_hour < 21):
    print("술시")
elif (now_hour >= 21 and now_hour < 23):
    print("해시")
else:
    print("자시")


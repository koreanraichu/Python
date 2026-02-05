from datetime import datetime

birth = input('생일을 yyyy-mm-dd형식으로 입력해주세요: ')

birthday = datetime.strptime(birth,"%Y-%m-%d")

now_year = datetime.today().year
now_month = datetime.today().month
now_day = datetime.today().day
# 오늘 년월일

birth_year = birthday.year
birth_month = birthday.month
birth_day = birthday.day
# 생일 년월일

isbirthdaypass = False
# 음 대충 생일 플래그인걸로 합시다 

if birth_month < now_month : # 생일 월보다 현재 날짜의 월이 더 크면 생일이 지난것이므로 
    isbirthdaypass = True # 만나이 +1
elif birth_month == now_month: # 생일 월과 현재 월이 같다면
    if birth_day <= now_day : # 현재 일이 생일보다 크거나 같나요? 
        isbirthdaypass = True # 응 만나이 먹었어
    else: # 아니야? 
        isbirthdaypass = False # 응 아직 아니야
else: 
    isbirthdaypass = False # 생일 월이 현재 날짜보다 크다면 아직 안 지난 것

if isbirthdaypass == False:
    print(now_year - birth_year - 1)
else: 
    print(now_year - birth_year)

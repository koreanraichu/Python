a=input("입력해주세요 \n")
a=a.lower() # 영어일 경우 전부 소문자로
a=a.replace(" ","") # 공백이 있을 경우 공백을 붙여버림

if a == a[::-1]:
    print(True)
else:
    print(False)
# 그래서 짜잔 나왔다
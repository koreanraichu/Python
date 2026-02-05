#숫자야구를 한번 해보겠습니다
import random
rn = ["0","0","0"]
rn[0]=str(random.randrange(1,9,1))
rn[1]=rn[0]
rn[2]=rn[0]
while (rn[0] == rn[1]):
    rn[1]=str(random.randrange(1,9,1))
while (rn[0] == rn[2] or rn [1] == rn [2]):
    rn[2]=str(random.randrange(1,9,1))

t = 0
s = 0
b = 0

while (s<3):
    num = str(input("숫자 3자리를 입력하세요: "))
    s=0
    b=0
    for i in range (0,3):
        for j in range (0,3):
            if (num[i] == str(rn[j]) and i == j):
                s=s+1
            elif (num [i] == str(rn[j]) and i != j):
                b=b+1
    print(s,"strike",b,"ball")
    t=t+1
print(t,"번만에 정답을 맞추셨습니다!")
#코드는 https://wikidocs.net/1027 <여기 참조했습니다 ;ㅅ;

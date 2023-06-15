import math;
print('2차방정식의 근의 공식은 다음과 같습니다: \n'
      'a, b, c가 실수이며 a<>0일때 이차방정식 ax^2 + bx + c의 해를 구하는 공식 '
      '-b +- 루트(b^2 - 4ac) / 2a');
print('또한 이차방정식의 판별식인 b^2 - 4ac를 이용해 근이 중근인지, 서로 다른 실근인지, 허근인지도 알 수 있습니다. ');
a=int(input('이차항 계수를 입력해주세요 '));
b=int(input('일차항 계수를 입력해주세요 '));
c=int(input('상수항 계수를 입력해주세요 '));
d=(b*b)-(4*a*c);

if d>0:
    print('이 방정식은 서로 다른 두 실근을 가집니다. ');
    e = round((-b + math.sqrt((b * b) - 4 * a * c)) / (2 * a),3);
    f = round((-b - math.sqrt((b*b)-4*a*c))/(2*a),3);
    print(e);
    print(f);
elif d==0:
    print('이 방정식은 중근을 갖습니다. ');
    e = round((-b + math.sqrt((b * b) - 4 * a * c)) / (2 * a),3);
    print(e);
else:
    print('이 방정식은 허근을 갖습니다. ');
    e = (-b / (2 * a));
    f = round(math.sqrt(abs(b * b - 4 * a * c)) / 2 * a,3);
    print(str(e)+'+-'+str(f)+'i');
function agrotime(~,~)
disp('이 함수를 싱행한 걸 보니 식물에 형질전환을 할 모양이구나! ');
disp('균이 너무 자라면 안되기때문에 미리 계산하고 알아서 넣어줘야 하는 게 진리지. ');
disp('일단 이 함수를 실행하기 전에 YEP에 subculture한 균을 붓고 OD를 달고 와 줘. ');
disp('사실 생물학에 100%라는 건 없지. 이 함수르 계산하는 OD값은 실제 OD값과 다를 수 있으니 값자체를 너무 맹신하지는 말고');
disp('그냥 대략적으로 몇 시간 후면 자라겠구나...를 예측하는 정도로만 써 줘. ');
OD=input('현재 A.tumefaciens의 OD값은 얼마야? ');
time=0
while OD<3
    OD=OD*2
    time=time+2
end
fprintf('아마 %s시간 후면 박테리아는 OD가 3을 넘어갈거야. \n', num2str(time));
fprintf('별로 정확하지는 않지만 그 시간까지 키우게 돼면 OD는 %s까지 갈거고. \n', num2str(OD));
disp('그럼 형질전환 열심히 해!');

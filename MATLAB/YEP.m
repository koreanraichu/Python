function YEP (~,~)
% 본격 개드립 작렬
disp('어서와, 여긴 처음이지? ');
disp('YEP 배지를 만들거지? ');
pause(2);
vol=input('얼마나 만들거야? 단위는 ml로 입력해줘. ');
agar=input('고체 배지도 만들거니? 만들거면 단위는 ml로 입력해줘. ');
disp('좋아, 이제 조금만 기다려~ ');
pause(2);
% 자 이제 계산하자
fprintf('\n넣어야 할 Yeast excact는 %s g이고 \n', num2str(10*(vol/1000)));
fprintf('넣어야 할 Bacto-peptone은 %s g이고 \n', num2str(10*(vol/1000)));
fprintf('넣어야 할 NaCl은 %s g이야. \n', num2str(5*(vol/1000)));
fprintf('혹시 고체 배지도 만드는거면 agar는 %s g을 넣어주면 돼. \n', num2str(15*(vol/1000)));
pause(2);
disp('YEP 배지를 만드는 걸 보니, 너 형질전환 할 거지? ');
disp('박테리아 잘 키우고 형질전환 잘해 :) ');
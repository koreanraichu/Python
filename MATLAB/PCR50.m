function PCR50(~)
%개간만에 하는 개정판 작업.. mastermix 부피 고정하고 20, 50짜리 만듭니다. 어차피 그 둘 외에는 안쓰잖음? ㅇㅇ
%근데 이거 어디서부터 손을 대야돼냐... 
disp('귀찮으니까 빨리 간다. ');
conc=input('...야 됐고 mastermix 몇배냐. ');
% 누가 이거 해결좀
% 계산하기 귀찮으니 걍 때려박어
disp('일단 1x일때 들어가는 비율 이거니까 노트에 써라. ');
fprintf('template %s ul \n', num2str(1))
fprintf('dNTP %s ul \n', num2str(1))
fprintf('10x buffer %s ul \n', num2str(5))
fprintf('forward primer %s ul \n', num2str(1))
fprintf('reverse primer %s ul \n', num2str(1))
fprintf('polymerase %s ul \n', num2str(0.2))
fprintf('DW %s ul \n \n', num2str(40.8))
disp('이상. 이제 mastermix 간다.');
% 여기까지는 condition, 즉 1x일 때 얼마나 들어가느냐임
fprintf('Mastermix의 농도 %s ul \n', num2str(conc))
% Mastermix 농도
fprintf('dNTP %s X \n', num2str(1*conc))
fprintf('10x buffer %s ul \n', num2str(5*conc))
fprintf('forwrd primer %s ul \n', num2str(1*conc))
fprintf('reverse primer %s ul \n', num2str(1*conc))
fprintf('polymerase %s ul \n', num2str(0.2*conc))
fprintf('DW %s ul \n \n', num2str(40.8*conc))
disp('PCR total volume 50이니까 이거 실행한거지? 그럼 이대로 걍 해. ');
% 코딩하느라 죽는 줄 알았네... ㅡㅡ 아무튼 여기는 mstermix에 넣어야 하는 것. 
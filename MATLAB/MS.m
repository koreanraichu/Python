function MS(~,~,~)
disp('어서와! 이 함수를 실행했다는 건 MS배지를 만들러 왔다는거겠지? ');
disp('LB배지 전용 함수도 있으니 많이 이용해줘! 나한테 화풀이는 하지 말고. ');
pause(2)
vol=input('배지는 얼마나 만들거야? 단위는 ml로 적어줘. ');
agar=input('만들 배지 중 고체배지는 얼마나 돼? 단위는 역시 ml로 적어줘. ');
agarp=input('좋아, 그럼 배지에 agar는 몇%로 넣는거지? ');
disp('OK. 배지 만들 준비는 다 했겠지? ');
% 질문 다받음여
fprintf('\n넣어야 할 MS는 %s g이고 \n', num2str(2.2*(vol/1000)));
fprintf('넣어야 할 MES는 %s g이고 \n', num2str(0.5*(vol/1000)));
fprintf('넣어야 할 Sucrose는 %s g이고 \n', num2str(5*(vol/1000)));
pause(2);
disp('pH는 5N KOH로 5.7까지 맞춰줘. ');
fprintf('넣어야 할 Phyto agar는 %s g이야. \n', num2str(1000*(agarp/100)*(agar/1000)));
pause(2);
disp('그럼, 식물 잘 심어! ')
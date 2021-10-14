%CAGR 계산용 함수%
%아 뭐 작두타다 왔어 왜%
%만들다 밥상 뒤집을뻔함... 어려워!!!%
function cagr(~,~,~,~)
disp('그냥 심심해서 만들어봤대. 한번 해 봐.');
disp('만들다가 밥상 뒤집을 뻔 하긴 했는데... 일단 입력하라는 것, 입력만 잘 하면 돼.');
starty=input('계산을 시작할 연도는?');
endy=input('계산을 끝낼 연도는?');
strate=input('좋아, 그럼 시작 년도의 값은?');
enrate=input('끝 연도의 값은?');
disp('ㅇㅋ 그럼 잠만 기둘려~');
pause(3)
cagr=(enrate/strate)^(1/(endy-starty))
disp('좋아, 계산 끝!');
fprintf('연평균성장률은 %s(이)라고 나오네. \n', num2str(cagr));
disp('근데 데이터는 신빙성 있는거지?');
%야 누가 이거 줄바꿈좀 해줘봐라% 

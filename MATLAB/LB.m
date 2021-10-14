function LB(~,~)
% 개드립도 넣어볼까... ㅡㅡ
disp('어서와, 이 프로그램은 처음이지? ');
disp('이 함수를 실행한 걸 보니, 네가 만들 배지가 LB배지가 맞는거지? ');
disp('개발자의 능력에도 한계가 있기 때문에 아니라고 해서 내가 이걸 닫거나 하는 건 불가능해. 그럼 이제 질문을 해 볼까? ');
vol=input('이 배지는 얼마나 만들거야? 단위는 ml로 적어주길 바래. ');
solid=input('그럼 이 중에서 고체 배지는 얼마나 만들어? 단위는 ml로 적어주길 바래. ');
% 질문 다 받은듯. 
% 끗
fprintf('\n넣어야 할 Yeast excact는 %s g이고 \n', num2str(5*(vol/1000)));
fprintf('넣어야 할 Trypton은 %s g이고 \n', num2str(10*(vol/1000)));
fprintf('넣어야 할 NaCl은 %s g이야. \n', num2str(10*(vol/1000)));
fprintf('그리고 고체 배지에 넣어야 할 bacto agar는 %s g이야. \n', num2str(15*(solid/1000)));
disp('이제 비커, stirring bar, 배지 담을 플라스크 다 1차 증류수로 헹구고 ')
disp('스파츌라는 3차 증류수로 헹궈서 물기 닦아줘. ');
disp('저울은 시약지 올린 다음 영점 맞추고! ');
disp('어라, 미리 하고 왔다고? 대단한걸? ');
disp('이제 시약을 준비한 다음 만들면 돼. ')

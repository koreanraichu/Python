function PCRtime(~,~,~,~,~,~,~);
%왜 매틀랩에서는 시간을 더하고 빼는 게 불가능한가. ...아니 내가 못찾는거임?
disp('내가 하다하다 이제는 시간까지 계산해줘야돼냐...');
disp('근데 사실 이것도 정확한 건 아냐.. 기기의 매커니즘을 완벽히 알고 있는 게 아니니까. ');
atemp=input('annealing temperature가 어떻게 돼냐? ');
pro=input('cycle 들어가기 전에 94도에서 몇분? ');
first=input('denaturation 몇초? ');
second=input('annealing 몇초? ');
third=input('extension time 얼마임? 초로 써라. ');
epi=input('마지막에 몇분이야. ');
cycle=input('몇 cycle? ');
disp('좀 걸릴거다. 아무래도 분으로 입력한거 초로 바꿔서 다 더할거니까.');
disp('그동안 condition이나 좀 짜보지 그러냐?');
%아 계산하려니 갑자기 짜증이 올라오네. 아니 난 코딩만 하면 돼잖아. 
totalsec=(pro*60)+((first+second+third+(94-atemp)/2)*cycle)+(epi*60)
fprintf('\n전부 더했을 때 초로 바꾸면 %s 초가 나온다. \n', num2str(totalsec))
totalmin=totalsec/60
fprintf('\n분으로 하면 대략 %s 분이고... \n', num2str(totalmin))
disp('시간정도는 니가 계산해. ');
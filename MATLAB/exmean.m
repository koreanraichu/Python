function exmean(~,~)
pathway=input('경로를 입력해주세요. '); %'' 포함할것
avr=input('범위는? '); %따옴표 ㅇㅇ 
X=xlsread(pathway,1,avr);
fprintf('%s \n', num2str(mean(X)))
%시간 있는 축 적어놓고 뭔 개짓을 한거냐 나레기... 난 이제 델타 함수 짜러 간다 ㅇㅇ 
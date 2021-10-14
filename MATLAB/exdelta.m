function exdelta(~,~,~)
pathway=input('경로를 입력해주세요. '); %'' 포함할것
del1=input('첫 번째 범위를 넣어주세요. '); %따옴표 ㅇㅇ 
del2=input('두 번째 범위를 넣어주세요. '); %따옴표 ㅇㅇ 
avr1=xlsread(pathway,1,del1);
avr2=xlsread(pathway,1,del2);
DELTA1=mean(avr1);
DELTA2=mean(avr2);
DELTA=DELTA2-DELTA1;
fprintf('Δ는 %s \n', num2str(DELTA))
%음 좋아 이상무 ㅇㅇ%

function extridelta(~,~,~,~,~,~)
global del1 del2 del3 del4
path=input('경로를 입력해주세요. ','s'); 
name=input('파일 이름은?' ,'s'); 
pathway=strcat(path,'\');
filename=strcat(name,'.xlsx'); %(경로+\)+(파일명+확장자)
        del1=input('첫 번째 범위의 시작점을 넣어주세요. ','s'); 
        del2=input('첫 번째 범위의 끝을 넣어주세요. ','s'); 
        del3=input('두 번째 범위의 시작점을 넣어주세요. ','s'); 
        del4=input('두 번째 범위의 끝을 넣어주세요. ','s'); 
    DEL1=strcat('B',del1,':','B',del2);
    DEL2=strcat('B',del3,':','B',del4);
        avr1=xlsread(strcat(pathway,filename),1,DEL1);
        avr2=xlsread(strcat(pathway,filename),1,DEL2);
    DELTA1=mean(avr1);
    DELTA2=mean(avr2);
    DELTA=DELTA2-DELTA1;
    DEL3=strcat('C',del1,':','C',del2);
    DEL4=strcat('C',del3,':','C',del4);
        avr3=xlsread(strcat(pathway,filename),1,DEL3);
        avr4=xlsread(strcat(pathway,filename),1,DEL4);
    DELTA3=mean(avr3);
    DELTA4=mean(avr4);
    dDELTA=DELTA3-DELTA4;
fprintf('Δ=%s \n', num2str(DELTA))
fprintf('Δ=%s \n', num2str(dDELTA))
%음 좋아 이상무 ㅇㅇ 
function extriplot(~,~,~)
path=input('경로를 입력해주세요. ','s'); 
name=input('파일 이름은?' ,'s'); 
graphname=input('그래프 이름은?' ,'s'); 
pathway=strcat(path,'\');
filename=strcat(name,'.xlsx');
disp('일단 그래프를 그리려면 행렬을 먼저 만들어야 해. 범위만 입력해주면 알아서 집을게.');
    shx1=input('각 축의 시작점은? ','s'); %숫자만 써... 
    shx2=input('각 축의 끝부분은? ','s'); 
        sheetX=strcat('A',shx1,':','A',shx2);
        sheetY=strcat('B',shx1,':','B',shx2);
        sheetY2=strcat('C',shx1,':','C',shx2);
        sheetY3=strcat('D',shx1,':','D',shx2);
X=xlsread(strcat(pathway,filename),1,sheetX);
Y=xlsread(strcat(pathway,filename),1,sheetY);
Y2=xlsread(strcat(pathway,filename),1,sheetY2);
Y3=xlsread(strcat(pathway,filename),1,sheetY3);
    plot(X,Y,'color',[.9 .09 .1],'LineWidth',2);
    hold on
    plot(X,Y2,'color',[0 .54 .8],'LineWidth',2);
    plot(X,Y3,'-.','color',[0 0 0]);
xlabel('Time(sec)');
ylabel('Pix');
title(graphname)
legend('CTCGC','CCCGC','reference ch.');
function expentplot(~,~,~)
global path name pathway filename shx1 shx2
figure(1);
path=input('경로! ','s'); 
name=input('파일 이름은?' ,'s'); 
name2=strcat('AJ',name);
graphname=input('그래프 이름은?' ,'s'); 
pathway=strcat(path,'\');
filename=strcat(name,'.xlsx');
disp('일단 그래프를 그리려면 행렬을 먼저 만들어야 해. 범위만 입력해주면 알아서 집을게.');
    shx1=input('각 축의 시작점은? ','s'); %숫자만 써... 
    shx2=input('각 축의 끝부분은? ','s'); 
        sheetX=strcat('A',shx1,':','A',shx2);
        sheetY=strcat('B',shx1,':','B',shx2);
        sheetY2=strcat('C',shx1,':','C',shx2);
    X=xlsread(strcat(pathway,filename),1,sheetX);
    Y=xlsread(strcat(pathway,filename),1,sheetY);
    Y2=xlsread(strcat(pathway,filename),1,sheetY2);
        plot(X,Y,'color',[.9 .09 .1],'LineWidth',2);
        hold on
        plot(X,Y2,'color',[0 .54 .8],'LineWidth',2);
xlabel('Time(sec)');
ylabel('Pix');
title(strcat(graphname,'(AJ)'));
legend('CTCGC','CCCGC');

figure(2);
path2=path;
name3=name;
graphname2=input('그래프 이름은?' ,'s'); 
pathway2=pathway;
filename2=filename;
        sheetZ=strcat('A',shx1,':','A',shx2);
        sheetW=strcat('B',shx1,':','B',shx2);
        sheetW2=strcat('C',shx1,':','C',shx2);
        sheetW3=strcat('D',shx1,':','D',shx2);
Z=xlsread(strcat(pathway2,filename2),1,sheetZ);
W=xlsread(strcat(pathway2,filename2),1,sheetW);
W2=xlsread(strcat(pathway2,filename2),1,sheetW2);
W3=xlsread(strcat(pathway2,filename2),1,sheetW3);
    plot(Z,W,'color',[.9 .09 .1],'LineWidth',2);
    hold on
    plot(Z,W2,'color',[0 .54 .8],'LineWidth',2);
    plot(Z,W3,'-.','color',[0 0 0]);
xlabel('Time(sec)');
ylabel('Pix');
title(graphname2)
legend('CTCGC','CCCGC','reference ch.');
end

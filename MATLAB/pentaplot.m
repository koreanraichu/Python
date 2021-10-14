function pentaplot (~)
%경로와 파일명, 범위는 비슷한데 통합이 안되고있어...
%참고: 그래프 레전드나 라벨은 함수단에서 바꿔야 합니다. 이건 나 쓰려고 만든거지 배포용으로 만든게 아님. 
disp('어떤 그래프를 그리러 온 거야? adjusted? 아님 reference channel 있는 거?');
select=input('reference channel이 있는 그래프를 그리러 왔다면 3, 아니면 2를 입력해줘. 둘 다 그리는거면 2+3은 5! ');
    if (select==3)
        run extriplot;
    elseif (select==2)
        run exduplot;
    elseif (select==5)
        run expentplot;
    else
        disp('똑바로 입력하지 못하겠어?');
    end
    disp('저장은 saveas를 이용하면 편...한가? 아 모르겠다 난 귀찮아! 자, 내 일은 여기까지!');
end

function exduplot(~,~,~)
path=input('경로! ','s'); 
name2=input('파일 이름은?' ,'s'); 
name=strcat('AJ',name2);
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
end

function extriplot(~,~,~)
path=input('경로! ','s'); 
name=input('파일 이름은?' ,'s'); 
graphname=input('그래프 이름은?' ,'s'); 
pathway=strcat(path,'\');
filename=strcat(name,'.xlsx');
disp('일단 그래프를 그리려면 행렬을 먼저 만들어야 해. 범위만 입력해주면 알아서 집을게. 혹시 둘 다 그리는거면 뭐... 알겠지? ');
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
end

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

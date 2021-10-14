function cycletimer(~)
%하 나레기 언젠가 이거 다 합칠꼬야 ㅇㅇ% 
disp('안정화 끝나고 진행중인거?');
disp('좋아 좋아. 그럼 슬슬 샘플 준비를 해 두는 게 어때?');
disp('버퍼 맞게 가져왔는지 체크하고 부족한 시약도 체크해야지 실험에 지장이 없어.');
disp('다 확인된 것 같으면 슬슬 로딩 준비해도 될 것 같아. ');
disp('혹시 calibration이 안 됐다면 이 함수는 실행하지 마. cavitation 생겨.');
ST=input('시작할 준비가 돼면 1을 입력해줘! 1만이야! 글자 안돼!');
    if ST == 1 
        t = timer('TimerFcn', 'stat=false; disp(''땡!'')','StartDelay',1200); 
        start(t) 

        stat=true; 
        a=0;
        while(stat==true) 
            a=a+1;
          fprintf('%s초 \n', num2str(a))
          pause(1) 
        end 
        stop(t)
        delete(t) 

    else 
        disp('ㅡㅡ+')
    end
    pause(1);
    disp('이번이 첫 번째 cycle이지?');
    ST=input('washing 준비가 돼면 1을 입력해줘! 1만이야! 글자 안돼!');
    if ST == 1 
        t = timer('TimerFcn', 'stat=false; disp(''땡!'')','StartDelay',1800); 
        start(t) 

        stat=true; 
        g=0;
        while(stat==true) 
            g=g+1;
          fprintf('%s초 \n', num2str(g))
          pause(1) 
        end 
        stop(t)
        delete(t) 

    else 
        disp('ㅡㅡ+')
    end
        pause(1);
    disp('이제 두 번째 cycle이지?');
    ST=input('준비가 돼면 1을 입력해줘! 1만이야! 글자 안돼!');
    if ST == 1 
        t = timer('TimerFcn', 'stat=false; disp(''땡!'')','StartDelay',1200); 
        start(t) 

        stat=true; 
        b=0;
        while(stat==true) 
            b=b+1
          fprintf('%s초 \n', num2str(b))
          pause(1) 
        end 
        stop(t)
        delete(t) 

    else 
        disp('ㅡㅡ+')
    end
        pause(1);
    disp('오호. 벌써 두 번 washing이구나. ');
    ST=input('washing 준비가 돼면 1을 입력해줘! 1만이야! 글자 안돼!');
    if ST == 1 
        t = timer('TimerFcn', 'stat=false; disp(''땡!'')','StartDelay',1800); 
        start(t) 

        stat=true; 
         c=0;
        while(stat==true) 
            c=c+1
          fprintf('%s초 \n', num2str(c))
          pause(1) 
        end 
        stop(t)
        delete(t) 

    else 
        disp('ㅡㅡ+')
    end
            pause(1);
    disp('좋아 좋아, 이제 마지막?');
    disp('buffer 교체가 끝나고 안정화하는 데 시간이 걸릴거야. 안정화가 다 돼면 졸아오도록 해.');
    pause(10)
    ST=input('준비가 돼면 1을 입력해줘! 1만이야! 글자 안돼!');
    if ST == 1 
        t = timer('TimerFcn', 'stat=false; disp(''땡!'')','StartDelay',1200); 
        start(t) 

        stat=true; 
        d=0;
        while(stat==true) 
            d=d+1;
          fprintf('%s초 \n', num2str(d))
          pause(1) 
        end 
        stop(t)
        delete(t) 

    else 
        disp('ㅡㅡ+')
    end
        pause(1);
    disp('마지막 washing이구나. ');
    ST=input('washing 준비가 돼면 1을 입력해줘! 1만이야! 글자 안돼!');
    if ST == 1 
        t = timer('TimerFcn', 'stat=false; disp(''땡!'')','StartDelay',1800); 
        start(t) 

        stat=true; 
        e=0;
        while(stat==true) 
            e=e+1;
          fprintf('%s초 \n', num2str(e))
          pause(1) 
        end 
        stop(t)
        delete(t) 

    else 
        disp('ㅡㅡ+')
    end
    disp('수고했어! 이제 DW로 washing만하면 끝이야~ 유속은 100ul/m으로 설정해줘.');
    pause(10);
        ST=input('washing 준비가 돼면 1을 입력해줘! 1만이야! 글자 안돼!');
    if ST == 1 
        t = timer('TimerFcn', 'stat=false; disp(''땡!'')','StartDelay',1800); 
        start(t) 

        stat=true; 
        f=0;
        while(stat==true) 
            f=f+1;
          fprintf('%s초 \n', num2str(f))
          pause(1) 
        end 
        stop(t)
        delete(t) 

    else 
        disp('ㅡㅡ+')
    end

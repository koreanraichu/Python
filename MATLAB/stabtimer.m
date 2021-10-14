function stabtimer(~)
%하 나레기 드디어 멈추는 법 발견했다능 ㅇㅅㅇ%
disp('처음 기기 가동하고 안정화중인거?');
disp('좋아 좋아 이해해. 그거 되게 오래 걸리지...');
disp('뭐, 일단 세는 건 20분씩이지만... 오래 걸릴 지 모르니 총 40분 셀 수 있게끔 코딩해놨어.');
disp('그리고 그 부분은 그래프에서 필요없는 부분이니까 초도 기록해뒀다가 나중에 데이터 낼 떄 빼버려!');
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
 disp('안정화는 잘 돼 가?');
 disp('시그널 괜찮지?');
ST=input('혹시 안정화가 더 필요할 것 같으면 1을 입력해줘!');
    if ST == 1 
        t = timer('TimerFcn', 'stat=false; disp(''땡!'')','StartDelay',1200); 
        start(t) 

        stat=true; 
        b=0;
        while(stat==true) 
            b=b+1;
          fprintf('%s초 \n', num2str(b))
          pause(1) 
        end 
        stop(t)
        delete(t) 

    else 
        disp('오, 안정화 성공? 좋아, 그럼 실험 개시!');
    end
disp('아직 안정화가 안 된거야?')
ST=input('아직 안정화가 안 된거라면 1을 입력해줘!');
    if ST == 1 
        t = timer('TimerFcn', 'stat=false; disp(''땡!'')','StartDelay',1200); 
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
        disp('오, 안정화 성공? 좋아, 그럼 실험 개시!');
    end
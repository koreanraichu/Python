function Timer(~)
%input의 수는 개발하면서 바뀔 예정이긴 한데... 타이머 멈추는 법 아는 사람?%
disp('YO!! 이번에는 타이머지롱!');
disp('아 물론 시험판이라;; 정식으로 개발되기까지는 오래 걸릴거야.');
disp('그래서 이번에는 간단히 샘플 처리에 소요되는 시간만 counting하도록 코딩했어!');
ST=input('sample을 넣고 나면 1을 입력해줘! 1만이야! 글자 안돼!');
    if ST == 1 
        t = timer('TimerFcn', 'stat=false; disp(''땡!'')','StartDelay',61); 
        start(t) 

        stat=true;
        a=0;
        m=0;
        while(stat==true) 
            a=a+1;
            if a>60
                a=a-60;
                m=m+1;
            else
                a=a;
                m=0;
            end
          fprintf('%s분 ', num2str(m))
          fprintf('%s초 \n', num2str(a))
          pause(1) 
        end 
        stop(t)
        delete(t) 

    else 
        disp('ㅡㅡ+')
    end
    %샘플 열처리 시간 ㅇㅇ%
 disp('sample 꺼낼 시간이야!');
 disp('얼음에 넣고 온 거지?!');
ST=input('만약 얼음에 넣었다면 1을 입력해줘!');
    if ST == 1 
        t = timer('TimerFcn', 'stat=false; disp(''땡!'')','StartDelay',60); 
        start(t) 

        stat=true; 
        b=0;
        while(stat==true) 
            b=b+1;
                        if b>60
                b=b-60;
                m=m+1;
            else
                b=b;
                m=0;
            end
          fprintf('%s분 ', num2str(m))
          fprintf('%s초 \n', num2str(b))
          pause(1) 
        end 
        stop(t)
        delete(t) 

    else 
        disp('ㅡㅡ+')
    end

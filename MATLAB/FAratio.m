function FAratio(~,~,~,~)
disp('순순히 묻는 말에 대답한다면 얼마든지 구해주겠어!');
V=input('total volume은 얼마?');
D=input('dilution factor는? 희석 배수 입력하면 돼.');
FA=input('formamide는 몇 %?');
S=input('buffer는 몇배 농축된거야? 이름 앞에 숫자+x로 돼 있는데 그 숫자 말하는거야.');
buffer=V/S; %부피/농축된 정도
    if D==0 
        DNA=0;
    else
        DNA=V*(1/D); 
    end
%DNA 역시 dilution factor에 따라 역수로 곱해준다. ...0일때 에러나서 수정 ㅇㅇ 
FAmide=V*(FA/100); %백분율인데 나누기해서 삑살났음... 3_3 현재 수정. 
DW=V-buffer-DNA-FAmide; %심플하져? 
fprintf('\n buffer %s \n', num2str(buffer));
fprintf('\n DNA %s \n', num2str(DNA));
fprintf('\n formamide %s \n', num2str(FAmide));
fprintf('\n DW %s \n', num2str(DW));
pause(1);

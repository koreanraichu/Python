function PCR(~,~,~,~,~,~,~)
%언니 힘들다...
disp('어서와 이건 처음이지? ');
disp('자, 내가 하는 질문에 대답하면 금방 계산해줄게! ');
template=input('PCR에 사용하는 template는 얼마? ');
dNTP=input('PCR에 사용하는 dNTP는 얼마? ');
buffer=input('PCR에 사용하는 buffer는 얼마? ');
primerF=input('PCR에 사용하는 forward primer는 얼마? ');
primerR=input('PCR에 사용하는 reverse primer는 얼마? ');
pol=input('PCR에 사용하는 polymerase는 얼마? ');
total=input('total volume은 얼마야? ');
conc=input('Mastermix의 농도는 얼마? ');
disp('이제 계산한다~ 1초만 기다려! 아, 요즘은 1초도 길다던데... ');
% 누가 이거 해결좀
DW=total-(template+dNTP+primerF+primerR+buffer+pol); 
% 계산하기 귀찮으니 걍 때려박어
fprintf('\ncondition of template is %s ul \n', num2str(template))
fprintf('condition of dNTP is %s ul \n', num2str(dNTP))
fprintf('condition of 10x buffer is %s ul \n', num2str(buffer))
fprintf('condition of forward primer is %s ul \n', num2str(primerF))
fprintf('condition of reverse primer is %s ul \n', num2str(primerR))
fprintf('condition of polymerase is %s ul \n', num2str(pol))
fprintf('condition of DW is %s ul \n \n', num2str(DW))
% 여기까지는 condition, 즉 1x일 때 얼마나 들어가느냐임
fprintf('Mastermix의 농도는 %s X \n', num2str(conc))
% Mastermix 농도
fprintf('Mastermix in dNTP is %s ul \n', num2str(dNTP*conc))
fprintf('Mastermix in 10x buffer is %s ul \n', num2str(buffer*conc))
fprintf('Mastermix in forwrd primer is %s ul \n', num2str(primerF*conc))
fprintf('Mastermix in reverse primer is %s ul \n', num2str(primerR*conc))
fprintf('Mastermix in polymerase is %s ul \n', num2str(pol*conc))
fprintf('Mastermix in DW is %s ul \n \n', num2str(DW*conc))
fprintf('total volume은 %s 이야! \n', num2str(total))
% 코딩하느라 죽는 줄 알았네... ㅡㅡ 아무튼 여기는 mstermix에 넣어야 하는 것. 
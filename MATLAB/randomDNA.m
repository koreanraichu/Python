function randomDNA(~,~)
n=input('몇 개나 만들거야?');
m=input('몇 bp?');
path=input('저장할 파일 이름은?','s');
exp_tmp = cell(n,2) ;
for k=1:n;
exp_tmp{k}=['DNA',num2str(k),' ',randseq(m)] ;
end
xlswrite(strcat('C:\Users\BFSL\Desktop\',path,'.xlsx'),exp_tmp);
%사실 단순히 DNA 시퀀스 만드는거라서 실험적으로 쓸만한게 나오지는 않습니다. 뭐 GC가 너무 많다거나 헤어핀이 나온다거나 할 수 있으니 쓰지 마세요. 

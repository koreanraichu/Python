function randomDNA(~,~)
n=input('몇 개나 만들거야?');
m=input('몇 bp?');
path=input('저장할 파일 이름은?','s');
exp_tmp = cell(n,2) ;
for k=1:n;
exp_tmp{k}=['DNA',num2str(k),' ',randseq(m)] ;
end
xlswrite(strcat('C:\Users\BFSL\Desktop\',path,'.xlsx'),exp_tmp);
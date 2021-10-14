function exhist(~,~,~)
pathway=input('경로를 입력해주세요. ');
sheet=input('읽을 sheet의 범위는? ');
bins=input('histogram의 빈도 수는? ');
ex=xlsread(pathway,1,sheet);
hist(ex,bins)
function exmerge(~,~,~,~,~,~)
pathway1=input('첫 번째 경로를 입력해주세요. '); %1차 합체 대상(...)
pathway2=input('두 번째 경로를 입력해주세요. '); %2차 합체 대상
range1=input('첫 번째 파일의 범위는? '); %1차 범위 
range2=input('두 번째 파일의 범위는? '); %2차 범위
save=input('저장할 위치는? '); %디렉토리 ㅇㅇ
name=input('파일명을 적어주세요. '); %이름이쟈나 그렇쟈나
srange=input('저장할 범위는? '); %네 말 그대로입니다
X1=xlsread(pathway1,1,range1); %1차 합체 대상에서 따 온 범위
X2=xlsread(pathway2,1,range2); %2차 합체 대상에서 따 온 범위
merge=cat(2,X1,X2);
xlswrite(strcat(save,name),merge,srange);

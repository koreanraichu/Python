function writeinxls(~,~,~)
save=input('저장할 위치는? ','s'); %디렉토리 ㅇㅇ 뒤에 \ 추가해주세요. 
merge=input('뭐 저장할겨?')
name=input('파일명을 적어주세요. ','s'); %이름이쟈나 그렇쟈나 확장자 매너쟈나 
srange=input('저장할 범위는? ','s'); %네 말 그대로입니다
xlswrite(strcat(save,name),merge,srange);
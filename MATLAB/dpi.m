function dpi (~,~)
disp('꽤 고생인걸? 수고가 많네.')
disp('역시나 나는 질문 받는 것을 좋아하지! 자, 그럼 시작해보자고.')
area=input('이미지의 크기는?');
per=input('몇 dpi?');
pause(2);
disp('끄응... 역시 이 쪽은 어려운걸. 그래도 이미지 프로세싱이라니, 언젠간 반드시 쓸데가 있을거라고 생각해.');
fprintf('cm로 변환한 크기는 %s야.\n',num2str(area/per*2.54));
function MS(~,~,~)
disp('���! �� �Լ��� �����ߴٴ� �� MS������ ���鷯 �Դٴ°Ű���? ');
disp('LB���� ���� �Լ��� ������ ���� �̿�����! ������ ȭǮ�̴� ���� ����. ');
pause(2)
vol=input('������ �󸶳� ����ž�? ������ ml�� ������. ');
agar=input('���� ���� �� ��ü������ �󸶳� ��? ������ ���� ml�� ������. ');
agarp=input('����, �׷� ������ agar�� ��%�� �ִ°���? ');
disp('OK. ���� ���� �غ�� �� �߰���? ');
% ���� �ٹ�����
fprintf('\n�־�� �� MS�� %s g�̰� \n', num2str(2.2*(vol/1000)));
fprintf('�־�� �� MES�� %s g�̰� \n', num2str(0.5*(vol/1000)));
fprintf('�־�� �� Sucrose�� %s g�̰� \n', num2str(5*(vol/1000)));
pause(2);
disp('pH�� 5N KOH�� 5.7���� ������. ');
fprintf('�־�� �� Phyto agar�� %s g�̾�. \n', num2str(1000*(agarp/100)*(agar/1000)));
pause(2);
disp('�׷�, �Ĺ� �� �ɾ�! ')
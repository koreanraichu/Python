function lottery (~,~)
many=input('몇 개나 추첨하려고?'); 
range=input('얼마나 추첨하려고?'); 
a=rand(1,many);
a=a*range;
a=a+1;
round(a)
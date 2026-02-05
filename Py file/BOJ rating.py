import sys
total,right,a,b,c,d,e,f=map(int,sys.stdin.readline().split(" "))
# 입력 순서: 제출-맞았습니다-출력형식-틀렸습니다-시간초과-출력초과-런타임 에러-컴파일 에러
# 원래 시간초과 변수는 없었는데 최근 추가했습니다... 허허 
right_rate=round(right/total*100,2)
format=round(a/total*100,2)
wrong=round(b/total*100,2)
time_excessed=round(c/total*100,2)
excessed=round(d/total*100,2)
runtime_error=round(e/total*100,2)
compile_error=round(f/total*100,2)
print("Right ans. rate: {0}%\nFormat error: {1}%, Wrong: {2}%, Excesses time: {3}%, Excesses output: {4}%, Runtime error: {5}%, Compile error: {6}%".format(right_rate,format,wrong,time_excessed,excessed,runtime_error,compile_error))

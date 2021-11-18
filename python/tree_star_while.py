a=list(range(10))
i=0
# 참고: 코드 파일은 걍 올렸는데 저거 하나씩 보셔야 합니다.
# 다른 코드 주석처리 안 하면 결과 안보여요. 특히 맨 위에거...

while i < a[-1]:
    print("a"*a[i])
    i=i+1
# 일반 삼각형

while i < a[-1]:
    print(" "*a[-i],"a"*a[i])
    i=i+1
# 아 우측정렬

while i <= a[-1]:
    print("c"*a[-i])
    i=i+1
# 아 역삼각형

while i <= a[-1]:
    print(" "*a[i],"c"*a[-i])
    i=i+1
# 아 역삼각형 우측정렬

while i <= a[-1]:
    print("@"*(a[-i]*2+1))
    i=i+1
# 홀수로 뽑아보자

while i <= a[-1]:
    print("@"*(a[-i]*2-1))
    i=i+1
# 홀수 역삼각형 가즈아!!!

while i <= a[-1]:
    print(" "*(a[-i]),"♥️"*(a[i]*2-1))
    i=i+1
# 가운데정렬!
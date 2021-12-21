a = int(input())
bin_list = []
while a >= 1:
    bin_list.append(a%2)
    a = int(a/2)
bin = bin_list[::-1]
bin = ''.join(map(str,bin))
print(bin)
# 입력한 숫자를 이진수로 바꿔준다. (물론 수동 방식이다)
for i in range(len(bin_list)):
    if bin_list[i] == 1:
        bin_list[i] = 0
    else:
        bin_list[i] = 1
comp_1 = bin_list[::-1]
comp_1 = ''.join(map(str,comp_1))
print(comp_1)
# 1의 보수(2의 보수는 이 방식으로 할 경우 처리가 되게 애매해지는 문제가 있다)
b=int(comp_1,2)
b=b+1
print(b)
# 그래서 2의 보수는 일단 10진수로 바꾼 다음, 1을 더하고 다시 바꿀 예정. 
comp2_list=[]
while b >= 1:
    comp2_list.append(b%2)
    b = int(b/2)
comp_2 = comp2_list[::-1]
comp_2 = ''.join(map(str,comp_2))
print(comp_2)
# 아, 0 빠진건 알아서 붙이세요. 
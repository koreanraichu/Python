a = int(input())
oct_list = []
while a >= 1:
    oct_list.append(a % 8)
    a = int(a / 8)
oct = oct_list[::-1]
oct=''.join(map(str,oct))
print(oct)
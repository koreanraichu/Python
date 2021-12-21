a = int(input())
hex_list = []
while a >= 1:
    if a % 16 == 10: # 16진수에서 10~15까지는 각각 A~F로 표기한다. 즉, 여기에 대한 처리를 따로 진행해야 한다. 
        hex_list.append("A")
    elif a % 16 == 11:
        hex_list.append("B")
    elif a % 16 == 12:
        hex_list.append("C")
    elif a % 16 == 13:
        hex_list.append("D")
    elif a % 16 == 14: 
        hex_list.append("E")
    elif a % 16 == 15:
        hex_list.append("F")
    else: 
        hex_list.append(a % 16)
    a = int(a / 16)
hex = hex_list[::-1]
hex=''.join(map(str,hex))
print(hex)
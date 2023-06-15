a = input()
cipher = len(a) # 자릿수가 영어로 cipher였다니
a = a[::-1]
dec_number = 0

Hex_letter = ['A','B','C','D','E','F']
Hex_number = [10,11,12,13,14,15]

for i in range(cipher):
    try:
        dec_number += int(a[i]) * (16 ** i)
    except:
        dec_number += Hex_number[Hex_letter.index(a[i])] * (16 ** i)

print(dec_number)
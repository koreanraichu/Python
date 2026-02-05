a = input()
cipher = len(a) # 자릿수가 영어로 cipher였다니
a = a[::-1]
dec_number = 0

for i in range(cipher):
    dec_number += int(a[i]) * (2 ** i)

print(dec_number)

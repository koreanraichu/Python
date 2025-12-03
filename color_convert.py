# rgb 10진수를 16진수로
def color_hex(r = 255, g = 255, b = 255): 
    # rgb값을 16진수로 변환할건데, 이거 이대로 내면 안된다. 형식을 잡아줄거다. 
    r, g, b = hex(r), hex(g), hex(b)
    # 출력형식: #rrggbb
    return (f'#{r[2:]}{g[2:]}{b[2:]}')

# rgb 16진수를 10진수로 
# 입력은 #rrggbb를 상정한다. 
def color_dec(color = '#ffffff'):
    # #을 떼고 여섯자리로 만든 다음 
    color = color[1:]
    # 분리해야죠
    r, g, b = color[0:2], color[2:4], color[4:]
    # 이제 변환하면 된다. 
    r, g, b = int(r, 16), int(g, 16), int(b, 16)
    return (f'r = {r}, g = {g}, b = {b}')

print(color_hex())
print(color_dec("#F7cac9"))
#아니 무슨 맥주를 99병씩이나 어유 대단들하셔
#그정도면 간이 안남아날거같은데
for bottle in range (99,0,-1):
    if bottle > 1:
        print(bottle,"bottles of beer on the wall",bottle,"bottles of beer")
        if bottle > 2:
            lyric = str(bottle-1) + " bottles of beer on the wall"
        else:
            lyric = "1 bottle of beer on the wall"
    elif bottle == 1:
         print("1 bottle of beer on the wall, 1 bottle of beer.")
         lyric = "no more beer on the wall!"
    print("Take one down, pass it around,", lyric)
#실제로 맥주 이렇게 마시면 간이 욕합니다 여러분

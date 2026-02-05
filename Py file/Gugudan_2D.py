import sys
gugu_range = int(sys.stdin.readline())

gugudan_array = [[i * j for i in range(1,gugu_range+1)] for j in range(1,gugu_range+1)]

for x in range(gugu_range):
    for y in range(gugu_range):
        print(gugudan_array[x][y], end=" ")
    print()
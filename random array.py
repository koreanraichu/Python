import random

# 표 그려주는겁니다. (feat. GPT)
def drawing_table(data): 
    # 칼럼 너비 도출(제일 긴 칼럼 기준)
    col_width = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]

    # 표 위아래로 줄 그어주는 겁니다. (-가 글자수대로 하면 길이가 안맞아서 두개 늘렸음)
    def draw_line(sep="+",fill="-"):
        return sep + sep.join(fill * (w + 2) for w in col_width) + sep
    
    print(draw_line())

    # 세로줄+내용
    for i, row in enumerate(data):
        row_str = "| " + " | ".join(str(row[j]).ljust(col_width[j]) for j in range(len(row))) + " |"
        print(row_str)

    print(draw_line())

# n = 배열의 행/열 수를 결정(n*n배열)
# k = 난수 범위(randrange에 들어감)
def random_array(n, k): 
    n = int(n)
    # m = 난수 범위만큼 만드는 랜덤한 배열(여기서 배열 크기만큼 뽑아야 합니다)
    # 그래서 난수 범위가 작으면 오류남... (예: 7*7 배열에 난수 범위가 36까지면 오류납니다)
    try: 
        m = random.sample(range(1,k+1), n ** 2)
    except: 
        return f"난수 범위가 충분하지 않습니다! 난수 범위를 {n ** 2} 이상으로 해 주세요!"
    
    array = [[m.pop() for j in range(n)] for i in range(n)]

    return array

size = int(input('배열은 몇 곱하기 몇인가요?'))
a = random_array(size,1024)

drawing_table(a)
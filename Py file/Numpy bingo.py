import numpy as np
import random

# OOP 서타일은 클래스에서 시작이여
class Bingo:
    # 기본값은 5*5(기본 범위는 25)
    def __init__(self, size = 5, n = 25):
        self.size = size
        self.bingo_max = n
        self.bingo_range = range(1, self.bingo_max + 1)
        self.board = None
        self.number_list = list(self.bingo_range)

    # 빙고판 생성
    def make_bingo(self): 
        self.board = np.random.choice(self.bingo_range, size=(self.size, self.size), replace=False)
    
    # 숫자 뽑기
    def draw_number(self): 
        if len(self.number_list) > 0:
            bingo_pop = random.choice(self.number_list)
            self.number_list.remove(bingo_pop)
            return bingo_pop
        else: 
            print('No more draw!')
            return None
    
    # 빙고 체크 함수
    def isbingo(self, n = 1):
        count = 0
        # 줄 
        count += np.sum(np.all(self.board == 0, axis=1))
        count += np.sum(np.all(self.board == 0, axis=0))
        count += np.all(np.diag(self.board) == 0) # 대각선(좌상-우하)
        count += np.all(np.diag(np.fliplr(self.board)) == 0) # 대각선(우상-좌하)
        # 빙고가 됐어? 
        return count >= n
    # 마킹
    def marking(self, jebi):
        if jebi in self.board:
            self.board[self.board == jebi] = 0
            return True
        return False

    # 출력 관련임다. 깔끔하게 뽑을라고... 
    def print_board(self):
        for row in self.board:
            print(" ".join(f"{num:2}" for num in row))
        print("+-----------------------+")


# 빙고 보드 생성 
while True: 
    bingo_num = int(input('Write maximum number: '))
    size = 5 # 여기 바꾸시면 빙고 크기 바껴요! (기본 5*5)
    try: 
        if bingo_num < size ** 2:
            raise ValueError
        else: 
            game = Bingo(size, bingo_num)
            break
    except ValueError:
        print(f'Out ot range: You have to input number larger than {size ** 2}')

# 목표 설정
while True:
    max_line = 2 * size + 2
    bingo_line = int(input('How many lines for end game?: '))
    try: 
        if bingo_line >= 1 and bingo_line <= max_line: 
            break
        else: 
            raise ValueError
    except ValueError:
        print(f'Out ot range: You have to input number between 1 and {max_line}')

# 빙고판 생성
game.make_bingo()

# 몇트째임?
bingo_cnt = 1

# 이 숫자가 빙고판에 있으면 지우고, 없으면 패스. 
# 일단 가로세로대각선 1빙고 될 때까지 해봅시다. 
while True: 
    # 랜덤으로 숫자 하나를 뽑는다. (범위는 위에 빙고판 숫자랑 동일)
    bingo_jebi = game.draw_number()
    # 물론 그럴 일은 없겠지만 리스트 거덜나면 끝납니다. 
    if bingo_jebi is None:
        print("No more draw! Game over.")
        break

    # 체크(위에 있음)
    if game.marking(bingo_jebi):
        print(f'{bingo_cnt}: {bingo_jebi} hit! 👏')
    else: 
        print(f'{bingo_cnt}: {bingo_jebi} no hits... 😭')
    game.print_board()

    # 조건 ㅇㅋ->시마이
    bingo_cnt += 1
    if game.isbingo(bingo_line):
        print(f'🎉Congratulations!')
        break

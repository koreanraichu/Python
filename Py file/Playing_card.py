import random

def draw_card(a = 3):
    # 카드 문양+숫자
    full_number = ("A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K")
    full_suit = ("Spade", "Diamond", "Club", "Heart")

    # 덱(조커 포함)
    full_deck = [("Joker",1), ("Joker",2)]
    
    # 카드 문양+숫자로 52개 카드를 생성 
    for suit in full_suit:
        for number in full_number:
            full_deck.append((suit, number))
    
    try: 
        # 카드 뽑고 언패킹까지 함
        cards = random.sample(full_deck, a)
        card = ", ".join([f"{n} {s}" for n, s in cards])
        return card
    except:
        # 여러분 카드가 조커 껴도 54장인거 아셨습니까?
        return False

draw_card(3)
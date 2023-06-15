# reference: https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3
import random
class Card:
    def __init__(self,suit,val):
        self.suit=suit
        self.value=val

    def show(self):
        print("{}{}".format(self.suit,self.value))
# Card class

class Deck:
    def __init__(self):
        self.cards=[]
        self.build()

    def build(self):
        for s in ["♠","♦","♣","♥"]:
            for v in range(0,13):
                a=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
                self.cards.append(Card(s,a[v]))

    def show(self):
        for c in self.cards:
            c.show()
#덱 구축(A-K)
#저기 근데 조커는...?
    def shuffle(self):
        for i in range(len(self.cards) - 1,0,-1):
            r=random.randint(0,i)
            self.cards[i],self.cards[r]=self.cards[r],self.cards[i]

    def drawCard(self):
        return self.cards.pop()

#이쪽은 플레이어(섞고 하나 뽑는 사람 말하는 듯)
class Player:
    def __init__(self,name):
        self.name=name
        self.hand=[]

    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

deck=Deck()
deck.shuffle()

bob=Player("Bob")
bob.draw(deck)
bob.showHand()
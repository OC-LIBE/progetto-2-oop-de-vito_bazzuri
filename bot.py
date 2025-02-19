import random
import math
from modules.card import Card

# scartine -> priority: 1 ; figure -> priority: 2 ; carichi -> priority: 3 ; briscole -> priority: *-1


# carta 0, carta 1, carta 2, briscola, first_card
class Bot:
    def __init__(self):
            self.eval = [0,0,0]

    def play(self,cards, briscola, first_card):
        self.hand = cards
        self.briscola = briscola
        self.first_card = first_card
        if self.first_card == None: # Se sei il primo a giocare
            self.card_evaluation(1,1,-1)
            self.card_evaluation(-3,3,5)
        else: # Se non sei il primo a giocare
            if self.first_card.point < 2: # Se c'è giù una scartina
                self.card_evaluation(1,1,-1,-1)
                self.card_evaluation(-1,2,3,2)
                self.card_evaluation(-1,3,15,5)
            elif self.first_card.point >= 2 and self.first_card.point <= 2: # Se c'è giù una figura
                self.card_evaluation(0,1,0,0)
                self.card_evaluation(-1,2,-1,3)
                self.card_evaluation(-1,3,15,5)
            elif self.first_card.point >= 10: # Se c'è giù un carico
                self.card_evaluation(-5,1,-1,0)
                self.card_evaluation(-1,2,-1,0)
                self.card_evaluation(-1,3,-15,5)
        

    def card_evaluation(self,change,priority,briscolamult=0,strozz=0):
        for i in self.hand:
            if i.suit == self.briscola.suit:
                mult = briscolamult
            elif self.first_card != None and i.suit == self.first_card.suit and i.rank > self.first_card.rank:
                add = strozz
            else:
                add = 0
                mult = 1
            
            if i.point < 2 and  priority == 1:
                self.eval[i] += change * mult + add
            elif i.point >= 2 and i.point <= 4 and priority == 2:
                self.eval[i] += change * mult
            elif i.point >= 10 and priority == 3:
                self.eval[i] += change * mult

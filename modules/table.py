from modules.card import Card
from modules.deck import Deck

class Table:
    def __init__ (self, briscola, first_card,second_card, first, second):
        self.briscola = briscola
        self.second_card =second_card
        self.first_card = first_card
        self.first = first 
        self.second = second
   
    def win_hand(self):
       # somebody who had won the hand because he had the card more lawsful
        if self.first_card.point >= self.second_card.point:
            self.first.score.extend([self.second_card, self.first_card])
        else:
             self.second.score.extend([self.second_card, self.first_card])


    def laws(self):
        if self.first_card == self.briscola and self.second_card != self.briscola:
            self.first win_hand
        elif self.second_card == self.briscola and self.first_card != self.briscola:
        for self.first_card in self.short.suit:
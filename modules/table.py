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
        if self.first_card.suit == self.second_card.suit:
            # this is for the same suit (also "briscola")
            if self.first_card.point >= self.second_card.point:
                self.first.score.extend([self.second_card, self.first_card])
            else:
                self.second.score.extend([self.second_card, self.first_card])
        elif self.first_card.suit != self.second_card.suit and self.first_card.suit !=  self.briscola.suit and self.second_card.suit !=  self.briscola.suit:
            # this is when in table there are two cards with differents suits (without "briscola")
                self.first.score.extend([self.second_card, self.first_card])
        else:
            # this is when in table there are two cards with differents suits (with "briscola")
            if self.second_card.suit == self.briscola.suit:
                self.second.score.extend([self.second_card, self.first_card])
            else:
                self.first.score.extend([self.second_card, self.first_card])
                
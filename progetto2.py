import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        if self.rank == 1:
            self.card_scores = [1, 10]
        else:
            self.card_scores = [self.rank, self.rank]
    

        if self.suit == 'Spade':
            self.short_suit = 'S'
        elif self.suit == 'Bastoni':
            self.short_suit = 'B'
        elif self.suit == 'Coppe':
            self.short_suit = 'C'
        elif self.suit == "Denari":
            self.short_suit = 'D'

        
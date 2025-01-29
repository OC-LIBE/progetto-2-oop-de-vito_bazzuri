import random


class Player:
    def __init__(self,cards,opponent=True):
        self.cards = []
        self.cards.extend(cards)
        if opponent:
            self.switch()
            

    def switch(self):
        i = 0
        for card in self.cards:
            self.cards[i] = card.hide()
            i = 1+ i
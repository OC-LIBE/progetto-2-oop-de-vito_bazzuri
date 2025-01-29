import random


class Player:
    def __init__(self,cards,opponent=True):
        self.cards = []
        self.cards.extend(cards)
        if opponent:
            self.switch()
            

    def switch(self):
        temp = []
        for card in self.cards:
            temp.append(card.turn())
        self.cards = temp
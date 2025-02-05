import random


class Player:
    def __init__(self,cards,bot):
        self.cards = []
        self.cards.extend(cards)
        if bot:
            self.switch()
            

    def switch(self):
        temp = []
        for card in self.cards:
            temp.append(card.turn())
        self.cards = temp
import math

class Player:
    def __init__(self,cards,bot,score=[]):
        self.cards = []
        self.score = score
        self.cards.extend(cards)
        if bot:
            self.switch()
            
    def switch(self):
        temp = []
        for card in self.cards:
            temp.append(card.turn())
        self.cards = temp

    def points_sum(self):
        points_sum = 0
        for card in self.score:
            points_sum += math.floor(card.point)
        return points_sum

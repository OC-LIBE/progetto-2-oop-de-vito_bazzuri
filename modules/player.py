import math

class Player:
    def __init__(self,cards,bot):
        self.cards = []
        self.score = []
        self.cards.extend(cards)
        self.last_index=None
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
    
    def add_card(self,card):
        if self.last_index != None:
            self.cards[self.last_index]=card
        else:
            self.cards.append(card)
        
    def play_card(self, card_index):
        played_card = self.cards[card_index]
        self.cards[card_index] = None
        self.last_index = card_index
        return played_card
        


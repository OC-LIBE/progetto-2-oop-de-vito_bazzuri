import math

class Player:
    def __init__(self,cards,bot):   #qua diciamo cosa serve per questo classe
        self.cards = []
        self.score = []
        self.cards.extend(cards)
        self.last_index=None
        if bot:
            self.switch()
            
    def switch(self): # per avere le carte del bot girate, ovvero si vede il rettro
        temp = []
        for card in self.cards:
            temp.append(card.turn())
        self.cards = temp

    def points_sum(self):  # calcolo per dare il risltato dei punti finali
        points_sum = 0
        for card in self.score:
            points_sum += math.floor(card.point)
        return int(points_sum)
    
    def add_card(self,card):   # fa in modo che abbiamo sempre 3 carte in mano, tranne alla fine
        if self.last_index != None:
            self.cards[self.last_index]=card
        else:
            self.cards.append(card)  # se non trova una carta, perché giocata, allora te ne da una
        
    def play_card(self, card_index): # serve per giocare le carte a tua scelta
        played_card = self.cards[card_index]
        self.cards[card_index] = None
        self.last_index = card_index
        return played_card
        
    @property
    def points(self):
        return self.points_sum